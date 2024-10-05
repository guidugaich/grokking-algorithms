def binary_search(arr, target):
  low = 0 # index of the lowest/first value
  high = len(arr)-1 # index of the highest/last value

  while low <= high:
    mid = (low + high) // 2
    guess = arr[mid] # guess the value in the middle
    if guess == target:
      return mid
    elif guess > target:
      high = mid - 1 # guess was too high - the new high is in the middle (everything else is too high)
    else:
      low = mid + 1 # guess was too low - the new low is in the middle (everything else is too low
  return None

print(binary_search([1,3,5,7,9], 3))
print(binary_search([1,3,5,7,9], 11))
print(binary_search([1,3,5,7,9], 9))
