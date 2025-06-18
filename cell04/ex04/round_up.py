import math

def main():
    user_input = input("Give me a number: ")
    try:
        number = float(user_input)
        rounded = math.ceil(number)
        print(rounded)
    except ValueError:
        print("Invalid input.")    

if __name__ == "__main__":
    main()       