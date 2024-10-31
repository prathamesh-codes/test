encoded_lists = [
    [1,2,3,4,6],
    [5,7,8,9,15],
    [12,14,16,18],
    [10,11,12,13,16,17,18,20]
    ]

def explode_chains(encoded_lists):
    def remove_consecutive_sequences(lst):
        i = 0
        while i < len(lst) - 2:
            if lst[i] == lst[i+1]+1 == lst[i+2]+2:
                lst.pop(i)
                lst.pop(i+1)
                lst.pop(i+2)
            else:
                i += 1

    new_encoded_lists = [lst.copy() for lst in encoded_lists]
    exploded = True

    while exploded:
        exploded = False
        for lst in new_encoded_lists:
            original_length = len(lst)
            remove_consecutive_sequences(lst)
            if len(lst) < original_length:
                exploded = True

    return new_encoded_lists

exploded_lists = explode_chains(encoded_lists)
for lst in exploded_lists:
    print(lst)
