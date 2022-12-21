def sum_range(min,max):
    if min>max:
        min,max=max,min
    return sum(range(min,max+1))

print(sum_range(2,20))
