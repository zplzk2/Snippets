##############################
# Solve the Fuel Injection Perfection problem.
# You know where it comes from.
##############################

def Cal(num):
    b = num
    print("Input:", bin(b), b)
    counter = 0
    while b > 3:
        counter += 1
        if b % 2 == 0:
            b = b >> 1
            print("#", counter, bin(b), b)
        else:
            c = b
            #print(bin(c))
            len1 = 0
            while c % 2 == 1:
                c = c >> 1
                len1 += 1
            #print(len1)
            if len1 > 1:
                b += 1
            else:
                b -= 1
            print("#", counter, bin(b), b)
    counter += (b - 1)
    print("Extra:", (b - 1))
    print("Result:", num, bin(num), counter)
    print("---------------")
    return counter

#for i in range (1, 2 ** 11):
#    Cal(i)

Cal(1)
Cal(2)
Cal(3)
Cal(4)

Cal(2**4)
Cal(2**4 - 1)
Cal(2**4 - 2)
Cal(2**4 - 3)

Cal(0b11000011)

Cal(0b11000011111)
Cal(0b11000001111)

Cal(0b11000101111)

#Cal(2**10 + 1)
#Cal(2**300 + 1)
#Cal(2**300)
#Cal(2**300 - 1)
#Cal(2**300 - 2)
#Cal(2**300 - 3)

#Cal(2**309)
#Cal(2**309 + 2 ** 5 - 1)
