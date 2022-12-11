def bigger(value: int):
    if(value > 9):
        number = [digit for digit in str(value)]
        number[-1], number[-2] = number[-2], number[-1]
        new_value = int(''.join(number))
        if(new_value > value):
            return new_value
    return -1


if __name__ == "__main__":
    print(bigger(48))
    print(bigger(513))
    print(bigger(2017))
    print(bigger(9))
    print(bigger(111))
    print(bigger(531))
