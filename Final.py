from math import *
#import matplotlib
#matplotlib.use("Agg")
#import matplotlib.pyplot as plt
#------------------------------------------------------------------------------------------------------
def CompoundInterest():
    keepGoing = True
    while keepGoing == True:
        try:
            principle = float(input("How much initial money? "))
            if principle <= 0:
                print("Enter a positive, non-zero number.")
                continue
        except:
            print("Please, enter a number. Omit any '$,%,#'")
        else:
            break
    while keepGoing == True:
        try:
            rate = float(input("What is the interest rate? (Percentage) "))
            if rate <= 0:
                print("Enter a positive, non-zero number.")
                continue
        except:
            print("Please, enter a number. Omit any '$,%,#'")
        else:
            rate = rate/100
            break
    while keepGoing == True:
        try:
            time = float(input("How long are you investing/borrowing? (Years) "))
            if time <= 0:
                print("Enter a positive, non-zero number.")
                continue
        except:
            print("Please, enter a number. Omit any '$,%,#'")
        else:
            break
    while keepGoing == True:
        try:
            numberOfCompounds = int(input("How many times is it compounded? (Per Year) "))
            if numberOfCompounds <= 0:
                print("Enter a positive, non-zero number.")
                continue
        except:
            print("Please, enter a number. Omit any '$,%,#'")
        else:
            break
    CompoundedInterest = round((principle * (1+(rate/numberOfCompounds))**(numberOfCompounds * time)),2)
    print("This is how much your $" + str(principle) + " would be worth in " + str(time) + " years at a rate of " +
    str(rate*100) + "% compounded " + str(numberOfCompounds) + " time(s) per year: $" + str(CompoundedInterest))
#------------------------------------------------------------------------------------------------------
def CreditCard():
    keepGoing = True
    while keepGoing == True:
        try:
            balance = float(input("What is your current credit card balance? "))
            if balance <= 0:
                print("Enter a positive, non-zero number.")
                continue
        except:
            print("Please, enter a number. Omit any '$,%,#'")
        else:
            break
    while keepGoing == True:
        try:
            monthlyPayment = float(input("What is your minimum monthly payment? "))
            if monthlyPayment <= 0:
                print("Enter a positive, non-zero number.")
                continue
        except:
            print("Please, enter a number. Omit any '$,%,#'")
        else:
            break
    while keepGoing == True:
        try:
            dailyInterest = float(input("What is your APR? (Percentage) "))
            if dailyInterest <= 0:
                print("Enter a positive, non-zero number.")
                continue
        except:
            print("Please, enter a number. Omit any '$,%,#'")
        else:
            dailyInterest = dailyInterest/36500
            break
    while keepGoing == True:
        try:
            log(1+(balance/monthlyPayment)*(1-(1+dailyInterest)**30))/(-30 *(log(1+dailyInterest)))
        except:
            print("Your monthly payment is less than your monthly interest! Please try again and enter correct numbers.")
            print()
            return
        else:
            break
    timeToPay = log(1+(balance/monthlyPayment)*(1-(1+dailyInterest)**30))/(-30 *(log(1+dailyInterest)))
    print("It will take {} months to pay off ${} with a daily interest rate of {}% with monthly payments of ${}".format(round(timeToPay),balance,round(dailyInterest*100,2),monthlyPayment))
    print()
#------------------------------------------------------------------------------------------------------
def MonthlyPayment():
    keepGoing = True
    while keepGoing == True:
        try:
            principle = float(input("How much initial money? "))
            if principle <= 0:
                print("Enter a positive, non-zero number.")
                continue
        except:
            print("Please, enter a number. Omit any '$,%,#'")
        else:
            break
    while keepGoing == True:
        try:
            rate = float(input("What is the interest rate? (Percentage) "))
            if rate <= 0:
                print("Enter a positive, non-zero number.")
                continue
        except:
            print("Please, enter a number. Omit any '$,%,#'")
        else:
            rate = rate/1200
            break
    while keepGoing == True:
        try:
            time = float(input("How long are you investing/borrowing? (Months) "))
            if time <= 0:
                print("Enter a positive, non-zero number.")
                continue
        except:
            print("Please, enter a number. Omit any '$,%,#'")
        else:
            break
    MonthlyPayment = round((principle * ((rate)/(1-((1+rate)**(-time))))),2)
    print("Your monthly payment on $" + str(principle) + " for " + str(time) +
    " months at an interest rate of " + str(rate*1200) + "% is: $" + str(MonthlyPayment) +
    "\nThat means you will pay $" + str(round((MonthlyPayment * time)-principle,2)) + " in interest")
#------------------------------------------------------------------------------------------------------
def SalesTax():
    keepGoing = True
    while keepGoing == True:
        try:
            price = float(input("How much is the item? "))
            if price <= 0:
                print("Enter a positive, non-zero number.")
                continue
        except:
            print("Please, enter a number. Omit any '$,%,#'")
        else:
            break
    tax = price * .07
    newPrice = tax + price
    print("With tax being at 7%, the total price of your item is: $" + str(round(newPrice,2)))
#------------------------------------------------------------------------------------------------------
def DoubleTime():
    keepGoing = True
    while keepGoing == True:
        try:
            principle = float(input("How much are you investing/borriwng? "))
            if principle <= 0:
                print("Enter a positive, non-zero number.")
                continue
        except:
            print("Please, enter a number. Omit any '$,%,#'")
        else:
            break
    while keepGoing == True:
        try:
            rate = float(input("What is the interest rate? (Percentage) "))
            if rate <= 0:
                print("Enter a positive, non-zero number.")
                continue
        except:
            print("Please, enter a number. Omit any '$,%,#'")
        else:
            rate = rate/100
            break
    yearsToDouble = int(log(2)/(log(1+rate)))
    print("It would take " + str(yearsToDouble)+ " years to double $"+ str(principle) +
    " at a rate of " + str(rate*100) + "%")
#------------------------------------------------------------------------------------------------------
def ShowHelp():

    print("""
    This is a program that can calculate many real world
    things for you, such as Compound Interest and Monthly Payments; it can
    even help you make a Budget Sheet!

    Compound Interest: Interest that is calculated on the combined total
    of the original sum borrowed principal and the interest it has already accrued.

    Monthly Credit Card Disbursement: How many months it will take to pay off a credit
    card balance with a specific APR and Monthly Payment.

    Monthly Payment: How much you will have to pay per month on an amount of money
    with a specific interest rate over a specific amount of time.

    Sales Tax: Shows how much an item is after the standard Indiana sales tax.

    Double Time: Shows how long it will take to double your initial value in years.

    Budget Sheet: This shows you your spending based off your monthly income and includes
    Categories such as Home, Food, Car and so on, with subcategories such as Home: Insurance,
    Rent or Car: Gas, Insurance. You can decide what to put in, it does not have to be Home Or Food,
    it can be things such as personal. It then will ask how much you spend on those per month, and
    then have a total per category and a grand total to show you how much you can spend or if you have
    to cut some expenses.
    Example Questions:
    How much is your monthly income? 2000
    What is a monthly expense?(Enter one at a time) Home
    What is a monthly expense?(Enter one at a time) Personal
    What is a monthly expense?(Enter one at a time) Next
    What specifically is/are the expense(s) for Home (Enter one at a time) Rent
    What specifically is/are the expense(s) for Home (Enter one at a time) Insurance
    What specifically is/are the expense(s) for Personal (Enter one at a time) Netflix
    How much do you spend on Rent a month? 500
    How much do you spend on Insurance a month? 135
    How much do you spend on Netlfix a month? 15

    Written Check Example: This shows you a diagram of a check and how to fill it out.

    Have fun calculating, See ya on the other side!
    """)
    input("Hit the 'enter' key to continue")
#------------------------------------------------------------------------------------------------------
def menu():
    print("""Please choose the number in front of the selection
Type '6' if you are not sure what the selection means""")
    print("1.) Compound Interest")
    print("2.) Monthly Credit Card Disbursement")
    print("3.) Monthly Payment")
    print("4.) Sales tax...For indiana")
    print("5.) Double Time")
    print("6.) Help")
    print("7.) Create Budget Sheet")
    print("8.) Written Check Example")
    print("9.) Quit")
    response = input("What would you like to calculate? ")
    return response
#------------------------------------------------------------------------------------------------------
def CreateBudget():
    budgetName = input("What would you like to name your budget? ")

    file = open(budgetName + ".txt","w")
    Expenses = []
    keepGoing = True
    while keepGoing == True:
        try:
            monthlyIncome = float(input("How much is your monthly income? "))
            if monthlyIncome <= 0:
                print("Enter a positive, non-zero number.")
                continue
        except:
            print("Please, enter a number. Omit any '$,%,#'")
        else:
            file.write("Monthly Income: ${}\n".format(monthlyIncome))
            break

    print("An example of a monthly expense is 'Home' or 'Food'")
    while keepGoing == True:
        eachExpense = input("What is a monthly expense?(Enter one at a time) ")
        print("Type 'next' if you are done typing your expenses.")
        if eachExpense.upper() == "NEXT":
            break
        else:
            Expenses.append(eachExpense)

    print("An example of a specific expense is 'Rent' or 'Insurance'.")
    counter = 0
    subcategories = [[] for i in range(len(Expenses))]
    while keepGoing == True:
        for expense in Expenses:
            index = Expenses.index(expense)
            while keepGoing == True:
                specificExpense = input("What specifically is/are the expense(s) for {} (Enter one at a time) ".format(expense))
                print("Type 'next' when you want to move to your next category")
                if specificExpense.upper() == "NEXT":
                    counter += 1
                    if counter == len(Expenses):
                        break
                    break
                else:
                    subcategories[index].append(specificExpense)
            if  counter == len(Expenses):
                break
        if  counter == len(Expenses):
            break

    ExpenseCounter = -1
    MoneySpent=[]
    for subcat in subcategories:
        ExpenseCounter += 1
        for i in range(0,len(subcat)):
            while keepGoing == True:
                try:
                    averageSpent = float(input("How much do you spend on {} a month?({}) ".format(subcat[i],Expenses[ExpenseCounter])))
                    if averageSpent <= 0:
                        print("Enter a positive, non-zero number.")
                        continue
                except:
                    print("Please, enter a number. Omit any '$,%,#'")
                else:
                    MoneySpent.append(averageSpent)
                    break
    decider = 0
    totalList = []
    entireTotal = 0
    for monthlyExpense in Expenses:
        index = Expenses.index(monthlyExpense)
        file.write("\n")
        file.write("{}:\n".format(monthlyExpense))
        totalPerExpense = 0
        for i in range(0,len(subcategories[index])):
            file.write("{}: ${}\n".format(subcategories[index][i],MoneySpent[decider]))
            totalPerExpense = totalPerExpense + MoneySpent[decider]
            decider += 1
        totalList.append(totalPerExpense)
        file.write("Total: ${}\n".format(totalList[index]))
        entireTotal = totalList[index] + entireTotal
    file.write("\nComplete Total: ${}\n".format(entireTotal))
    leftOverMoney = monthlyIncome-entireTotal
    file.write("\nMoney Left Over: ${}\n".format(leftOverMoney))
    if leftOverMoney > 0:
        file.write("Try putting that left over money in a Savings account or investing!\n")
    elif leftOverMoney < 0:
        file.write("You have spent too much! Try cutting some expenses in places you do not need them in!\n")
    else:
        file.write("Nice Job! You are perfectly Balanced!\n")
    file.close()
    print()
    print("Check the file: '{}.txt' for your budget!".format(budgetName))
    print("If you would rather see a visual, find 'Budget.png'")
    print()

    Expenses.append('Left Over Money')
    pieChartSizeList = []
    for number in totalList:
        pieChartSizeList.append(round(((number/monthlyIncome)*100),2))
    pieChartSizeList.append(round(((leftOverMoney/monthlyIncome)*100),2))
    #figure1, ax1 = plt.subplots()
    if pieChartSizeList[len(pieChartSizeList)-1] < 0:
        sizes = [100]
        labels = ['']
        #ax1.set_title('You have spent too much money!\n Try cutting your expenses.')
    else:
        sizes = pieChartSizeList
        labels = Expenses
        #ax1.set_title(budgetName)
    #ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
    #ax1.axis('equal')
    #plt.savefig("Budget.png")
#------------------------------------------------------------------------------------------------------
def howToCheck():
    print("""
_____________________________________________________
| John Doe                                (11) 0001 |
| 123 Main St (1)                                   |
| Anywhere US 10111               Date_(6)_____     |
|                                                   |
| Pay to the (2)                         |-(3)--|   |
|   order of__________________________   |______|   |
|                                                   |
|   (4)________________________________ Dollars     |
|   Your Bank(8)                                    |
|                                                   |
|  MEMO____(5)________       ___(7)______________   |
|                                                   |
|(9)|:123456789:|(10)1001001234||'001(11)           |
|___________________________________________________|
""")
    print("The numbers in parenthesis are the labels of each part of a check.")
    print(
"""
1.) This has your personal information on it, things such as your name and address.
2.) This is your payee line, in other words, who you are writing the check to.
3.) This is the dollar box, you write how much money (in USD) your are giving, in actual numbers.
4.) This is the amount line, write the dollar amount in words. (20 = twenty)
5.) This is the memo line, this does not have to filled out, but is used to tell what the check is for.
6.) This is the date line, you write the date you filled this check out.
7.) This is the signature line, you sign your name on this line.
8.) This is where your banks contact info is, and the address of the bank.
9.) This is your routing number.
10.) This is your account number.
11.) This is the check number, every check has a different number.
""")
    input("Hit the 'enter' key to continue")

#------------------------------------------------------------------------------------------------------
def main():
    keepGoing = True
    while keepGoing == True:
        toDo = menu()
        if toDo.upper() == "1":
            CompoundInterest()
        elif toDo.upper() == "2":
            CreditCard()
        elif toDo.upper() == "3":
            MonthlyPayment()
        elif toDo.upper() == "4":
            SalesTax()
        elif toDo.upper() == "5":
            DoubleTime()
        elif toDo.upper() == "6":
            ShowHelp()
        elif toDo.upper() == "7":
            CreateBudget()
        elif toDo.upper() =="8":
            howToCheck()
        elif toDo.upper() == "9":
            keepGoing = False
            print("Have a nice day! \nI hope I could help!")
        else:
            print("""
        Enter a valid response
        Or type '6' if you do not understand
        """)
if __name__ == "__main__":
    main()