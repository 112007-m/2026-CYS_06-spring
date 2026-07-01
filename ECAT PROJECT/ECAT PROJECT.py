# ECAT EXAM PORTAL (TERMINAL BASED)

## 🔹 DATA STORAGE

questions = [
{"q": "2+2=?", "A": "3", "B": "4", "C": "5", "D": "6", "ans": "B"},
{"q": "Capital of Pakistan?", "A": "Lahore", "B": "Karachi", "C": "Islamabad", "D": "Quetta", "ans": "C"},
{"q": "5*2=?", "A": "10", "B": "12", "C": "8", "D": "15", "ans": "A"},
{"q": "Sun rises from?", "A": "West", "B": "North", "C": "South", "D": "East", "ans": "D"},
{"q": "Python is?", "A": "Snake", "B": "Language", "C": "Game", "D": "Food", "ans": "B"},
{"q": "10/2=?", "A": "3", "B": "4", "C": "5", "D": "6", "ans": "C"},
{"q": "Water formula?", "A": "H2O", "B": "CO2", "C": "O2", "D": "NaCl", "ans": "A"},
{"q": "3^2=?", "A": "6", "B": "9", "C": "12", "D": "3", "ans": "B"},
{"q": "Earth is?", "A": "Star", "B": "Planet", "C": "Moon", "D": "Sun", "ans": "B"},
{"q": "Speed unit?", "A": "m/s", "B": "kg", "C": "m", "D": "s", "ans": "A"}
]

all_results = []




# LOGIN
def login(user, pwd):
    for i in range(3):
        u = input("Username: ")
        p = input("Password: ")
        if u == user and p == pwd:
            return True
        else:
            print("Wrong! Attempts left:", 2-i)
    return False





# EXAM
def start_exam(name, roll):
    answers = {}
    correct = 0
    wrong = 0
    skip = 0

    for i in range(len(questions)):
        q = questions[i]

        print("\nQ", i+1, q["q"])
        print("A)", q["A"], "B)", q["B"], "C)", q["C"], "D)", q["D"])

        ans = input("Answer (A/B/C/D/S/SUBMIT): ").upper()

        if ans == "SUBMIT":
            break

        answers[i] = ans

        if ans == "S":
            skip += 1
        elif ans == q["ans"]:
            print("Correct ✅")
            correct += 1
        else:
            print("Wrong ❌")
            wrong += 1

    score = correct*4 - wrong
    total = len(questions)*4
    percent = (score/total)*100

    if percent >= 80:
        grade = "EXCELLENT"
    elif percent >= 65:
        grade = "GOOD"
    elif percent >= 50:
        grade = "AVERAGE"
    else:
        grade = "BELOW AVERAGE"

    print("\nScore:", score)
    print("Percentage:", percent)
    print("Grade:", grade)

    result = {
        "name": name,
        "roll": roll,
        "score": score,
        "percent": percent,
        "grade": grade
    }

    all_results.append(result)




# ADMIN FUNCTIONS
def view_questions():
    for i in range(len(questions)):
        q = questions[i]
        print(i+1, q["q"], "Ans:", q["ans"])



def add_question():
    q = input("Enter question: ")
    A = input("A: ")
    B = input("B: ")
    C = input("C: ")
    D = input("D: ")
    ans = input("Correct (A/B/C/D): ").upper()

    questions.append({"q": q, "A": A, "B": B, "C": C, "D": D, "ans": ans})





def delete_question():
    n = int(input("Enter question number: "))
    if n <= len(questions):
        questions.pop(n-1)




def view_results():
    for r in all_results:
        print(r)




# MAIN MENU
while True:
    print("\n1. Admin Portal")
    print("2. Student Portal")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        if login("ecat_admin", "ecat@2024"):
            while True:
                print("\n1.View Questions 2.Add 3.Delete 4.Results 5.Back")
                c = input("Choice: ")

                if c == "1":
                    view_questions()
                elif c == "2":
                    add_question()
                elif c == "3":
                    delete_question()
                elif c == "4":
                    view_results()
                else:
                    break

    elif choice == "2":
        if login("student", "student123"):
            name = input("Enter Name: ")
            roll = input("Enter Roll: ")
            start_exam(name, roll)

    elif choice == "3":
        break

    else:
        print("Invalid choice")



