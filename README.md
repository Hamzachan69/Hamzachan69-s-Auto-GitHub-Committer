![Auto Committer Banner](./ReadMe%20Assets/Gemini_Generated_Image_p949lzp949lzp949.png)

# 🚀 HamzaChan69's Auto GitHub Committer

<p align="center">
  **A smart, OS-aware Python script to automate your daily GitHub activity with style.**
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  </a>
  <a href="https://git-scm.com/">
    <img src="https://img.shields.io/badge/Git-Required-f05032?style=for-the-badge&logo=git" alt="Git">
  </a>
  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  </a>
</p>

---

## 📋 Table of Contents
- [The Struggle & 🕵️ The Mystery](#-the-struggle--the-mystery)
- [📜 Instructions](#-instructions)
    - [🪟 Windows Setup (Complete Guide)](#-windows-setup-complete-guide)
    - [🐧 Linux Setup (Complete Guide)](#-linux-setup-complete-guide)
    - [🍎 macOS Note](#-macos-note)
- [🔧 Troubleshooting](#-troubleshooting)
- [📝 License](#-license-mit)

---

## 🛑 The Struggle & 🕵️ The Mystery

**The Struggle:** We have all been there. You want to keep your GitHub profile green, but you didn't have time to code today.

So what do you usually do?
1. Open a `README.md`.
2. Add a space.
3. Delete the space.
4. Commit manually.

**Why suffer doing that?** It is boring, repetitive, and unnecessary manual labor.
<p align="center">
  <img src="./ReadMe%20Assets/5d95873d98e7b97ffabb8f28c225f553__1_-removebg-preview.png" width="500" alt="Tired Programmer / Tired Wojack">
</p>

**The Mystery:** Do I actually use this script myself? Maybe... maybe not. That is a mystery you’ll have to solve! 😂 But while you're guessing, this script is busy making sure no one else has to suffer through those manual edits again.

### 🌿 The Result: An Evergreen Profile
With this script running, your contribution graph becomes a lush forest of consistency—without the manual exhaustion.

<p align="center">
  <img src="./ReadMe%20Assets/1722092058475.png" width="500" alt="Green Profile">
</p>

---

## 📜 Instructions

Follow the steps for your Operating System to set up your repository and make automation compulsory.

### 🪟 Windows Setup (Complete Guide)

1.  **Prerequisites:**
    * Install [Python 3](https://www.python.org/downloads/).
    * Install [Git for Windows](https://git-scm.com/download/win).

2.  **Step 1: Get the Script (Hyperlink Download):**
    <p align="center">
      <a href="https://raw.githubusercontent.com/HamzaChan69/HamzaChan69-s-Auto-GitHub-Committer/main/autocommit.py" download>
        <img src="https://img.shields.io/badge/Download-autocommit.py-blue?style=for-the-badge&logo=python" alt="Download Script">
      </a>
    </p>
     Tip:
             Click the badge above to download. If it opens in a new tab, just press `Ctrl + S` to save it.

3.  **Step 2: Setup Your Log:**
    * Create a new GitHub repo (Public or Private) named `my-daily-log`.
    * Clone it: `git clone https://github.com/YOUR-USERNAME/my-daily-log.git`.
    * Place `autocommit.py` inside that folder.
    * **Test:** Run `python autocommit.py` in your terminal.

4.  **Step 3: Automate (Task Scheduler):**
    * Open **Task Scheduler** and click **Create Basic Task**.
    * **Trigger:** Daily at your preferred time.
    * **Action:** Start a program -> Program: `python.exe`.
    * **Arguments:** `autocommit.py`.
    * **Start in (CRITICAL):** Paste the full path to your folder (e.g., `C:\Users\Hamza\my-daily-log`).
    * **Settings:** Check "Run task as soon as possible after a scheduled start is missed".

---

### 🐧 Linux Setup (Complete Guide)

1.  **Prerequisites:** Ensure Python 3 and Git are installed.
2.  **Setup Your Log:**
    * Create a new GitHub repo and clone it locally.
    * Download `autocommit.py` and move it into the folder.
    * **Test:** Run `python3 autocommit.py`.
3.  **Automate (Crontab):**
    * Open Terminal and type `crontab -e`.
    * Add this line at the bottom (replace with your paths):
    ```bash
    # Runs every day at 10:00 AM
    0 10 * * * cd /home/yourname/my-daily-log && /usr/bin/python3 autocommit.py
    ```
    * Save and exit.

---

### 🍎 macOS Note
I haven't tested this on a Mac yet (don't have the cash for one right now! 😂). If you are a macOS user, you'll need to figure out the automation—though the Linux `crontab` method should work similarly.

---

## 🔧 Troubleshooting

The script includes a built-in "Doctor" to help you find and fix setup problems.

| Error | Reason | Solution |
| :--- | :--- | :--- |
| **"Git is not installed"** | Missing Software | Install Git from the official site. |
| **"Permission Denied (403)"** | GitHub Security | Use a **Personal Access Token** instead of a password. |
| **No Commit Created?** | Path Issue | (Windows) Double-check the "Start In" path in Task Scheduler. |

---

## 📝 License (MIT)

Copyright (c) 2025 HamzaChan69

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.
