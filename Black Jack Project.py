#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Welcome to the Noah's Black Jack Game

'''
Create a deck of 52 cards
Shuffle the deck
Ask the Player for their bet
Make sure that the Player's bet does not exceed their available chips

Deal two cards to the Dealer and two cards to the Player
Show only one of the Dealer's cards, the other remains hidden
Show both of the Player's cards
Ask the Player if they wish to Hit, and take another card
If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
Determine the winner and adjust the Player's chips accordingly
Ask the Player if they'd like to play again

'''
import random
import time
from IPython.display import clear_output

all_cards = []

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card():

    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return(self.rank + " of " + self.suit)

class Deck():
    
    def __init__(self):
    
        for suit in suits:
            for rank in ranks:  
                newcard = Card(suit,rank) 
                all_cards.append(newcard)
            
    def deal_one(self):
        
        return all_cards.pop(0)
    
    def shuffle(self):
        
        random.shuffle(all_cards)
        
class Bank():
    
    def __init__(self,balance):
        
        self.balance=balance
        self.bet_amount=0
        self.userBet = 0
    def bet(self,amount):
        
        while True:
            if amount > self.balance:
                print("\nInsufficent Funds!\n")
                print ("How much would you like to bet?\n")
                amount = user_input()
                
            else:
                self.userBet = amount
                self.balance = self.balance - amount
                self.bet_amount = amount
                break
                
    def win(self):
        
        self.balance = self.balance + (self.userBet*2)
        
    def draw(self):
        self.balance = self.balance + self.userBet
        
def user_input():
    
    while True:
        try:
            Balance = int(input())

        except :
            print("Whoops! Assure your input was an Integer! ")

        else:
            return Balance
        

class GameLogic():

    
    
    def __init__(self):
    
        newDeck = Deck()
        newDeck.shuffle()
        roundNumber=1
        playerCards=[]
        playerValue = 0
        computerCards=[]
        self.UsersCards=[]
        time.sleep(.75)
        
        choice = ''
        i=2
        r=2
        choices = ['Y','y','N','n']
        time.sleep(2)

        print(f"Welcome to Noah's Black Jack Game!\n")
        time.sleep(1)

        print("Lets start by creating you a Casino Bank Account!\n")

        print("How much would you like to deposit into casino account?" )
        
        balance = user_input()
        BankAccount=Bank(balance)

        print(f"\nYour casino balance is ${BankAccount.balance}! ")

        choice = ''
        i=2
        r=2
        choices = ['Y','y','N','n']
        time.sleep(2)





        time.sleep(.25)
        
        def printTable(self):
            
            print("Your Cards:                                    The dealers cards:")
            print("                                                                 ")
            playerCards.append(newDeck.deal_one())
            playerCards.append(newDeck.deal_one())

            computerCards.append(newDeck.deal_one())
            computerCards.append(newDeck.deal_one())

            print(f"{playerCards[0]} ({playerCards[0].value})                           {computerCards[0]} ({computerCards[0].value})")
            print(f"{playerCards[1]} ({playerCards[1].value})                           (The other card is Hidden)")
            
                      
        def printDashboard(self):
            
            print(f"\nCurrent Bet: ${BankAccount.bet_amount} | Current Round: Round {roundNumber} | Current Balance: ${BankAccount.balance}\n")
            
        def calculateUserTotal(self):
            total=0
            i=0
            
            for x in playerCards:
                total = total + playerCards[i].value
                i+=1
                
            return total
        
        def calculateComputerTotal(self):
            total=0
            i=0
            
            for x in computerCards:
                total = total + computerCards[i].value
                i+=1
            
            return total
        
    
        while BankAccount.balance != 0:
            
                BankAccount.bet_amount=0
                i=2
                r=2
                
                
                playerCards=[]
                playerValue = 0
                computerCards=[]
                newDeck.shuffle()
                choice =''
                clear_output()
                time.sleep(0.5)
                printDashboard(self)
                print ("How much would you like to bet?")
                bet = user_input()
                BankAccount.bet(bet)
                clear_output()

                printDashboard(self)
                print("--------------------------------------------------------------------------------")
                printTable(self)
                playerValue=calculateUserTotal(self)
                computerValue=calculateComputerTotal(self)
                gameOn= True


                while gameOn == True:


                    while choice != 'n' and playerValue < 21:


                        time.sleep(1)
                        choice = input(("Would you like to hit? Y/N\n"))

                        while choice not in choices:

                                print("Assure your choice was either Y or N")
                                choice = input(("Would you like to hit? Y/N\n"))

                        if choice == 'Y' or choice == 'y':
                            
                            playerCards.append(newDeck.deal_one())
                            
                            if playerCards[-1].rank == 'Ace' and playerValue > 10:
                                
                                print(f"{playerCards[-1]} (1)")
                                playerValue+=1
                                playerCards.pop(-1)
                                playerValue=calculateUserTotal(self)

                            else:

                                print(f"{playerCards[-1]} ({playerCards[-1].value})")

                                playerValue=calculateUserTotal(self)

                            print(playerValue)

                        elif choice == 'N' or choice == 'n':
                            choice = 'n'
                            break
                            playerValue=calculateUserTotal(self)

                    if playerValue >21:

                            print("You Busted! Dealer Wins!")
                            roundNumber+=1
                            gameOn==False

                            break        


                    while computerValue<=17:

                        print("\nDealer Decides to Hit.")
                        time.sleep(1)
                        computerValue=calculateComputerTotal(self)

                        computerCards.append(newDeck.deal_one())


                        if computerCards[-1].rank == 'Ace' and computerValue > 10:
                            computerValue+=1
                            print(f"Dealer gets the {computerCards[r]} ({computerCards[r].value})")
                            computerCards.pop()
                            computerValue=calculateComputerTotal(self)


                        else:

                            computerValue=calculateComputerTotal(self)
                            time.sleep(.5)
                            print(f"Dealer gets the {computerCards[r]} ({computerCards[r].value})")

                            r+=1

                        computerValue=calculateComputerTotal(self)

                    if computerValue > 21:
                        time.sleep(1)
                        print("Dealer Busts! You win!")
                        time.sleep(.5)
                        print (f"\nHis hidden card was the {computerCards[1]}")
                        gameOn==False
                        roundNumber+=1
                        BankAccount.win()
                        break

                    time.sleep(1)

                    print("\nDealer Decides to stay")


                    if computerValue>=17 and computerValue <= 21:

                        if 21 - computerValue > 21 - playerValue:
                            time.sleep(1)
                            print("\nYou Win!")

                            print (f"\nHis hidden card was the {computerCards[1]}")
                            BankAccount.win()
                            gameon=False
                            roundNumber+=1



                        if 21 - computerValue < 21 - playerValue:
                            time.sleep(1)
                            print(f"\nDealer Wins! {computerValue}") 
                            print (f"\nHis hidden card was the {computerCards[1]}")
                            gameon=False
                            roundNumber+=1
                            Bank

                        if 21 - computerValue == 21 - playerValue:
                            time.sleep(1)
                            print("The round was a draw!")
                            print (f"\nHis hidden card was the {computerCards[1]}")
                            BankAccount.draw()
                            gameon=False
                            roundNumber+=1
                        break
                
                if BankAccount.balance == 0:
                    time.sleep(2)
                    clear_output()
                    print("Your out of money!")
                    break

                else:
                    
                    playagain = input(("Would you like to play another round? Y/N\n"))

                    while choice not in choices:

                        print("Assure your choice was either Y or N")
                        choice = input(("Would you like to hit? Y/N\r"))

                    if playagain == 'Y' or playagain == 'y':

                        clear_output()
                        gameOn==True

                    else:
                        print("Game Over\n")

                        break
                    
        time.sleep(3)
        print("Thanks for Playing!")


def black_jack():
    #new Deck Created and then Shuffled:

    GameLogic()
    
    
black_jack()


#  
