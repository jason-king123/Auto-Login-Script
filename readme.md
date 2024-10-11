# Auto Login Script

**Read this in other languages: [中文](readme_zh.md).**

## Introduction

Due to the frequent need to log in to some accounts, entering the same username or password can be quite tedious. Therefore, this script is written to simplify the login process.  
This script can automatically fill in and submit login information after positioning the cursor in the login form input box.

## Security

All account data is stored locally, and the script does not make any network requests during execution, so there is no need to worry about data security issues.

## Installation Method

### Running Locally

1. Ensure that the Python environment is installed on your computer.
2. Download the script file.
3. Place the script file in the directory where you want to run it.
4. Ensure that the required dependencies for the script (such as `pyautogui`) are installed. If not installed, you can install the `pyautogui` library by running `pip install pyautogui`.
5. Run the script with `python auto_login.py`.

**Tip for easy use:**
You can create a `auto_login.bat` batch file on your desktop (Windows), and double-click to run it quickly.

```bat
@echo off
cd /d D:\code\python\scripts\auto_login\ REM (replace with your own directory)
python auto_login.py
pause
```

## Usage

### Select Account for Auto Login

1. After running the script, you will see a menu, select "1. Select account to auto login" to start the auto login process.
2. Choose the account you want to log in to according to the prompt.
3. Ensure that the cursor is in the username or password input box that needs to be auto-filled.
4. The script will automatically fill in the information and attempt to log in.

### Add a New Account

1. Select "2. Add account" to add a new account.
2. Enter the account name and follow the prompts to enter the information required for login.
3. After entering, type "q" and press Enter to save the account information.

### Delete an Account

1. Select "3. Delete account" to delete an existing account.
2. Choose the account you want to delete according to the prompt.
3. After confirming the deletion, the account information will be removed.

### Exit the Program

1. Select "4. Exit" to exit the script.

## Precautions

- Before using the auto login feature, ensure that the cursor is in the correct input box so that the script can fill in the information correctly.
- To protect your account security, do not use this script on public or insecure computers.
- Update your account information regularly to ensure that the login information in the script is up to date.

## Future Optimization and Improvements

### Add More Exception Handling Processes

- Enhance the script's error capture and handling capabilities to ensure that in case of unexpected situations, it can provide clear error prompts and safely terminate or recover operations.

### Add a Graphical User Interface to Simplify Operations

- Develop a graphical user interface (GUI) that allows users to complete account selection, addition, and deletion by clicking buttons and filling out forms, thus simplifying the operation process.

### More Aesthetically Pleasing

- Beautify the graphical user interface to provide a more intuitive and friendly user interaction experience.

With this auto login script, you can manage your online accounts more quickly and securely.
