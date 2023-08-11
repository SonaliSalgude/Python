evodTuple = (11, 34, 17, 44, 66, 19, 89, 64, 90)
print("Even and Odd Tuple Items = ", evodTuple)

tEvenCount = tOddCount = 0
for oetup in evodTuple:
    if(oetup % 2 == 0):
        tEvenCount = tEvenCount + 1
    else:
        tOddCount = tOddCount + 1

print("The Count of Even Numbers in evodTuple = ", tEvenCount)
print("The Count of Odd  Numbers in evodTuple = ", tOddCount)