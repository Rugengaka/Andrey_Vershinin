def format_string(string: str):
    return_string = str()
    set_of_pairs = string.split(";")                          # split to pairs
    for i in range(len(set_of_pairs)):
        pair_list = set_of_pairs[i].split(":")               # split by name, surname
        pair_list.reverse()                                  # reverse surname with name
        pair_list = [pair.upper() for pair in pair_list]     # Up all symbols
        set_of_pairs[i] = pair_list                          # override pair
    set_of_pairs.sort()
    for surname, name in set_of_pairs:
        return_string += f"({surname}, {name})"
    return return_string

if __name__ == "__main__":
    s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
    print(format_string(s))
