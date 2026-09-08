7과 Lambda Expression

lambda parameters: (리턴 수식)
활용
sorted(x,key = lambda a : a[0])
min(x,key = lambda a : a[3])
list(map(lambda t: round(float(t)**2,x)))

# 7과. Lambda Expression

## 1. Lambda Expression이란?

**lambda 표현식**은 이름이 없는 **익명 함수(anonymous function)** 를 한 줄로 작성하는 방법이다.

일반적인 함수는 `def`를 사용한다.

```python
def add(a, b):
    return a + b
```

같은 함수를 lambda로 작성하면:

```python
lambda a, b: a + b
```

### 기본 문법

```python
lambda parameter1, parameter2, ... : return_expression
```

즉,

```text
lambda 매개변수 : 리턴할 식
```

예:

```python
lambda x: x * 2
```

→ `x`를 받아서 `x * 2`를 반환

```python
lambda a, b: a + b
```

→ `a`, `b`를 받아서 `a + b`를 반환

> ⭐ `lambda` 함수에서는 `return`을 직접 쓰지 않는다.
> 콜론(`:`) 뒤의 **표현식 결과가 자동으로 반환**된다.

---

## 2. 일반 함수와 Lambda 비교

### 일반 함수

```python
def square(x):
    return x ** 2

print(square(5))
```

결과:

```text
25
```

### Lambda

```python
square = lambda x: x ** 2

print(square(5))
```

결과:

```text
25
```

둘은 같은 기능을 한다.

다만 lambda는 보통 **잠깐 사용할 간단한 함수를 인자로 전달할 때** 많이 사용한다.

---

# 3. Lambda의 주요 활용

Lambda는 특히 다음과 함께 자주 사용한다.

```text
sorted()
min()
max()
map()
filter()
```

---

## 3-1. sorted() + lambda

리스트 안의 값을 어떤 기준으로 정렬하고 싶을 때 `key`에 lambda를 넣을 수 있다.

```python
x = [('apple', 500), ('kiwi', 300), ('banana', 700)]

print(sorted(x, key=lambda a: a[1]))
```

결과:

```text
[('kiwi', 300), ('apple', 500), ('banana', 700)]
```

### 의미

```python
key=lambda a: a[1]
```

각 요소 `a`에서 **두 번째 값 `a[1]`을 정렬 기준으로 사용**한다.

즉,

```text
('apple', 500)  → 500
('kiwi', 300)   → 300
('banana', 700) → 700
```

이 값을 기준으로 정렬한다.

### 내림차순

```python
sorted(x, key=lambda a: a[1], reverse=True)
```

---

## 3-2. min() + lambda

`min()`에서도 `key`를 사용할 수 있다.

```python
x = [
    ('apple', 'red', 500, 10),
    ('kiwi', 'brown', 300, 20),
    ('banana', 'yellow', 700, 5)
]

print(min(x, key=lambda a: a[3]))
```

결과:

```text
('banana', 'yellow', 700, 5)
```

### 의미

```python
key=lambda a: a[3]
```

각 튜플의 **네 번째 값**을 비교해서 가장 작은 요소를 찾는다.

```text
apple  → 10
kiwi   → 20
banana → 5
```

따라서 `banana`가 반환된다.

> ⭐ `min()`은 **key의 결과값이 가장 작은 원본 요소**를 반환한다.

---

# 4. map() + lambda

`map()`은 여러 값에 **같은 함수를 적용**할 때 사용한다.

### 기본 형태

```python
map(function, iterable)
```

lambda를 이용하면:

```python
list(map(lambda x: x * 2, [1, 2, 3, 4]))
```

결과:

```text
[2, 4, 6, 8]
```

동작 과정:

```text
1 → 1 * 2 → 2
2 → 2 * 2 → 4
3 → 3 * 2 → 6
4 → 4 * 2 → 8
```

---

## 4-1. input()과 map() + lambda

문자열을 입력받아서 계산할 때도 자주 사용한다.

```python
x = input().split()

print(list(map(lambda t: float(t) ** 2, x)))
```

예를 들어:

```text
1.5 2 3
```

입력하면:

```text
[2.25, 4.0, 9.0]
```

### 과정

```python
input().split()
```

↓

```python
['1.5', '2', '3']
```

↓

```python
lambda t: float(t) ** 2
```

↓

```text
'1.5' → 2.25
'2'   → 4.0
'3'   → 9.0
```

---

# 5. 네가 적은 코드 수정

네가 적은 코드:

```python
list(map(lambda t: round(float(t)**2,x)))
```

여기에는 `map()`의 두 번째 인자인 **iterable이 빠져 있다.**

`map()`은 기본적으로:

```python
map(함수, 반복할_대상)
```

형태여야 한다.

예를 들어 `x`가 입력 데이터라면:

```python
list(map(lambda t: round(float(t) ** 2, 2), x))
```

여기서:

```python
lambda t: round(float(t) ** 2, 2)
```

는

1. `t`를 실수로 변환
2. 제곱
3. 소수점 둘째 자리까지 반올림

한다.

예:

```python
x = ['1.234', '2.345', '3.456']

print(list(map(lambda t: round(float(t) ** 2, 2), x)))
```

결과:

```text
[1.52, 5.5, 11.94]
```

---

# 6. Lambda + filter()

`filter()`는 조건을 만족하는 값만 골라낼 때 사용한다.

```python
x = [1, 2, 3, 4, 5, 6]

print(list(filter(lambda a: a % 2 == 0, x)))
```

결과:

```text
[2, 4, 6]
```

### 의미

```python
lambda a: a % 2 == 0
```

→ `a`가 짝수이면 `True`

따라서 짝수만 남는다.

```text
1 → False → 제외
2 → True  → 선택
3 → False → 제외
4 → True  → 선택
5 → False → 제외
6 → True  → 선택
```

---

# 7. Lambda + sorted() 핵심 패턴

튜플이나 리스트 내부의 특정 위치를 기준으로 정렬할 때 매우 자주 사용한다.

```python
x = [
    ('apple', 500),
    ('kiwi', 300),
    ('banana', 700)
]
```

### 첫 번째 값 기준

```python
sorted(x, key=lambda a: a[0])
```

### 두 번째 값 기준 오름차순

```python
sorted(x, key=lambda a: a[1])
```

### 두 번째 값 기준 내림차순

```python
sorted(x, key=lambda a: a[1], reverse=True)
```

---

# 8. Lambda + min(), max()

```python
min(x, key=lambda a: a[1])
```

→ 두 번째 값을 기준으로 가장 작은 요소

```python
max(x, key=lambda a: a[1])
```

→ 두 번째 값을 기준으로 가장 큰 요소

---

# 9. ⭐ 핵심 암기

```text
lambda
    ↓
이름 없는 간단한 함수
```

기본 문법:

```python
lambda parameter: return_expression
```

### 자주 사용하는 패턴

```python
sorted(x, key=lambda a: a[0])
```

→ `a[0]`을 기준으로 정렬

```python
min(x, key=lambda a: a[3])
```

→ `a[3]`을 기준으로 최솟값

```python
max(x, key=lambda a: a[3])
```

→ `a[3]`을 기준으로 최댓값

```python
list(map(lambda a: a * 2, x))
```

→ 모든 요소에 `a * 2` 적용

```python
list(filter(lambda a: a > 0, x))
```

→ `a > 0`인 요소만 선택

### 한 줄 암기

```text
sorted → 기준을 정한다
min/max → 기준으로 최소/최대 찾는다
map → 모든 요소를 변환한다
filter → 조건에 맞는 요소만 골라낸다
```

### Lambda에서 특히 기억할 것

```python
lambda a: a[0]
```

여기서

```text
a     → 입력값
a[0]  → 반환값
```

즉,

**`lambda 입력 : 결과`**

라고 생각하면 가장 쉽다.
