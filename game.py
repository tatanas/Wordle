import random
from wordle import compare, get_remaining_possible_answers, get_best_guess, ANSWERS, GUESSES, score_guess

ATTEMPTS = 6
HARD_MODE = False
WORST_CASE = True

if __name__ == "__main__":
    solution = random.choice(ANSWERS)
    remaining_attempts = ATTEMPTS
    remaining_answers = ANSWERS.copy()

    while remaining_attempts > 0:
        guess = input("Enter your guess: ")
        comparison = compare(guess, solution)
        print(f"Comparison: {comparison}")
        score = score_guess(guess, remaining_answers, worst_case=WORST_CASE)
        _, best_score = get_best_guess(remaining_answers, hard_mode=HARD_MODE, worst_case=WORST_CASE)
        print(f"Your score: {score}. Best score: {best_score}")

        remaining_answers = get_remaining_possible_answers(guess, comparison)
        print(f"Remaining answers: {len(remaining_answers)}")

        if comparison == "22222":
            print("Congratulations! You've guessed the word!")
            break

        remaining_attempts -= 1

        if remaining_attempts == 0:
            print(f"Game over! The word was {solution}.")