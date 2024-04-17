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
        self.current_word = tk.StringVar()
        self.current_word.set("Click 'Start' to begin!")
        
        self.user_input = tk.StringVar()
        self.user_input.set("")

        self.score = 0
        self.start_time = 0
        self.is_playing = False

        self.create_widgets()

    def create_widgets(self):
        self.label_word = tk.Label(self.root, textvariable=self.current_word, font=("Helvetica", 20))
        self.label_word.pack(pady=20)

        self.entry_input = tk.Entry(self.root, textvariable=self.user_input, font=("Helvetica", 14))
        self.entry_input.pack(pady=10)

        self.label_score = tk.Label(self.root, text="Score: 0", font=("Helvetica", 16))
        self.label_score.pack()

        self.label_speed = tk.Label(self.root, text="Typing Speed: 0 WPM", font=("Helvetica", 16))
        self.label_speed.pack()

        self.button_start = tk.Button(self.root, text="Start", command=self.start_game)
        self.button_start.pack(pady=20)

        self.root.bind('<Return>', self.check_word)

    def start_game(self):
        if not self.is_playing:
            self.is_playing = True
            self.score = 0
            self.start_time = time.time()
            self.next_word()

    def next_word(self):
        self.user_input.set("")
        if self.is_playing:
            word = random.choice(self.word_list)
            self.current_word.set(word)

    def check_word(self, event):
        if self.is_playing:
            typed_word = self.user_input.get().strip()
            current_word = self.current_word.get()

            if typed_word == current_word:
                self.score += 1
                self.label_score.config(text=f"Score: {self.score}")
                self.next_word()

        if self.is_playing:
            elapsed_time = time.time() - self.start_time
            typing_speed = self.score / (elapsed_time / 60)
            self.label_speed.config(text=f"Typing Speed: {typing_speed:.2f} WPM")

    def stop_game(self):
        if self.is_playing:
            self.is_playing = False
            self.current_word.set("Game Over!")
            elapsed_time = time.time() - self.start_time
            typing_speed = self.score / (elapsed_time / 60)
            self.label_speed.config(text=f"Final Typing Speed: {typing_speed:.2f} WPM")

if __name__ == "__main__":
    root = tk.Tk()
    typing_test = TypingTestGame(root)
    root.mainloop()
