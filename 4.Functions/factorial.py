#calculate the factorial


# n=5
# fact=1
# for i in range(1,n+1):
#     fact *= i
# print(fact)


def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    print(fact)
    
cal_fact(6)
cal_fact(5)