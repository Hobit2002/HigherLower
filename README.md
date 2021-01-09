# HigherLower
A simple terminal game written in Python. For more information read README.md

## Prerequisities
All you need to enter into the world of average gambling game is:
- **Python 3**, no third party libraries are needed. 
- **A terminal which can display symbols such as hearth or diamond properly**

## Rules
(It is not necssary to study this part thoroughly, after the launch, game introduces itself
However, in terms of explaining, more is always better so...)
> 1)To start a game, you have to doubleclick on RunMe.py (or ) a terminal window will pop up and you'll see:
>- Game rules
>- Ten cards of which only the first one is turned face up
> 2)You have to corectlly estimate multiple times in a row if the next card will be of higher,lower or equal value than the already turned one. First of all you'll choose how many times, you'll be given this tasks (your choice has to be at least 4 and at most 9), then you'll have to decide how much money you want to bet (you start with 1000€).
> 3)Time for estimation! Insert your guess and see the turning of the next card. If your guess is incorrect, you'll loose the money you've bet and the turn will end. Otherwise, the game continues.
> 4)If all your guesses are correct, you'll obtain a price worth of the staked sum multiplied by two for each guess.
> 5)One turn ends and other starts  

## Codeguide
Since code itself has comments inside which should be enough to explain its structure, I'll describe only shadow of its skeleton here.
The whole programm stands on three important lists:
- Deck
- Table
- Deck for discarded cards

All these lists are filled with card dictionaries during the game.
Card dictionaries are data structures that contain following items:
- 'value' : numeric value of the card
- 'image' : numeric or in the case of stronger cards letteric value + symbol of the card (they were added to the game just to bring terminal window nearer to Las Vegas casinos, but don't influence it in any way)

Just after its activation the programm prepares the deck (using very simple cycles generates the cards and puts them into the game deck which is shuffled after this proccess).
Then it defines methods for:
- preparing a game turn (filling in table list so that there are ten cards in it and then showing the first card)
- showing a new card (gets number of cards which should shown as a parameter and then prints their images)
Definitions of these simple functions are followed by explanation of rules for players too impatient to read these
instructions after which cycle of turns starts.
During each turn player sees the table with one shown and nine covert cards (their line is printed by the first of above-mentioned functions) and has to decide:
- How many cards he want to guess
- How much money he wants to bet (this sum is automaticly substracted from player's finances)
In both cases the program keeps asking, until user inserts proper data.(No type errors should occur if there are letters or special symbols in his answers and also such cheats as negative wages aren't accepted).
And then the turn can start!
The turn consist in cycle in which the following procedures happen for n times where n equals to maximal number of guessed cards:
By (not) inserting approppriate values the player guesses how mighty next card will be. Program saves his estimation to the variable and by calling the second above-metioned functions shows to the player what the next card's value was. If players' guess was right, the variable in which he bet money is multiplied by two, otherwise the cycle is ended.
If player win all his guesses the variable with his price is added back to his finances as the turn ends.
After each turn cycle, all showed cards from Table, except the last one which serves as the opening card of the next turn, are moved to Deck for discarded cards from which they are, shuffled, returned back to the game deck, if its cards run out and it therefore throws IndexError during the first of above-mentioned functions.
The game cycle is connditioned bythe fact, that the player has more than 0€, once this condition is negative, game ends. However whenever a turn ends, the program reminds the player, that he can end it anytime by pressing Ctrl+C, if it become boring, which is very likely to happen quite soon.
