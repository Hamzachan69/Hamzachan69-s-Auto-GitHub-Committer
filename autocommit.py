import os # To Handle/Find System files(in this case the .git and the .txt files) 
import sys # To handle System Errors 
import subprocess # To Run Commands like git inside of the python script 
import datetime # To get time and date as per the users system
import platform # To check users Operating System
import shutil  # NEW TOOL : This lets us measure the screen width

FILE_NAME = "daily_log.txt"

# using r""" to tell Python this is a "Raw String" (don't mess with the spacing)
ASCII_ART = r"""
                                                                      
                                     ▄                                
██  ██  ▄▄▄  ▄▄   ▄▄ ▄▄▄▄▄  ▄▄▄  ▄█████ ▄▄ ▄▄  ▄▄▄  ▄▄  ▄▄ ▄██▀▀▀ ▄█▀▀█▄ ▀ ▄▄▄▄ 
██████ ██▀██ ██▀▄▀██   ▄█▀ ██▀██ ██     ██▄██ ██▀██ ███▄██ ██▄▄▄   ▀▀▀██  ███▄▄ 
██  ██ ██▀██ ██   ██ ▄██▄▄ ██▀██ ▀█████ ██ ██ ██▀██ ██ ▀██ ▀█▄▄█▀  ▄▄██▀  ▄▄██▀ 
                                                                      
                                                                      
                                                                      
▄████▄ ▄▄ ▄▄ ▄▄▄▄▄▄ ▄▄▄      ▄████  ▄▄ ▄▄▄▄▄▄ ██  ██ ▄▄ ▄▄ ▄▄▄▄     ▄█████  ▄▄▄  ▄▄   ▄▄ ▄▄   ▄▄ ▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄  
██▄▄██ ██ ██   ██  ██▀██    ██  ▄▄▄ ██   ██   ██████ ██ ██ ██▄██    ██     ██▀██ ██▀▄▀██ ██▀▄▀██ ██   ██     ██   ██▄▄  ██▄█▄ 
██  ██ ▀███▀   ██  ▀███▀     ▀███▀  ██   ██   ██  ██ ▀███▀ ██▄█▀    ▀█████ ▀███▀ ██   ██ ██   ██ ██   ██     ██   ██▄▄▄ ██ ██ 
                                                                      
"""

def show_banner():
   # Gets Screen width of the terminal. if it cant detech it then it assumes via "fallback" that the size is 80 columns
    screen_width = shutil.get_terminal_size(fallback=(80, 20)).columns
    
    # Prints the ASCII ART as is with split lines 
    lines = ASCII_ART.splitlines()
    print("\n") 
    
    # used for moving the ASCII ART in the center of the screen 
    for line in lines:
        print(line.center(screen_width))
    print("\n")

def get_os_advice():
    """Returns specific advice for installing Git based on your OS."""
    os_name = platform.system()
    if os_name == "Windows":
        return "💡 ➡️(For Windows) Download the git installer from https://git-scm.com/download/win and install git in your System"
    elif os_name == "Darwin": 
        return "💡 ➡️(For Mac) Run 'xcode-select --install' in terminal."
    elif os_name == "Linux":
        return "💡 ➡️(For Ubuntu/Debian based systems) Run 'sudo apt-get install git'.\n💡 ➡️(For RedHat based systems) Run 'sudo dnf install git',\n💡 ➡️(For Arch based systems) Run 'sudo pacman -S git'."
    else:
        return "'❓ Unknown OS: Check Google for 'Install Git' for your operating system."

def run_command(command_list):
    """Runs a command and captures errors nicely."""
    try:
        result = subprocess.run(
            command_list, 
            check=True, 
            text=True, 
            capture_output=True
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr
    except FileNotFoundError:
        return False, "PROGRAM_MISSING"

def main():
    # print art
    print("=" * 200)
    show_banner()
    print("=" * 200)
    print(f"💻 Operating System Detected ({platform.system()}) perform a commit... ---")

    # check if git is installed on the user's system
    success, message = run_command(["git", "--version"])
    
    if not success:
        print("\n❌ CRITICAL ERROR: Git is not installed.")
        print("=" * 60)
        print(get_os_advice())
        print("=" * 60)
        return

    # check if the user is in the repo folder or not 
    if not os.path.exists(".git"):
        print("\n❌ ERROR: This folder is not a Git Repository.")
        print("\n⌨️ Fix: Run 'git init' in your terminal first.")
        print("\n♻️ if that doesnt work then clone / reclone the git repo on you local machine")
        return

    # performs git pull before the commit
    print("⬇️ Pulling latest changes from GitHub...")
    success, err = run_command(["git", "pull"])
    
    if not success:
        # If pull fails, we usually shouldn't continue, because we might create a mess.
        print("\n❌ PULL FAILED")
        print("=" * 60)
        if "conflict" in err.lower():
             print("   Reason: ⚔️ Merge Conflict. (You changed something that GitHub also changed)")
             print("   Fix: You need to resolve conflicts manually.")
        elif "no tracking information" in err.lower() or "remote" in err.lower():
             print("   Reason: 🔗 No Remote Linked.")
             print("   Fix: Run 'git remote add origin <url>' and 'git push -u origin main' first.")
        else:
            print(f"   Reason: Unknown Git error during pull.\n   Raw log: {err}")
        print("=" * 60)
        return # STOP THE SCRIPT HERE TO BE SAFE
    else:
        print("✅ Successfully pulled latest changes.")

    # modify the txt file
    try:
        timestamp = datetime.datetime.now()
        with open(FILE_NAME, "a") as f:
            f.write(f"Log: {timestamp}\n")
        print(f"✅ Successfully wrote time stamp of the commit to {FILE_NAME}")
    except PermissionError:
        print(f"\n❌ ERROR: Permission Denied to write file.")
        print("\n💡 Fix: Close the file if it's open, or check permissions.")
        return

    # run git commands
    print("🔄 Processing Git commands...")
    
    # Git Add
    success, err = run_command(["git", "add", "."])
    if not success:
        print(f"❌ Failed to Stage files.\n   Raw Error: {err}")
        return

    # Git Commit
    success, err = run_command(["git", "commit", "-m", "Auto-update"])
    if not success:
        if "nothing to commit" in err:
            print("⚠️ Notice: No changes found to save.")
            return
        else:
            print(f"❌ Failed to Commit.\n   Raw Error: {err}")
            return

    # Git Push
    print("🚀 Pushing to GitHub...")
    success, err = run_command(["git", "push"])
    
    if not success:
        print("\n❌ PUSH FAILED")
        print("=" * 60)
        if "403" in err or "permission" in err.lower():
            print("   Reason: 🔐 Permission Denied.")
            print("   Fix: Check your Personal Access Token.")
        elif "Could not resolve host" in err:
            print("   Reason: 🌐 No Internet Connection.")
        elif "rejected" in err:
             print("   Reason: ⚡ Conflict (Remote is newer).")
             print("   Fix: Run 'git pull' first.")
        else:
            print(f"   Reason: Unknown Git error.\n   Raw log: {err}")
        print("=" * 60)
    else:
        print("🎊 SUCCESS! a Commit has been push to GitHub. \n+1🟩.")

if __name__ == "__main__":
    main()