import discordrp
import time
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
import threading

client_id = "your_application_id" # you can visit the discord developar portal to generate one.

def update_presence():
    try:
        state = state_entry.get()
        details = details_entry.get()
        large_image = large_image_entry.get()
        large_text = large_text_entry.get()
        small_image = small_image_entry.get()
        small_text = small_text_entry.get()

        button1_label = button1_label_entry.get()
        button1_url = button1_url_entry.get()

        button2_label = button2_label_entry.get()
        button2_url = button2_url_entry.get()

        presence_data = {
            "state": state,
            "details": details,
            "timestamps": {
                "start": int(time.time()),
            },
            "assets": {
                "large_image": large_image,
                "large_text": large_text,
                "small_image": small_image,
                "small_text": small_text,
            },
            "buttons": [
                {
                    "label": button1_label,
                    "url": button1_url,
                },
                {
                    "label": button2_label,
                    "url": button2_url,
                },
            ],
        }
        presence.set(presence_data)
        status_label.config(text="Presence updated")
    except Exception as e:
        status_label.config(text="Error: " + str(e))
def exit_application():
    root.quit()
def save_presence():
    presence_data = {
        "state": state_entry.get(),
        "details": details_entry.get(),
        "large_image": large_image_entry.get(),
        "large_text": large_text_entry.get(),
        "small_image": small_image_entry.get(),
        "small_text": small_text_entry.get(),
        "button1_label": button1_label_entry.get(),
        "button1_url": button1_url_entry.get(),
        "button2_label": button2_label_entry.get(),
        "button2_url": button2_url_entry.get(),
    }

    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if file_path:
        with open(file_path, "w") as file:
            json.dump(presence_data, file)
            status_label.config(text=f"Presence saved to {file_path}")
def load_presence():
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file_path:
        with open(file_path, "r") as file:
            presence_data = json.load(file)
            state_entry.delete(0, tk.END)
            state_entry.insert(0, presence_data.get("state", ""))
            details_entry.delete(0, tk.END)
            details_entry.insert(0, presence_data.get("details", ""))
            large_image_entry.delete(0, tk.END)
            large_image_entry.insert(0, presence_data.get("large_image", ""))
            large_text_entry.delete(0, tk.END)
            large_text_entry.insert(0, presence_data.get("large_text", ""))
            small_image_entry.delete(0, tk.END)
            small_image_entry.insert(0, presence_data.get("small_image", ""))
            small_text_entry.delete(0, tk.END)
            small_text_entry.insert(0, presence_data.get("small_text", ""))
            button1_label_entry.delete(0, tk.END)
            button1_label_entry.insert(0, presence_data.get("button1_label", ""))
            button1_url_entry.delete(0, tk.END)
            button1_url_entry.insert(0, presence_data.get("button1_url", ""))
            button2_label_entry.delete(0, tk.END)
            button2_label_entry.insert(0, presence_data.get("button2_label", ""))
            button2_url_entry.delete(0, tk.END)
            button2_url_entry.insert(0, presence_data.get("button2_url", ""))
            status_label.config(text=f"Presence loaded from {file_path}")
def stop_presence():
    presence.clear()
    status_label.config(text="Presence stopped")
def display_help():
    help_text = """Discord Rich Presence Help
- State: The state of your current activity.
- Details: Details about your current activity.
- Large Image assest code or url: the image assest code generated in the developer portal rich presence section or you can use the image url.
- Image Text: Text to display for the large image.
- Small Image assest code or url: the image assest code generated in the developer portal rich presence section or you can use the image url.
- Small Image Text: Text to display for the small image.
- Button 1 Label: Label for the first button.
- Button 1 URL: URL to open when the first button is clicked.
- Button 2 Label: Label for the second button.
- Button 2 URL: URL to open when the second button is clicked.
Click 'Update Presence' to update your Discord Rich Presence based on the provided information.

developor: ore.e
"""
    help_window = tk.Toplevel(root)
    help_window.title("Help")
    help_label = ttk.Label(help_window, text=help_text, wraplength=400, font=("Arial", 12))
    help_label.pack(padx=10, pady=10)
def toggle_dark_mode():
    dark_mode = dark_mode_var.get()
    if dark_mode:
        background_color = "#333"
        foreground_color = "#EEE"
        button_background_color = "black"
        button_foreground_color = "white"
    else:
        background_color = "white"
        foreground_color = "black"
        button_background_color = "#4CAF50"
        button_foreground_color = "white"
    root.tk_setPalette(background=background_color, foreground=foreground_color)
    style.configure("Custom.TLabel", foreground=foreground_color)
    style.configure("Custom.TEntry", background=background_color, foreground=foreground_color)
    style.configure("Custom.TButton", background=button_background_color, borderwidth=1, relief="raised")
    style.configure("Round.TButton", background=button_background_color, borderwidth=1, relief="raised", foreground=button_foreground_color)
    update_button.configure(style="RoundDark.TButton" if dark_mode else "Round.TButton")


root = tk.Tk()
root.title("Discord Rich Presence")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
style = ttk.Style()
style.theme_use("clam") 
style.configure("Custom.TLabel", padding=5, font=("Arial", 12))
style.configure("Custom.TEntry", padding=5, font=("Arial", 12))
style.configure("Custom.TButton", padding=5, relief="raised", background="#4CAF50", borderwidth=1)
style.configure("Round.TButton", padding=5, relief="raised", background="#4CAF50", borderwidth=1, foreground="white")
style.configure("RoundDark.TButton", padding=5, relief="raised", background="#4CAF50", borderwidth=1, foreground="black")
dark_mode_var = tk.BooleanVar(value=False)
def create_label_entry(parent, text, row, col):
    label = ttk.Label(parent, text=text, style="Custom.TLabel")
    label.grid(row=row, column=col, sticky="w")
    entry = ttk.Entry(parent, style="Custom.TEntry")
    entry.grid(row=row, column=col+1, sticky="ew")
    return entry
    
row = 0
state_entry = create_label_entry(root, "State:", row, 0)
row += 1
details_entry = create_label_entry(root, "Details:", row, 0)
row += 1
large_image_entry = create_label_entry(root, "Large Image assest code/url:", row, 0)
row += 1
large_text_entry = create_label_entry(root, "Image Text:", row, 0)
row += 1
small_image_entry = create_label_entry(root, "Small Image assest code/url:", row, 0)
row += 1
small_text_entry = create_label_entry(root, "Small Image Text:", row, 0)
row += 1
button1_label_entry = create_label_entry(root, "Button 1 Label:", row, 0)
row += 1
button1_url_entry = create_label_entry(root, "Button 1 URL:", row, 0)
row += 1
button2_label_entry = create_label_entry(root, "Button 2 Label:", row, 0)
row += 1
button2_url_entry = create_label_entry(root, "Button 2 URL:", row, 0)
row += 1
update_button = ttk.Button(root, text="Update Presence", command=update_presence, style="Round.TButton")
update_button.grid(row=row, column=0, columnspan=2, pady=(10, 20), sticky="w")
stop_button = ttk.Button(root, text="Stop Presence", command=stop_presence, style="RoundStop.TButton")
stop_button.grid(row=row, column=2, columnspan=2, pady=(10, 20), sticky="w")
dark_mode_checkbutton = ttk.Checkbutton(root, text="Dark Mode", variable=dark_mode_var, command=toggle_dark_mode, style="Custom.TLabel")
dark_mode_checkbutton.grid(row=0, column=3, padx=10)
status_label = ttk.Label(root, text="", style="Custom.TLabel")
status_label.grid(row=row+1, column=0, columnspan=4)
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_presence)
file_menu.add_command(label="Load", command=load_presence)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_application)
help_menu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Show Help", command=display_help)
with discordrp.Presence(client_id) as presence:
    print("Connected")
    root.mainloop()