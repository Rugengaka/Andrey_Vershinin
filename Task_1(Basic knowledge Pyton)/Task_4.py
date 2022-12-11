def get_pair_for_target(list: list, target: int):
    return_list_of_pairs = []
    for i in range(len(list)):                                  # iteration all items
        for j in range(i, len(list)):                           # iteration items after i
            if((list[i], list[j]) not in return_list_of_pairs): # check if tuple unique
                if(list[i] + list[j] == target):                # main condition
                    return_list_of_pairs.append((list[i], list[j]))
    return return_list_of_pairs


if __name__ == "__main__":
    print(get_pair_for_target([1, 3, 6, 2, 2, 0, 4, 5], 5))
