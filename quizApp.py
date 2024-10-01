import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("600x500")

        self.canvas = tk.Canvas(self.root, width=600, height=500)
        self.canvas.pack(fill="both", expand=True)
        self.create_gradient()

        self.header_label = tk.Label(self.root, text="Quiz App", font=("Arial", 24, "bold"), bg="yellow", fg="black")
        self.header_label.place(relwidth=1, y=10)  

        self.questions = [
            "What book holds the record for the fastest selling book in history?",
            "How old was Queen Elizabeth II when she was first crowned the Queen of England?",
            "Which blood type is a universal donor?",
            "What is the capital of Australia?",
            "Who painted the Mona Lisa?",
            "Which planet is known as the Red Planet?",
            "What is the smallest country in the world?",
            "Who is known as the 'Father of Computers'?",
            "In what year did the Titanic sink?",
            "Which element has the chemical symbol 'O'?"
        ]

        self.answers = [
            ["A. The Hunger Games", "B. Harry Potter and the Deathly Hallows", "C. To Kill A Mockingbird"],
            ["A. 27", "B. 24", "C. 31"],
            ["A. O negative", "B. B Positive", "C. AB"],
            ["A. Sydney", "B. Canberra", "C. Melbourne"],
            ["A. Van Gogh", "B. Picasso", "C. Leonardo da Vinci"],
            ["A. Mars", "B. Jupiter", "C. Venus"],
            ["A. Monaco", "B. Vatican City", "C. San Marino"],
            ["A. Charles Babbage", "B. Alan Turing", "C. Ada Lovelace"],
            ["A. 1905", "B. 1912", "C. 1921"],
            ["A. Hydrogen", "B. Oxygen", "C. Helium"]
        ]

        self.correctAnswers = [1, 1, 0, 1, 2, 0, 1, 0, 1, 1]
        self.current_question = 0
        self.player_score = 0

        self.create_widgets()

    def create_gradient(self):
        steps = 500  
        for i in range(steps):
            r = int(139 + (255 - 139) * i / steps)  
            g = int(69 + (255 - 69) * i / steps)
            b = int(19 + (0 - 19) * i / steps)
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas.create_rectangle(0, i, 600, i + 1, outline=color, fill=color)

    def create_widgets(self):
        
        self.question_label = tk.Label(self.root, text=f"Question {self.current_question + 1}: {self.questions[self.current_question]}", 
                                       font=("Arial", 16, "bold"), wraplength=500, bg="yellow", fg="black")
        self.question_label.place(x=50, y=80, width=500)  

        
        self.radio_var = tk.IntVar()
        self.radio_var.set(-1)

        self.option_buttons = []
        for i in range(3):
            rb = tk.Radiobutton(self.root, text=self.answers[self.current_question][i], variable=self.radio_var, value=i,
                                font=("Arial", 14), bg="yellow", fg="black", activebackground="#f8f9fa", 
                                activeforeground="#333333", selectcolor="#add8e6", anchor="w", justify="left")
            rb.place(x=50, y=140 + i*40, width=500, height=30) 
            self.option_buttons.append(rb)

        self.submit_button = tk.Button(self.root, text="Submit Answer", command=self.check_answer,
                                       font=("Arial", 16), bg="#8B4513", fg="white", activebackground="#6B3F12", 
                                       activeforeground="white", padx=10, pady=5)
        self.submit_button.place(x=200, y=300, width=200, height=50)  

    def check_answer(self):
        selected_option = self.radio_var.get()

        if selected_option == -1:
            messagebox.showwarning("No answer selected", "Please select an answer before submitting.")
            return

        self.option_buttons[selected_option].config(bg="#FFCCCB")  

        if selected_option == self.correctAnswers[self.current_question]:
            self.player_score += 1

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.show_final_score()

    def update_question(self):
        self.radio_var.set(-1)
        self.question_label.config(text=f"Question {self.current_question + 1}: {self.questions[self.current_question]}")
        for i in range(3):
            self.option_buttons[i].config(text=self.answers[self.current_question][i], bg="yellow")  # Reset colors

    def show_final_score(self):
        score_message = f"Quiz Completed!\nYour score is: {self.player_score}/{len(self.questions)}"
        messagebox.showinfo("Quiz Finished", score_message)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
