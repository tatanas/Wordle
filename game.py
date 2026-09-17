from wordle import compare, get_remaining_possible_answers, get_best_guess, ANSWERS, GUESSES, score_guess

ATTEMPTS = 6
HARD_MODE = False
WORST_CASE = False
INITIAL_GUESS = "arise" # hardcoded to save time

def solve(solution):
    remaining_attempts = ATTEMPTS
    remaining_answers = ANSWERS.copy()

    flow = []

    while remaining_attempts > 0:
        if remaining_attempts == ATTEMPTS:
            guess = INITIAL_GUESS 
        else:
            guess, _ = get_best_guess(remaining_answers, hard_mode=HARD_MODE, worst_case=WORST_CASE)

        flow.append(guess)

        remaining_attempts -= 1
        comparison = compare(guess, solution)
        flow.append(comparison)

        remaining_answers = get_remaining_possible_answers(guess, comparison, remaining_answers)
        
        if comparison == "22222":
            break

    # return number of attempts and each of the guesses used
    return ATTEMPTS - remaining_attempts, flow

if __name__ == "__main__":
    # dictionary where keys are solutions and values are a tuple with the number of guesses it took to solve and the list of guesses used
    results = {}
    for solution in ANSWERS[100:200]:
        print(f"Solving for {solution}...")
        attempts, flow = solve(solution)
        print(f"    Solution {solution} took {attempts} attempts. Flow: {flow}")
        results[solution] = (attempts, flow)

    # write to a file
    with open(f"results_{INITIAL_GUESS}-2.txt", "w") as f:
        for solution, (attempts, flow) in results.items():
            f.write(f"{solution}: {attempts}. Flow: {flow}\n")