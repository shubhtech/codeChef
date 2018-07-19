withdraw_amount= float(raw_input())
current_balance=float(raw_input())

if(withdraw_amount%5==0):
    if(current_balance>=withdraw_amount):
        remaining_balance=current_balance-withdraw_amount-.50
        print "{:.2f}".format(remaining_balance)