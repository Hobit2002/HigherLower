import random
print("Welcome in Higher Lower Casiono. The higher will be your risk, the lower you'll win!")
#Prepare deck
GameDeck=[]
Table=[]
DiscardDeck=[]
for Symbol in ['♠','♡','♢','♣']:
    for relValue,imageValue in enumerate(['2','3','4','5','6','7','8','9','10','J','Q','K','A']):
        GameDeck.append({'image':imageValue+Symbol,'value':relValue})
random.shuffle(GameDeck)

def placeCards():
    NeededCards=10-len(Table)
    Table+=GameDeck[0:NeededCards]
    del GameDeck[0:NeededCards]
    LineToPrint = Table[0]["image"] + 9*" ?"
    print(LineToPrint)

#Introduce player to the game
print("""Hi, You came here with 1000€ and my job is to strip you of them.
    However, not to be shut down immediately, I'll give you a chance to be the one, who enriches himself.
    In a moment, I've already placed ten cards here, of with only one is turned faced up.
    At first, you'll choose a number from interval <4,10> and amount of money, you're willing to bet.
    Then I'll start turning the cards over. Their count will be equal to the number you've chosen.
    Before each turnover, youl'll bet if the next card is of smaller, equal or biger value to the 
    preceding one. If the truth will be on your side, the amount of your money will be multiplied by two
    (and if you keep your success till the end, I'll giv it to you).
    However, if you'll mislead, I'll take your money away.""")

placeCards()
Finances = 1000
CardNum = int(input("With how many cards do you want play Choose at least 4 and at most 10? "))
Bet = int(input("How much money do you but. (You have {Finances}€ in the moment)"))
