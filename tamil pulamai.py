import tkinter as tk
from tkinter import ttk

# Tamil letters
uyir_letters = ["அ", "ஆ", "இ", "ஈ", "உ", "ஊ", "எ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ"]
mei_letters = ["க்", "ச்", "ட்", "ண்", "த்", "ந்", "ப்", "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்", "ன்"]

# Splash Screen
def show_splash():
    splash = tk.Toplevel()
    splash.overrideredirect(True)
    splash.configure(bg='white')
    splash.geometry("400x200+500+300")

    label = tk.Label(splash, text="தமிழ் புலமை", font=("Latha", 30, "bold"), fg="dark green", bg='white')
    label.pack(expand=True)

    splash.after(2000, splash.destroy)

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
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def clear_content():
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

    # Display Full Tamil Letters Chart
    def show_chart():
        clear_content()
        tk.Label(scrollable_frame, text="தமிழ் எழுத்து பட்டியல்", font=("Latha", 26, "bold"), bg="white", fg="dark blue").pack(pady=10)

        table_frame = tk.Frame(scrollable_frame, bg="white")
        table_frame.pack()

        header = [""] + uyir_letters
        uyirmei_map = {
            "க": ["க", "கா", "கி", "கீ", "கு", "கூ", "கெ", "கே", "கை", "கொ", "கோ", "கௌ"],
            "ச": ["ச", "சா", "சி", "சீ", "சு", "சூ", "செ", "சே", "சை", "சொ", "சோ", "சௌ"],
            "ட": ["ட", "டா", "டி", "டீ", "டு", "டூ", "டெ", "டே", "டை", "டொ", "டோ", "டௌ"],
            "ண": ["ண", "ணா", "ணி", "ணீ", "ணு", "ணூ", "ணெ", "ணே", "ணை", "ணொ", "ணோ", "ணௌ"],
            "த": ["த", "தா", "தி", "தீ", "து", "தூ", "தெ", "தே", "தை", "தொ", "தோ", "தௌ"],
            "ந": ["ந", "நா", "நி", "நீ", "நு", "நூ", "நெ", "நே", "நை", "நொ", "நோ", "நௌ"],
            "ப": ["ப", "பா", "பி", "பீ", "பு", "பூ", "பெ", "பே", "பை", "பொ", "போ", "பௌ"],
            "ம": ["ம", "மா", "மி", "மீ", "மு", "மூ", "மெ", "மே", "மை", "மொ", "மோ", "மௌ"],
            "ய": ["ய", "யா", "யி", "யீ", "யு", "யூ", "யெ", "யே", "யை", "யொ", "யோ", "யௌ"],
            "ர": ["ர", "ரா", "ரி", "ரீ", "ரு", "ரூ", "ரெ", "ரே", "ரை", "ரொ", "ரோ", "ரௌ"],
            "ல": ["ல", "லா", "லி", "லீ", "லு", "லூ", "லெ", "லே", "லை", "லொ", "லோ", "லௌ"],
            "வ": ["வ", "வா", "வி", "வீ", "வு", "வூ", "வெ", "வே", "வை", "வொ", "வோ", "வௌ"],
            "ழ": ["ழ", "ழா", "ழி", "ழீ", "ழு", "ழூ", "ழெ", "ழே", "ழை", "ழொ", "ழோ", "ழௌ"],
            "ள": ["ள", "ளா", "ளி", "ளீ", "ளு", "ளூ", "ளெ", "ளே", "ளை", "ளொ", "ளோ", "ளௌ"],
            "ற": ["ற", "றா", "றி", "றீ", "று", "றூ", "றெ", "றே", "றை", "றொ", "றோ", "றௌ"],
            "ன": ["ன", "னா", "னி", "னீ", "னு", "னூ", "னெ", "னே", "னை", "னொ", "னோ", "னௌ"]
        }

        for j, h in enumerate(header):
            tk.Label(table_frame, text=h, font=("Latha", 16, "bold"), borderwidth=1, relief="solid", width=5, bg="#f0f0f0").grid(row=0, column=j)

        for i, mei in enumerate(uyirmei_map.keys()):
            tk.Label(table_frame, text=mei, font=("Latha", 16, "bold"), borderwidth=1, relief="solid", width=5, bg="#f0f0f0").grid(row=i+1, column=0)
            for j, letter in enumerate(uyirmei_map[mei]):
                tk.Label(table_frame, text=letter, font=("Latha", 16), borderwidth=1, relief="solid", width=5).grid(row=i+1, column=j+1)

    # Display Uyir Letters
    def show_uyir():
        clear_content()
        label = tk.Label(scrollable_frame, text="உயிர் எழுத்துகள்:\nஅ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ",
                         font=("Latha", 24), bg="white", fg="black")
        label.pack(pady=20)

    # Display Ayudha Ezhuthu
    def show_ayutha():
        clear_content()
        label = tk.Label(scrollable_frame, text="ஆய்த எழுத்து:\nஃ", font=("Latha", 30), bg="white", fg="dark red")
        label.pack(pady=20)
        desc = tk.Label(scrollable_frame,
                        text="ஃ - ஆய்த எழுத்து (Ayudha Ezhuthu) is a special character in Tamil.\nIt is not a vowel or consonant and is used phonetically in some words.",
                        font=("Arial", 16), bg="white", wraplength=600, justify="left")
        desc.pack(pady=10)

    # Display Mei Letters
    def show_mei():
        clear_content()
        label = tk.Label(scrollable_frame, text="மெய் எழுத்துகள்:\nக் ச் ட் ண் த் ந் ப் ம் ய் ர் ல் வ் ழ் ள் ற் ன்",
                         font=("Latha", 24), bg="white", fg="black")
        label.pack(pady=20)

    # Display UyirMei Chart
    def show_uyirmei():
        clear_content()
        label = tk.Label(scrollable_frame, text="உயிர்மெய் எழுத்துகள்:\nThese are compound letters formed by combining Uyir + Mei.",
                         font=("Arial", 18), bg="white", fg="black")
        label.pack(pady=20)
        show_chart()

    # LEFT MENU (ORDERED)
    ttk.Button(menu_frame, text="தமிழ் எழுத்துகள்", command=show_chart).pack(pady=10, fill='x')
    ttk.Button(menu_frame, text="உயிர் எழுத்துகள்", command=show_uyir).pack(pady=10, fill='x')
    ttk.Button(menu_frame, text="ஆய்த எழுத்து", command=show_ayutha).pack(pady=10, fill='x')
    ttk.Button(menu_frame, text="மெய் எழுத்துகள்", command=show_mei).pack(pady=10, fill='x')
    ttk.Button(menu_frame, text="உயிர்மெய் எழுத்துகள்", command=show_uyirmei).pack(pady=10, fill='x')

    root.mainloop()

# Run with splash
root = tk.Tk()
root.withdraw()
show_splash()
root.after(2000, lambda: [root.destroy(), main_app()])
root.mainloop()
