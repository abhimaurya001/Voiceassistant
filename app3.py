import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "Who developed Python?",
        "options": ["Bill Gates", "Guido van Rossum", "Elon Musk", "Mark Zuckerberg"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "Which language is used for Android development?",
        "options": ["Kotlin", "HTML", "CSS", "PHP"],
        "answer": "Kotlin"
    }
]

current_question = 0
score = 0

def load_question():
    question_label.config(text=questions[current_question]["question"])

    option1.config(text=questions[current_question]["options"][0], value=questions[current_question]["options"][0])
    option2.config(text=questions[current_question]["options"][1], value=questions[current_question]["options"][1])
    option3.config(text=questions[current_question]["options"][2], value=questions[current_question]["options"][2])
    option4.config(text=questions[current_question]["options"][3], value=questions[current_question]["options"][3])

    selected_option.set(None)

def next_question():
    global current_question, score

    if selected_option.get() == "":
        messagebox.showwarning("Warning", "Please select an option")
        return

    if selected_option.get() == questions[current_question]["answer"]:
        score += 1

    current_question += 1

    if current_question < len(questions):
        load_question()
    else:
        messagebox.showinfo(
            "Quiz Finished",
            f"Your Score: {score}/{len(questions)}"
        )
        root.destroy()

root = tk.Tk()
root.title("Python Quiz App")
root.geometry("500x350")

question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=450)
question_label.pack(pady=20)

selected_option = tk.StringVar()

option1 = tk.Radiobutton(root, text="", variable=selected_option)
option1.pack(anchor="w", padx=50)

option2 = tk.Radiobutton(root, text="", variable=selected_option)
option2.pack(anchor="w", padx=50)

option3 = tk.Radiobutton(root, text="", variable=selected_option)
option3.pack(anchor="w", padx=50)

option4 = tk.Radiobutton(root, text="", variable=selected_option)
option4.pack(anchor="w", padx=50)

next_button = tk.Button(
    root,
    text="Next Question",
    command=next_question,
    font=("Arial", 12)
)
next_button.pack(pady=20)

load_question()

root.mainloop()