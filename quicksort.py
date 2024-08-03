def quicksort(list):
    # base case
    if len(list) < 2:
        return list
    # recursive case
    pivot = list[0]
    left = [i for i in list[1:] if i <= pivot]
    right = [i for i in list[1:] if i > pivot]

    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([23,43,53,46,457,456,34,532,53,46,46,45,64,5]))