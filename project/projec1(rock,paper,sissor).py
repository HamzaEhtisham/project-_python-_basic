"""
rock--1
paper--2
sissor--3
"""

# Ensure you have Pillow installed: pip install pillow

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import random

def game_interface():
    def play(choice):
        computer = random.choice([1, 2, 3])
        dict1 = {1: "rock", 2: "paper", 3: "sissor"}
        dict2 = {"rock": 1, "paper": 2, "sissor": 3}
        you = dict2[choice]
        computer_choice = dict1[computer]
        
        result = ""
        if computer_choice == choice:
            result = "!It's a draw!"
        else:
            if (you == 1 and computer == 3) or (you == 2 and computer == 1) or (you == 3 and computer == 2):
                result = "!!You win!!"
                scores['player'] += 1
            else:
                result = "!!!You lose!!!"
                scores['computer'] += 1
        
        update_score()
        messagebox.showinfo("Result", f"Your choice: {choice}\nComputer choice: {computer_choice}\n{result}")

    def update_score():
        score_label.config(text=f"Player: {scores['player']}  Computer: {scores['computer']}")

    def reset_game():
        scores['player'] = 0
        scores['computer'] = 0
        update_score()

    def on_exit():
        root.destroy()

    def load_image(filename, fallback_text):
        try:
            return ImageTk.PhotoImage(Image.open(filename).resize((80, 80), Image.ANTIALIAS))
        except FileNotFoundError:
            img = Image.new('RGB', (80, 80), color = (73, 109, 137))
            d = ImageDraw.Draw(img)
            d.text((10, 30), fallback_text, fill=(255, 255, 0))
            return ImageTk.PhotoImage(img)

    root = tk.Tk()
    root.title("Rock, Paper, Scissor Game")
    root.geometry("400x300")
    root.resizable(False, False)

    scores = {'player': 0, 'computer': 0}

    title_label = tk.Label(root, text="Rock, Paper, Scissor Game", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(pady=10)

    rock_img = load_image("rock.png", "Rock")
    paper_img = load_image("paper.png", "Paper")
    sissor_img = load_image("sissor.png", "Sissor")

    tk.Button(frame, image=rock_img, command=lambda: play("rock")).grid(row=0, column=0, padx=10)
    tk.Button(frame, image=paper_img, command=lambda: play("paper")).grid(row=0, column=1, padx=10)
    tk.Button(frame, image=sissor_img, command=lambda: play("sissor")).grid(row=0, column=2, padx=10)

    score_label = tk.Label(root, text="Player: 0  Computer: 0", font=("Helvetica", 12))
    score_label.pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Reset", command=reset_game, width=10).grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Exit", command=on_exit, width=10).grid(row=0, column=1, padx=5)

    root.mainloop()

if __name__ == "__main__":
    game_interface()