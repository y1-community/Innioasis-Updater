# Agent Collaboration & Git Workflow Guidelines

This document defines synchronization and development protocols for all autonomous and pair-programming agents (Antigravity, Cursor, Claude, Copilot, Cline, Freebuff, and Cloud Agents) collaborating on `y1-community/Innioasis-Updater`.

---

## 1. Primary Repository & Synchronization

- **Upstream / Collaborative Remote**: `https://github.com/y1-community/Innioasis-Updater.git`
- **Personal Fork / Mirror**: `https://github.com/ryan-specter/Innioasis-Updater.git`
- **Default Branch**: `main`

### Push Configuration
Ensure git is configured to push to both remotes simultaneously:
```bash
git remote set-url --add --push origin https://github.com/ryan-specter/Innioasis-Updater.git
git remote set-url --add --push origin https://github.com/y1-community/Innioasis-Updater.git
```
Or push directly to `y1-community`:
```bash
git push y1-community main
```

---

## 2. Commit & Push Cadence

1. **Pull Before Work**: Always fetch and merge the latest remote state before beginning any modifications:
   ```bash
   git fetch y1-community && git merge y1-community/main
   ```
2. **Atomic, Regular Commits**: Commit work as soon as each logical unit, script, page, or bugfix is completed. Avoid batching multiple unrelated changes into large monolithic commits.
3. **Immediate Push**: Push immediately after committing so cloud agents and automated workflows can immediately see and build upon your changes:
   ```bash
   git push origin main
   git push y1-community main
   ```
4. **Commit Message Format**: Follow Conventional Commits:
   - `feat(...)`: New features, tools, or UI components
   - `fix(...)`: Bug fixes
   - `i18n(...)`: Translation catalogs, locales, script adjustments
   - `docs(...)`: Documentation, guides, agent hand-offs
   - `chore(...)`: Maintenance, dependency or config updates

---

## 3. Multilingual & Site Policies

- See `I18N.md` and `I18N_TODO.md` for complete multilingual rollout architecture.
- **Rule**: Content changes must ship across all languages simultaneously. When pages or UI strings are modified, extract strings and update catalogs accordingly.
- Keep `donors.csv` and `notice.xml` synchronized with `InnioasisY1Themes` via the established automated workflows.
