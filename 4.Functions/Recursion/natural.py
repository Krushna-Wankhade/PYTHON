##write a recursive function to calculate yhe sum of first n natural number.

def calc_sum(n):
    if (n==0):
        return 0
    return calc_sum(n-1) + n
    
sum=calc_sum(10)
print(sum)