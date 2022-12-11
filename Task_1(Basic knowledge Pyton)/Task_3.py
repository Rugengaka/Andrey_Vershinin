def digital_root(value: int):
    value_str = str(value)
    sum_of_digits = sum([int(digit) for digit in value_str])
    if (sum_of_digits > 9):
        sum_of_digits = digital_root(sum_of_digits)
    return sum_of_digits


if __name__ == "__main__":
    print(digital_root(16))
    print(digital_root(832))
    print(digital_root(164867))
    print(digital_root(4862762))
