# Run through every possible answer in the game.
# Always use "arise" as first guess.
# Store a dictionary where the key is the answer and the value is the number of attempts it took to guess it.

from collections import defaultdict
from wordle import compare, get_remaining_possible_answers, get_best_guess, ANSWERS, GUESSES, score_guess

HARD_MODE = False
WORST_CASE = False
MAX_ATTEMPTS = 6

results = defaultdict()

for solution in ANSWERS[:100]:
    remaining_attempts = MAX_ATTEMPTS
    remaining_answers = ANSWERS.copy()
    results[solution] = 0

    while remaining_attempts > 0:
        if remaining_attempts == MAX_ATTEMPTS:
            guess = "arise"
        else:
            guess, _ = get_best_guess(hard_mode=HARD_MODE, worst_case=WORST_CASE)
        print(f"Solution: {solution}. Remaining attempts: {remaining_attempts}.")
        
        results[solution] += 1
        comparison = compare(guess, solution)
        remaining_answers = get_remaining_possible_answers(guess, comparison)

        if comparison == "22222":
            break

        print(f"Guess: {guess}. Comparison: {comparison}. Remaining answers: {len(remaining_answers)}")    

        remaining_attempts -= 1
        print(f"Remaining attempts for {solution}: {remaining_attempts}")
        if remaining_attempts == 0:
            print(f"Failed to guess {solution} in {MAX_ATTEMPTS} attempts.")

    print(f"Solution {solution} took {results[solution]} attempts.")

