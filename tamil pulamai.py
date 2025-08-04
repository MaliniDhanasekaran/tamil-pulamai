import tkinter as tk
import random

# Tamil letter groups
uyir_eluthugal = [
    "அ", "ஆ", "இ", "ஈ", "உ", "ஊ", "எ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ"
]

mei_eluthugal = [
    "க்", "ங்", "ச்", "ஞ்", "ட்", "ண்", "த்", "ந்", "ப்", "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்", "ன்"
]

uyirmei_eluthugal = []
# Combine uyir + mei to create 216 uyirmei letters (excluding invalid ones)
combinations = {
    "அ": "", "ஆ": "ா", "இ": "ி", "ஈ": "ீ", "உ": "ு", "ஊ": "ூ", 
    "எ": "ெ", "ஏ": "ே", "ஐ": "ை", "ஒ": "ொ", "ஓ": "ோ", "ஔ": "ௌ"
}

# Mei letters with base consonant
mei_base = [
    ("க்", "க"), ("ங்", "ங"), ("ச்", "ச"), ("ஞ்", "ஞ"),
    ("ட்", "ட"), ("ண்", "ண"), ("த்", "த"), ("ந்", "ந"),
    ("ப்", "ப"), ("ம்", "ம"), ("ய்", "ய"), ("ர்", "ர"),
    ("ல்", "ல"), ("வ்", "வ"), ("ழ்", "ழ"), ("ள்", "ள"),
    ("ற்", "ற"), ("ன்", "ன")
]

for mei, base in mei_base:
    for uyir, suffix in combinations.items():
        if uyir == "அ":
            uyirmei_eluthugal.append(base)
        else:
            uyirmei_eluthugal.append(base + suffix)

# Aaytha ezhuthu
aaytha_eluthu = ["ஃ"]

class TamilApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("தமிழ் புலமை (Tamil Pulamai)")
        self.root.geometry("800x600")

        self.create_widgets()
        self.show_tamil_eluthugal()
        self.root.mainloop()

    def create_widgets(self):
        self.menu_frame = tk.Frame(self.root, bg="#333")
        self.menu_frame.pack(side="left", fill="y")

        self.main_frame = tk.Frame(self.root, bg="#f4f4f4")
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.buttons = [
            ("தமிழ் எழுத்துகள்", self.show_tamil_eluthugal),
            ("உயிர் எழுத்துகள்", self.show_uyir),
            ("ஆய்த எழுத்து", self.show_aaytha),
            ("மெய் எழுத்துகள்", self.show_mei),
            ("உயிர் மெய் எழுத்துகள்", self.show_uyirmei),
            ("வினாடி வினா", self.show_quiz)
        ]

        for text, command in self.buttons:
            btn = tk.Button(self.menu_frame, text=text, fg="white", bg="#555", font=("Arial", 12), command=command)
            btn.pack(fill="x", padx=5, pady=5)

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_letters(self, letters):
        self.clear_main_frame()
        container = tk.Frame(self.main_frame, bg="#f4f4f4")
        container.pack(padx=20, pady=20)
        row = col = 0
        for letter in letters:
            tile = tk.Button(container, text=letter, width=5, height=2, font=("Arial", 20), relief="raised", bg="#fff")
            tile.grid(row=row, column=col, padx=10, pady=10)
            col += 1
            if col >= 10:
                col = 0
                row += 1

    def show_tamil_eluthugal(self):
        all_letters = uyir_eluthugal + aaytha_eluthu + [mei for mei, _ in mei_base] + uyirmei_eluthugal
        self.show_letters(all_letters)

    def show_uyir(self):
        self.show_letters(uyir_eluthugal)

    def show_mei(self):
        self.show_letters([mei for mei, _ in mei_base])

    def show_aaytha(self):
        self.show_letters(aaytha_eluthu)

    def show_uyirmei(self):
        self.show_letters(uyirmei_eluthugal)

    def show_quiz(self):
        self.clear_main_frame()
        self.quiz_index = 0
        self.quiz_letters = random.sample(uyir_eluthugal + aaytha_eluthu + [mei for mei, _ in mei_base] + uyirmei_eluthugal, len(uyir_eluthugal + aaytha_eluthu + mei_eluthugal + uyirmei_eluthugal))

        self.quiz_label = tk.Label(self.main_frame, text=self.quiz_letters[self.quiz_index], font=("Arial", 100), bg="#f4f4f4")
        self.quiz_label.pack(pady=100)

        self.next_btn = tk.Button(self.main_frame, text="அடுத்தது (Next)", command=self.next_quiz, font=("Arial", 16))
        self.next_btn.pack(pady=20)

    def next_quiz(self):
        self.quiz_index += 1
        if self.quiz_index >= len(self.quiz_letters):
            self.quiz_label.config(text="முடிந்தது! (Done!)")
            self.next_btn.config(state="disabled")
        else:
            self.quiz_label.config(text=self.quiz_letters[self.quiz_index])

if __name__ == "__main__":
    app = TamilApp()
