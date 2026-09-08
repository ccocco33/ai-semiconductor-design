# # 정수값인 사번(id)를 넣으면 팀 번호를 리턴하는 함수 check_team 함수를 설계하라.
# # 단, 팀 번호는 사번 끝자리 값으로 정한다.
# # (주의) 템플릿 코드를 사용하되 주어진 코드는 변형하면 안됨
# # 입출력 예시
# # 입력 1
# # 1234567
# # 출력 1
# # 7

# def check_team(id) :
#     return id % 10

# n = int(input())
# print(check_team(n))

# # 첫째 줄에 n개의 정수가 공백으로 분리되어 입력된다.
# # 둘째 줄에 찾을 보석에 해당하는 정수 x가 입력된다.
# # 이들 숫자 중에서 보석에 해당하는 값의 개수를 구하고자 한다.
# # 이를 위하여 함수 find_gem을 설계하라.
# # find_gem 함수는 다음과 같이 2개의 parameter를 갖는다.
# # box: n개의 정수를 저장하고 있는 map 타입
# # gem: 보석으로 인정되는 정숫값
# # 리턴 : 전달받은 box에 들어 있는 gem과 같은 수의 개수
# # 입출력 예시
# # 입력 1
# # 1 3 56 89 23 40 23 45 80 40 9 1 3
# # 3
# # 출력 1
# # 2

# def find_gem(box, gem) :
#     return tuple(box).count(gem)

# n = map(int, input().split())
# x = int(input())
# print(find_gem(n, x))

# # n명의 학생 성적을 전달받아서 평균과 1등의 성적을 리턴하는 함수를 설계하라.
# # 입력되는 성적은 iterable 타입이며 리턴은 평균과 1등 성적을 튜플로 반환해야 한다.
# # 단, 평균은 소수부 둘째 자리에서 round 처리한다.
# # 입출력 예시
# # 입력 1
# # 37 50 90 72 23 80 99 100 88 77 66
# # 출력 1
# # (71.09, 100)

# def score(x) :
#     x = tuple(x)
#     return round(sum(x)/len(x), 2), max(x)

# n = map(int, input().split())
# print(score(n))

# # 함수가 호출될 때마다 입력받은 값의 합을 계속 누적 합계를 구하여 결괏값을 리턴하는 함수를 구하라.
# # 함수 이름은 func로 하며 func(1), func(3), func(10) 순서로 호출이 되었다면
# # 리턴 값은 처음에는 1, 다음에는 1+3 즉, 4, 다음에는 4+10 즉, 14가 되어야 한다.
# # 주어진 코드를 사용하되 기존 코드는 수정하면 안 되며 필요시 전역변수 등은 자유롭게 추가할 수 있다.
# # 입출력 예시
# # 입력 1
# # 1 2 3 4 10
# # 출력 1
# # 1 3 6 10 20

# def func(n) :
#     global s
#     s += n
#     return s

# s = 0
# x = map(int, input().split())
# y = map(func, x)
# print(*y)

# # clean 함수는 문자열을 입력 받으면 ()로 감싸서 쓰리기통(전역변수로 생성된 list 타입의 bin)에 추가한다.이러한 동작을 수행하는 clean 함수를 설계하라.
# # 입출력 예시
# # 입력 1
# # cup dish can toy radio pen
# # 출력 1
# # ['(cup)']
# # ['(cup)', '(dish)']
# # ['(cup)', '(dish)', '(can)']
# # ['(cup)', '(dish)', '(can)', '(toy)']
# # ['(cup)', '(dish)', '(can)', '(toy)', '(radio)']
# # ['(cup)', '(dish)', '(can)', '(toy)', '(radio)', '(pen)']

# def clean(x) :
#     bin.append('('+x+')')

# bin = []

# for y in input().split() :
#     clean(y)
#     print(bin)

# # 전달된 문자열 s의 시작과 끝에 전달된 문자열 x를 추가시킨 문자열을 리턴하는 func 함수를 설계하라.
# # 단, x를 전달하지 않을 경우는 시작과 끝에 *를 추가한다.
# # 즉, print(func(s, x))로 함수를 호출하면 s 앞과 뒤애 x를 붙인 문자열을 리턴하고
# # print(func(s))로 호출하면 s 앞과 뒤에 *을 붙인 문자열을 리턴해야 한다.
# # 입력 예처럼 kim %%%를 받은 상태에서 아래와 같이 두 번 함수를 호출하면 출력 예시와 같이
# # 처음 호출은 kim 앞, 뒤에 %%%을 붙인 문자열이
# # 두 번째 호출은 kim 앞, 뒤에 *을 붙인 문자열이 리턴되면 된다
# # print(func(s, x))
# # print(func(s))
# # 입출력 예시
# # 입력 1
# # kim %%%
# # 출력 1
# # %%%kim%%%
# # *kim*

# def func(s, x = '*') :
#     return x + s + x

# s, x = input().split()
# print(func(s, x))
# print(func(s))