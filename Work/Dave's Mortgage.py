# Dave's Mortgage.py

principal = 500000.0 # the total cost of the house now owed via mortgage
rate = 0.05 #the interest rate
payment = 2684.11 #the payment
total_paid = 0.0 #variable to hold the amount paid
month = 0 #variable to hold the month number

extra_payment = 1000.0 #the amount of the extra payment
extra_payment_start_month = 61 #the month to start applying an extra payment
extra_payment_end_month = 108 #the month to stop applying an extra payment

while principal > 0: #a loop to iterate through proceeding code on the condition that the principal variable's value does not equal 0 
    month = month + 1 #while principal is greater than 0 add months beginning at month 0 and add 1. iterate through until principal is 0
    principal = principal * (1+rate/12) - payment #total principal iterates as principal times mortgage rate - 1 payment made until reaching 0
    total_paid = total_paid + payment # the total amount paid for each iteration
    #print(month, principal, total_paid)

    if month >= extra_payment_start_month and month <= extra_payment_end_month: #if the month is between month 61 and 108 then execute following
       principal = principal - extra_payment #subtract the extra amount paid from principal
       total_paid = total_paid + extra_payment #add total amount paid to mortgage on top of payment

    if principal < payment and principal > 0: #if the principal is less than the payment and greater than 0
       
       lastPayment = principal #make the last payment = to principal
       principal = principal - lastPayment #make the new principal = to the last principal minus the last payment (remaining principal)
       total_paid = total_paid + lastPayment #total paid iterates again but now with the last payment (remaining principal) applied
  
    print(month, round(total_paid,2), round(principal, 2)) #iterates through all months and prints the month, the total paid and remaining principal
    
# print('Total paid', round(total_paid, 2))
# print('Months', month)
#310 880074.1 -1871.53