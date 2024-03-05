import hug
from binary_search import do_bs

arr = []


@hug.get('/remembrall_store')
def rememberall_store(a: hug.types.delimited_list(',')):
    print(f'a is {a}')
    a = [int(x) for x in a]
    arr.extend(a)
    return f"the current arr is {arr}"


@hug.get('/remembrall')
def remembrall(num: hug.types.number):
    arr.sort()
    ans = do_bs(arr, num)
    if ans >= 0:
        return "Yes I have seen that number before"
    else:
        return "No I have not seen that number before"
