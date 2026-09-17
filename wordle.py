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

def score_guess(guess, remaining_answers=ANSWERS, worst_case=False):
    """
    Scores a guess by comparing it to all remaining possible answers and calculating how much it reduces its search space.
    
    Create a dictionary that stores possible comparisons (like 02200) as keys and lists of answers that would yield such comparison as values.
    If worst_case:
    - Store the length of the worst case scenario as the value of the guess in the scores dictionary.
    Else:
    - Store the average length of all possible comparisons as the value of the guess in the scores dictionary.
    """

    comparisons = defaultdict(list)
    for answer in remaining_answers:
        comparison = compare(guess, answer)
        comparisons[comparison].append(answer)

    if worst_case:
        score = max(len(comparison) for comparison in comparisons.values())
    else:
        score = sum(len(comparison) for comparison in comparisons.values()) / len(comparisons)

    return score

def score_all_guesses(remaining_answers=ANSWERS, hard_mode=False, worst_case=False):
    scores = {}
    for guess in (GUESSES if not hard_mode else remaining_answers): 
        score = score_guess(guess, remaining_answers, worst_case)
        scores[guess] = score
    return scores

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

def get_best_guess(remaining_answers=ANSWERS, hard_mode=False, worst_case=False):
    """
    Finds the best possible guess within a group of selected answers.
    Returns both the guess itself and its score.
    
    Scores every guess and returns the guess with the lowest score. If a guess is also a possible answer and has only one possible answer remaining in the worst case scenario, then it must be the solution. Return it.
    """

    scores = score_all_guesses(remaining_answers, hard_mode, worst_case)

    for answer in remaining_answers:
        if scores[answer] == 1:
            return answer, scores[answer]

    best_guess = min(scores, key=scores.get)
    return best_guess, scores[best_guess]

