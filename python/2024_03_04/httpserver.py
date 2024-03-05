import hug
from binary_search import do_bs

arr = []


@hug.get('/remembrall_store')
def rememberall_store(a: hug.types.delimited_list(',')):
    print(f'a is {a}')
    a = [int(x)
         for x in a]  #Converting string to int has to happen, how to modularize this into a type?
    arr.extend(a)
    return f"the current arr is {arr}"


@hug.get('/remembrall')
def remembrall(num: hug.types.number):
    arr.sort()  #TODO sorting every time is expensive
    ans = do_bs(arr, num)
    if ans >= 0:
        return "Yes I have seen that number before"
    else:
        return "No I have not seen that number before"
