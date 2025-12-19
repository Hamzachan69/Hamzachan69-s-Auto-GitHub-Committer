![Auto Committer Banner](./assets/banner.png)

# 🚀 HamzaChan69's Auto GitHub Committer

**A smart, OS-aware Python script to automate your daily GitHub activity with style.**

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Git](https://img.shields.io/badge/Git-Required-f05032?style=for-the-badge&logo=git)](https://git-scm.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

---

## 📋 Table of Contents
- [The Problem & 🕵️ The Mystery](#-the-problem--the-mystery)
- [📜 Instructions](#-instructions)
    - [🪟 Windows Setup](#-windows-setup-complete-guide)
    - [🐧 Linux Setup](#-linux-setup-complete-guide)
    - [🍎 macOS Note](#-macos-note)
- [🔧 Troubleshooting](#-troubleshooting)
- [📝 License](#-license-mit)

---

## 🛑 The Problem & 🕵️ The Mystery

**The Struggle:** You want that legendary "All Green" GitHub profile, but life gets in the way. Manually editing files just to keep a streak alive is tedious and boring.

<p align="center">
  <img src="https://i.imgflip.com/5xy5qs.png" width="500" alt="Distracted Boyfriend: Automation vs Manual Commits">
</p>

**The Mystery:** Do I actually use this script myself? Maybe... maybe not. That is a mystery you’ll have to solve! 😂 But while you're guessing, this script is busy keeping everything green.

### 🌿 The Result: An Evergreen Profile
With this script running, your contribution graph becomes a lush forest of consistency.

![My Evergreen Graph](./assets/green-graph.png)

**The Solution:** **No More Manual Edits.** This tool pulls your repo, picks a random catchy phrase, logs it, and pushes it to GitHub automatically.

---

## 📜 Instructions

Follow the steps for your Operating System to set up your repository and make the automation compulsory.

### 🪟 Windows Setup (Complete Guide)

1.  **Prerequisites:** * Install [Python 3](https://www.python.org/downloads/). 
    * Install [Git for Windows](https://git-scm.com/download/win).
2.  **Setup Your Log:**
    * Create a new GitHub repo (Public or Private) named `my-daily-log`.
    * Clone it: `git clone https://github.com/YOUR-USERNAME/my-daily-log.git`.
    * Place `autocommit.py` inside that folder.
    * **Test:** Run `python autocommit.py` in your terminal.
3.  **Automate (Task Scheduler):**
    * Open **Task Scheduler** and click **Create Basic Task**.
    * **Trigger:** Daily at your preferred time.
    * **Action:** Start a program -> Program: `python.exe`.
    * **Arguments:** `autocommit.py`.
    * **Start in (CRITICAL):** Paste the full path to your folder (e.g., `C:\Users\Hamza\my-daily-log`).
    * *Tip:* In Properties, check "Run task as soon as possible after a scheduled start is missed".

---

### 🐧 Linux Setup (Complete Guide)

1.  **Prerequisites:** * Ensure Python 3 and Git are installed.
2.  **Setup Your Log:**
    * Create a new GitHub repo and clone it.
    * Move `autocommit.py` into the folder.
    * **Test:** Run `python3 autocommit.py`.
3.  **Automate (Crontab):**
    * Open Terminal and type `crontab -e`.
    * Add this line at the bottom (replace with your paths):
    ```bash
    0 10 * * * cd /home/yourname/my-daily-log && /usr/bin/python3 autocommit.py
    ```
    * Save and exit.

---

### 🍎 macOS Note
I haven't tested this on a Mac yet (don't have the cash for one right now! 😂). If you are using macOS, you will need to figure out the automation part yourself—though the Linux `crontab` method above should work similarly!

---

## 🔧 Troubleshooting

The script helps you find and fix setup problems to keep your graph green.

| Error | Reason | Solution |
| :--- | :--- | :--- |
| **"Git is not installed"** | Missing Software | Install Git from the official site. |
| **"Permission Denied (403)"** | GitHub Security | Use a **Personal Access Token** instead of a password. |
| **No Commit?** | Path Issue | (Windows) Double-check the "Start In" path in Task Scheduler. |

---

## 📝 License (MIT)

Copyright (c) 2025 HamzaChan69

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.
