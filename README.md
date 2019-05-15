BlackJack a classic casino game

# Overview of the game
* Dealer is the machine
* A Players starts with 100 chips
* If the hand is won, bet is added to chips total
* Face Cards[KING, QUEEN, JACK] value equals 10pts
* Normal Cards [2-10 (any suit)] value equals [faceValue]pts
    - eg: 4 of Hearts = 4pts
    - eg: 10 of Diamonfs = 10pts
* Aces have 11pt or 1pts depending on players position in the game
    - if the current hand of the player goes beyond 21 with the new hit and player holds an ace, his new value is adjusted to value = original_value + newCard_pts - 10
* Dealers Drwas card till it reaches a total hand value of 17

# Who Wins
* If the player exceeds 21 player looses
* If the dealer exceeds 21 player wins
* If the player exceeds dealer value but is less than or equals 21 in total player wins
* If the dealer exceeds player value but is less than or equuals 21 in total plyaer losses
* If the points are equal game is tied



# How To Play?
Clone the repo


# Contribute
* Multiplayer Design
* Adding User Interface [Godot Engine]
* Code Refactor
* Documentaion and Commenting [High Priority]

```sh
$ cd repo
$ python3 Play.py
```

