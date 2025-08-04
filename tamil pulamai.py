import tkinter as tk
from tkinter import ttk
import random

# Tamil letters
uyir_eluthugal = ["அ", "ஆ", "இ", "ஈ", "உ", "ஊ", "எ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ"]
mei_eluthugal = ["க்", "ச்", "ட்", "த்", "ப்", "ற்", "ஞ்", "ங்", "ண்", "ந்", "ம்", "ன்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்"]
mei_eluthugal[-1] = "ன்"  # Add dot

# UyirMei logic
kombu = {
    "அ": "", "ஆ": "ா", "இ": "ி", "ஈ": "ீ", "உ": "ு", "ஊ": "ூ",
    "எ": "ெ", "ஏ": "ே", "ஐ": "ை", "ஒ": "ொ", "ஓ": "ோ", "ஔ": "ௌ"
}

uyirmei_eluthugal = []
for mei in mei_eluthugal:
    row = []
    for uyir in uyir_eluthugal:
        uyirmei = mei[0] + kombu[uyir]
        row.append(uyirmei)
    uyirmei_eluthugal.append(row)

# Quiz Questions
quiz_questions = random.sample(sum(uyirmei_eluthugal, []), 10)

# App Class
class TamilApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("தமிழ் புலமை")
        self.geometry("900x600")

        self.frames = {}
        self.create_menu()
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.show_frame("TamilEluthugalPage")

    def create_menu(self):
        menu = tk.Menu(self)
        self.config(menu=menu)
        pages = [
            ("தமிழ் எழுத்துகள்", "TamilEluthugalPage"),
            ("உயிரெழுத்துகள்", "UyirPage"),
            ("மெய்யெழுத்துகள்", "MeiPage"),
            ("உயிர்மெய் எழுத்துகள்", "UyirMeiPage"),
            ("வினாடி வினா", "VinadiVinaPage"),
        ]
        for name, frame in pages:
            menu.add_command(label=name, command=lambda f=frame: self.show_frame(f))

    def show_frame(self, name):
        if name not in self.frames:
            if name == "UyirPage":
                frame = UyirPage(self.container)
            elif name == "MeiPage":
                frame = MeiPage(self.container)
            elif name == "UyirMeiPage":
                frame = UyirMeiPage(self.container)
            elif name == "VinadiVinaPage":
                frame = VinadiVinaPage(self.container)
            else:
                frame = TamilEluthugalPage(self.container)
            self.frames[name] = frame
            frame.pack(fill="both", expand=True)
        for f in self.frames.values():
            f.pack_forget()
        self.frames[name].pack(fill="both", expand=True)

# Scrollable Frame
class ScrollableFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

# Tamil Eluthugal Page
class TamilEluthugalPage(ScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)
        frame = self.scrollable_frame
        title = tk.Label(frame, text="247 தமிழ் எழுத்துகள்", font=("Helvetica", 18, "bold"))
        title.grid(row=0, column=0, columnspan=13, pady=10)

        # Header row: Uyir
        for j, uyir in enumerate([""] + uyir_eluthugal):
            tk.Label(frame, text=uyir, font=("Helvetica", 14, "bold"), borderwidth=1, relief="solid", width=5).grid(row=1, column=j)

        # Mei and Uyirmei
        for i, mei in enumerate(mei_eluthugal):
            tk.Label(frame, text=mei, font=("Helvetica", 14, "bold"), borderwidth=1, relief="solid", width=5).grid(row=i+2, column=0)
            for j, uyir in enumerate(uyir_eluthugal):
                text = mei[0] + kombu[uyir]
                tk.Button(frame, text=text, font=("Helvetica", 14), width=5).grid(row=i+2, column=j+1, padx=1, pady=1)

# Uyir Page
class UyirPage(ScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)
        frame = self.scrollable_frame
        tk.Label(frame, text="உயிரெழுத்துகள்", font=("Helvetica", 18, "bold")).pack(pady=10)
        for ch in uyir_eluthugal:
            tk.Button(frame, text=ch, font=("Helvetica", 16), width=5).pack(pady=2)

# Mei Page
class MeiPage(ScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)
        frame = self.scrollable_frame
        tk.Label(frame, text="மெய்யெழுத்துகள்", font=("Helvetica", 18, "bold")).pack(pady=10)
        for ch in mei_eluthugal:
            tk.Button(frame, text=ch, font=("Helvetica", 16), width=5).pack(pady=2)

# UyirMei Page
class UyirMeiPage(ScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)
        frame = self.scrollable_frame
        tk.Label(frame, text="216 உயிர்மெய் எழுத்துகள்", font=("Helvetica", 18, "bold")).pack(pady=10)
        for row in uyirmei_eluthugal:
            row_frame = tk.Frame(frame)
            row_frame.pack()
            for ch in row:
                tk.Button(row_frame, text=ch, font=("Helvetica", 14), width=5).pack(side="left", padx=1, pady=1)

# Quiz Page
class VinadiVinaPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.index = 0
        self.score = 0

        self.label = tk.Label(self, text="வினாடி வினா", font=("Helvetica", 18, "bold"))
        self.label.pack(pady=20)

        self.question_label = tk.Label(self, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self, font=("Helvetica", 16))
        self.answer_entry.pack(pady=10)

        self.feedback = tk.Label(self, text="", font=("Helvetica", 14))
        self.feedback.pack(pady=5)

        self.next_btn = tk.Button(self, text="பதிலளி", command=self.check_answer)
        self.next_btn.pack(pady=10)

        self.update_question()

    def update_question(self):
        if self.index < len(quiz_questions):
            self.question_label.config(text=f"எழுத்தை காண்பி: {quiz_questions[self.index]}")
            self.answer_entry.delete(0, tk.END)
            self.feedback.config(text="")
        else:
            self.label.config(text="வினாடி வினா முடிவடைந்தது!")
            self.question_label.config(text=f"மொத்த மதிப்பெண்: {self.score}/{len(quiz_questions)}")
            self.answer_entry.pack_forget()
            self.next_btn.pack_forget()

    def check_answer(self):
        ans = self.answer_entry.get().strip()
        if ans == quiz_questions[self.index]:
            self.score += 1
            self.feedback.config(text="சரியான பதில்!", fg="green")
        else:
            self.feedback.config(text=f"தவறு! சரியானது: {quiz_questions[self.index]}", fg="red")
        self.index += 1
        self.after(1000, self.update_question)

# Run the App
if __name__ == "__main__":
    app = TamilApp()
    app.mainloop()
