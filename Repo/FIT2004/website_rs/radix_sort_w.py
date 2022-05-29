from counting_sort_w import counting_sort

def get_digit(n, d):
  for i in range(d-1):
    n //= 10
  return n % 10

def get_num_difit(n):
  i = 0
  while n > 0:
    n //= 10
    i += 1
  return i

def get_digit_at(num, place, base):
  '''
  place = 1, most right
  '''
  retval = num//(pow(base,place-1))%base
  return retval


print(get_digit_at(12345, 2, 10))

def nums_rad_sort(arr, max_value):
  num_digits = get_num_difit(max_value)
  # O(k(n+k))
  for d in range(num_digits):
    # Counting sort takes O(n+k)
    arr = counting_sort(arr, max_value, lambda a: get_digit(a, d+1))
  return arr

# print(radix_sort([21, 233],333))