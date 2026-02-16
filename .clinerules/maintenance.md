# Pyfolio Maintenance Runbook

## Human Setup
- Install the Python version specified in `pyproject.toml` (`requires-python`), `uv`, and `make`.
- Run `make install-dev` (uv handles the venv and dependencies automatically, including the `dev` extra).
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
- Update DataTables:
  - Find CDN links in `base_site/templates/base.html`.
  - Update version in URL (e.g., `dt-1.13.6` -> `dt-2.0.0`).
  - Update `integrity` hash with the one from [datatables.net](https://datatables.net/download/).
- Update any other JS/CSS libraries in `base.html` similarly (always verify SRI hashes).

## Periodic Updates
- Ensure Python version and GitHub Action versions are consistent across `pyproject.toml`, `app.yaml`, and `.github/workflows/build.yml` (refer to `requires-python` in `pyproject.toml`).
- Update copyright year in LICENSE or templates.

## Internationalization (Spanish)
- `uv run manage.py makemessages -l es` (per app: `base_site`, `emr`)
- `uv run manage.py compilemessages`

## Version & Deployment (CRITICAL SEQUENCE)
1. **Verification**: Run `make lint` (includes formatting check via `ruff`) and `make test`.
2. **Prepare Local Content**:
   - Check `base_site/templates/base.html` for any CDN dependencies that need bumping (update versions and SRI hashes).
   - Run `uv run manage.py makemessages -l es` (per app: `base_site`, `emr`).
   - Run `uv run manage.py compilemessages`.
   - Run `uv run manage.py collectstatic` (ensures `staticfiles/` is updated).
3. **Bump Version**:
   - Update `pyfolio/__init__.py` with the new semantic version (this is the dynamic source for the build system).
   - Run `make lock && make export` to reflect the version in `uv.lock` and `requirements.txt`.
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
