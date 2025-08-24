from main import ANSWERS, get_remaining_possible_answers, compare, get_best_guess
from collections import defaultdict

turns = defaultdict(int)
initial_guess = input("Enter guess for simulation (best is \'arise\'): ")
for solution in ANSWERS:
    guess = initial_guess
    print("SOLUTION:", solution)
    remaining_answers = ANSWERS
    for i in range(6):
        print(f"Guess [{i}]: {guess}")
        comparison = compare(guess, solution)
        remaining_answers = get_remaining_possible_answers(guess, comparison, remaining_answers)
        
        if len(remaining_answers) == 1 and guess == remaining_answers[0]:
            print("You won!\n")
            turns[i] += 1
            break
        
        best_guess, _ = get_best_guess(remaining_answers)
        guess = best_guess
    
    print("----------------------")

print(f"Total wins: {turns} / {len(ANSWERS)}")