def find_smallest(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

def selection_sort(arr):
  sorted_arr = []
  copied_arr = list(arr)
  for i in range(len(copied_arr)):
    smallest = find_smallest(copied_arr)
    sorted_arr.append(copied_arr.pop(smallest)) # removes element from copied_arr and appends it to sorted - next iteration copied)arr will be smaller
    
  return sorted_arr

print(selection_sort([5,7,89,12,2,3,5,3]))