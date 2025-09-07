import random
import time

# Function to create a random question
def create_question(var_min_num, var_max_num):
    var_num1 = random.randint(var_min_num, var_max_num)
    var_num2 = random.randint(var_min_num, var_max_num)
    var_operator = random.choice(["+", "-"])
    return f"{var_num1} {var_operator} {var_num2}"

# Function to ask a question and check answer
def ask_question(var_question):
    var_start_time = time.time()
    var_user_answer = int(input(f"What is {var_question}? "))
    var_end_time = time.time()

    var_time_taken = int(var_end_time - var_start_time)
    var_correct_answer = eval(var_question)

    if var_user_answer == var_correct_answer:
        return True, var_time_taken
    else:
        return False, var_time_taken

# ---------------- Main Program ---------------- #
print("Welcome to Greg's Maths Test!")

# Difficulty selection
print("Select a difficulty:")
print("1) Easy")
print("2) Medium")
print("3) Hard")
    
while True:
    var_difficulty_choice = input("> ")

    if var_difficulty_choice == "1":
        var_num_questions = 5
        var_max_num = 10
        print("Easy mode selected!")
        break
    elif var_difficulty_choice == "2":
        var_num_questions = 10
        var_max_num = 20
        print("Medium mode selected!")
        break
    elif var_difficulty_choice == "3":
        var_num_questions = 15
        var_max_num = 50
        print("Hard mode selected!")
        break
    else:
        print("Invalid choice! Enter 1, 2 or 3.")

var_score = 0
var_correctness_list = []
var_time_list = []

# Loop through questions
for var_q_number in range(1, var_num_questions + 1):
    print(f"\nScore: {var_score}")
    print(f"Question {var_q_number} of {var_num_questions}")

    # Last question = challenge
    if var_q_number == var_num_questions:
        print("Challenge question!")
        var_question = create_question(var_max_num, var_max_num * 2)
    else:
        var_question = create_question(var_max_num // 2, var_max_num)

    var_is_correct, var_time_taken = ask_question(var_question)

    var_correctness_list.append(var_is_correct)
    var_time_list.append(var_time_taken)

    if var_is_correct:
        var_points_awarded = max(10 - var_time_taken, 1)
        var_score += var_points_awarded
        print(f"Correct! You answered in {var_time_taken} second(s) - {var_points_awarded} point(s) awarded.")
    else:
        print(f"Incorrect! You answered in {var_time_taken} second(s) - no points awarded.")

# Results
var_total_correct = var_correctness_list.count(True)
var_percentage_correct = round((var_total_correct / var_num_questions) * 100)
var_avg_time = round(sum(var_time_list) / len(var_time_list))

print("\nResults:")
print(f"Final score: {var_score}")
print(f"Correct answers: {var_percentage_correct}%")
print(f"Average response time: {var_avg_time}s")

print("\nBreakdown:")
print("Question   Correct   Time")
print("--------   --------  -------")
for i in range(var_num_questions):
    var_correct_str = "Yes" if var_correctness_list[i] else "No"
    print(f"    {i+1:<9}{var_correct_str:<9}{var_time_list[i]}s")



