def main():
    first_prompt = "What you gotta say? :"
    next_prampt = "I got that! Anything else? :"

    user_input = input(first_prompt)

    while user_input != "STOP" :
        user_input = input(next_prampt)

        if __name__ == "__main__":
            main()