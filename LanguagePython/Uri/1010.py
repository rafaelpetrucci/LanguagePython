codeA, numberA, priceA = input().split()
codeB, numberB, priceB = input().split()

numberA = int(numberA)
numberB = int(numberB)
priceA = float(priceA)
priceB = float(priceB)

total = priceA * numberA + priceB * numberB
print("VALOR A PAGAR: R$ {:.2f}".format(total))
