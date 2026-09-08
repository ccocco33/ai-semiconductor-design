
#8번
# n = int(input())
# data = []

# for a in range(n):
#     name_,price_,number_= input().split()
#     data.append((name_,int(price_),int(number_)))
    
# data.sort(key= lambda a : a[0])
# data.sort(key= lambda a :a[1]*a[2] ,reverse= True)
# for a in range(n):
#     print(data[a][0])


#9번
# a = int(input())
# data = []
# for b in range(a):
#     n,y,p = input().split()
#     data.append((n,y,p))
# print(data)
# data.sort(key = lambda a : (a[1],a[2],a[0]) )
# print(data[0][0])

#10번
# n = int(input())
# data = []
# for a in range(n):
#     name_, p, num, per = input().split()
#     data.append((name_,int(p),int(num),float(per),int(p)*int(num)*(1-float(per)*0.01)))
# data.sort(key= lambda a: a[0])
# data.sort(key = lambda a: a[2]
#           )
# data.sort(key= lambda a: a[4],reverse= True)

# print(*(x[0] for x in data), sep='\n')

#11번
x = [
    ('apple', 1000),
    ('banana', 2000),
    ('kiwi', 500),
    ('orange', 3000)
]
r =1000
y = map(lambda a: (a[0],int( a[1] * 1.1)) if a[1] > r else a, x)



print(*y, sep= '\n')