import random
import datetime

ANSWERS = [line.strip() for line in open("answers.txt")]
GUESSES = [line.strip() for line in open("guesses.txt")]
NUMBER_OF_ANSWERS = len(ANSWERS)

def compare(guess, answer):
    result = [0, 0, 0, 0, 0]
    used = [False, False, False, False, False]

    for i in range(len(guess)):
        if guess[i] == answer[i]:
            result[i] = 2
            used[i] = True

    for i in range(len(guess)):
        if result[i] == 0 and guess[i] in answer:
            index_in_answer = answer.index(guess[i])
            while used[index_in_answer]:
                index_in_answer = answer.find(guess[i], index_in_answer + 1)
                if index_in_answer == -1:
                    break
            
            if index_in_answer != -1:
                result[i] = 1
                used[index_in_answer] = True
    
    return [(guess[i], result[i]) for i in range(len(guess))]

def get_remaining_possible_answers(comparison):
    remaining = []
    for answer in ANSWERS:
        valid = True
        for i, (char, result) in enumerate(comparison):
            if result == 2 and answer[i] != char:
                valid = False
                break
            if result == 0 and char in answer:
                valid = False
                break
            if result == 1 and (char not in answer or answer[i] == char):
                valid = False
                break
        if valid:
            remaining.append(answer)
    return remaining

with open("results.txt", "w") as file:
    i = 0
    for guess in GUESSES:
        if i % 10 == 0:
            print(f"[{datetime.datetime.now()}] Processing guess {i}: {guess}")
        sum_of_remaining_answers = 0
        
        for answer in ANSWERS:
            comparison = compare(guess, answer)
            number_of_remaining_answers = len(get_remaining_possible_answers(comparison))
            sum_of_remaining_answers += number_of_remaining_answers
        average_remaining_answers = sum_of_remaining_answers / (NUMBER_OF_ANSWERS ** 2)
        
        if average_remaining_answers < 0.03:
            print(f"Great word found: {guess} ({average_remaining_answers:.4f})")
        if average_remaining_answers > 0.2:
            print(f"Terrible word found: {guess} ({average_remaining_answers:.4f})")
        
        file.write(f"{guess}: {average_remaining_answers}\n")
        i += 1