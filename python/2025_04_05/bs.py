arr = [5, 4, 2, 1, 6, 8]
arr.sort()
print(arr)
low = 0
high = len(arr) - 1
search_ele = 8
found = False
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == search_ele:
        found = True
        print(f'search element {search_ele} found at {mid}')
        break
    elif arr[mid] < search_ele:
        low = mid + 1
    elif arr[mid] > search_ele:
        high = mid - 1

if not found:
    print(f'search element {search_ele} not found')

print('program execution complete')