def collatz(number):

        if number % 2 == 0:
            return number // 2
        else:
            return 3 * number + 1

print("Please enter any integer number of your choice.")

while True:
    try:
        break_number = collatz(int(input()))
        print(break_number)
        if break_number == 1:
            break
    except ValueError:
        print("That's not a valid integer. Please try again.")
