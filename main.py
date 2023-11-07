import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
should_continue= True
start=input("Do you want to start blackjack? 'y' or 'n': ")
if start=='y':
        # for i in cards:
         while should_continue:
            your_card1=random.choice(cards)
            your_card2=random.choice(cards)
            print(f"YOUR CARDS ARE {your_card1} and {your_card2}\n")
            
            com_card1=random.choice(cards)
            com_card2=random.choice(cards)
            print(f"COMPUTER'S CARDS ARE {com_card1} and ??\n")
            
            your_result=your_card1+your_card2
            com_result=com_card1+com_card2
            hit=input("Do you want to hit? 'y' or 'n': ")
            if hit=='y':
                    your_card3=random.choice(cards)
                    print(f"\nYOUR CARDS ARE NOW {your_card1}, {your_card2}, {your_card3}\n")
                    your_result=your_card1+your_card2+your_card3
                    if your_result>21:
                        if your_card1==11:
                              your_card1=1
                              break
                        elif your_card2==11:
                              your_card2=1
                              break
                        elif your_card3==11:
                              your_card3=1
                              break                          
                        else:
                          continue

                    your_result=your_card1+your_card2+your_card3
                    print(f"YOUR RESULT IS {your_result}\n")
                    
                    if your_result>21:
                           print("BUSTED! GAME OVER! COMPUTER WINS!\n")
                           break
                           should_continue=False
                    if your_result==com_result:
                          print("PUSH! GAME OVER! IT'S A TIE!\n")
                          break
                          should_continue=False
                    if your_result>com_result:
                          print(f"CONGRATULATIONS YOU WON THE GAME AS YOUR CARDS WERE {your_card1},{your_card2} AND {your_card3} AND YOUR TOTAL WAS {your_result}\n WHEREAS THE COMPUTER HAD {com_card1} AND {com_card2} AS THEIR CARDS AND THEIR RESULT WAS {com_result} \n")
                          break
                          should_continue=False
                    else:
                          print(f"COMPUTER HAS WON THE GAME AS THEY HAD {com_card1} AND {com_card2} CARDS AND THEIR TOTAL WAS {com_result}\n WHILE YOURS WERE {your_result} AND YOUR CARDS WERE {your_card1}, {your_card2} AND {your_card3}\n")
                          should_continue= False
            if hit=='n':
                  print(f"\nFINAL SCORES:\n YOU: {your_result}\n COMPUTER: {com_result}")
                  print(f"YOUR CARDS: {your_card1},{your_card2}\n COMPUTER'S CARDS: {com_card1}, {com_card2}\n")
                  if your_result>21:
                        print("\nBUSTED! GAME OVER! COMPUTER WINS!\n")
                        should_continue=False
                  elif your_result>com_result:
                        print("\nCONGRATULATIONS, YOU HAVE WON THE GAME!\n")
                        should_continue=False
                  else:
                    print("\nGAME OVER, COMPUTER WINS!\n")
                    should_continue=False
if start=='n':
      print(f"\n"*100, "Goodbye! Thanks for playing.")
      