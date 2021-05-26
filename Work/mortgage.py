principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
year = 0

while principal > 0:
    if year <= 12:
        principal = principal * (1+rate/12) - (payment + 1000)
        total_paid = total_paid + (payment + 1000)
        year += 1

    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

print('Total paid:', round(total_paid, 2))
