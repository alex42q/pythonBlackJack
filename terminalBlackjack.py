import random
from time import sleep
import numpy as np

class Game:
    def __init__ (self):
        self.cards = [10,2,3,4,5,6,7,8,9,10,10,10,10]
        self.DEALER = []
        self.PLAYER = []
        self.gameStart = False
        self.playerTurn = False
        self.dealerTurn = False
        self.arrayDealer = np.array(self.DEALER)
        self.arrayPlayer = np.array(self.PLAYER)
        self.checkIfTrue = False

    def startGame(self):
        val = input("Are you ready to start the game? ")
        if val == 'y':
            self.gameStart = True
            self.PLAYER.append(random.choice(self.cards))
            self.playerTurn = True
            print(f"PLAYER has {self.arrayPlayer}")

    def checkIfDontWantOtherCard(self):
        q = input("Thes na trabikseis k allo fullo?")
        if q == 'y':
            return True
        else:
            self.playerTurn = False
            return False


    def checkSum(self):
        if sum(self.PLAYER) > 21 and sum(self.DEALER) < 21:
            print("Dealer loose")
            self.gameStart = False
        if sum(self.PLAYER) > 21 and sum(self.DEALER) < 21:
            print("Player loose")
            self.gameStart = False
        if sum(self.DEALER)== 21:
            print("Dealer win")
            self.gameStart = False
        if sum(self.PLAYER) == 21:
            print("Player win")
            self.gameStart = False
        if sum(self.PLAYER) < sum(self.DEALER):
            print("Dealer win")
            self.gameStart = False
        if sum(self.DEALER) < sum(self.PLAYER):
            print("Player win")
            self.gameStart = False
        if sum(self.DEALER) == sum(self.PLAYER):
            print("Dealer win")
            self.gameStart = False

    def PlayerTurn(self):
        print(f"PLAYER has {sum(self.PLAYER)}")
        while self.playerTurn:
            self.PLAYER.append(random.choice(self.cards))
            print(f"PLAYER has {sum(self.PLAYER)}")
            print(sum(self.PLAYER))
            if sum(self.PLAYER) > 21:
                print("Player loose")
                self.gameStart = False
                break
            elif sum(self.PLAYER) == 21:
                print("Dealer loose")
                self.gameStart = False
                break
            if self.checkIfDontWantOtherCard() == False:
                self.dealerTurn = True

    def DealerTurn(self):
        print("Dealers turn")
        print(sum(self.DEALER))
        while self.dealerTurn:
            self.DEALER.append(random.choice(self.cards))
            print(f"DEALER has {sum(self.DEALER)}")
            sleep(1)
            if sum(self.DEALER) == 17:
                self.dealerTurn = False
                self.checkSum()
                break
            elif sum(self.DEALER) == 18:
                self.dealerTurn = False
                self.checkSum()
                break
            elif sum(self.DEALER) == 19:
                self.dealerTurn = False
                self.checkSum()
                break
            elif sum(self.DEALER) == 20:
                self.dealerTurn = False
                self.checkSum()
                break
            elif sum(self.DEALER) > 21:
                self.gameStart = False
                print("Player Wins")
                break
            elif sum(self.DEALER) == 21:
                self.gameStart = False
                print("Dealer Wins")
                break

    def shuffle(self):
        self.DEALER.append(random.choice(self.cards))
        self.PLAYER.append(random.choice(self.cards))
        print(f"DEALER has {self.DEALER}")
        print(f"PLAYER has {self.PLAYER}")

    def initialize(self):
        self.startGame()
        while self.gameStart:
            self.PlayerTurn()
            self.DealerTurn()
        print(f"Final score is \n Dealer: {sum(self.DEALER)} \n Player: {sum(self.PLAYER)}")

t = Game()
t.initialize()


