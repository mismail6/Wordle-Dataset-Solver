Initially I wanted to consider a Deep Learning based approach to efficiently solve wordle. However, after implementing an algorithm to filter out possible words after each guess, I realized a simple game like Wordle doesn't really need the power of ML.

The CSV dataset contains about 2310 words that the game randomly selects for their daily wordle. The algorithm continuously narrows down the dataframe in a while loop until the word is found.

Running the tester class on 500+ plays shows that the algorithm guesses on average 3~4 turns which correlated with the average turns people take to win.
This average can reduce depending on the strategy of the subsequent guesses. For example, selecting words with 2 or 3 vowels leads to a faster win than usual.

The line below is the strategy I used to get an average guess turn of about 3.34%
```
dv = df[df['num_vowels'] == 3]
```

Feel free to suggest any improvements!
