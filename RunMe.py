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
    global Table
    global GameDeck
    global DiscardDeck
    NeededCards=10-len(Table)
    try:
        Table+=GameDeck[0:NeededCards]
    except IndexError:
        random.shuffle(DiscardDeck)
        GameDeck+=DiscardDeck
        DiscardDeck=[]
        Table+=GameDeck[0:NeededCards]
        print("I've shuffeld discarded card to the deck, so be ready to see them")
    del GameDeck[0:NeededCards]
    LineToPrint = Table[0]["image"] + 9*" ?"
    print(LineToPrint)

def turnCard(serialNum):
    ToPrint=""
    for sn in range(serialNum+1):
        ToPrint+=Table[sn]['image']+" "
    ToPrint+="? "*(9-serialNum)
    print(ToPrint)

#Introduce player to the game
print("""
    Hi, You came here with 1000€ and my job is to strip you of them.
    However, not to be shut down immediately, I'll give you a chance to be the one, who enriches himself.
    In a moment, I've already placed ten cards here, of with only one is turned faced up.
    At first, you'll choose a number from interval <4,10> and amount of money, you're willing to bet.
    Then I'll start turning the cards over. Their count will be equal to the number you've chosen.
    Before each turnover, youl'll bet if the next card is of smaller, equal or biger value to the 
    preceding one. If the truth will be on your side, the amount of your money will be multiplied by two
    (and if you keep your success till the end, I'll giv it to you).
    However, if you'll mislead, I'll take your money away.
    If you get bored, press Ctrl+C""")
#Start the game
Finances = 1000
while Finances>0:
    #Show cards and ask player for Game parameters
    placeCards()
    #Ask for a number of cards player wants to play with
    CardNum=0
    while CardNum<3 or CardNum>9:
        try:
            CardNum = int(input("With how many cards do you want play? Choose at least 4 and at most 9. "))
            if CardNum>9:print("Your number can't be higher than 9.")
            elif CardNum<4:print("Your number can't be lower than 4")
        except ValueError:
            print("Your answer has to be a number.")
    #Let the player bet his money 
    Bet=-1
    while Bet > Finances or Bet<0:
        try:
            Bet = int(input("How much money do you bet(You have %s€ in the moment)?"%(Finances)))
            if Bet>Finances:print("Come on! You can't bet money you don't have.")
            elif Bet<0:print("Do you think we are fools? Stop begging and play!")
        except ValueError:
            print("Your answer has to be a number.")
    Finances-=Bet
    #Start turning the cards over
    for cn in range(1,CardNum+1):
        #Let player bet
        Prediction = input("Higher:h; Lower:l;Equal: nothing, just press Enter:")+" "
        #Turn over the next card
        print("Lets turn the card:")
        turnCard(cn)
        #If the prediction was wrong, end the turn and move to the next
        OldValue=Table[cn-1]['value']
        NewValue=Table[cn]['value']
        HigherCond = Prediction[0].lower()=="h" and NewValue>OldValue
        LowerCond = Prediction[0].lower()=="l" and NewValue<OldValue
        EqualCond = len(Prediction)==0 and NewValue==OldValue
        if HigherCond or LowerCond or EqualCond:
            Bet*=2
            print("Lucky you! Your bet was multiplied so now I owe you %s€"%Bet)
        else:
            print("I'm sorry. But you've lost.")
            Bet=-1
            break
    #If player wins all guesses, give him money he deserves
    if Bet>0:
        print("Congratulations. You've won and I'll give you %s€"%Bet)
        Finances+=Bet
    #Discard revealed cards except the last one
    DiscardDeck+=Table[0:cn]
    del Table[0:cn]
    #End the turn
    print("One turn behind us. I'm looking forward to the next, but if you want to leave, press Ctrl+C.")
print("Goodbye,looser")
