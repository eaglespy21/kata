import hug

arr = []


@hug.get('/add_numbers')
def add_numbers(a: hug.types.delimited_list(',')):
    a = [int(x) for x in a]
    arr.extend(a)
    return f'New list is {arr}'


@hug.get('/find_number')
def find_number(num: hug.types.number):
    try:
        i = arr.index(num)
    except ValueError as ve:
        return f'{num} not found in list {arr}'
    return f'{num} found in list at index {i}'
