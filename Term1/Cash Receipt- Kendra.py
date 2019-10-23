#Cash Register - Kendra Davis

#names of variables 
numItems = 17
costPerItem = 13.00
subTotal = numItems * costPerItem
taxRate = 0.09
taxAmount = subTotal *  taxRate
totalAmount = subTotal + taxAmount

#receipt print
print("SALES RECEIPT")
print("Number of items       : " + str(numItems))
print("Cost of item             : " + str(costPerItem))
print("Tax Rate                  : " + str(taxRate))
print("Tax Amount              : " + str(taxAmount))
print("TOTAL SALE PRICE : " + str(totalAmount))
