def main():
    i = 0
    while i <= 10:
        j = 0
        output = f="Table de {i}:"
        while j <= 10:
            output += f"{i * j}"
            j += 1
            print(output)
            i += 1

            if __name__== "__main__":
                main()