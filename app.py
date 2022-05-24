balance = int(input("What is the current balace left on your mortgage? "))
value = int(input("What is the current appraised value of your mortgage? "))
ltv = balance // value
print("You're current LTV is " + str(ltv) + " !")
