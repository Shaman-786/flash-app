import tkinter as tk
from random import choice

# Sample flashcards
flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the color of the sky?", "answer": "Blue"}
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")
        
        self.card = choice(flashcards)
        
        self.question_label = tk.Label(root, text=self.card["question"], font=("Arial", 18))
        self.question_label.pack(pady=20)
        
        self.answer_label = tk.Label(root, text="", font=("Arial", 18))
        self.answer_label.pack(pady=20)
        
        self.show_answer_button = tk.Button(root, text="Show Answer", command=self.show_answer)
        self.show_answer_button.pack(pady=10)
        
        self.next_button = tk.Button(root, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=10)
        
    def show_answer(self):
        self.answer_label.config(text=self.card["answer"])
        
    def next_question(self):
        self.card = choice(flashcards)
        self.question_label.config(text=self.card["question"])
        self.answer_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()