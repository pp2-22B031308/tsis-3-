def unique_list(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

print(unique_list([1, 2, 3, 3, 4, 5, 5, 6]))


