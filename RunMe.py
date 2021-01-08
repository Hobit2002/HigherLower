print("Welcome in Higher Lower Casiono. The higher will be your risk, the lower you'll win!")
#Prepare deck
Deck=[]
for Symbol in ['♠','♡','♢','♣']:
    for relValue,imageValue in enumerate(['2','3','4','5','6','7','8','9','10','J','Q','K','A']):
        Deck.append({'image':imageValue+Symbol,'value':relValue})
