import os
import random
import pyperclip

if __name__ == '__main__':
    if os.path.exists("config.ini"):
        with open("config.ini", "r") as f:
            lines = f.readlines()
        lines = [line.strip().split() for line in lines]
        p_length = int(lines[0][-1])
        p_count = int(lines[1][-1])
    else:
        p_length = int(input("Choose amount of symbols of your password: "))
        p_count = int(input("Choose amount of passwords: "))
        with open("config.ini", "w") as f:
            f.writelines([f"length {p_length}\n", f"count {p_count}\n"])
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
    symbol_case = "!#@~$^.,-+%?*=<>_`"
    password_case = list()
    for num in range(p_count):
        password_case.append("")

        for p in range(0, p_length):
            choice = random.choice([1, 2, 3, 4])
            if choice == 1:
                password_case[-1] += lower_case[random.randint(0, len(lower_case)-1)]
            if choice == 2:
                password_case[-1] += upper_case[random.randint(0, len(upper_case)-1)]
            if choice == 3:
                password_case[-1] += symbol_case[random.randint(0, len(symbol_case)-1)]
            if choice == 4:
                password_case[-1] += str(random.randint(0, 9))

        print(num+1, password_case[-1])
    index = int(input("Choose number of your password: "))
    pyperclip.copy(password_case[index-1])
    print(pyperclip.paste())
    key = input(" \nEnter any key for exit...")



