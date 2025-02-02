import keyboard
import pyautogui
import tkinter as tk
import time

# A dictionary of key bindings and their corresponding messages
key_messages = {
    '1': 'That was so clean, my monitor just got shinier.',
    '2': 'That shot was MARVELOUS!',
    '3': 'AMAZING shot!',
    '4': 'Teamwork makes the dream work!',
    '5': 'Goalkeeper training arc complete!',
    '6': 'WHAT A SAVEE!',
    '7': 'Thank you mate!',
    '8': 'Not a problem!',
    '9': 'Nothing to worry about, we got it!',
    '0': 'My apologies, that ones on me.',
    '-': 'I can just type extremely fast, thats all.',
    'q': 'Everyone lets have a clean, good, fast paced good game. And don\'t forget to have fun!',
    'w': 'That was a terrific game everyone. Well played!',
    'e': 'That was a close one!',
    'r': 'HOLY GUACAMOLE!',
    'i': 'My teammate is cooking yall!',
    'o': 'Jeepers!',
    'p': 'Yikes!',
    'a': 'Is there a breeeze!?',
    's': 'Yes.',
    'd': 'No.',
    'f': 'Yup.',
    'g': 'Nah.',
    'h': 'Ain\'t no shame in gettin\' out the game.',
    'j': 'Holy shinikers!',
    'k': 'Golly gee willikers!',
    'l': 'Zoinks!', 
    'z': 'I guess I\'m whiffing.', 

}

# Flag to control whether the program should listen
listening = False

# Function to send the message for the key pressed
def send_message(key):
    message = key_messages.get(key, None)  # Get the message for the key
    if message:
        time.sleep(0.1) 
        pyautogui.press('t')  
        time.sleep(0.1) 
        pyautogui.write(message, 0.005) 
        pyautogui.press('enter')

# Listen for the 'esc' key to toggle listening mode on and off
def toggle_listening():
    global listening
    listening = not listening 
    if listening:
        status_label.config(text="Listening Enabled", fg="green")
    else:
        status_label.config(text="Listening Disabled", fg="red")

# Function to check if a key is pressed and send the corresponding message
def check_keys():
    if keyboard.is_pressed("="):
            toggle_listening()
            time.sleep(0.1)
    if listening:
        for key in key_messages.keys(): 
            if keyboard.is_pressed(key): 
                send_message(key) 
                break 
    window.after(50, check_keys)  # Re-run this function

# Set up the GUI
window = tk.Tk()
window.title("Keyboard Listener")
window.geometry("600x650")


status_label = tk.Label(window, text="Listening Disabled", fg="red", font=("Arial", 12))
status_label.pack(pady=10)


toggle_button = tk.Button(window, text="Toggle Listening", command=toggle_listening)
toggle_button.pack(pady=10)


keybinds_label = tk.Label(window, text="Keybinds:\n" + "\n".join([f"{key}: {message}" for key, message in key_messages.items()]), font=("Arial", 10), anchor="w", justify="left")
keybinds_label.pack(pady=10, padx=10, anchor="w")

# Start checking keys in the background
window.after(50, check_keys)


window.mainloop()

