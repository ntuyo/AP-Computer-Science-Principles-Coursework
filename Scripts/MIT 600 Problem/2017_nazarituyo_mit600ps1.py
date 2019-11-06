current_balance = input("Please enter your current balance:")

current_interest_rate = input("Please enter your annual interest rate:")

minimum_monthly_payment_rate = input("Please enter your minimum monthly payment rate:")


total_principal_paid = 0
total_interest_paid = 0
for month in range(1, 13):

    minimum_monthly_payment = float(minimum_monthly_payment_rate)/100.0 * float(current_balance)

    interest_paid = float(current_interest_rate)/100.0/12 * float(current_balance)

    principal_paid = float(minimum_monthly_payment) - float(interest_paid)

    remaining_balance = float(current_balance) - float(principal_paid)

    rounded_balance = round(remaining_balance, 2)

    print("Your remaining balance is for month " + str(month) + " is: ", rounded_balance,

          ', and your Principal Paid is:', round(principal_paid, 2))
    total_principal_paid = principal_paid + total_principal_paid
    total_interest_paid = interest_paid + total_interest_paid
    current_balance = rounded_balance
total_amount_paid = total_principal_paid + total_interest_paid
print("Your total amount paid is:", round(total_amount_paid, 2))


