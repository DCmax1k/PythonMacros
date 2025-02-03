import keyboard
import pyautogui
import tkinter as tk
import time

# A dictionary of key bindings and their corresponding messages
section1 = 7
section2 = 15
section3 = 22
section4 = 33
key_messages = {
    # Compliments 0 - 7
        '1': 'That was so clean, my monitor just got shinier.',
        '2': 'That shot was MARVELOUS!',
        '3': 'AMAZING shot!',
        '4': 'Teamwork makes the dream work!',
        '5': 'Goalkeeper training arc complete!',
        '6': 'WHAT A SAVEE!',
        'i': 'My teammate is cooking yall!',
        'b': 'Banger alert!',

    # Responses 8 - 15
        '7': 'Thank you mate!',
        '8': 'No problemo!',
        '9': 'Nothing to worry about, we got it!',
        '0': 'My apologies, that ones on me.',
        's': 'Yes.',
        'd': 'No.',
        'f': 'Yup.',
        'g': 'Nah.',

    # Remarks 16 - 22
        'q': 'Everyone lets have a clean, fast paced good game. And don\'t forget to have fun!',
        'w': 'That was a terrific game everyone. Well played!',
        'e': 'That was a close one!',
        '[': 'I just think the current quick chats are outdated, and these new ones are better and more useful!',
        '-': 'I can just type extremely fast, thats all.',
        'm': 'Check score.',
        'h': 'Ain\'t no shame in gettin\' out the game.',

    # Fun phrases 23 - 33
        'r': 'HOLY GUACAMOLE!',
        'o': 'Jeepers!',
        'p': 'Yikes!',
        'a': 'Is there a breeeze!?',
        'j': 'Holy shinikies!',
        'k': 'Golly gee willikers!',
        'l': 'Zoinks!', 
        'z': 'I guess I\'m whiffing.', 
        'c': 'My bad, my controller unplugged.', 
        'v': 'Well butter my biscuit!',
        'n': 'Oops! That\'s a one-way ticket to the report queue.',
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
        #status_label.config(text="Listening Enabled", fg="green")
        toggle_button.config(text="Enabled", fg="green")
    else:
        toggle_button.config(text="Disabled", fg="red")
        #status_label.config(text="Listening Disabled", fg="red")

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
window.geometry("1100x620")

toggle_button = tk.Button(window, text="Disabled", command=toggle_listening, fg="red", font=("Arial", 12))
toggle_button.pack(pady=10)

# Frame
phraseFrame = tk.Frame(window)
phraseFrame.columnconfigure(0, weight=1)
phraseFrame.columnconfigure(1, weight=1)
phraseFrame.columnconfigure(2, weight=1)
phraseFrame.columnconfigure(3, weight=1)

all_keybinds = [f"{key}:    {message}" for key, message in key_messages.items()]
keybind_keys = list(key_messages.keys())
keybind_values = list(key_messages.values())
title_size = 15
keybinds_size = 12
wrap_width = 250
phrase_pady = 3
category_colors = {
    "Compliments": "#A7E22E",
    "Responses": "#66CCFF",
    "Remarks": "#FFB300",
    "Fun Phrases": "#D17BFF"
}

# COMPLIMENTS
compliment_label = tk.Label(phraseFrame, text="Compliments", font=("Arial", title_size), fg="white", bg=category_colors["Compliments"])
compliment_label.grid(row=0, column=0, sticky=tk.W, pady=10)

compliment_label_section = tk.Frame(phraseFrame)
compliment_label_section.columnconfigure(0, weight=1)
compliment_label_section.columnconfigure(1, weight=10)
for i in range(0, section1+1):
    label = tk.Label(compliment_label_section, text=keybind_keys[i], font=("Arial", keybinds_size+2), fg="white", bg=category_colors["Compliments"], justify="left")
    label.grid(row=i, column=0, sticky=tk.W+tk.N, pady=phrase_pady)
for j in range(0, section1+1):
    label = tk.Label(compliment_label_section, text=keybind_values[j], font=("Arial", keybinds_size), justify="left", wraplength=wrap_width)
    label.grid(row=j, column=1, sticky=tk.W, pady=phrase_pady)
compliment_label_section.grid(row=1, column=0, sticky="news")


# RESPONSES
responses_label = tk.Label(phraseFrame, text="Responses", font=("Arial", title_size), fg="white", bg=category_colors["Responses"])
responses_label.grid(row=0, column=1, sticky=tk.W, pady=10)

responses_label_section = tk.Frame(phraseFrame)
responses_label_section.columnconfigure(0, weight=1)
responses_label_section.columnconfigure(1, weight=10)
for i in range(section1+1, section2+1):
    label = tk.Label(responses_label_section, text=keybind_keys[i], font=("Arial", keybinds_size+2), fg="white", bg=category_colors["Responses"], justify="left")
    label.grid(row=i-section1, column=0, sticky=tk.W+tk.N, pady=phrase_pady)
for j in range(section1+1, section2+1):
    label = tk.Label(responses_label_section, text=keybind_values[j], font=("Arial", keybinds_size), justify="left", wraplength=wrap_width)
    label.grid(row=j-section1, column=1, sticky=tk.W, pady=phrase_pady)
responses_label_section.grid(row=1, column=1, sticky="news")


# REMARKS
remarks_label = tk.Label(phraseFrame, text="Remarks", font=("Arial", title_size), fg="white", bg=category_colors["Remarks"])
remarks_label.grid(row=0, column=2, sticky=tk.W, pady=10)

remarks_label_section = tk.Frame(phraseFrame)
remarks_label_section.columnconfigure(0, weight=1)
remarks_label_section.columnconfigure(1, weight=10)
for i in range(section2+1, section3+1):
    label = tk.Label(remarks_label_section, text=keybind_keys[i], font=("Arial", keybinds_size+2), fg="white", bg=category_colors["Remarks"], justify="left")
    label.grid(row=i-section2, column=0, sticky=tk.W+tk.N, pady=phrase_pady)
for j in range(section2+1, section3+1):
    label = tk.Label(remarks_label_section, text=keybind_values[j], font=("Arial", keybinds_size), justify="left", wraplength=wrap_width)
    label.grid(row=j-section2, column=1, sticky=tk.W, pady=phrase_pady)
remarks_label_section.grid(row=1, column=2, sticky="news")


# FUN PHRASES
phrases_label = tk.Label(phraseFrame, text="Fun Phrases", font=("Arial", title_size), fg="white", bg=category_colors["Fun Phrases"])
phrases_label.grid(row=0, column=3, sticky=tk.W, pady=10)

funphrases_label_section = tk.Frame(phraseFrame)
funphrases_label_section.columnconfigure(0, weight=1)
funphrases_label_section.columnconfigure(1, weight=10)
for i in range(section3+1, section4+1):
    label = tk.Label(funphrases_label_section, text=keybind_keys[i], font=("Arial", keybinds_size+2), fg="white", bg=category_colors["Fun Phrases"], justify="left")
    label.grid(row=i-section3, column=0, sticky=tk.W+tk.N, pady=phrase_pady)
for j in range(section3+1, section4+1):
    label = tk.Label(funphrases_label_section, text=keybind_values[j], font=("Arial", keybinds_size), justify="left", wraplength=wrap_width)
    label.grid(row=j-section3, column=1, sticky=tk.W, pady=phrase_pady)
funphrases_label_section.grid(row=1, column=3, sticky="news")

phraseFrame.pack(pady=10, padx=10, fill='x')

# Start checking keys in the background
window.after(50, check_keys)

window.mainloop()

