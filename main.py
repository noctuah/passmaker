import os
import random
import pyperclip


class Generator:
    def __init__(self):
        self.__lower_case = "abcdefghijklmnopqrstuvwxyz"
        self.__upper_case = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
        self.__symbol_case = "!#@~$^.,-+%?*=<>_`"

    def p_generate(self, length):
        out = ""
        for p in range(0, length):
            choice = random.choice([1, 2, 3, 4])
            if choice == 1:
                out += self.__lower_case[random.randint(0, len(self.__lower_case) - 1)]
            if choice == 2:
                out += self.__upper_case[random.randint(0, len(self.__upper_case) - 1)]
            if choice == 3:
                out += self.__symbol_case[random.randint(0, len(self.__symbol_case) - 1)]
            if choice == 4:
                out += str(random.randint(0, 9))
        return out

    def p_generates(self, count, length):
        password_case = list()
        for num in range(count):
            password_case.append("")
            password_case[num] = self.p_generate(length)
            print(num + 1, '-', password_case[num])
        return password_case

    @staticmethod
    def p_input(prompt="", limit=None):
        while True:
            param = input(prompt)
            if param.isdigit() and int(param) > 0:
                if limit is not None:
                    if int(param) <= limit:
                        param = int(param)
                        break
                    else:
                        print(f"Limitation: {param} > {limit}")
                        continue
                else:
                    param = int(param)
                    break
            print(f"Incorrect {param}")
        return param


if __name__ == '__main__':
    pGen = Generator()

    if os.path.exists("config.ini"):
        with open("config.ini", "r") as f:
            lines = f.readlines()
        lines = [line.strip().split() for line in lines]
        p_count_max = int(lines[0][-1])
        p_count = int(lines[1][-1])
        p_length_max = int(lines[2][-1])
        p_length = int(lines[3][-1])
    else:
        p_count_max = 16
        p_count = pGen.p_input("Choose amount of passwords: ", p_count_max)

        p_length_max = 256
        p_length = pGen.p_input("Choose amount of symbols of your password: ", p_length_max)

        with open("config.ini", "w") as f:
            f.writelines([f"count_max {p_count_max}\n", f"count {p_count}\n",
                          f"length_max {p_length_max}\n", f"length {p_length}\n"])

    print("Generated:")
    passwords = pGen.p_generates(p_count, p_length)
    index = pGen.p_input("Choose number of password to copy: ", p_count)

    chosen_password = passwords[index - 1]
    pyperclip.copy(chosen_password)
    print("Buffered:", pyperclip.paste())
    key = input("\nEnter any key for exit...")



