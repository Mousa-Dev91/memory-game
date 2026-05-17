# Memory Game

A simple color matching memory game built with Python and Tkinter.

## Requirements

- Python 3.10 or newer
- Tkinter, which is included with most Python installations

## How to Run

Clone the repository, then run:

```bash
python3 memory_game.py
```

The game opens a 4 by 4 board. Click two tiles at a time to reveal their colors. Matching colors stay visible. Non-matching colors flip back after a short delay. Match all pairs to win.

## Project Files

- `memory_game.py`: main game source code
- `README.md`: setup and execution guide
- `docs/git-workflow.md`: team workflow and configuration management guide
- `.gitignore`: ignored generated files

## GitHub Repository

Public repository: <https://github.com/Mousa-Dev91/memory-game>

## Configuration Management Expectations

The team should avoid one large commit for the whole project. Use small commits that each describe one clear change, for example:

```bash
git add README.md .gitignore
git commit -m "Add project documentation"

git add memory_game.py
git commit -m "Implement Tkinter memory game"

git add docs/git-workflow.md
git commit -m "Document team git workflow"
```

For team work, create feature branches:

```bash
git checkout -b feature/timer
```

Commit work regularly, open a pull request, review it, then merge into `main`.
