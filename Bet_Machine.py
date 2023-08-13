import  random

print("Welcome To Slot Machine $")
name=input("Enter Your Name PLease:")
deposit=int(input("what would you like to deposit?:"))
winingAmount=0
while(True):
    if(deposit<0):
        print("Sorry you dont have enough money to play :(")
        break
    condition = input("Are you sure to play (yes/no):")
    if (condition.lower() == "no"):
        break
    bet_Line=int(input("Enter the number of line to bet on ? [1,2,3]:"))
    bet_Amount=int(input("Enter the amount:"))
    print(f"Deposit amount is:{deposit-bet_Amount}")

    if(bet_Amount>deposit):
        print("your enter amount that is greater than your current balance so please enter correct amount")
        continue
    print(f"You are betting line number {bet_Line} the betting amount is{bet_Amount*3}")

    col1 = ['A', 'B', 'C']
    col2 = ['A', 'B', 'C']
    col3 = ['A', "B", 'C']

    line1_1 = random.choice(col1)
    line1_2 = random.choice(col1)
    line1_3 = random.choice(col1)

    line2_1 = random.choice(col2)
    line2_2 = random.choice(col2)
    line2_3 = random.choice(col2)

    line3_1 = random.choice(col3)
    line3_2 = random.choice(col3)
    line3_3 = random.choice(col3)

    print(f"{line1_1} | {line2_1} | {line3_1}")
    print(f"{line1_2} | {line2_2} | {line3_2}")
    print(f"{line1_3} | {line2_3} | {line3_3}")

    if(bet_Line==1):
        if(line1_1==line2_1 and line1_1==line3_1):
            winingAmount+=bet_Amount*3
            deposit = deposit - bet_Amount
            deposit=deposit+winingAmount
            print(f"You won{bet_Amount*3}$")
        else:
            print(f"You lose {bet_Amount*3} hard luck :)")
            deposit=deposit-bet_Amount*3
    elif(bet_Line==2):
        if (line1_2 == line2_2 and line1_2 == line3_2):
            winingAmount += bet_Amount * 3
            deposit=deposit-bet_Amount
            deposit = deposit + winingAmount
            print(f"You won{bet_Amount * 3}$")
        else:
            print(f"You lose {bet_Amount * 3} hard luck :)")
            deposit = deposit - bet_Amount * 3
    elif(bet_Line==3):
        if (line1_3 == line2_3 and line1_3 == line3_3):
            winingAmount += bet_Amount * 3
            deposit = deposit - bet_Amount
            deposit = deposit + winingAmount
            print(f"You won{bet_Amount * 3}$")
        else:
            print(f"You lose {bet_Amount * 3} hard luck :)")
            deposit = deposit - bet_Amount * 3
    else:
        print("Invalid line number")


    print(f"Current balance is : {deposit}")


if(deposit<0):
    print(f"you have to pay {deposit}  amount  to cousino ")
else:
    print(f"{name} Your wining amount is : {deposit}")












