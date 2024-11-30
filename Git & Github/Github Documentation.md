# Introduction to Git and GitHub

## What is Git?
Git is a **distributed version control system** that helps developers manage and track changes in code projects, enabling collaborative work with ease.

## What is GitHub?
GitHub is a **web-based platform** that hosts Git repositories, allowing developers to share, collaborate, and contribute to code projects seamlessly.

---

## Installation Instructions

1. For Windows: Download Git from git-scm.com, run the installer, and follow the setup instructions.
2. For macOS: Install Git using Homebrew with brew install git.
3. For Linux: Use the command sudo apt install git (Debian/Ubuntu) or sudo yum install git (RHEL/Fedora).

# Setup Global Identity
1. Set username:- git config --global user.name "Your Name"
2. Setup Email:- git config --global user.email "your.email@example.com"
3. Verify Configuration:- git config --list

# Github Commands
1. Initialization and Cloning
- git init: Initialize a new Git repository in the current directory.
- git clone <url>: Clone a repository from a remote URL to your local machine.
2. Adding and Committing Changes
- git add <file>: Stage a specific file for commit.
- git add .: Stage all modified and new files for commit.
- git commit -m "message": Commit staged changes with a descriptive message.
3. Branching and Merging
- git branch: List all branches in the repository.
- git branch <branch-name>: Create a new branch.
- git checkout <branch-name>: Switch to an existing branch.
- git checkout -b <branch-name>: Create and switch to a new branch.
- git merge <branch-name>: Merge the specified branch into the current branch.
4. Viewing Changes
- git status: Show the working directory and staging area status.
- git diff: Show changes in the working directory that are not yet staged.
- git diff --staged: Show changes that are staged for the next commit.
- git log: Display the commit history of the current branch.
- git show <commit-id>: Show details of a specific commit.
5. Working with Remotes
- git remote -v: List all remote connections.
- git remote add <name> <url>: Add a new remote repository.
- git push <remote> <branch>: Push commits from the local branch to the remote branch.
- git pull <remote> <branch>: Fetch and integrate changes from the remote branch.
6. Undoing Changes
- git restore <file>: Discard changes in the working directory for a specific file.
- git restore --staged <file>: Unstage a file without modifying the working directory.
- git reset <commit-id>: Reset to a specific commit, keeping changes in the working directory.
- git reset --hard <commit-id>: Reset to a specific commit and discard all changes in the working directory.
7. Tagging
- git tag <tag-name>: Create a tag for a specific commit.
- git tag -a <tag-name> -m "message": Create an annotated tag with a message.
- git push origin <tag-name>: Push a specific tag to the remote repository.
8. Stashing
- git stash: Save changes temporarily without committing.
- git stash apply: Reapply stashed changes to the working directory.
- git stash pop: Reapply and remove the latest stashed changes.
- git stash list: List all saved stashes.
9. Viewing Configuration and Help
- git config --list: Display all Git configuration settings.
- git config user.name / git config user.email: Show the configured username or email.
- git help <command>: Display help information for a specific Git command.



