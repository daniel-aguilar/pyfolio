# Pyfolio AI Maintenance & Release Workflow

When asked to perform maintenance, upgrades, or releases for this project, follow these rules:

1.  **Workflow**: Follow the sequence in the `Pyfolio Maintenance Runbook` section below.
2.  **Technical Execution**: Use the `Makefile` targets.
3.  **Constraints**: Refer to `pyproject.toml` (specifically **Django LTS**).

**Goal**: A tagged release commit ready for `gcloud app deploy`.

## Human-Only Execution

AI assistants may prepare the repository, commit changes, and create local tags. However, they must **never** execute `git push` or `gcloud app deploy`. These final steps are strictly reserved for humans.

## Notes for LLMs

### Updating DataTables (CDN)

SRI hashes must **never** be guessed or assumed. Use `fetch_and_hash` (defined once below) so a bad version/URL fails loudly instead of silently hashing a 404 page or truncated response as if it were real:

```bash
# Reusable helper: downloads a URL, fails if the HTTP request errored or the
# body is suspiciously small (a 404/error page, not a real minified asset),
# then prints the SRI hash. Run this once per shell session before the
# per-library blocks below.
fetch_and_hash() {
    local url="$1" algo="$2" min_bytes="${3:-200}"
    local tmp; tmp=$(mktemp)
    if ! curl -sfL "$url" -o "$tmp"; then
        echo "ERROR: request failed for $url (bad version or dead URL)" >&2
        rm -f "$tmp"; return 1
    fi
    local size; size=$(wc -c < "$tmp")
    if [ "$size" -lt "$min_bytes" ]; then
        echo "ERROR: response for $url is only ${size} bytes (< ${min_bytes}) — likely an error page, not the real asset" >&2
        rm -f "$tmp"; return 1
    fi
    openssl dgst "-${algo}" -binary "$tmp" | base64 | sed "s/^/${algo}-/"
    rm -f "$tmp"
}

# 1. Get the latest DataTables version
DT_VERSION=$(curl -s https://api.github.com/repos/DataTables/DataTables/releases/latest | jq -r '.tag_name')
echo "Latest DataTables: $DT_VERSION"

# 2. Compute the JS SRI hash (fails loudly if $DT_VERSION doesn't exist on the CDN)
echo "JS SRI:" && fetch_and_hash "https://cdn.datatables.net/v/bs5/jq-3.7.0/dt-${DT_VERSION}/datatables.min.js" sha384

# 3. Compute the CSS SRI hash
echo "CSS SRI:" && fetch_and_hash "https://cdn.datatables.net/v/bs5/jq-3.7.0/dt-${DT_VERSION}/datatables.min.css" sha384
```

If either `fetch_and_hash` call errors out, **stop** — do not fall back to a remembered or guessed hash. Investigate the actual version/URL instead.

Update the version in the CDN URL and the `integrity` attribute in `base_site/templates/base.html` with these values. Also verify that the jQuery version in the CDN URL path (`jq-3.7.0`) still matches what is bundled with the new DataTables release; update it if it has changed.

### Updating Other CDN Libraries (Handlebars.js, Bootstrap Datepicker)

SRI hashes must **never** be guessed or assumed. Use the same `fetch_and_hash` helper defined above (re-declare it if running in a fresh shell) to check versions and compute hashes:

```bash
# 1. Check Handlebars.js version
HANDLEBARS_VERSION=$(curl -s "https://api.cdnjs.com/libraries/handlebars.js" | jq -r '.version')
echo "Latest Handlebars.js: $HANDLEBARS_VERSION"

# 2. Compute Handlebars.js SRI hash
echo "Handlebars.js SRI:" && fetch_and_hash "https://cdnjs.cloudflare.com/ajax/libs/handlebars.js/${HANDLEBARS_VERSION}/handlebars.min.js" sha512

# 3. Check Bootstrap Datepicker version
DATEPICKER_VERSION=$(curl -s "https://api.cdnjs.com/libraries/bootstrap-datepicker" | jq -r '.version')
echo "Latest Bootstrap Datepicker: $DATEPICKER_VERSION"

# 4. Compute Bootstrap Datepicker JS SRI hash
echo "Datepicker JS SRI:" && fetch_and_hash "https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/${DATEPICKER_VERSION}/js/bootstrap-datepicker.min.js" sha512

# 5. Compute Bootstrap Datepicker Spanish locale SRI hash (locale file is small, lower the size floor)
echo "Datepicker ES SRI:" && fetch_and_hash "https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/${DATEPICKER_VERSION}/locales/bootstrap-datepicker.es.min.js" sha512 200

# 6. Compute Bootstrap Datepicker CSS SRI hash
echo "Datepicker CSS SRI:" && fetch_and_hash "https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/${DATEPICKER_VERSION}/css/bootstrap-datepicker.min.css" sha512
```

If any `fetch_and_hash` call errors out, **stop** — do not fall back to a remembered or guessed hash. Investigate the actual version/URL instead.

Update the version numbers in the CDN URLs and the `integrity` attribute values in `base_site/templates/base.html`. Ensure all Bootstrap Datepicker resources (JS, Spanish locale, CSS) use the same version.

---

# Pyfolio Maintenance Runbook

## Human Setup

- Install the Python version specified in `pyproject.toml` (`requires-python`), `uv`, and `make`.
- Run `make install-dev` (uv handles the venv and dependencies automatically, including the `dev` extra). This ensures all development dependencies (like `ruff`) are installed.
- Configure `.env` file (see README.rst for required variables).

## Dependency Management (using uv)

- Update dependencies in `pyproject.toml`
  - **Source of Truth**: Always treat `pyproject.toml` as the master reference for Python versions and dependency constraints.
  - **Constraint**: Stick to **Django LTS** versions. Verify the current version in `pyproject.toml` against the official Django roadmap. Do not upgrade to a new major version unless it is the current LTS.
  - **Compatibility**: Before upgrading Django, verify that key third-party packages (e.g., `django-extensions`, `django-bootstrap5`, `django-s3-storage`) support the target LTS version.
- Synchronize and lock: `make lock`
- **Eager Upgrade**: Run `uv lock --upgrade` to update all dependencies to their latest allowed versions.
- Export for CI/Production: `make export`
- Update `.env` with any new required variables

## Frontend Dependencies (Manual CDN)

- Update DataTables: use the automated recipe in the **Notes for LLMs** section above to get the latest version and compute the correct SRI hashes, then update `base_site/templates/base.html`.
- Update any other JS/CSS libraries in `base.html` similarly (always verify SRI hashes).

## Periodic Updates

- Ensure Python version and GitHub Action versions are consistent across `pyproject.toml`, `app.yaml`, and `.github/workflows/build.yml` (refer to `requires-python` in `pyproject.toml`).
- Update copyright year in LICENSE or templates.

## Internationalization (Spanish)

- `uv run manage.py makemessages -l es`
- `uv run manage.py compilemessages`

## Version & Deployment (CRITICAL SEQUENCE)

1. **Verification**: Run `make lint` (includes formatting check via `ruff`) and `make test`.
2. **Prepare Local Content**:
   - Check `base_site/templates/base.html` for any CDN dependencies that need bumping (update versions and SRI hashes).
   - Run `uv run manage.py makemessages -l es` (from project root, processes all apps).
   - Run `uv run manage.py compilemessages`.
   - Run `uv run manage.py collectstatic` (ensures `staticfiles/` is updated).
3. **Bump Version**:
   - Update `pyfolio/__init__.py` with the new semantic version (this is the dynamic source for the build system).
   - Run `make export` to reflect the version in `uv.lock` and `requirements.txt`.
4. **Commit & Tag**:
   - `git add .`
   - `git commit -m "Pyfolio vX.Y.Z"`
   - `git tag vX.Y.Z`
   - **Human**: `git push --atomic origin HEAD vX.Y.Z`
5. **Deploy**:
   - **Human**: `gcloud app deploy` (uploads the exact state of the repo).

## Quick Reference

- Use `make install-dev` for local development setup.
- Use `make lock` to update `uv.lock` after editing `pyproject.toml`.
- Use `make export` to update the root `requirements.txt`.
- Use `uv lock --upgrade` for an eager dependency upgrade.
- **Django Upgrades**: Always check if the target version is an LTS release.
- **Deployment**: Follow the **Critical Sequence** exactly to avoid deploying stale assets or uncompiled messages.
- The project uses `uv` for all dependency and environment management.
- Root `requirements.txt` is a generated artifact for App Engine compatibility.
- See `pyproject.toml` for the single source of truth for Python version and dependencies.
