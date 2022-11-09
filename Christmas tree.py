import os
import sys
from time import sleep


class SumName:

    def __init__(self, ss):
        self.count = ss
        self.suka()

    def suka(self):

        auto_el = []
        line = []
        # count = 20
        for i in range(5):
            # print(i)
            if i == 0:
                line = []
                itr = int(self.count / 2 - 2)
                line_count = 1
                back = '\\'
                while itr >= 0:
                    if itr == int(self.count / 2 - 2):
                        line.append(f"{' ' * (itr + 1)}{'/' * line_count}|{back * line_count}\n")
                    else:
                        line.append(f"{' ' * itr}o{'/' * line_count}|{back * line_count}o\n")
                    if not itr == int(self.count / 2 - 2):
                        line.append(f"{' ' * (itr + 2)}{'/' * (line_count - 1)}|{back * (line_count - 1)}\n")
                    itr -= 1
                    line_count += 1
                line.insert(0, f'{" " * (int(self.count / 2 - 1))} X\n')
            elif i == 1:
                line = []
                itr = int(self.count / 2 - 2)
                line_count = 1
                back = '\\'
                while itr >= 0:
                    if itr == int(self.count / 2 - 2):
                        line.append(f"{' ' * (itr + 1)}{'/' * line_count}|{back * line_count}\n")
                    else:
                        line.append(f"{' ' * itr}₀{'/' * line_count}|{back * line_count}₀\n")
                    if not itr == int(self.count / 2 - 2):
                        line.append(f"{' ' * (itr + 2)}{'/' * (line_count - 1)}|{back * (line_count - 1)}\n")
                    itr -= 1
                    line_count += 1
                line.insert(0, f'{" " * (int(self.count / 2 - 1))} *\n')
            elif i == 2:
                line = []
                itr = int(self.count / 2 - 2)
                line_count = 1
                back = '\\'
                while itr >= 0:
                    if itr == int(self.count / 2 - 2):
                        line.append(f"{' ' * (itr + 1)}{'/' * line_count}|{back * line_count}\n")
                    else:
                        line.append(f"{' ' * itr}.{'/' * line_count}|{back * line_count}.\n")
                    if not itr == int(self.count / 2 - 2):
                        line.append(f"{' ' * (itr + 2)}{'/' * (line_count - 1)}|{back * (line_count - 1)}\n")
                    itr -= 1
                    line_count += 1
                line.insert(0, f'{" " * (int(self.count / 2 - 1))} +\n')
            elif i == 3:
                line = []
                itr = int(self.count / 2 - 2)
                line_count = 1
                back = '\\'
                while itr >= 0:
                    if itr == int(self.count / 2 - 2):
                        line.append(f"{' ' * (itr + 1)}{'/' * line_count}|{back * line_count}\n")
                    else:
                        line.append(f"{' ' * itr}₀{'/' * line_count}|{back * line_count}₀\n")
                    if not itr == int(self.count / 2 - 2):
                        line.append(f"{' ' * (itr + 2)}{'/' * (line_count - 1)}|{back * (line_count - 1)}\n")
                    itr -= 1
                    line_count += 1
                line.insert(0, f'{" " * (int(self.count / 2 - 1))} *\n')
            elif i == 4:
                line = []
                itr = int(self.count / 2 - 2)
                line_count = 1
                back = '\\'
                while itr >= 0:
                    if itr == int(self.count / 2 - 2):
                        line.append(f"{' ' * (itr + 1)}{'/' * line_count}|{back * line_count}\n")
                    else:
                        line.append(f"{' ' * itr}.{'/' * line_count}|{back * line_count}.\n")
                    if not itr == int(self.count / 2 - 2):
                        line.append(f"{' ' * (itr + 2)}{'/' * (line_count - 1)}|{back * (line_count - 1)}\n")
                    itr -= 1
                    line_count += 1
                line.insert(0, f'{" " * (int(self.count / 2 - 1))} x\n')
            auto_el.append(''.join(line))

        while True:
            for ii in auto_el:
                print(ii)
                sleep(.15)
                os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    c = SumName(int(sys.argv[1]))


