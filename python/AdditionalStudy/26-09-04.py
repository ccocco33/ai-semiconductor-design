# # 다음 함수를 Lambda 식으로 바꿔라.
# # def calc(x, y):
# #     return x * y + 10
# f = lambda x,y : x*y+10
# print(f(3,5))

# # 다음 리스트의 모든 숫자를 3배한 결과를 리스트로 만들어라.
# x = [2, 4, 6, 8, 10]
# x = list(map(lambda a : a*3 ,x))
# print(x)

# # 공백으로 입력된 숫자들을 모두 실수로 변환한 뒤 반올림한 값을 출력하라.
# x = input().split()
# x = list(map(lambda a : round(float(a)),x))
# print(*x)

# 두 숫자를 입력받아 다음 네 가지 값을 하나의 tuple로 반환하는 lambda를 만들어라.

# 합
# 차
# 곱
# 나눗셈
# a,b = map(int,input().split())
# r = lambda t,g : (t+g, t - g,t*g,t/g)
# print(r(a,b))

# # 다음 데이터에서 나이가 가장 적은 사람의 tuple을 찾아라.
# x = (
#     ('kim', 25),
#     ('lee', 19),
#     ('park', 31),
#     ('choi', 22)
# )
# r = min(x , key= lambda a: a[1])
# print(r)

# # 다음 상품 중 가격이 가장 비싼 상품을 찾아라.
# x = (
#     ('apple', 3000),
#     ('banana', 1500),
#     ('kiwi', 4500),
#     ('orange', 2800)
# )
# print(max(x,key=lambda a: a[1]))

# # 다음 학생들을 점수가 낮은 순서 → 높은 순서로 정렬하라.

# x = [
#     ('kim', 80),
#     ('lee', 95),
#     ('park', 72),
#     ('choi', 88)
# ]
# print(sorted(x,key= lambda a : a[1]))

# # 다음 상품들을 가격이 높은 순서로 정렬하라.
# x = [
#     ('apple', 3000),
#     ('kiwi', 4500),
#     ('banana', 1500),
#     ('orange', 2800)
# ]
# print(sorted(x,key= lambda a : a[1], reverse= True))
# print(sorted(x,key= lambda a : -a[1]))

# # 다음 상품 데이터를 가지고 있다.
# # 다음 조건으로 정렬하라.
# # 가격은 작은 순서
# # 가격이 같다면 상품 이름은 가나다순(알파벳순)
# x = [
#     ('apple', 'red', 500),
#     ('kiwi', 'brown', 300),
#     ('banana', 'yellow', 300),
#     ('orange', 'orange', 500)
# ]
# print(sorted(x, key= lambda a : (a[2],a[0])))

# 다음 창고 데이터가 있다.
# 다음 조건으로 정렬하라.
# 세 번째 값(가격)은 작은 순서
# 가격이 같다면 첫 번째 값(상품 이름)은 알파벳순
# x = [
#     ('apple', 'red', 500),
#     ('kiwi', 'brown', 300),
#     ('banana', 'yellow', 300),
#     ('orange', 'orange', 500)
# ]
# print(sorted(x, key= lambda a : (a[2],a[0])))

#가격 오름차순 + 알파벳 내림차순 !!!!!!!!!!!!!!!!!!!!!!!!!!
# x = [
#     ('apple', 500),
#     ('kiwi', 300),
#     ('banana', 500),
#     ('orange', 300)
# ]
# x = sorted(x,key = lambda a : a[0],reverse = True) #알파벳부터 내림차순으로 정렬먼저하기
# x = sorted(x , key= lambda a : a[1])
# print(x)

##########################################################################################################
# # 한 줄에 여러 개의 정수가 문자열로 입력된다.
# # 각 숫자에 대해
# # 숫자를 정수로 변환 → 3을 더함 → 제곱
# # 한 결과를 리스트로 만들어라.
# x = input().split()
# r = map(lambda a: (int(a)+3)**2,x)
# print(list(r))

# # 다음 데이터가 있다.
# # 각 tuple을 다음 형태로 변경하라.
# # ('kim', 20)
# # ('lee', 40)
# # ('park', 60)
# # ('choi', 80)
# # 즉, 두 번째 값에 2를 곱한다.
# # 결과는 리스트로 만들어라.
# x = [
#     ('kim', 10),
#     ('lee', 20),
#     ('park', 30),
#     ('choi', 40)
# ]
# print(list(map(lambda a: (a[0],a[1]*2),x)))

# 각 학생의 3과목 평균이 높은 순서로 정렬하라.
# 단, 평균이 같다면 이름 알파벳순으로 정렬한다.
# x = [
#     ('kim', 80, 90, 70),
#     ('lee', 90, 80, 100),
#     ('park', 70, 70, 80),
#     ('choi', 100, 60, 90)
# ]
# t = sorted(x , key= lambda a : (-(a[1]+a[2]+a[3]),a[0]))
# print(t)