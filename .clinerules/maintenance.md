# Pyfolio Maintenance Runbook

## Human Setup
- Install latest Python, uv, and make (see README.rst for details)
- Run `make install-dev` (uv handles the venv and dependencies automatically)
- Configure `.env` file (see README.rst for required variables)

## Dependency Management (using uv)
- Update dependencies in `pyproject.toml`
  - **Constraint**: Stick to **Django LTS** versions. Do not upgrade to the latest major version unless it is the current LTS.
  - **Compatibility**: Before upgrading Django, verify that key third-party packages (e.g., `django-extensions`, `django-bootstrap5`, `django-s3-storage`) support the target LTS version.
- Synchronize and lock: `make lock`
- **Eager Upgrade**: Run `uv lock --upgrade` to update all dependencies to their latest allowed versions.
- Export for CI/Production: `make export`
- Update `.env` with any new required variables

## Frontend Dependencies (Manual CDN)
- Update DataTables:
  - Find CDN links in `base_site/templates/base.html`.
  - Update version in URL (e.g., `dt-1.13.6` -> `dt-2.0.0`).
  - Update `integrity` hash with the one from [datatables.net](https://datatables.net/download/).
- Update any other JS/CSS libraries in `base.html` similarly (always verify SRI hashes).

## Periodic Updates
- Update Python version and GitHub Action versions in `pyproject.toml`, `app.yaml`, and `.github/workflows/build.yml`.
- Update copyright year in LICENSE or templates.

## Internationalization (Spanish)
- `uv run manage.py makemessages -l es` (per app: `base_site`, `emr`)
- `uv run manage.py compilemessages`

## Version & Deployment (CRITICAL SEQUENCE)
1. **Verification**: Run `make lint` and `make test`.
2. **Prepare Local Content**:
   - Check `base_site/templates/base.html` for any CDN dependencies that need bumping (update versions and SRI hashes).
   - Run `uv run manage.py makemessages -l es` (per app: `base_site`, `emr`).
   - Run `uv run manage.py compilemessages`.
   - Run `uv run manage.py collectstatic` (ensures `staticfiles/` is updated).
3. **Bump Version**:
   - Update `pyfolio/__init__.py` with the new semantic version.
   - Run `make lock && make export` to reflect the version in generated files.
4. **Commit & Tag**:
   - `git add .`
   - `git commit -m "Pyfolio vX.Y.Z"`
   - `git tag vX.Y.Z`
   - **Human**: `git push --atomic origin HEAD vX.Y.Z`
5. **Deploy**:
   - **Human**: `gcloud app deploy` (uploads the exact state of the repo).

## Notes for LLMs
- Use `make install-dev` for local development setup.
- Use `make lock` to update `uv.lock` after editing `pyproject.toml`.
- Use `make export` to update the root `requirements.txt`.
- Use `uv lock --upgrade` for an eager dependency upgrade.
- **Django Upgrades**: Always check if the target version is an LTS release.
- **Frontend**: Managed manually in `base_site/templates/base.html`. Always update SRI `integrity` hashes.
- **Deployment**: Follow the **Critical Sequence** exactly to avoid deploying stale assets or uncompiled messages.
- The project uses `uv` for all dependency and environment management.
- Root `requirements.txt` is a generated artifact for App Engine compatibility.
- See `pyproject.toml` for the single source of truth for Python version and dependencies.
