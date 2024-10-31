# LOL-

This Python program creates a simulated "lock screen" using Tkinter, designed to mimic a ransomware scenario as a security demonstration. It includes functionality for blocking certain keyboard shortcuts, locking the screen, and requiring a password to unlock the system. Here is a description for the README:

---

# Ransomware Simulation Lock Screen

This project is a Python-based simulation of a "lock screen" for educational and security awareness purposes. It demonstrates how malicious software could restrict user access by locking their screen, blocking system shortcuts, and requiring a password to unlock.

## Features

- **Full-Screen Lock Screen**: The program creates a full-screen window with a simulated "ransom" message.
- **Password Verification**: Users must enter a correct password to unlock the screen and regain system access.
- **System Shortcut Blocking**: Blocks common system shortcuts like `Ctrl+Alt+Del`, `Alt+Tab`, `Alt+F4`, and the Windows key to prevent easy escape.
- **Task Manager Control**: Disables Task Manager on Windows, further restricting user control.
- **Background Music**: Plays a looped sound file (`KRUSH_ALERT.mp3`) to simulate background noise common in scareware tactics.
  
## Dependencies

- `Tkinter` (for GUI)
- `ctypes` (for system calls, e.g., to disable Task Manager on Windows)
- `pygame` (for audio playback)

## Important Note

This code is intended strictly for educational purposes and should not be used maliciously. Always respect legal boundaries and ethical standards when using such programs.

## Usage

1. **Install Dependencies**: Make sure you have `pygame` installed:
   ```bash
   pip install pygame
   ```

2. **Run the Script**:
   Run the Python script in an environment where you can safely test full-screen applications.

3. **Terminate the Lock Screen**:
   If you need to stop the script, you can use `Ctrl+C` in the terminal or restart your system if the screen cannot be closed.

## How it Works

- **Password Entry**: Enter the pre-defined password (`mypassword` in this code) to close the lock screen.
- **Blocking Input**: The script disables certain keyboard shortcuts to simulate an actual lock screen experience.
- **Audio Feedback**: Background music plays to enhance the simulated effect.

**Warning**: This script modifies system accessibility features and is intended for controlled environments only.

--- 

This README offers an overview of the project's purpose, functionality, dependencies, and usage, emphasizing its ethical and educational use.
