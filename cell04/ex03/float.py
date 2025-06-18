def main():
    user_input = input("Give me a number:")
    try:
        number = float(user_input)
        if number.is_integer():
            print("This number is an intagar.")
        else:
            print("This number is a decimal.")  
    except ValueError:
            print("Invalid input.")    

if __name__ == "__main__":
     main()            
