# Type Writer

Type Writer is a simple desktop utility that automates typing text or code files into the active application window. It is built with `PySide6` for the GUI and `pyautogui` for keystroke automation.

## What it does

- Opens a graphical window.
- Lets you select a text or code file from disk.
- Waits 10 seconds so you can switch to your target editor or input field.
- Types the contents of the selected file into whichever window is currently active, character by character.

> Note: This tool does not compile or execute code. It only simulates typing the contents of a file.

## Requirements

- Python 3.8+ (recommended)
- `PySide6`
- `pyautogui`

If you are using the included virtual environment, activate it before installing packages.

## Installation

Download the latest `tW.exe` from the [Releases](https://github.com/your-repo/releases) page and run it directly. No additional setup required.

## Usage

1. Launch the application:


2. Click `1. Select CPP File`.
3. Choose any text or code file from your filesystem.
4. Once the file is loaded, click `2. Start Typing (10s delay)`.
5. Quickly switch to the editor or target window where you want the code inserted.
6. Wait for the typing process to complete.

## How it works

- The app reads the selected file into memory.
- A 10-second countdown gives you time to focus the correct window.
- `pyautogui.typewrite()` sends each character one at a time to the active application.
- The code adds a small delay after newlines and spaces to make the typing appear more natural.

## Important warnings

- Make sure the target window is active and ready before clicking `Start Typing`.
- Do not move the mouse or switch windows while the typing is in progress.
- If the active window changes during typing, the text may be inserted into the wrong application.
- This tool is intended for automation/demo use only. Use carefully when sending keystrokes to other programs.



## Notes

- The UI is intentionally simple: select a file, wait for the delay, and let it type.
- Supported file filters include `*.cpp`, `*.h`, `*.txt`, and `All Files (*)` so you can use any text-based file.
- If an error occurs while loading a file, the UI will display the error message.
