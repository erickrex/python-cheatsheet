#Get info about the loan
money_owed = float(input("So how much do you owe?\n")) # a 50k loan gets paid in 54 months with a 3% apr and 1k payments
annual_percentage_rate = float(input("What is the annual percentage rate? \n"))
payment = float(input("How much can you pay monthly?"))
forecast_payments = int(input("How many months do you want to forecast?"))

#Divided by 100 to make it a percent, then divided by 12 to make it monthly
monthly_rate = annual_percentage_rate/100/12

for i in range(forecast_payments):
    #Added interest
    interest_paid_monthly = money_owed * monthly_rate
    money_owed = money_owed + interest_paid_monthly

    if (money_owed - payment < 0):
        print('That is enough, please pay the remaining', money_owed)
        break

    #Payments made are subtracted from the total
    money_owed = money_owed - payment

    #print the results after this month
    print('Paid', payment, 'of which', interest_paid_monthly, 'was interest', end=' ')
    print('Now I owe', money_owed)
