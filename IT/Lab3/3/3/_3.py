
def binary_search(alist, l, r, key):
    if not l < r:
        return -1
    m = (l + r)//2
    if alist[m] < key:
        return binary_search(alist, m + 1, r, key)
    elif alist[m] > key:
        return binary_search(alist, l, m, key)
    else:
        return m
 
 
alist = input('Enter the list of numbers(sorted): ')
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input('Search element: '))
 
index = binary_search(alist, 0, len(alist), key)
if index < 0:
    print('{} not found.'.format(key))
else:
    print('{} found at index {}.'.format(key, index))