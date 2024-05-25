import pandas as pd
import random

def do_turn(df, answer, guess):
    turn = ['X', 'X', 'X', 'X', 'X']
    seen = []
    i = 0
    for answer_char, guess_char in zip(answer, guess):
        if answer_char == guess_char:
            turn[i] = 'G'
            df = df[df['word'].str[i] == guess_char]
            # print(df.count())
            # print()
        elif guess_char in answer:
            if guess_char not in seen:
                turn[i] = 'Y'
                df = df[(df['word'].str.contains(guess_char)) & (df['word'].str[i] != guess_char)]
                # print(df.count())
                # print()
        else:
            df = df[~df['word'].str.contains(guess_char)]
            # print(df.count())
            # print()
        i = i + 1
        seen.append(guess_char)
    return df, turn


def count_vowels(word):
    vowels = 'aeiouAEIOU'
    return sum(1 for letter in word if letter in vowels)


attempt_count = []
for i in range(500):
    df = pd.read_csv('wordle_answers.csv')
    df['num_vowels'] = df['word'].apply(count_vowels)
    dv = df[df['num_vowels'] == 0]

    random_row1 = df.sample(n=1)
    answer = str(random_row1['word'].values[0])

    attempts = 0
    random_3vow = dv.sample(n=1)
    guess = str(random_3vow['word'].values[0])
    while answer != guess:
        df, turn = do_turn(df, answer, guess)
        random_row = df.sample(n=1)
        guess = str(random_row['word'].values[0])
        attempts = attempts + 1

    print("Total Attempts: ", attempts)
    attempt_count.append(attempts)

mean = sum(attempt_count) / len(attempt_count)
print(mean)
