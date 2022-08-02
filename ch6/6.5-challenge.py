"""
In this challenge, you will write a program called invest.py that tracks the growing amount 
of an investment over time. An initial deposit, called the principal amount, is made. 
Each year, the amount increases by a fixed percentage, called the annual rate of return.

For example, a principal amount of $100 with an annual rate of return of 5% increases the first year by $5. 
The second year, the increase is 5% of the new amount $105, which is $5.25. Write a function called invest with three parameters: 
the principal amount, the annual rate of return, and the number of years to calcu- late. The function signature might look something like this:
"""

def invest(amount: int, rate: float, years: int):
  for i in range(1, years + 1):
    interest =  amount * rate
    amount += interest

    print(f"Year {i}: ${amount:.2f}")


# invest(100, 0.05, 5)
amount = int(input("Enter the amount: "))
rate = (float(input("Enter rate: ")) / 100)
years = int(input("Enter years: "))

invest(amount, rate, years)