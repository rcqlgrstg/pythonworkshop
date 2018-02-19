money = input("How much is your money on hand?")
amount = input ("How much is the iPhone X?")

print ("You can avail",money/amount)
print (" iPhone X, and will have an extra" , money%amount," pesos")
print ("You'll need", amount-(money%amount)," pesos to avail another iPhone X.")
