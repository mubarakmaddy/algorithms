my_list = [1, 3, 5, 7, 9]


def binary_search_1(arr, item):
  min = 0
  max = len(arr) - 1
  mid = 0

  while max >= min:
    mid = (min + max) // 2
    guess = arr[mid]
    if guess == item:
      return mid
    elif guess > item:
      max = mid - 1
    else:
      min = mid + 1
  return None


print(binary_search_1(my_list, 9))


#Using recursion:
def recursive_binary_search(arr, item, min, max):
  if max >= min:
    mid = (min + max) // 2
    guess = arr[mid]
    if guess == item:
      return mid
    elif guess > item:
      return recursive_binary_search(arr, item, min, mid - 1)
    else:
      return recursive_binary_search(arr, item, mid + 1, max)
  else:
    return None


print(recursive_binary_search(my_list, 9, 0, len(my_list) - 1))
