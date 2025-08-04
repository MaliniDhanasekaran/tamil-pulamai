import tkinter as tk
import random

class TamilApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("தமிழ் புலமை")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        self.sidebar = tk.Frame(self, width=200, bg="#404040")
        self.sidebar.pack(side="left", fill="y")

        self.container = tk.Frame(self, bg="white")
        self.container.pack(side="right", fill="both", expand=True)

        self.init_menu()
        self.show_tamil_eluthugal()

    def init_menu(self):
        buttons = [
            ("தமிழ் எழுத்துகள்", self.show_tamil_eluthugal),
            ("உயிர் எழுத்துகள்", self.show_uyir_eluthugal),
            ("ஆய்த எழுத்து", self.show_ayutha_eluthu),
            ("மெய் எழுத்துகள்", self.show_mei_eluthugal),
            ("உயிர்மெய் எழுத்துகள்", self.show_uyirmei_eluthugal),
            ("வினாடி வினா", self.show_quiz)
        ]

        for text, command in buttons:
            btn = tk.Button(self.sidebar, text=text, command=command, bg="#606060", fg="white", relief="flat")
            btn.pack(fill="x", pady=2, padx=5)

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_tamil_eluthugal(self):
        self.clear_container()

        tamil_letters = [
            'அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ',
            'க்', 'ங்', 'ச்', 'ஞ்', 'ட்', 'ண்', 'த்', 'ந்', 'ப்', 'ம்', 'ய்', 'ர்', 'ல்', 'வ்', 'ழ்', 'ள்', 'ற்', 'ன்',
            'க', 'கா', 'கி', 'கீ', 'கு', 'கூ', 'கெ', 'கே', 'கை', 'கொ', 'கோ', 'கௌ'
        ]

        grid_frame = tk.Frame(self.container, bg="white")
        grid_frame.grid(row=0, column=0, sticky="nsew")

        row = 0
        col = 0
        for char in tamil_letters:
            tile = tk.Button(grid_frame, text=char, font=("Arial", 20), width=4, height=2)
            tile.grid(row=row, column=col, padx=10, pady=10)
            col += 1
            if col >= 6:
                col = 0
                row += 1

    def show_uyir_eluthugal(self):
        self.clear_container()
        uyir = ['அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ']

        grid_frame = tk.Frame(self.container, bg="white")
        grid_frame.grid(row=0, column=0, sticky="nsew")

        for i, char in enumerate(uyir):
            tile = tk.Button(grid_frame, text=char, font=("Arial", 20), width=4, height=2)
            tile.grid(row=i // 6, column=i % 6, padx=10, pady=10)

    def show_ayutha_eluthu(self):
        self.clear_container()
        ayutha = ['ஃ']

        grid_frame = tk.Frame(self.container, bg="white")
        grid_frame.grid(row=0, column=0, sticky="nsew")

        tile = tk.Button(grid_frame, text=ayutha[0], font=("Arial", 20), width=4, height=2)
        tile.grid(row=0, column=0, padx=10, pady=10)

    def show_mei_eluthugal(self):
        self.clear_container()
        mei = ['க்', 'ங்', 'ச்', 'ஞ்', 'ட்', 'ண்', 'த்', 'ந்', 'ப்', 'ம்', 'ய்', 'ர்', 'ல்', 'வ்', 'ழ்', 'ள்', 'ற்', 'ன்']

        grid_frame = tk.Frame(self.container, bg="white")
        grid_frame.grid(row=0, column=0, sticky="nsew")

        for i, char in enumerate(mei):
            tile = tk.Button(grid_frame, text=char, font=("Arial", 20), width=4, height=2)
            tile.grid(row=i // 6, column=i % 6, padx=10, pady=10)

    def show_uyirmei_eluthugal(self):
        self.clear_container()
        uyir = ['அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ']
        mei = ['க', 'ங', 'ச', 'ஞ', 'ட', 'ண', 'த', 'ந', 'ப', 'ம', 'ய', 'ர', 'ல', 'வ', 'ழ', 'ள', 'ற', 'ன']

        uyirmei = []
        for m in mei:
            for u in uyir:
                combo = m + u
                uyirmei.append(combo)

        grid_frame = tk.Frame(self.container, bg="white")
        grid_frame.grid(row=0, column=0, sticky="nsew")

        row = 0
        col = 0
        for char in uyirmei:
            tile = tk.Button(grid_frame, text=char, font=("Arial", 20), width=4, height=2)
            tile.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col >= 6:
                col = 0
                row += 1

    def show_quiz(self):
        self.clear_container()
        self.quiz_letters = [
            'அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ',
            'க்', 'ங்', 'ச்', 'ஞ்', 'ட்', 'ண்', 'த்', 'ந்', 'ப்', 'ம்', 'ய்', 'ர்', 'ல்', 'வ்', 'ழ்', 'ள்', 'ற்', 'ன்',
            'க', 'கா', 'கி', 'கீ', 'கு', 'கூ', 'கெ', 'கே', 'கை', 'கொ', 'கோ', 'கௌ'
        ]
        random.shuffle(self.quiz_letters)
        self.quiz_index = 0

        self.quiz_frame = tk.Frame(self.container, bg="white")
        self.quiz_frame.grid(row=0, column=0, sticky="nsew")

        self.letter_label = tk.Label(self.quiz_frame, text="", font=("Arial", 40), pady=20)
        self.letter_label.pack()

        self.next_button = tk.Button(self.quiz_frame, text="Next", command=self.next_letter, font=("Arial", 14))
        self.next_button.pack(pady=10)

        self.next_letter()

    def next_letter(self):
        if self.quiz_index < len(self.quiz_letters):
            self.letter_label.config(text=self.quiz_letters[self.quiz_index])
            self.quiz_index += 1
        else:
            self.letter_label.config(text="முடிந்தது!")

if __name__ == "__main__":
    app = TamilApp()
    app.mainloop()