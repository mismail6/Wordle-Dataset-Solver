import pandas as pd
from wordle_scraper import WordleScraper

df = pd.read_csv('wordle_answers.csv')

def count_vowels(word):
    vowels = 'aeiouAEIOU'
    return sum(1 for letter in word if letter in vowels)


df['num_vowels'] = df['word'].apply(count_vowels)
dv = df[df['num_vowels'] == 3]


# Today's New York Times Wordle
scraper = WordleScraper()
answer = scraper.get_wordle_for_today().lower()
print("Today's Wordle: ", answer)

print()
print('Total words: ', df['word'].count())
print('answer: ', answer)
print()

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


attempts = 0
random_3vow = dv.sample(n=1)
guess = str(random_3vow['word'].values[0])
print('FIRST GUESS IS: ', guess)
while answer != guess:
    df, turn = do_turn(df, answer, guess)
    print(guess)
    print(df['word'].count())
    print(turn)
    print()
    random_row = df.sample(n=1)
    guess = str(random_row['word'].values[0])
    attempts = attempts + 1

print()
print("Total Attempts: ", attempts)
