from suitsRank import Suit, Rank
from card import Card
from operator import attrgetter

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def getCard(self, card):
        try:
            self.hand.remove(card)
            return card
        except ValueError:
            print('No card found in Hand!')
            return None

    def addCard(self, card):
        self.hand.append(card)
    
    def getTrumps(self):
        suitList = [Suit.Clubs, Suit.Diamonds, Suit.Hearts, Suit.Spades]
        suitGroup = [0, 0, 0, 0]
        for card in self.hand:
            if (card.suit == suitList[0]): suitGroup[0] += 1
            elif (card.suit == suitList[1]): suitGroup[1] += 1   
            elif (card.suit == suitList[2]): suitGroup[2] += 1   
            else: suitGroup[3] += 1
        if max(suitGroup) == 1:
            return self.hand[self.getMax(self.hand)].suit
        elif max(suitGroup) == 2:
            return self.hand[self.getMax(self.hand)].suit
        else:
            return suitList[suitGroup.index(max(suitGroup))]

    def getMax(self, cardList = []):
        return self.hand.index(max(cardList, key=attrgetter('value')))

    def getMin(self, cardList = []):
        return self.hand.index(min(cardList, key=attrgetter('value')))

    def setCardEnable(self, tableCards = []):
        if not tableCards:
            for card in self.hand:
                card.enable = True
        else:
            playable = [card for card in self.hand if tableCards[0].card.suit == card.suit]
            if len(playable) > 0:
                for card in self.hand:
                    if card.suit == tableCards[0].card.suit:
                        card.enable = True
                    else:
                        card.enable = False
            else:
                for card in self.hand:
                    card.enable = True

    def setCardDiseble(self):
        for card in self.hand:
            card.enable = False

    def nonTrumpMin(self, trump):
        nonTrump = []
        myTrump = []
        for card in self.hand:
            if trump == card.suit:
                myTrump.append(card)
            else:
                nonTrump.append(card)
        if not nonTrump:
            return self.hand.index(myTrump[self.getMin(myTrump)])
        else:
            return self.hand.index(nonTrump[self.getMin(nonTrump)])
    
    def player(self, tableCards, trump):
        table = []
        for tCard in tableCards:
            table.append(tCard.card)
        cardToPlay = None
        if len(self.hand) > 1:
            if table:
                currentSuit = table[0].suit
                playableCard = []
                myTrump = []
                for card in self.hand:
                    if card.suit == trump:
                        myTrump.append(card)
                    if card.suit == currentSuit:
                        playableCard.append(card)
                tableMax = table[self.getMax(table)]
                if playableCard and len(playableCard) > 1:
                    if len(playableCard) == 2:
                        if table[0].value > playableCard[self.getMax(playableCard)].value:
                            cardToPlay = self.getCard(playableCard[self.getMin(playableCard)])
                        
                

