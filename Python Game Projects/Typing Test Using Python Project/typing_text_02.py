import tkinter as tk
import random
import time
import nltk

nltk.download('words')

from nltk.corpus import words

class TypingTestGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Test Game")
        self.root.geometry("600x400")

        self.word_list = words.words()
        self.paragraph_length = 2  # Number of lines in the paragraph
        self.current_paragraph = tk.StringVar()
        self.current_paragraph.set("Click 'Start' to begin!")
        
        self.user_input = tk.StringVar()
        self.user_input.set("")

        self.score = 0
        self.start_time = 0
        self.is_playing = False

        self.create_widgets()

    def create_widgets(self):
        self.label_paragraph = tk.Label(self.root, textvariable=self.current_paragraph, font=("Helvetica", 14), wraplength=500, justify='center')
        self.label_paragraph.pack(pady=20)

        self.entry_input = tk.Entry(self.root, textvariable=self.user_input, font=("Helvetica", 14))
        self.entry_input.pack(pady=10)

        self.label_score = tk.Label(self.root, text="Score: 0", font=("Helvetica", 16))
        self.label_score.pack()

        self.label_speed = tk.Label(self.root, text="Typing Speed: 0 WPM", font=("Helvetica", 16))
        self.label_speed.pack()

        self.label_meter = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.label_meter.pack()

        self.button_start = tk.Button(self.root, text="Start", command=self.start_game)
        self.button_start.pack(pady=20)

        self.root.bind('<Return>', self.check_word)

    def generate_paragraph(self):
        paragraph = []
        for _ in range(self.paragraph_length):
            sentence = random.choices(self.word_list, k=random.randint(5, 10))
            paragraph.append(" ".join(sentence))
        return "\n".join(paragraph)

    def start_game(self):
        if not self.is_playing:
            self.is_playing = True
            self.score = 0
            self.start_time = time.time()
            self.current_paragraph.set(self.generate_paragraph())
            self.next_word()

    def next_word(self):
        self.user_input.set("")
        if self.is_playing:
            word_list = self.current_paragraph.get().split()
            self.current_word = word_list[self.score]
            self.current_paragraph.set(" ".join(word_list[self.score: self.score + 10]))

    def check_word(self, event):
        if self.is_playing:
            typed_word = self.user_input.get().strip()
            if typed_word == self.current_word:
                self.score += 1
                self.label_score.config(text=f"Score: {self.score}")
                self.next_word()
        
        if self.is_playing:
            elapsed_time = time.time() - self.start_time
            typing_speed = self.score / (elapsed_time / 60)
            self.label_speed.config(text=f"Typing Speed: {typing_speed:.2f} WPM")
            self.update_meter(typing_speed)

    def update_meter(self, typing_speed):
        meter_width = min(int(typing_speed * 3), 300)  # Scale the width of the meter
        meter_fill = "green" if typing_speed >= 40 else "yellow" if typing_speed >= 20 else "red"
        self.label_meter.config(text="", width=meter_width, bg=meter_fill)

    def stop_game(self):
        if self.is_playing:
            self.is_playing = False
            self.current_paragraph.set("Game Over!")
            elapsed_time = time.time() - self.start_time
            typing_speed = self.score / (elapsed_time / 60)
            self.label_speed.config(text=f"Final Typing Speed: {typing_speed:.2f} WPM")
            self.update_meter(typing_speed)

if __name__ == "__main__":
    root = tk.Tk()
    typing_test = TypingTestGame(root)
    root.mainloop()
