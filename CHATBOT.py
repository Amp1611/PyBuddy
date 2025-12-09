#=============================================
#  IMPORTING NECESSARY MODULES
#=============================================

import random
import sys
import traceback
import textwrap
import os
import csv
import time
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from functools import reduce
from textwrap import fill



# ============================================
#       DAILY CHALLENGES BY ANKITHA
# ============================================

daily_questions = [
# Python Basics
"Write a program to find factorial using recursion.",
"Write a program to check if a number is prime.",
"Write a program to count vowels in a string.",
"Write a program to reverse a number.",
"Write a function to check palindrome string.",
# Data Structures
"Write code to remove duplicates from a list.",
"Write a program to find the largest number in a list.",
"Write a program to merge two dictionaries.",
"Write a program to sort a list without using sort().",
"Write code to flatten a nested list.",
# OOP
"Create a class Car with attributes and methods.",
"Create a class Animal and a subclass Dog.",
"Demonstrate method overriding using two classes.",
"Create a class Student with a method to calculate percentage.",
"Implement a class for BankAccount with deposit/withdraw.",
# File Handling
"Write a program to count words in a text file.",
"Write code to copy content from one file to another.",
"Write a program to read a file and print line numbers.",
# Pandas / NumPy
"Use pandas to read a CSV file and print first 5 rows.",
"Use pandas to filter rows based on a condition.",
"Use NumPy to create a 3x3 matrix.",
"Use NumPy to find mean, median, mode of an array.",
# Functional Programming
"Use map() to convert list of numbers to squares.",
"Use lambda + filter to get even numbers.",
"Use reduce() to calculate factorial.",
# Loops / Logic
"Write a pattern printing program (triangle or pyramid).",
"Write a program to generate Fibonacci series.",
"Write a program to count duplicate elements in a list.",
"Write a program to check Armstrong number.",
"Write a program to print unique characters from a string.",
]

def daily_challenge():
  print("\n===== DAILY CHALLENGE =====")
  print("Here are your 5 tasks for today:\n")
  for task in random.sample(daily_questions, 5):
    print("-", task)
  print("\nReturning to menu...")
# ============================================

# FIND ERROR BY ASHISH

# ============================================

ERROR_QUESTIONS = {
"easy": [
{"code": "for i in range(3)\n    print(i)",
"error": "Missing colon after range(3).",
"fix": "for i in range(3):\n    print(i)"},
{"code": "x = '5'\nprint(x + 2)",
"error": "Can't add string and integer.",
"fix": "print(int(x) + 2)"}
],
"medium": [
{"code": "def add(a, b)\n    return a + b",
"error": "Missing colon in function definition.",
"fix": "def add(a, b):\n    return a + b"},
{"code": "a = [1,2,3]\nprint(a[5])",
"error": "Index out of range (list has 3 items).",
"fix": "print(a[-1])  # or valid index"}
],
"hard": [
{"code": "class A:\n    def **init**(self):\n        self.x = 5\n\ndef show():\n    print(x)",
"error": "Variable x is inside class, not global.",
"fix": "obj = A()\nprint(obj.x)"},
{"code": "import pandas as pd\ndf = pd.read('data.csv')",
"error": "pd.read does not exist — should be pd.read_csv().",
"fix": "df = pd.read_csv('data.csv')"}
]
}

def try_run(code):
    try:
        exec(code, {}, {})
        return "NO ERROR FOUND (but question says there is one)"
    except Exception:
        return traceback.format_exc()

def find_error_menu():
    print("\n===== FIND THE ERROR =====")
    level = input("Choose difficulty (easy / medium / hard): ").lower()
    if level not in ERROR_QUESTIONS:
        print("Invalid level.")
        return

    q = random.choice(ERROR_QUESTIONS[level])
    print("\nFind the error in the following code:\n")
    print(textwrap.indent(q["code"], "   "))

    input("\nPress Enter to reveal error...")
    print("\n=== ERROR FOUND ===")
    print(q["error"])

    if input("\nSee corrected code? (y/n): ").lower() == "y":
        print("\nCorrected Code:\n")
        print(textwrap.indent(q["fix"], "   "))

    if input("\nSimulate Python's actual error? (y/n): ").lower() == "y":
        print("\nPython Error Traceback:")
        print(try_run(q["code"]))

    print("\nReturning to menu...\n")



# ============================================
#       GUESS THE OUTPUT BY ASHISH
# ============================================

OUTPUT_QUESTIONS = {
"easy": [
{"code": "x = 3\nprint(x * 2)", "answer": "6", "explanation": "3 multiplied by 2 gives 6."},
{"code": "s = 'Hello'\nprint(s[1])", "answer": "e", "explanation": "Index 1 of 'Hello' is 'e'."}
],
"medium": [
{"code": "for i in range(3):\n    print(i, end=' ')", "answer": "0 1 2 ", "explanation": "range(3) gives 0,1,2."},
{"code": "def f(n):\n    if n == 0:\n        return 1\n    return n * f(n-1)\n\nprint(f(4))", "answer": "24", "explanation": "4! = 24 using recursion."}
],
"hard": [
{"code": "a = [1,2,3]\nb = a\nb.append(4)\nprint(a)", "answer": "[1, 2, 3, 4]", "explanation": "a and b point to same list."},
{"code": "def x(a, b=[1]):\n    b.append(a)\n    return b\nprint(x(3))\nprint(x(5))", "answer": "[1, 3, 5]", "explanation": "Default mutable list persists across calls."}
]
}

import random
import textwrap

def guess_output_menu():
    print("\n===== GUESS THE OUTPUT =====")
    level = input("Choose difficulty (easy / medium / hard): ").lower()
    if level not in OUTPUT_QUESTIONS:
        print("Invalid level.")
        return

    q = random.choice(OUTPUT_QUESTIONS[level])
    print("\nPredict the output of this code:\n")
    print(textwrap.indent(q["code"], "   "))

    user_ans = input("\nYour answer: ").strip()
    correct = q["answer"].strip()

    print("\n=== RESULT ===")
    if user_ans == correct:
        print("✔ Correct!")
    else:
        print(f"✘ Incorrect! Correct Output: {correct}")

    if input("\nSee explanation? (y/n): ").lower() == "y":
        print("\nExplanation:")
        print(q["explanation"])

    print("\nReturning to menu...\n")



# ============================================
#          MCQs BY AMARTYA
# ============================================

questions_mcq = {
    "Control Structures": [
        ("Which keyword is used for conditional branching?",
         ["if", "loop", "define", "case"], "if"),
        ("Which statement exits a loop?",
         ["exit", "stop", "break", "end"], "break"),
        ("Which loop runs until a condition is false?",
         ["for", "while", "until", "repeat"], "while"),
        ("Which keyword skips the current iteration?",
         ["skip", "continue", "pass", "next"], "continue"),
        ("Which keyword is used for alternate conditions?",
         ["elif", "else if", "elseif", "alt"], "elif"),
        ("Which statement ends a function?",
         ["stop", "end", "return", "exit"], "return"),
        ("Indentation in Python defines ______.",
         ["variables", "memory", "code blocks", "comments"], "code blocks"),
        ("A loop inside another loop is called ______.",
         ["nested loop", "inner loop", "double loop", "block loop"], "nested loop"),
        ("Which control structure executes code multiple times?",
         ["condition", "loop", "switch", "branch"], "loop"),
        ("Which operator is used for comparison?",
         ["=", "==", "equals", "same"], "=="),
    ],

    "Data Structures": [
        ("Which DS stores key-value pairs?",
         ["List", "Tuple", "Dictionary", "Set"], "Dictionary"),
        ("Which DS is ordered and mutable?",
         ["Tuple", "List", "Set", "Dictionary"], "List"),
        ("Which DS stores unique values?",
         ["List", "Set", "Tuple", "Dictionary"], "Set"),
        ("Which DS is immutable?",
         ["List", "Tuple", "Set", "Dictionary"], "Tuple"),
        ("Which DS is LIFO?",
         ["Queue", "Stack", "Tree", "List"], "Stack"),
        ("Which DS is FIFO?",
         ["Tree", "Graph", "Queue", "Set"], "Queue"),
        ("Which method adds a list element?",
         ["push()", "append()", "add()", "insert()"], "append()"),
        ("Which removes a dictionary key?",
         ["delete()", "remove()", "pop()", "clear()"], "pop()"),
        ("Which DS is used for adjacency lists?",
         ["Linked list", "Stack", "Graph", "Tuple"], "Graph"),
        ("Which DS allows indexing?",
         ["Set", "List", "Dictionary", "Queue"], "List"),
    ],

    "Files (TXT & CSV)": [
        ("Which function opens a file?",
         ["file()", "open()", "read()", "start()"], "open()"),
        ("Mode for reading a file:",
         ["w", "a", "r", "x"], "r"),
        ("Mode that overwrites:",
         ["w", "r", "a", "rw"], "w"),
        ("Which module handles CSV?",
         ["json", "csv", "file", "reader"], "csv"),
        ("Which reads all lines?",
         ["read()", "readline()", "readlines()", "fetch()"], "readlines()"),
        ("Which closes a file?",
         ["stop()", "end()", "close()", "exit()"], "close()"),
        ("CSV default delimiter:",
         ["semicolon", "tab", "comma", "space"], "comma"),
        ("Append mode:",
         ["a", "w", "x", "aw"], "a"),
        ("Which writes to a file?",
         ["writer()", "write()", "insert()", "append()"], "write()"),
        ("Which reads CSV as dict?",
         ["DictReader", "DictRead", "csvReader", "Reader"], "DictReader"),
    ],

    "Functions": [
        ("Keyword to define a function:",
         ["func", "define", "def", "lambda"], "def"),
        ("Function with no return:",
         ["none", "empty", "void", "zero"], "void"),
        ("Functions inside functions are:",
         ["global", "nested", "private", "hidden"], "nested"),
        ("Anonymous functions are called:",
         ["void", "lambda", "hidden", "clave"], "lambda"),
        ("Function that calls itself:",
         ["recursive", "looping", "callback", "static"], "recursive"),
        ("Default return value:",
         ["zero", "none", "false", "null"], "none"),
        ("Functions that belong to objects are:",
         ["methods", "types", "calls", "operators"], "methods"),
        ("Keyword to return value:",
         ["output", "end", "return", "back"], "return"),
        ("Arguments with default values:",
         ["static args", "optional args", "default args", "extra args"], "default args"),
        ("What stores function definition?",
         ["header", "signature", "prototype", "base"], "signature"),
    ],

    "Modules (NumPy, PIL, NLTK, Pandas)": [
        ("NumPy is used for:",
         ["Strings", "Arrays", "Images", "Audio"], "Arrays"),
        ("PIL is used for:",
         ["Images", "Audio", "Graphs", "Networking"], "Images"),
        ("NLTK is used for:",
         ["Networking", "Databases", "NLP", "Images"], "NLP"),
        ("Pandas is used for:",
         ["Audio", "Machine Learning", "DataFrames", "Encryption"], "DataFrames"),
        ("NumPy array type:",
         ["array2d", "ndarray", "matrix", "tensor"], "ndarray"),
        ("PIL stands for:",
         ["Picture Imaging Library", "Python Image Library", "Photo Image Loader", "Pixel Imaging Lab"], "Python Image Library"),
        ("NLTK stands for:",
         ["Natural Lab Toolkit", "Natural Language Toolkit", "NLP Toolkit", "Natural Learning Keys"], "Natural Language Toolkit"),
        ("Which is a Pandas structure?",
         ["DataFrame", "Image", "Tree", "Matrix"], "DataFrame"),
        ("PIL function to load image?",
         ["load()", "open()", "read()", "import()"], "open()"),
        ("NLTK provides:",
         ["Tokenization", "Hardware control", "Image filters", "Encoders"], "Tokenization"),
    ],

    "Lambda / Map / Reduce / Filter": [
        ("Keyword for anonymous function:",
         ["def", "lambda", "anon", "func"], "lambda"),
        ("Which applies a function to all items?",
         ["map", "reduce", "filter", "apply"], "map"),
        ("Which returns items that meet a condition?",
         ["map", "reduce", "filter", "extract"], "filter"),
        ("Which reduces list to one value?",
         ["map", "reduce", "compress", "merge"], "reduce"),
        ("reduce() comes from:",
         ["functools", "itertools", "collections", "os"], "functools"),
        ("Lambda has how many expressions?",
         ["one", "two", "three", "infinite"], "one"),
        ("map returns a:",
         ["list", "tuple", "iterator", "dict"], "iterator"),
        ("filter returns:",
         ["iterator", "string", "list", "set"], "iterator"),
        ("reduce returns:",
         ["list", "single value", "iterator", "dict"], "single value"),
        ("lambda x: x+1 returns x increased by:",
         ["3", "2", "1", "5"], "1"),
    ],

    "Zip & List Comprehension": [
        ("zip() combines:",
         ["numbers", "conditions", "iterables", "strings"], "iterables"),
        ("zip returns:",
         ["list", "iterator", "tuple", "dict"], "iterator"),
        ("List comprehension creates:",
         ["sets", "strings", "lists", "dicts"], "lists"),
        ("[x*x for x in range(5)] gives:",
         ["5 squares", "3 squares", "infinite", "none"], "5 squares"),
        ("zip stops at:",
         ["longest iterable", "first iterable", "shortest iterable", "last iterable"], "shortest iterable"),
        ("List comprehension is ______ than loops.",
         ["slower", "same", "faster", "useless"], "faster"),
        ("Condition in list comprehension uses:",
         ["when", "if", "cond", "case"], "if"),
        ("List comprehension uses:",
         ["{}", "()", "[]", "<>"], "[]"),
        ("zip is used to create:",
         ["graphs", "pairs", "numbers", "sets"], "pairs"),
        ("List comprehension reduces:",
         ["speed", "code size", "memory", "functions"], "code size"),
    ],

    "OOP": [
        ("Keyword for class:",
         ["function", "object", "class", "define"], "class"),
        ("Process of using parent class features:",
         ["recursion", "inheritance", "composition", "mapping"], "inheritance"),
        ("Changing method in child class:",
         ["overloading", "overriding", "copying", "extending"], "overriding"),
        ("Python supports ______ inheritance:",
         ["single", "multiple", "double", "no"], "multiple"),
        ("Constructor method:",
         ["__start__", "__make__", "__init__", "__begin__"], "__init__"),
        ("Keyword that refers to object:",
         ["this", "self", "own", "obj"], "self"),
        ("Class instances are called:",
         ["objects", "modules", "types", "packages"], "objects"),
        ("Polymorphism means:",
         ["one object many forms", "single function", "same input", "same form"], "one object many forms"),
        ("Iterator method:",
         ["__next__", "__iter__", "__loop__", "__getitem__"], "__iter__"),
        ("Exception handling keyword:",
         ["error", "handle", "try", "except"], "try"),
    ],
}
import random

def mcq_menu():
    print("\n========= PYTHON MCQ PRACTICE =========\n")
    print("Available topics:\n")
    for t in questions_mcq:
        print(" -", t)

    topic = input("\nEnter topic to practice exactly as shown: ").strip()
    if topic not in questions_mcq:
        print("\n❌ Invalid topic!")
        return

    qlist = questions_mcq[topic]
    score = 0
    print(f"\n=========== {topic.upper()} QUIZ ===========\n")

    for q, opts, correct in qlist:
        print(q)
        random.shuffle(opts)
        for i, o in enumerate(opts, start=1):
            print(f"{i}. {o}")

        user = input("Your answer (1-4): ").strip()
        if user in ["1", "2", "3", "4"] and opts[int(user)-1] == correct:
            print("✔ Correct!\n")
            score += 1
        else:
            print(f"✘ Wrong! Correct answer: {correct}\n")

    print("============================================")
    print(f" SCORE: {score}/{len(qlist)}")
    print("============================================")



# ============================================
#         RIDLLES BY CHAITRA
# ============================================

def start_file9():
    class RiddleQuizGUI:
        def __init__(self, root):
            self.root = root
            self.root.title("Python Riddle Quiz")
            self.root.geometry("700x400")
            self.root.resizable(False, False)

            self.riddles = self.load_riddles()
            if not self.riddles:
                self.root.destroy()
                return

            self.index = 0
            self.score = 0
            self.streak = 0
            self.skips = 2
            self.start_time = 0
            self.after_id = None

            self.question_label = tk.Label(root, text="", wraplength=650, font=("Arial", 16))
            self.question_label.pack(pady=20)

            self.answer_entry = tk.Entry(root, font=("Arial", 14), width=30)
            self.answer_entry.pack(pady=10)
            self.answer_entry.bind('<Return>', lambda e: self.submit_answer())

            self.feedback_label = tk.Label(root, text="", fg="blue", font=("Arial", 14))
            self.feedback_label.pack()

            button_frame = tk.Frame(root)
            button_frame.pack(pady=20)

            self.submit_btn = tk.Button(button_frame, text="Submit", command=self.submit_answer, width=10)
            self.submit_btn.grid(row=0, column=0, padx=10)

            self.hint_btn = tk.Button(button_frame, text="Hint", command=self.show_hint, width=10)
            self.hint_btn.grid(row=0, column=1, padx=10)

            self.skip_btn = tk.Button(button_frame, text=f"Skip ({self.skips})", command=self.skip_question, width=10)
            self.skip_btn.grid(row=0, column=2, padx=10)

            self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
            self.score_label.pack()

            self.load_question()

        def load_riddles(self, filename="riddles.csv"):
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, filename)
            riddles = []

            try:
                with open(file_path, "r", newline="", encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        riddles.append({
                            "question": row.get("question", ""),
                            "answer": row.get("answer", "").lower().strip(),
                            "hint": row.get("hint", "")
                        })
                random.shuffle(riddles)
            except FileNotFoundError:
                messagebox.showerror("Error", f"Could not find '{filename}'\nLooking in: {script_dir}")
                return []

            return riddles

        def load_question(self):
            if self.index >= len(self.riddles):
                self.end_quiz()
                return

            question = self.riddles[self.index]["question"]
            self.question_label.config(text=f"Q{self.index + 1}: {question}")
            self.answer_entry.delete(0, tk.END)
            self.feedback_label.config(text="")
            self.answer_entry.focus()
            self.start_time = time.time()

        def submit_answer(self):
            user_answer = self.answer_entry.get().lower().strip()
            if not user_answer:
                return

            correct_answer = self.riddles[self.index]["answer"]
            time_taken = time.time() - self.start_time
            points = 10

            if user_answer == correct_answer:
                if time_taken > 10:
                    points -= 2
                self.streak += 1
                if self.streak % 3 == 0:
                    points += 5
                self.feedback_label.config(text=f"Correct! +{points} points", fg="green")
                self.score += points
            else:
                self.feedback_label.config(text=f"Wrong! Correct answer: {correct_answer}", fg="red")
                self.streak = 0

            self.score_label.config(text=f"Score: {self.score}")
            self.index += 1

            if self.index % 5 == 0 and self.index < len(self.riddles):
                messagebox.showinfo("Progress", f"After {self.index} questions, your score is: {self.score}")

            self.after_id = self.root.after(1200, self.load_question)

        def show_hint(self):
            hint = self.riddles[self.index]["hint"]
            if hint:
                messagebox.showinfo("Hint", hint)
                self.score -= 3
                self.score_label.config(text=f"Score: {self.score}")
            else:
                messagebox.showinfo("Hint", "No hint available for this question.")

        def skip_question(self):
            if self.skips > 0:
                self.skips -= 1
                self.skip_btn.config(text=f"Skip ({self.skips})")
                self.index += 1
                self.load_question()
            else:
                messagebox.showwarning("No Skips", "You have no skips left!")

        def end_quiz(self):
            if self.after_id is not None:
                try:
                    self.root.after_cancel(self.after_id)
                except:
                    pass
            messagebox.showinfo("Quiz Finished", f"Your final score: {self.score}")
            try:
                self.root.destroy()
            except:
                pass

    root = tk.Tk()
    app = RiddleQuizGUI(root)
    root.mainloop()
    try:
      root.destroy()
    except:
      pass
    print()

start_file9() #



# ============================================
#         FLASHCARDS BY ANKITHA
# ============================================

DATA_DIR = "data"
FLASHCARDS_CSV = os.path.join(DATA_DIR, "flashcards.csv")

DEFAULT_CARDS = [
    ("Function", "A block of reusable code defined with def."),
    ("Class", "Blueprint for creating objects with attributes and methods."),
    ("List Comprehension", "[expr for item in iterable if condition]"),
    ("Lambda", "Anonymous function: lambda x: x+1"),
    ("Map", "Apply function to all items: map(func, iterable)"),
    ("Filter", "Keep items matching condition: filter(func, iterable)"),
    ("Pandas DataFrame", "2D labeled data structure from pandas."),
    ("NumPy array", "Homogeneous n-dimensional array with fast ops."),
]

def flashcards():
    # ======= Ensure flashcards file exists =======
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(FLASHCARDS_CSV):
        with open(FLASHCARDS_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["term", "definition"])
            writer.writerows(DEFAULT_CARDS)

    # ======= Load flashcards =======
    cards = []
    with open(FLASHCARDS_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cards.append((row["term"], row["definition"]))

    if not cards:
        print("No flashcards found.")
        return

    # ======= Session mode =======
    print("\n--- Flashcards Mode ---")
    print("Options: 1) Sequential  2) Shuffle")
    mode = input("Choose mode (1/2): ").strip()
    if mode == "2":
        random.shuffle(cards)

    # ======= Flashcards loop =======
    correct = 0
    total = 0
    for term, definition in cards:
        print(f"\nTerm: {term}")
        input("Think of the definition, then press Enter to reveal...")
        print(fill(f"Definition: {definition}", width=80))
        resp = input("Mark: (y) I got it / (n) I didn't: ").strip().lower()
        total += 1
        if resp == "y":
            correct += 1

    print(f"\nSession complete. You remembered {correct}/{total}.")


    
# ============================================
#       SUMMARIES BY AMARTYA
# ============================================

summaries = {
    "control structures": """Control structures are the building blocks that decide how a program flows. 
They include conditional statements like if, elif, and else, which help a program make decisions. 
Loops such as for and while let you repeat actions efficiently. Control structures prevent repetition, 
improve readability, and help handle different scenarios. With them, you can validate user input, 
iterate through collections, and break or continue flows based on conditions. They make programs dynamic, 
flexible, and capable of reacting to real-time situations. Almost every Python program uses control 
structures, and mastering them is essential for writing logical, well-organized code.""",

    "dictionary": """Dictionaries in Python are unordered collections that store data as key-value pairs. 
They allow fast access because each key directly points to its value. Keys must be unique and 
immutable, while values can be of any type. Dictionaries are ideal for representing structured data 
like JSON objects, configuration details, or records. They support operations such as adding, updating, 
deleting, searching, and iterating through keys and values. Python dictionaries are highly optimized and 
widely used in real applications, including data processing and APIs. Their flexibility and speed make them 
one of the most important data structures in Python.""",

    "list": """Lists are ordered, mutable collections used to store multiple items in a single variable. 
They allow storing mixed data types and support indexing, slicing, appending, inserting, and removing items. 
Lists are dynamic, meaning they grow or shrink as needed. They are commonly used for loops, data processing, 
and managing collections of information. Python’s list operations such as sort, reverse, extend, and 
comprehension make working with sequences powerful and efficient. Lists are foundational in Python and appear 
in almost every program, from handling user input to storing database records or processing files.""",

    "tuple": """Tuples are ordered, immutable collections that store data much like lists, but their values 
cannot be changed once created. They are used when you need reliable, fixed data that should not be modified. 
Tuples are memory-efficient and faster than lists, making them useful for performance-critical tasks. They are 
often used for grouping related values like coordinates, RGB colors, database records, and return values from 
functions. Because tuples are hashable, they can be used as dictionary keys or set elements. Their immutability 
helps ensure safer, more predictable code and prevents accidental modifications during execution.""",

    "string": """Strings in Python are sequences of characters used for storing and manipulating text. 
They are immutable, meaning once created, they cannot be changed directly. Python offers many string methods 
like upper, lower, replace, split, join, and find, allowing flexible text processing. Strings support 
indexing, slicing, formatting using f-strings, and escape characters for special symbols. They are essential 
for displaying messages, reading files, user input, constructing URLs, and building dynamic text. Python’s 
rich string manipulation abilities make working with data, logs, and natural language tasks easy, clean, 
and powerful in everyday programming.""",

    "set": """Sets are unordered collections of unique elements in Python. They automatically remove 
duplicates and are useful for mathematical operations like union, intersection, and difference. Sets are 
fast because they use hash tables internally. They are used to filter duplicates, compare groups, and check 
membership efficiently. Since sets do not maintain order or allow indexing, they are best suited for 
situations where uniqueness matters more than sequence. Python also includes frozen sets, which are 
immutable versions useful as dictionary keys. Sets help simplify logic and improve performance when dealing 
with large collections of items.""" ,

    "csv": """CSV (Comma-Separated Values) files store tabular data using commas to separate fields. 
Python’s built-in csv module allows easy reading and writing of rows using reader and writer objects. 
CSV files are lightweight, human-readable, and commonly used for exporting spreadsheets, databases, or 
machine learning datasets. You can loop through rows, convert them into dictionaries, or write new records. 
CSV is extremely useful when exchanging data between applications. Its simplicity and flexibility make it 
one of the most important formats for data storage and processing in Python programming and real-world 
projects.""",

    "txtfile": """TXT files store plain text and are one of the simplest and most universal file formats. 
Python provides open(), read(), write(), and close() to work with them. You can read line by line, append 
text, or overwrite content. Text files are useful for logs, notes, configuration settings, and simple data 
storage. Using context managers (with open...), Python ensures safe file handling. TXT processing is useful 
when working with scripts, automation tasks, and data cleaning. Even though they are simple, text files are 
used everywhere and understanding them is essential for file-based applications.""",

    "functions": """Functions in Python group reusable code into named blocks that perform specific tasks. 
They improve organization, reduce repetition, and make programs easier to maintain. Functions accept 
parameters, return values, and allow default or keyword arguments. They support variable scope, recursion, 
and modular design. Using functions, you can break large programs into smaller, logical components. Python 
also supports anonymous functions using lambda expressions. Functions are essential for clean, structured, 
and efficient programming, and form the foundation of most real-world Python applications.""",

    "closure": """A closure is a Python function that remembers values from its enclosing scope, even after 
the outer function has finished executing. Closures occur when an inner function uses variables defined in 
the outer function and is returned for later use. They enable data hiding, state retention, and function 
factories. Closures are useful for building decorators, callbacks, event handlers, and custom function 
generators. They help create cleaner, modular, and more flexible code without relying on classes. Understanding 
closures deepens your comprehension of how Python handles functions and variable scopes.""",

    "decorator": """Decorators are special functions that modify or enhance other functions without changing 
their original code. They use the @ symbol and wrap a function with additional behavior, such as logging, 
timing, validation, or authentication. Decorators rely on higher-order functions and closures. They help 
write cleaner, reusable logic and follow the DRY principle. Python provides built-in decorators like @staticmethod 
and @property, and you can create custom ones easily. Decorators are powerful tools used widely in frameworks, 
APIs, and advanced Python applications to improve modularity and maintainability.""",

    "callback": """A callback is a function passed as an argument to another function so it can be executed 
later. Callbacks allow flexible program design where functions can trigger user-defined behavior. They are 
common in event-driven programming, GUIs, asynchronous tasks, and APIs. Callbacks help decouple code, making 
functions more reusable and modular. They also allow customizing how tasks like sorting, filtering, or 
communication behave. Understanding callbacks is essential for advanced Python, especially when dealing with 
timers, threads, or asynchronous operations.""",

    "generators": """Generators are special functions that produce values one at a time using the yield 
keyword. They are memory-efficient because they do not store all values at once. Instead, they generate 
values on demand. This makes them ideal for large datasets, file streams, and infinite sequences. Generators 
pause and resume execution automatically, preserving state between yields. Python also offers generator 
expressions for concise creation. Generators improve performance and allow writing elegant, efficient loops 
without managing indexes manually. They are widely used in advanced programming, pipelines, and asynchronous 
tasks.""",

    "numpy": """NumPy is a powerful Python library for numerical computing. It provides multi-dimensional 
arrays, mathematical functions, and tools for fast data processing. NumPy arrays are more efficient and 
faster than Python lists. The library supports vectorized operations, broadcasting, random number generation, 
linear algebra, and complex calculations. It is the foundation of data science, machine learning, and 
scientific computing in Python. NumPy enables concise, high-performance code for tasks like matrix operations, 
statistics, simulations, and data analysis, making it essential for technical and scientific work.""",

    "pil": """PIL, now known as Pillow, is a Python library for image processing. It allows opening, editing, 
resizing, cropping, filtering, and saving images in many formats. Pillow supports color adjustments, drawing, 
thumbnail creation, and format conversions. It is widely used in automation, web applications, machine 
learning pipelines, and computer vision tasks. Using Pillow, you can manipulate pixels, overlay text, add 
watermarks, and prepare images for further analysis. It is simple to use yet powerful, making it one of the 
most important libraries for image-related tasks in Python applications.""",

    "nltk": """NLTK (Natural Language Toolkit) is a leading Python library for working with human language 
data. It includes tools for tokenization, stemming, lemmatization, tagging, parsing, and text classification. 
NLTK comes with sample corpora, making it easy to experiment with real data. It is widely used for building 
chatbots, sentiment analysis, keyword extraction, and linguistic research. NLTK simplifies complex natural 
language processing tasks and helps beginners understand the basics of NLP. While modern libraries like spaCy 
exist, NLTK remains invaluable for education and foundational text-processing tasks.""",

    "list comprehension": """List comprehension is a concise way to create lists using a single readable 
expression. It replaces long loops with a compact syntax that improves clarity and speed. List comprehensions 
can include conditions, transformations, and nested loops. They are faster than traditional loops because 
they are optimized internally. They are widely used for filtering data, transforming sequences, extracting 
information, and creating dynamic lists. Their clean syntax encourages writing elegant and Pythonic code and 
is one of the most commonly used features in modern Python programming.""",

    "oop": """Object-Oriented Programming (OOP) organizes code into classes and objects. It helps structure 
complex programs through concepts like encapsulation, inheritance, and polymorphism. Classes group data and 
behavior, making code cleaner and reusable. OOP makes modeling real-world systems easier by representing 
entities as objects. It supports creating modular, scalable, and maintainable applications. Python's OOP 
system is flexible and powerful, enabling developers to build GUIs, games, frameworks, and large software 
projects. Understanding OOP is essential for professional Python development.""",

    "map": """map() applies a function to every item in an iterable and returns a map object. It is useful 
for transforming data without writing explicit loops. map() works well with lambda functions and improves 
code readability when performing uniform operations on lists or sequences. It is memory-efficient and often 
faster than list-based loops. map() is commonly used in data cleaning, type conversion, and building 
pipelines. While list comprehensions are more common in Python, map() remains powerful for functional-style 
programming.""",

    "reduce": """reduce() from the functools module applies a function repeatedly to reduce a list to a 
single value. It is useful for tasks like summing numbers, finding products, or combining elements logically. 
reduce() encourages functional programming and eliminates the need for manual loops. Though often replaced by 
built-in functions like sum(), reduce() is valuable for custom aggregation tasks. It helps write concise, 
mathematical operations and remains widely used in data processing pipelines.""",

    "filter": """filter() selects elements from an iterable based on a condition. It returns a filter object 
containing only elements that meet the criteria. filter() works well with lambda functions and helps build 
clean, readable code for data validation, searching, and cleanup. It is memory-efficient because it produces 
results lazily. Although list comprehensions can also filter data, filter() remains useful in functional-style 
programming.""",

    "zip": """zip() pairs elements from multiple iterables into tuples. It is useful for combining lists, 
creating dictionaries, iterating through related sequences, and parallel looping. zip() stops at the shortest 
sequence to avoid errors. It improves readability and replaces manual indexing when working with multiple 
lists. Many practical tasks like merging data, pairing keys and values, and grouping coordinates rely on 
zip(). It is a simple yet powerful tool used frequently in Python programming."""
}


# ---------------- Decorator ----------------
def summary_bot(func):
    def wrapper(topic):
        topic = topic.lower().strip()

        if topic == "topics":
            print("\nAvailable topics:")
            for t in summaries:
                print(" -", t)
            print()
            return

        if topic == "exit":
            print("Returning to main menu...\n")
            return "exit"

        if topic not in summaries:
            print("❌ Topic not found. Type 'topics' to see available topics.\n")
            return

        result = func(topic)
        print("\n" + ("-" * 60))
        print(result)
        print("-" * 60 + "\n")

    return wrapper


# -------- Summary function (decorated) --------
@summary_bot
def get_summary(topic):
    return summaries[topic]


# -------- Summary Chatbot Loop --------
def summary_chatbot():
    print("\n📘 PYTHON SUMMARY ")
    print("Type a topic to receive a 100-word summary.")
    print("Type 'topics' to view list.")
    print("Type 'exit' to return to main menu.\n")

    while True:
        user_input = input("Enter topic: ")
        result = get_summary(user_input)

        if result == "exit":
            break



# ============================================================================
#               MAIN MENU BY ANKITHA AND AMARTYA
# ============================================================================

def start_file6():
    while True:
        print("\n========== PyBUDDY - A PYTHON LEARNING CHATBOT ==========")
        print()
        print()
        time.sleep(2)
        print("Welcome aboard! I’m here to guide you, learn with you, and make your journey enjoyable. Let’s explore and grow together!")
        time.sleep(3)
        print()
        print()
        print("Please choose what you want to do today")
        time.sleep(2)
        print()
        print("1. Riddles (GUI)")
        print("2. Daily Challenge")
        print("3. Guess the Output")
        print("4. Find the Error")
        print("5. MCQ Test")
        print("6.Flashcards")
        print("7. Python Summary")   
        print("8. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            start_file9()
        elif choice == '2':
            daily_challenge()
        elif choice == '3':
            guess_output_menu()
        elif choice == '4':
            find_error_menu()
        elif choice == '5':
            mcq_menu()
        elif choice=='6':
            flashcards()
        elif choice == '7':
            summary_chatbot()
        elif choice == '8':
            time.sleep(1)
            print("\n“Thanks for spending your time here! Take care, keep learning, and come back soon. Wishing you success and smiles ahead!”")
            break
        else:
            print("Invalid choice! Try again.")


# ============================================
#           RUN MAIN MENU
# ============================================

if __name__ == "__main__":
    start_file6()
