# 🐍 100 Days of Python Projects

Welcome to the 100 Days of Python Projects repository — a chronological record of small, focused Python projects built to practice core programming, automation, web development, and data work.

![Python](https://img.shields.io/badge/Python-3.11+-blue) ![Challenge](https://img.shields.io/badge/Challenge-100DaysOfCode-orange) ![License: MIT](https://img.shields.io/badge/License-MIT-green)

> This repo follows the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" as a learning scaffold and personal portfolio.

---

## Goal

- Build and document 100 concrete Python projects (small to medium)  
- Improve problem-solving, testing, debugging, and documentation habits  
- Produce a public portfolio suitable for interviews and demonstrations  
- Practice reproducible environments, CI, and deployment

---

## Key topics

Core Python, OOP, file I/O, testing, web (Flask), APIs, automation (requests, Selenium), web scraping (BeautifulSoup), data (Pandas, NumPy, Matplotlib), GUIs (Tkinter, Turtle), databases (SQLite/SQLAlchemy), deployment (Render/Azure/GitHub Pages).

---

## Repo layout

```
100-days-of-python-projects/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ requirements.txt                 # shared/dev dependencies
├─ .github/workflows/               # CI (lint, tests)
├─ resources/
│  ├─ images/
│  └─ references.md
├─ showcase/                        # polished projects
│  ├─ blackjack-plus/
│  └─ flask-blog-v2/
└─ days/
    ├─ day001-band-name-generator/
    ├─ day002-tip-calculator/
    ├─ ...
    └─ day100-final-capstone/
```

Naming rule for day folders:
```
dayNNN-short-slug   # three-digit day number keeps chronological order
```

Each day folder should include:
- main.py or app.py — entrypoint
- README.md — project goal, usage, concepts, stretch goals
- requirements.txt (optional) — project-specific deps
- tests/ (optional) — unit/integration tests

---

## Progress summary

- ✅ Days 001–015 — foundational exercises and small scripts (local)
- 🚀 Days 016+ — tracked projects in this repo (OOP apps, GUIs, Flask, APIs, DS)
- 🎯 Goal: finish Day 100 final capstone combining multiple skills

---

## Setup

1. Clone
```bash
git clone https://github.com/PhillipJBridgeman/100-days-of-python-projects.git
cd 100-days-of-python-projects
```
2. Create & activate virtual environment
Windows:
```powershell
python -m venv .venv
.venv\Scripts\activate
```
macOS / Linux:
```bash
python -m venv .venv
source .venv/bin/activate
```
3. Install shared dependencies
```bash
pip install -r requirements.txt
```
4. Run a project (example)
```bash
python days/day016-quiz-game/main.py
```
To install a project's dependencies:
```bash
pip install -r days/day036-stock-alert/requirements.txt
```

---

## Development conventions

- Branch naming:
  - feat/day059-add-blog, fix/day030-handle-keyerror, docs/day012-update-readme
- Commit messages: conventional commits-ish (type(scope): short description)
- Tests: prefer small unit tests under each project's tests/ folder
- Linting & formatting: use black, flake8 (configured in .github/workflows)

Example feature branch:
```bash
git checkout -b feat/day059-blog-v2
```

---

## Example day template

days/day016-quiz-game/
```
├─ main.py
├─ README.md
├─ requirements.txt   # optional
└─ tests/
```

README template (in the day's folder):
```markdown
# Day 16 — Quiz Game
**Goal:** Build a text-based quiz using OOP.

## How to run
python main.py

## Concepts practiced
- Classes & methods
- Input validation

## Stretch ideas
- Difficulty levels
- Fetch questions from Open Trivia DB API
- Create a GUI version with Tkinter
```

---

## Testing & CI

- Each project may include tests in tests/ using pytest.
- CI workflows run on push/PR: install deps, run linters, run tests.
- Add new workflow entries if a project has special build steps.

---

## Contribution

- Open issues for bugs, project suggestions, or improvements.
- Fork → branch → PR. Small, focused PRs preferred.
- Include README updates and tests where applicable.
- Respect code style (black) and add type hints when practical.

---

## Future enhancements

- Convert select console apps to web UIs (Flask / FastAPI)
- Add deployment examples (Render, Azure, GitHub Pages)
- Interactive progress badges & leaderboard
- More unit/integration tests per project

---

## License

This repository is licensed under the MIT License — see LICENSE for details.

---

## Acknowledgements

- Instructor: Dr. Angela Yu — App Brewery  
- Platform: Udemy  
- Student: Phillip Bridgeman (Started: May 21, 2025)

---

If you want, I can:
- Clean up a specific day folder README
- Add a GitHub Actions workflow template
- Generate a CONTRIBUTING.md or CODE_OF_CONDUCT.md
- Add sample tests for one project

Please let me know which, and I'll produce the files.
