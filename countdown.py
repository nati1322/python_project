import math
import time


def add_padding(number):
    if number < 10:
        return f"0{number}"
    else:
        return str(number)


def countdown_timer():
    minute = float(input("Enter the minute: "))
    second = int(minute * 60)
    for i in range(second, 0, -1):
        mm = add_padding(math.floor(i / 60))
        ss = add_padding(i % 60)
        print(f"{mm}:{ss}")
        time.sleep(1)


if __name__ == "__main__":
    countdown_timer()