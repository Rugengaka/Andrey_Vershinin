def first_non_repeating_letter(string: str):
    string_uppercased = string.upper()
    for letter in string:
        if(string_uppercased.count(letter.upper()) <= 1):
            return letter
    return None


if __name__ == "__main__":
    print(first_non_repeating_letter("stress"))
    print(first_non_repeating_letter("sTreSS"))
    print(first_non_repeating_letter("abbsas"))