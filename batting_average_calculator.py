#!/usr/bin/env python3

print("===============================================================")
print("                   Baseball Team Manager")
print("MENU OPTIONS")
print("1 - Calculate batting average")
print("2 - Exit program")
print("===============================================================")

while True:
    option = int(input("Menu option: "))
    if option == 1:
        print("Calculate batting average...")
        at_bats = int(input("Official number of at bats: "))
        hits = int(input("Number of hits: "))
        batting_average = round(hits / at_bats, 3)
        print(f"Batting average: {batting_average}")
        print()
    elif option == 2:
        print("Bye!")
        break;
    else:
        print("Not a valid option. Please try again.")
        print()
