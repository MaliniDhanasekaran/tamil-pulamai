import tkinter as tk
from tkinter import ttk

# Splash Screen Function
def show_splash():
    splash = tk.Toplevel()
    splash.overrideredirect(True)
    splash.configure(bg='white')
    splash.geometry("400x200+500+300")

    label = tk.Label(splash, text="தமிழ் புலமை", font=("Latha", 30, "bold"), fg="dark green", bg='white')
    label.pack(expand=True)

    splash.after(2000, splash.destroy)  # Display for 2 seconds

# Main Application
def main_app():
    root = tk.Tk()
    root.title("தமிழ் புலமை")
    root.geometry("800x500")

    # Left Menu Frame
    menu_frame = tk.Frame(root, width=200, bg="lightgrey")
    menu_frame.pack(side="left", fill="y")

    content_frame = tk.Frame(root, bg="white")
    content_frame.pack(side="right", expand=True, fill="both")

    # Content Label
    content_label = tk.Label(content_frame, text="", font=("Latha", 20), bg="white")
    content_label.pack(padx=20, pady=20)

    # Button Handlers
    def show_uyir():
        content_label.config(text="அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ")

    def show_mei():
        content_label.config(text="க் ச் ட் ண் த் ந் ப் ம் ய் ர் ல் வ் ழ் ள் ற் ன்")

    # Menu Buttons
    ttk.Button(menu_frame, text="உயிர் எழுத்துகள்", command=show_uyir).pack(pady=10, fill='x')
    ttk.Button(menu_frame, text="மெய் எழுத்துகள்", command=show_mei).pack(pady=10, fill='x')

    root.mainloop()

# Initialize with splash screen
root = tk.Tk()
root.withdraw()  # Hide main window
show_splash()

# Show main app after splash screen
root.after(2000, lambda: [root.destroy(), main_app()])
root.mainloop()
