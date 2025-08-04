import tkinter as tk
from tkinter import ttk
import random

# Define Tamil letters
uyir_eluthugal = ["அ", "ஆ", "இ", "ஈ", "உ", "ஊ", "எ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ"]
mei_eluthugal = ["க்", "ங்", "ச்", "ஞ்", "ட்", "ண்", "த்", "ந்", "ப்", "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்", "ன"]
aaytha_eluthu = ["ஃ"]

# 216 UyirMei combinations
uyirmei_eluthugal = []
combinations = {
    "அ": "", "ஆ": "ா", "இ": "ி", "ஈ": "ீ", "உ": "ு", "ஊ": "ூ",
    "எ": "ெ", "ஏ": "ே", "ஐ": "ை", "ஒ": "ொ", "ஓ": "ோ", "ஔ": "ௌ"
}

for mei in mei_eluthugal:
    row = []
    for uyir, suffix in combinations.items():
        if mei[0] in ["ங", "ஞ", "ண", "ந", "ம", "ன"] and uyir in ["ஔ"]:
            row.append("")
        else:
            row.append(mei[0] + suffix)
    uyirmei_eluthugal.append(row)

class TamilApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("தமிழ் புலமை")
        self.geometry("1000x600")

        self.create_widgets()

    def create_widgets(self):
        # Create navigation menu
        self.menu_frame = tk.Frame(self, bg="#f0f0f0", width=150)
        self.menu_frame.pack(side="left", fill="y")

        menu_items = [
            ("தமிழ் எழுத்துகள்", self.show_tamil_eluthugal),
            ("உயிர் எழுத்துகள்", self.show_uyir_eluthugal),
            ("ஆய்த எழுத்து", self.show_aaytha_eluthu),
            ("மெய் எழுத்துகள்", self.show_mei_eluthugal),
            ("உயிர் மெய் எழுத்துகள்", self.show_uyir_mei_eluthugal),
            ("வினாடி வினா", self.show_quiz),
        ]

        for name, command in menu_items:
            button = tk.Button(self.menu_frame, text=name, font=("Arial", 10), command=command, width=20, anchor="w")
            button.pack(pady=5, padx=5)

        # Main content frame
        self.content_frame = tk.Frame(self, bg="white")
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.show_tamil_eluthugal()

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_tamil_eluthugal(self):
        self.clear_content()
        label = tk.Label(self.content_frame, text="தமிழ் எழுத்துகள்", font=("Arial", 16))
        label.pack(pady=10)

    def show_uyir_eluthugal(self):
        self.clear_content()
        label = tk.Label(self.content_frame, text="உயிர் எழுத்துகள்", font=("Arial", 16))
        label.pack(pady=10)
        self.display_tiles(uyir_eluthugal)

    def show_mei_eluthugal(self):
        self.clear_content()
        label = tk.Label(self.content_frame, text="மெய் எழுத்துகள்", font=("Arial", 16))
        label.pack(pady=10)
        self.display_tiles(mei_eluthugal)

    def show_aaytha_eluthu(self):
        self.clear_content()
        label = tk.Label(self.content_frame, text="ஆய்த எழுத்து", font=("Arial", 16))
        label.pack(pady=10)
        self.display_tiles(aaytha_eluthu)

    def show_uyir_mei_eluthugal(self):
        self.clear_content()
        label = tk.Label(self.content_frame, text="உயிர் மெய் எழுத்துகள் (216)", font=("Arial", 16))
        label.pack(pady=10)

        table_frame = tk.Frame(self.content_frame, bg="white")
        table_frame.pack(padx=10, pady=10)

        for i, row in enumerate(uyirmei_eluthugal):
            for j, letter in enumerate(row):
                if letter:
                    tile = tk.Label(table_frame, text=letter, font=("Arial", 14), bd=1, relief="ridge", padx=10, pady=10)
                    tile.grid(row=i, column=j, padx=2, pady=2)

    def show_quiz(self):
        self.clear_content()
        label = tk.Label(self.content_frame, text="வினாடி வினா", font=("Arial", 16))
        label.pack(pady=10)

        self.quiz_index = 0
        self.quiz_letters = uyir_eluthugal + mei_eluthugal + [l for row in uyirmei_eluthugal for l in row if l]
        random.shuffle(self.quiz_letters)

        self.quiz_label = tk.Label(self.content_frame, text="", font=("Arial", 30))
        self.quiz_label.pack(pady=20)

        self.next_button = tk.Button(self.content_frame, text="அடுத்தது", command=self.next_question)
        self.next_button.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.quiz_index < len(self.quiz_letters):
            self.quiz_label.config(text=self.quiz_letters[self.quiz_index])
            self.quiz_index += 1
        else:
            self.quiz_label.config(text="முடிந்தது!")

    def display_tiles(self, letters):
        grid_frame = tk.Frame(self.content_frame, bg="white")
        grid_frame.pack(padx=10, pady=10)

        for i, letter in enumerate(letters):
            tile = tk.Label(grid_frame, text=letter, font=("Arial", 14), bd=1, relief="ridge", padx=10, pady=10)
            tile.grid(row=i//6, column=i%6, padx=5, pady=5)

if __name__ == "__main__":
    app = TamilApp()
    app.mainloop()