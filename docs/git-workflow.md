# Git Workflow Guide

This project should use Git as configuration management throughout development, not only at the end.

## Repository Rules

- The GitHub repository must be public so the whole team and instructor can inspect progress.
- The `main` branch should contain stable, working code.
- New work should happen on short-lived feature branches.
- Each commit should represent one meaningful change.
- Commit messages should be short and clear.

## Recommended Branch Flow

1. Update the local repository.

```bash
git checkout main
git pull
```

2. Create a branch for the task.

```bash
git checkout -b feature/task-name
```

3. Make a focused change and test it.

```bash
python3 memory_game.py
```

4. Commit the change.

```bash
git add .
git commit -m "Describe the completed task"
```

5. Push the branch and open a pull request.

```bash
git push -u origin feature/task-name
```

## Good Commit Examples

```text
Add initial Tkinter board
Implement tile matching logic
Add win message
Document setup instructions
Fix hidden tile color reset
```

## Poor Commit Examples

```text
final
stuff
all code
project done
```

## Suggested Team Task Split

- Developer 1: board layout and tile display
- Developer 2: matching logic and win condition
- Developer 3: README, testing notes, and GitHub project setup
- Developer 4: optional features such as score, timer, or restart button
