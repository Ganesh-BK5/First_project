import random
l = ["Rock", "Scissors", "Paper"]
while True:
    user_choice = int(input('''
1 for Start
2 for Exit

    '''))
    if user_choice == 1:
        uinput = int(input('''
  1 for Rock
  2 for Scissors
  3 for paper      
        '''))
        if uinput == 1:
            uchoice = "Rock"
        elif uinput == 2:
            uchoice = "Scissors"
        elif uinput == 3:
            uchoice = "Paper"
        Cchoice = random.choice(l)
        if(uchoice == Cchoice):
            print("Game Draw")
        elif(uchoice == "Paper" and Cchoice == "Rock") or (uchoice == "Rock" and Cchoice == "Scissors") or (uchoice == "Scissors" and Cchoice == "Paper"):
            print("Your choice ", uchoice)
            print("Computer Choice ", Cchoice)
            print("You win")
        else:
            print("Your choice ", uchoice)
            print("Computer Choice ", Cchoice)
            print("Computer Win")
    else:
        break
