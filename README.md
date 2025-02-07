The wordle_scraper gets the daily wordle and the solver mimicks the actual game and tries to guess the wordle in as few tries as possible.

Initially, I wanted to consider a Deep Learning based approach to efficiently solve wordle. However, after implementing an algorithm to filter out possible words after each guess, I realized a simple game like Wordle doesn't really need the power of ML.

The CSV dataset contains about 2310 words and the algorithm continuously narrows down the dataframe until the word is found.

Running the tester class on 500+ plays shows that the algorithm guesses on average 3~4 turns which correlates with the average turns people take to win.
This average can be reduced depending on the strategy of the subsequent guesses. For example, selecting words with 2 or 3 vowels leads to a faster win than usual.

The line below is the strategy I used to get an average guess turn of about 3.34%
```
dv = df[df['num_vowels'] == 3]
```

Feel free to suggest any improvements!
