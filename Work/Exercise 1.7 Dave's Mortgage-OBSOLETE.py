principal = 500000.0
monthsPerYear = 12
termInYears = 30
termInMonths = termInYears * monthsPerYear
rate = 0.05
prime = 1
interest = (prime + (rate/12))
payment = 2684.11
total_paid = 0.0
added_payment = payment + 1000.0


while termInMonths <= 12:
    principal = principal * interest 


#while principal > 0:
  #  principal = principal * (1 + rate / 12) - payment
  #  total_paid = total_paid + payment


print(interest)
print(principal)

print(500000 * (1+0.05/12) - 2684.11)
# principal = principal * (1 + rate / 12) - payment
# total_paid = total_paid + payment
    
    



    #total_paid = total_paid + payment
    #months = total_paid / payment
    #months_for_extra_payment = months - 12
    #total_paid = months_for_extra_payment


#print(total_paid)
#print(months)
# print(months_for_extra_payment)
# print(months)
# print('Total paid', total_paid)


