def squares_less_than_n(n):
    if n <1:
        print("Parameter value must be greater than 0")
    else:
        # Add your code here
        i = 1
        while i ** 2 <= n:
            print (i**2 , end=" ")
            i += 1
        print()



# Verify everything works as intended
value = 50
squares_less_than_n(value) # this should print 1 4 9 16 25 36 49