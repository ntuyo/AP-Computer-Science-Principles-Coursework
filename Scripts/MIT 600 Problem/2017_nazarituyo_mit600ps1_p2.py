outstanding_balance = input("What is the outstanding balance?")
annual_interest_rate = input("What is your annual interest rate? Please input it as a decimal.")

monthly_interest_rate = float(annual_interest_rate)/12.0
original_amount = float(outstanding_balance)*(1 + float(monthly_interest_rate))
payment = float(monthly_interest_rate) * float(outstanding_balance)

minimum_payment = 0
keep_running = True
updated_balance = 0
while keep_running is True:
    minimum_payment += 10
    updated_balance = original_amount
    for month in range(1, 13):
        updated_balance -= minimum_payment
        print('Your updated balance for the', str(month), 'month is:', updated_balance)
        if updated_balance < 0:
            keep_running = False
            print(month - 1)
            break
    if updated_balance > 0:
        print('Your monthly payment of', minimum_payment,  'does not work')


print(minimum_payment)
print(updated_balance)
