def sum(*args , **kwargs):
    sum_number = 0
    for arg in args:
        sum_number +=arg
    return 'sum is {}'.format(sum_number)

print(sum(1,5))
