import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random  # <-- added for shuffling

uyir_eluthugal = ["அ", "ஆ", "இ", "ஈ", "உ", "ஊ", "எ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ"]
mei_eluthugal = ["க்", "ங்", "ச்", "ஞ்", "ட்", "ண்", "த்", "ந்", "ப்", "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்", "ன்"]
uyirmei_eluthugal = []
combinations = {
    "அ": "", "ஆ": "ா", "இ": "ி", "ஈ": "ீ", "உ": "ு", "ஊ": "ூ",
    "எ": "ெ", "ஏ": "ே", "ஐ": "ை", "ஒ": "ொ", "ஓ": "ோ", "ஔ": "ௌ"
}

for mei in mei_eluthugal:
    row = []
    for uyir, suffix in combinations.items():
        row.append(mei[0] + suffix)
    uyirmei_eluthugal.append(row)

class TamilApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("தமிழ் புலமை")
        self.geometry("1000x600")

        self.create_widgets()
        self.show_tamil_eluthugal()

    def create_widgets(self):
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.menu_frame = tk.Frame(self.container, bg="lightgrey", width=150)
        self.menu_frame.pack(side="left", fill="y")

        self.content_frame = tk.Frame(self.container)
        self.content_frame.pack(side="left", fill="both", expand=True)

        self.menu_buttons = [
            ("தமிழ் எழுத்துகள்", self.show_tamil_eluthugal),
            ("உயிரெழுத்துகள்", self.show_uyir_eluthugal),
            ("மெய்எழுத்துகள்", self.show_mei_eluthugal),
            ("உயிர்மெய்எழுத்துகள்", self.show_uyirmei_eluthugal),
            ("வினாடி வினா", self.show_vinadi_vina)
        ]

        for text, command in self.menu_buttons:
            b = tk.Button(self.menu_frame, text=text, command=command)
            b.pack(fill="x", padx=10, pady=5)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_uyir_eluthugal(self):
        self.clear_content()
        title = tk.Label(self.content_frame, text="உயிரெழுத்துகள்", font=("Arial", 16))
        title.pack(pady=10)

        grid_frame = tk.Frame(self.content_frame)
        grid_frame.pack()

        for index, letter in enumerate(uyir_eluthugal):
            tile = tk.Label(grid_frame, text=letter, font=("Arial", 18), relief="raised", padx=10, pady=10)
            tile.grid(row=index // 6, column=index % 6, padx=5, pady=5)

    def show_mei_eluthugal(self):
        self.clear_content()
        title = tk.Label(self.content_frame, text="மெய்எழுத்துகள்", font=("Arial", 16))
        title.pack(pady=10)

        grid_frame = tk.Frame(self.content_frame)
        grid_frame.pack()

        for index, letter in enumerate(mei_eluthugal):
            tile = tk.Label(grid_frame, text=letter, font=("Arial", 18), relief="raised", padx=10, pady=10)
            tile.grid(row=index // 6, column=index % 6, padx=5, pady=5)

    def show_uyirmei_eluthugal(self):
        self.clear_content()
        title = tk.Label(self.content_frame, text="உயிர்மெய்எழுத்துகள்", font=("Arial", 16))
        title.pack(pady=10)

        canvas = tk.Canvas(self.content_frame)
        scrollbar = tk.Scrollbar(self.content_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for r, row in enumerate(uyirmei_eluthugal):
            for c, letter in enumerate(row):
                label = tk.Label(scrollable_frame, text=letter, font=("Arial", 14), relief="raised", width=4, height=2)
                label.grid(row=r, column=c, padx=2, pady=2)

    def show_tamil_eluthugal(self):
        self.clear_content()
        title = tk.Label(self.content_frame, text="தமிழ் எழுத்துகள் முழுமையாக", font=("Arial", 16))
        title.pack(pady=10)

        canvas = tk.Canvas(self.content_frame)
        scrollbar = tk.Scrollbar(self.content_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        header_font = ("Arial", 12, "bold")
        tk.Label(scrollable_frame, text="", font=header_font).grid(row=0, column=0)
        for col, uyir in enumerate(uyir_eluthugal):
            tk.Label(scrollable_frame, text=uyir, font=header_font, relief="ridge", width=4).grid(row=0, column=col+1)
        for row, mei in enumerate(mei_eluthugal):
            tk.Label(scrollable_frame, text=mei, font=header_font, relief="ridge", width=4).grid(row=row+1, column=0)
            for col, uyir in enumerate(uyir_eluthugal):
                letter = mei[0] + combinations[uyir]
                tk.Label(scrollable_frame, text=letter, font=("Arial", 14), relief="ridge", width=4).grid(row=row+1, column=col+1)

    def show_vinadi_vina(self):
        self.clear_content()
        self.vinadi_index = 0
        self.quiz_letters = [mei[0] + combinations[uyir] for mei in mei_eluthugal for uyir in uyir_eluthugal]
        random.shuffle(self.quiz_letters)  # <-- Randomly shuffle quiz letters
        self.show_quiz_letter()

    def show_quiz_letter(self):
        self.clear_content()

        if self.vinadi_index >= len(self.quiz_letters):
            label = tk.Label(self.content_frame, text="முடிந்துவிட்டது!", font=("Arial", 24))
            label.pack(pady=20)
            return

        letter = self.quiz_letters[self.vinadi_index]
        label = tk.Label(self.content_frame, text=letter, font=("Arial", 100))
        label.pack(pady=40)

        next_btn = tk.Button(self.content_frame, text="அடுத்து", font=("Arial", 14), command=self.next_quiz_letter)
        next_btn.pack()

    def next_quiz_letter(self):
        self.vinadi_index += 1
        self.show_quiz_letter()

if __name__ == "__main__":
    app = TamilApp()
    app.mainloop()
