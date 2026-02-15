# Pyfolio AI Maintenance & Release Workflow

When asked to perform maintenance, upgrades, or releases for this project, follow these rules:

1.  **Workflow**: Follow the sequence in `.clinerules/maintenance.md` strictly.
2.  **Technical Execution**: Use the `Makefile` targets.
3.  **Constraints**: Refer to `pyproject.toml` (specifically **Django LTS**).

**Goal**: A tagged release commit ready for `gcloud app deploy`.

## Human-Only Execution
AI assistants may prepare the repository, commit changes, and create local tags. However, they must **never** execute `git push` or `gcloud app deploy`. These final steps are strictly reserved for humans.
