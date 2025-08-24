from collections import defaultdict, Counter

ANSWERS = [line.strip() for line in open("answers.txt")]
GUESSES = [line.strip() for line in open("guesses.txt")]
NUMBER_OF_ANSWERS = len(ANSWERS)

def compare(guess, answer):
    """
    Compares two guesses.
    2 is green and means the character is in the right position.
    1 is yellow and means the character is in the answer, but in a different position.
    0 is black and means the character isn't in the answer (or rather, there are no more instances of this character within the solution).
    """
    result = ["0"] * 5
    answer_counts = Counter(answer)

    for i, (g, a) in enumerate(zip(guess, answer)):
        if g == a:
            result[i] = "2"
            answer_counts[g] -= 1

    for i, g in enumerate(guess):
        if result[i] == "0" and answer_counts[g] > 0:
            result[i] = "1"
            answer_counts[g] -= 1

    return "".join(result)

def get_remaining_possible_answers(guess, comparison, answers_universe=ANSWERS):
    """
    Finds possible answers given a guess and a comparison, within a group of possible answers.
    If the comparison yielded a 2 (green) this means that the character and position must be met in every solution. As such, we discard any solution that doesn't fit.
    If the comparison yielded a 1 (yellow) we have to make sure that there is an instance of this character in the solution, but not in that position.
    If the comparison yielded a 0 (black), then we have to make sure that the character doesn't show up elsewhere in the guess with a number different from zero.
    If it doesn't, then solutions can't include that character.
    """
    remaining = []
    for answer in answers_universe:
        valid = True
        for i, (char, result) in enumerate(zip(guess, comparison)):
            if result == "2" and answer[i] != char:
                valid = False; break
            if result == "0" and (answer[i] == char or char in answer and not any(c == char and r != "0" for c, r in zip(guess, comparison))):
                valid = False; break
            if result == "1" and (char not in answer or answer[i] == char):
                valid = False; break
        if valid:
            remaining.append(answer)
    return remaining


def get_best_guess(remaining_answers):
    """
    Finds the best possible guess within a group of selected answers.
    To do this, it runs every comparison between possible guesses and the group of remaining answers.
    For each guess, a comparisons dictionary is stored
    where keys are ocurring comparisons and values are lists of guesses that produce such comparisons.
    The value associated with each guess will be the comparison that is produced by the
    greatest amount of guesses.
    """

    values = {}
    for guess in GUESSES:
        comparisons = defaultdict(list)
        for answer in remaining_answers:
            comparison = compare(guess, answer)
            comparisons[comparison].append(answer)
        worst_case = max(len(comparison) for comparison in comparisons.values())
        values[guess] = worst_case        

    for answer in remaining_answers:
        if values[answer] == 1:
            return answer, values[answer]
    
    return min(values.items(), key=lambda kv: kv[1])

if __name__ == "__main__":
    while True:
        remaining_answers = ANSWERS
        guess = get_best_guess(remaining_answers)[0]
        for i in range(6):
            comparison = input(f"[{i + 1}] Enter your output after playing {guess}: ")
            if comparison == "": 
                print() 
                break

            remaining_answers = get_remaining_possible_answers(guess, comparison, remaining_answers)
            best_guess, value = get_best_guess(remaining_answers)
            guess = best_guess
        
            print(f"Remaining answers: {len(remaining_answers)} {(remaining_answers if len(remaining_answers) <= 10 else "")}")
            print(f"Your next best guess is {best_guess} ({value})")
        
            if len(remaining_answers) == 1:
                print("You won!\n")
                break   