import tkinter as tk
import random

# Thai consonants and their pronunciation
thai_consonants = [
    ("ก", "gor gai"), ("ข", "kho khai"), ("ค", "kho khwai"), ("ง", "ngor ngu"),
    ("จ", "jor jaan"), ("ฉ", "cho ching"), ("ช", "cho chang"), ("ซ", "so so"),
    ("ญ", "yor ying"), ("ฎ", "dor chada"), ("ฏ", "tor patak"), ("ฐ", "tho than"),
    ("ฑ", "tho montho"), ("ณ", "nor nen"), ("ด", "dor dek"), ("ต", "tor tao"),
    ("ถ", "tho thung"), ("ท", "tho thahan"), ("น", "nor nu"), ("บ", "bor baimai"),
    ("ป", "por pla"), ("ผ", "pho phueng"), ("ฝ", "fo fa"), ("พ", "pho phan"),
    ("ฟ", "fo fan"), ("ม", "mor ma"), ("ย", "yor yak"), ("ร", "ror rua"),
    ("ล", "lor ling"), ("ว", "wor waen"), ("ศ", "so sala"), ("ส", "so suea")
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.current_card = None
        
        self.label = tk.Label(root, text="Click 'Next' to begin", font=("Arial", 50), width=10, height=3)
        self.label.pack(pady=50)
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card, font=("Arial", 20))
        self.flip_button.pack()
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card, font=("Arial", 20))
        self.next_button.pack(pady=10)
        
        self.next_card()
        
    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.label.config(text=self.current_card[0])
        
    def flip_card(self):
        if self.current_card:
            self.label.config(text=self.current_card[1])

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()