num = int(input("Enter a number less ther 25\n"))
if num > 25:
    print("Error")
else:
    while num <= 25:
        print(f"Inside the loop, my variab is {num}")    
        num +=1