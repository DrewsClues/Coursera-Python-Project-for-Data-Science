n = int(input("Input Number:"))
i = 2
while i < n:
    if n%i ==0:
        print("This is not a prime number")
        break
    i+= 1   
else:
    print("This is a prime number")
