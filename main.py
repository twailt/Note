from tkinter import *
from tkinter import filedialog

def save_file(event=None):
    file_path = filedialog.asksaveasfilename(defaultextension='.txt') # Ask user for a file path to save
    if file_path: # If a path is provided
        with open(file_path, 'w') as file: # Open the file for writing
            file.write(text_area.get("1.0", END)) # Write the content of the text area to the file

def open_file(event=None):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")]) # Ask user for a file path to open
    if file_path: # If a path is provided
        with open(file_path, 'r') as file: # Open the file for reading
            text_area.delete("1.0", END) # Clear the content of the text area
            text_area.insert(END, file.read()) # Insert the file's content into the text area

def delete_text(event=None):
    text_area.delete("1.0", END) # Delete all text content

def change_to_light_theme(event=None):
    root.configure(bg='white')
    text_area.configure(bg='white', fg='black')

def change_to_black_theme(event=None):
    root.configure(bg='black')
    text_area.configure(bg='black', fg='white')

root = Tk() # Create the main window
root.title("Death Note") # Set the window title

text_area = Text(root) # Create the text area
text_area.pack(fill=BOTH, expand=True) # Place the text area in the main window, filling all available space

root.minsize(350, 500) # Set the minimum size of the main window

button_frame = Frame(root) # Create a frame for the buttons
button_frame.pack(side='top', fill=X) # Place the button frame at the top of the main window

save_button = Button(root, text='Save', command=save_file) # Create the Save button
save_button.pack(side=LEFT, padx=5, pady=5) # Place the Save button on the left side of the button frame

open_button = Button(root, text="Open", command=open_file) # Create the Open button
open_button.pack(side=LEFT, padx=5, pady=5) # Place the Open button in the center of the button frame

delete_button = Button(root, text="Delete All", command=delete_text) # Create the Delete All button
delete_button.pack(side=LEFT, padx=5, pady=5) # Place the Delete All button on the right side of the button frame

Light_Theme = Button(root, text="Light Theme", command=change_to_light_theme) 
Light_Theme.pack(side=LEFT, padx=5, pady=5) 

Black_Theme = Button(root, text="Black Theme", command=change_to_black_theme) 
Black_Theme.pack(side=LEFT, padx=5, pady=5) 

# Bind hotkeys to functions
root.bind("<Control-s>", save_file) # Bind Ctrl + S to the save_file function
root.bind("<Control-o>", open_file) # Bind Ctrl + O to the open_file function
root.bind("<Control-d>", delete_text) # Bind Ctrl + D to the delete_text function
root.bind("<Control-l>", change_to_light_theme)
root.bind("<Control-b>", change_to_black_theme)

root.mainloop() # Start the main window event loop
