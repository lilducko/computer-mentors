
  #lstname

#card1 = int(input("What is the first card?"))
#card2 = int(input("What is the second card?"))
#dealer_card = int(input("What is the dealer card?"))

#total = card1 + card2

#if total == 21:
 #   print("Blackjack")
#elif total >= 17:
 #       print("Standard")
#elif total >= 12:
    #    if dealer_card > 6:
   #         print("Hit")
  #      else:
 #           print("Stand")
#elif total > 9 or (total == 0 and dealer_card <= 6):
#    print("Double then hit")
#else:
#    print("hit")
#divisor = 2
#for 1 in range(0,10,2):
 #   print(i/divisor)
player1 = input("Player1? ")
player2 = input("Player2? ")

if player1 == "rock" and player2 == "rock":
    print("tie")
 if player1 == "rock" and player2 == "paper":
    print("Player2 wins")
if player1 == "rock" and player2 == "scissors":
    print("player1 winns")
if player1 == "paper" and player2 == "rock":
    print("player1 wins")
if player1 == "paper" and player2 == "scissors":
    print("player 2 wins")
if player1 == "paper" and player2 == "paper":
    print("tie")
if player1 == "scissors" and player2 == "rock":
    print("player2 wins")
if player1 == "scissors" and player2 == "paper":
    print("player1 wins")
    if player1 == "scissors" and player2 == "scissors":
    print("tie")


