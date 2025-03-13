import hug
from binary_search import bs

arr = []


@hug.get('/add_num')
def add_num(a):
    print(f'type of a is {type(a)}')
    a = [int(x) for x in a]
    arr.extend(a)
    return f"arr is {arr}"

@hug.get('/search_num')
def search_num(k):
    arr.sort()
    ans = bs(arr, int(k))
    return f'{k} found at index {ans}'

