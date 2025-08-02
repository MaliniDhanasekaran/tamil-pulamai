import tkinter as tk
from tkinter import ttk

# Tamil letters
uyir_eluthugal = "அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ"
mei_eluthugal = "க் ச் ட் ண் த் ந் ப் ம் ய் ர் ல் வ் ழ் ள் ற் ன்"
uyir_letters = ["அ", "ஆ", "இ", "ஈ", "உ", "ஊ", "எ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ"]
mei_letters = ["க", "ச", "ட", "ண", "த", "ந", "ப", "ம", "ய", "ர", "ல", "வ", "ழ", "ள", "ற", "ன"]

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
    root.geometry("1000x600")

    # Left Menu Frame
    menu_frame = tk.Frame(root, width=200, bg="lightgrey")
    menu_frame.pack(side="left", fill="y")

    content_frame = tk.Frame(root, bg="white")
    content_frame.pack(side="right", expand=True, fill="both")

    # Scrollable Canvas inside content_frame
    canvas = tk.Canvas(content_frame, bg="white")
    scrollbar = tk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="white")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def clear_content():
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

    # Button Handlers
    def show_uyir():
        clear_content()
        label = tk.Label(scrollable_frame, text="உயிர் எழுத்துகள்:\n" + uyir_eluthugal,
                         font=("Latha", 24), bg="white", fg="black")
        label.pack(pady=20)

    def show_mei():
        clear_content()
        label = tk.Label(scrollable_frame, text="மெய் எழுத்துகள்:\n" + mei_eluthugal,
                         font=("Latha", 24), bg="white", fg="black")
        label.pack(pady=20)

    def show_chart():
        clear_content()
        tk.Label(scrollable_frame, text="தமிழ் எழுத்து பட்டியல்", font=("Latha", 26, "bold"), bg="white", fg="dark blue").pack(pady=10)

        table_frame = tk.Frame(scrollable_frame, bg="white")
        table_frame.pack()

        header = [""] + uyir_letters
        # Header Row
        for j, h in enumerate(header):
            tk.Label(table_frame, text=h, font=("Latha", 16, "bold"), borderwidth=1, relief="solid", width=5, bg="#f0f0f0").grid(row=0, column=j, padx=1, pady=1)

        # Data Rows
        for i, mei in enumerate(mei_letters):
            tk.Label(table_frame, text=mei, font=("Latha", 16, "bold"), borderwidth=1, relief="solid", width=5, bg="#f0f0f0").grid(row=i+1, column=0, padx=1, pady=1)
            for j, uyir in enumerate(uyir_letters):
                cell = mei + uyir
                tk.Label(table_frame, text=cell, font=("Latha", 16), borderwidth=1, relief="solid", width=5).grid(row=i+1, column=j+1, padx=1, pady=1)

    # Menu Buttons
    ttk.Button(menu_frame, text="உயிர் எழுத்துகள்", command=show_uyir).pack(pady=10, fill='x')
    ttk.Button(menu_frame, text="மெய் எழுத்துகள்", command=show_mei).pack(pady=10, fill='x')
    ttk.Button(menu_frame, text="தமிழ் எழுத்துகள்", command=show_chart).pack(pady=10, fill='x')

    root.mainloop()

# Initialize with splash screen
root = tk.Tk()
root.withdraw()  # Hide main window
show_splash()

# Show main app after splash screen
root.after(2000, lambda: [root.destroy(), main_app()])
root.mainloop()
