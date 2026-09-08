
주요 Bulit in 함수
-Iterable이 아닌 object에 사용
abs(): 절댓값
pow(v,e,[,m]): v의 e 제곱, m 이 있으면 결과를 %m (나머지)의 결과 반환
divmod(a,b): (몫,나머지)-튜플
max(...[,key])
min(...[,key])
round(x,[,d]): d 음수 또는 0 - 정수부 d자리만큼 0으로만들고 윗자리는 round
               d 양수 - 소수부 d 자리에서 round
(ex) round(1236,-2) = 1200 ,round(3.745,1) = 3.7

-Iterable 타입 
len(): 갯수 반환
sum(it,[,stsrt]) : 합 , start는 합산 초기값
sorted(it,[,key,reverse]) : 오름차순 결과를 list로 반환, 원본 변경x
max(),min()

Sequence Type 메서드 (str,tuple,list,range)
s.index(x,[,m[,n]]) : m부터 n 직전 사이의 첫번째 x의 인덱스 번호 ,없으면 ValueError
s.count(x) : s에등장하는 x의 총개수 반환, 없으면 0

Iterator를 반환하는 Built in 함수
-> iterable을 처리하는 built in 함수
map(function,it[,...])
filter(function,it): 결과가 True인 item목록을 filter타입으로 반환
zip(*it[,strict]): iterable의 동일 인덱스의 item들을 튜플 쌍으로 반환, 결과는 zip타입, strict를 True로 하면 개수 다를시 ValueError
# dict(zip(a,b))
enumerate(it[,start = 0]) : start는 시작 번호, item들의 번호를 부여하며 (idx,value)의 튜플 쌍으로 생성
# t = dict(enumerate(x,0))

# 1과. 주요 Built-in 함수 정리

## 1. Built-in 함수

Python에서 기본적으로 제공하는 함수이다.

대표적으로 다음과 같은 함수들이 있다.

```text
abs()
pow()
divmod()
max()
min()
round()

len()
sum()
sorted()

map()
filter()
zip()
enumerate()
```

---

# 2. Iterable이 아닌 객체에 주로 사용하는 함수

## `abs()`

숫자의 **절댓값**을 반환한다.

```python
print(abs(-10))
print(abs(10))
```

출력:

```text
10
10
```

```text
abs(-3) → 3
abs( 3) → 3
```

---

## `pow()`

거듭제곱을 계산한다.

```python
pow(v, e)
```

→ `v`의 `e`제곱

```python
print(pow(2, 3))
```

출력:

```text
8
```

### 세 번째 인자

```python
pow(v, e, m)
```

→ `v ** e`를 계산한 뒤 `m`으로 나눈 **나머지**를 반환한다.

```python
print(pow(2, 3, 5))
```

계산:

```text
2³ = 8
8 % 5 = 3
```

결과:

```text
3
```

---

## `divmod()`

나눗셈의 **몫과 나머지**를 튜플로 반환한다.

```python
print(divmod(10, 3))
```

출력:

```text
(3, 1)
```

즉,

```text
divmod(a, b)
→ (몫, 나머지)
```

---

## `max()`

가장 큰 값을 반환한다.

```python
print(max(10, 30, 20))
```

출력:

```text
30
```

여러 값을 직접 넣을 수도 있고 Iterable을 넣을 수도 있다.

```python
max(10, 30, 20)
max([10, 30, 20])
```

### `key` 사용

어떤 기준으로 가장 큰 값을 찾을지 지정할 수 있다.

```python
x = ['apple', 'banana', 'kiwi']

print(max(x, key=len))
```

출력:

```text
banana
```

`len()`을 기준으로 가장 긴 문자열을 찾는다.

---

## `min()`

가장 작은 값을 반환한다.

```python
print(min(10, 30, 20))
```

출력:

```text
10
```

`max()`와 마찬가지로 `key`를 사용할 수 있다.

```python
x = ['apple', 'banana', 'kiwi']

print(min(x, key=len))
```

---

# 3. `round()`

반올림한 값을 반환한다.

```python
round(x)
round(x, d)
```

* `x` : 반올림할 값
* `d` : 반올림할 자릿수

---

## `d`가 양수

소수점 이하 `d`자리까지 반올림한다.

```python
round(3.745, 1)
```

→

```text
3.7
```

> ⚠️ Python의 `round()`는 우리가 일반적으로 생각하는 단순한 "5 이상이면 무조건 올림"과 조금 다르다.
>
> 부동소수점 표현 때문에 `round(3.745, 1)`은 `3.7`이 나온다.

---

## `d`가 0 또는 생략

소수점 이하를 반올림하여 정수 형태의 값을 반환한다.

```python
round(3.7)
```

→

```text
4
```

---

## `d`가 음수

정수부의 특정 자리를 기준으로 반올림한다.

```python
round(1236, -2)
```

→

```text
1200
```

`-2`는 **10의 자리까지 0으로 만들고 100의 자리에서 반올림**한다고 생각하면 이해하기 쉽다.

```text
1236
 ↓
1200
```

### 정리

```text
round(3.745, 1)
→ 소수 첫째 자리까지 반올림

round(1236, -2)
→ 100의 자리 단위로 반올림
→ 1200
```

---

# 4. Iterable에 사용하는 Built-in 함수

## `len()`

Iterable에 들어 있는 **item의 개수**를 반환한다.

```python
print(len([10, 20, 30]))
```

출력:

```text
3
```

문자열도 가능하다.

```python
print(len('hello'))
```

→

```text
5
```

---

## `sum()`

Iterable의 값을 모두 더한다.

```python
sum(it)
```

예:

```python
print(sum([1, 2, 3, 4]))
```

출력:

```text
10
```

### `start`

초기값을 지정할 수 있다.

```python
sum(it, start)
```

```python
print(sum([1, 2, 3], 10))
```

계산:

```text
10 + 1 + 2 + 3
```

결과:

```text
16
```

즉,

```text
sum(it, start)
→ start부터 Iterable의 값을 더함
```

---

# 5. `sorted()`

Iterable을 정렬한 **새로운 list**를 반환한다.

```python
sorted(it)
```

기본값은 오름차순이다.

```python
x = [3, 1, 4, 2]

y = sorted(x)

print(y)
print(x)
```

출력:

```text
[1, 2, 3, 4]
[3, 1, 4, 2]
```

> ⭐ `sorted()`는 **원본을 변경하지 않는다.**

---

## `reverse`

내림차순으로 정렬할 수 있다.

```python
sorted(x, reverse=True)
```

예:

```python
x = [3, 1, 4, 2]

print(sorted(x, reverse=True))
```

출력:

```text
[4, 3, 2, 1]
```

---

## `key`

정렬 기준을 지정할 수 있다.

```python
x = ['apple', 'kiwi', 'banana']

print(sorted(x, key=len))
```

출력:

```text
['kiwi', 'apple', 'banana']
```

문자열의 **길이**를 기준으로 정렬한다.

---

# 6. `max()` / `min()`

Iterable을 대상으로 사용할 수도 있다.

```python
x = [10, 30, 20]

print(max(x))
print(min(x))
```

출력:

```text
30
10
```

`key`를 사용하여 특정 기준으로 최대/최소를 찾을 수도 있다.

```python
x = ['apple', 'kiwi', 'banana']

print(max(x, key=len))
print(min(x, key=len))
```

결과:

```text
banana
kiwi
```

---

# 7. Sequence Type 메서드

대표적인 Sequence:

```text
str
tuple
list
range
```

이 자료형에서는 다음과 같은 메서드를 사용할 수 있다.

```text
index()
count()
```

---

## `s.index()`

특정 값 `x`가 **처음 등장하는 위치(index)**를 반환한다.

```python
s.index(x)
```

예:

```python
s = [10, 20, 30, 20]

print(s.index(20))
```

출력:

```text
1
```

`20`이 두 번 나오지만 **첫 번째 위치**인 `1`을 반환한다.

---

### 시작 위치 지정

```python
s.index(x, m)
```

`m`번 index부터 검색한다.

```python
s = [10, 20, 30, 20]

print(s.index(20, 2))
```

출력:

```text
3
```

---

### 검색 범위 지정

```python
s.index(x, m, n)
```

`m`부터 `n` **직전까지** 검색한다.

```text
s.index(x, m, n)

m → 포함
n → 미포함
```

찾는 값이 없으면:

```text
ValueError
```

가 발생한다.

---

## `s.count(x)`

Sequence에 `x`가 **몇 번 등장하는지** 반환한다.

```python
s = [1, 2, 2, 3, 2]

print(s.count(2))
```

출력:

```text
3
```

없으면:

```python
s.count(5)
```

→

```text
0
```

---

# 8. Iterator를 반환하는 Built-in 함수

다음 함수들은 Iterable을 처리하고 **Iterator 계열 객체**를 반환한다.

```text
map()
filter()
zip()
enumerate()
```

> ⭐ `list()`처럼 바로 모든 결과가 만들어지는 것이 아니라,
> 필요할 때 값을 꺼내는 방식으로 동작한다.

---

# 9. `map()`

Iterable의 각 item에 함수를 적용한다.

```python
map(function, it)
```

예:

```python
x = [1, 2, 3]

y = map(lambda a: a * 2, x)

print(list(y))
```

출력:

```text
[2, 4, 6]
```

즉:

```text
1 → 2
2 → 4
3 → 6
```

### 여러 Iterable

```python
map(function, it1, it2, ...)
```

함수가 여러 개의 인자를 받도록 만들 수 있다.

```python
a = [1, 2, 3]
b = [10, 20, 30]

result = map(lambda x, y: x + y, a, b)

print(list(result))
```

출력:

```text
[11, 22, 33]
```

---

# 10. `filter()`

조건 함수의 결과가 `True`인 item만 남긴다.

```python
filter(function, it)
```

예:

```python
x = [1, 2, 3, 4, 5]

y = filter(lambda a: a % 2 == 0, x)

print(list(y))
```

출력:

```text
[2, 4]
```

즉:

```text
1 → False → 제거
2 → True  → 남김
3 → False → 제거
4 → True  → 남김
5 → False → 제거
```

반환 타입은 `filter`이다.

```python
print(type(y))
```

```text
<class 'filter'>
```

---

# 11. `zip()`

여러 Iterable의 **같은 index에 있는 값들을 묶어 튜플로 만든다.**

```python
zip(it1, it2, ...)
```

예:

```python
a = [1, 2, 3]
b = ['a', 'b', 'c']

z = zip(a, b)

print(list(z))
```

출력:

```text
[(1, 'a'), (2, 'b'), (3, 'c')]
```

즉:

```text
a[0] + b[0] → (1, 'a')
a[1] + b[1] → (2, 'b')
a[2] + b[2] → (3, 'c')
```

---

## `zip()`의 특징

기본적으로 Iterable의 길이가 다르면 **짧은 쪽에 맞춰 종료**한다.

```python
a = [1, 2, 3]
b = ['a', 'b']

print(list(zip(a, b)))
```

결과:

```text
[(1, 'a'), (2, 'b')]
```

`3`은 대응되는 값이 없으므로 사용되지 않는다.

---

## `strict=True`

길이가 다르면 오류가 발생하도록 할 수 있다.

```python
zip(a, b, strict=True)
```

길이가 다르면:

```text
ValueError
```

가 발생한다.

---

# 12. `dict(zip(a, b))`

`zip()`을 이용하면 두 리스트를 **key-value 형태의 dict로 만들 수 있다.**

```python
a = ['apple', 'banana', 'kiwi']
b = [100, 200, 300]

d = dict(zip(a, b))

print(d)
```

결과:

```text
{'apple': 100, 'banana': 200, 'kiwi': 300}
```

과정:

```text
zip(a, b)
→ ('apple', 100)
→ ('banana', 200)
→ ('kiwi', 300)

dict()
→ {'apple': 100, 'banana': 200, 'kiwi': 300}
```

> ⭐ 시험에서 자주 나오는 형태
>
> ```python
> dict(zip(a, b))
> ```
>
> → `a`를 key, `b`를 value로 하는 dict 생성

---

# 13. `enumerate()`

Iterable의 각 item에 **번호(index)**를 붙여서 `(index, value)` 형태의 tuple로 만든다.

```python
enumerate(it)
```

예:

```python
x = ['a', 'b', 'c']

e = enumerate(x)

print(list(e))
```

출력:

```text
[(0, 'a'), (1, 'b'), (2, 'c')]
```

기본 시작 번호는 `0`이다.

---

## `start`

시작 번호를 지정할 수 있다.

```python
enumerate(it, start=1)
```

예:

```python
x = ['a', 'b', 'c']

print(list(enumerate(x, start=1)))
```

출력:

```text
[(1, 'a'), (2, 'b'), (3, 'c')]
```

---

# 14. `dict(enumerate())`

`enumerate()`를 이용하여 **index를 key로 하는 dict**를 만들 수 있다.

```python
x = ['a', 'b', 'c']

t = dict(enumerate(x))

print(t)
```

결과:

```text
{0: 'a', 1: 'b', 2: 'c'}
```

시작 번호를 `0`으로 명시할 수도 있다.

```python
t = dict(enumerate(x, start=0))
```

결과는 동일하다.

```text
{0: 'a', 1: 'b', 2: 'c'}
```

---

# ⭐ 1과 핵심 암기

```text
[숫자 관련]

abs(x)
→ 절댓값

pow(v, e)
→ v의 e제곱

pow(v, e, m)
→ (v ** e) % m

divmod(a, b)
→ (몫, 나머지)

max()
→ 최대값

min()
→ 최소값

round(x, d)
→ d자리까지 반올림
```

```text
[Iterable 관련]

len(it)
→ item 개수

sum(it)
→ 합

sum(it, start)
→ start부터 합산

sorted(it)
→ 정렬된 새로운 list
→ 원본 변경 X

sorted(it, reverse=True)
→ 내림차순

sorted(it, key=함수)
→ 함수의 결과를 기준으로 정렬
```

```text
[Sequence 메서드]

s.index(x)
→ x가 처음 등장하는 index

s.index(x, m, n)
→ m부터 n 직전까지 검색

s.count(x)
→ x의 등장 횟수
```

```text
[Iterator 반환]

map()
→ 각 item에 함수 적용

filter()
→ True인 item만 남김

zip()
→ 같은 index의 item끼리 tuple로 묶음

enumerate()
→ (index, value) 형태로 만듦
```

```text
[자주 나오는 조합]

dict(zip(a, b))
→ a를 key, b를 value로 하는 dict

dict(enumerate(x))
→ index를 key, item을 value로 하는 dict
```

---

# ⭐ map / filter / zip / enumerate 비교

| 함수            | 하는 일         | 결과 예시      |
| ------------- | ------------ | ---------- |
| `map()`       | 각각 변환        | `2 → 4`    |
| `filter()`    | 조건에 맞는 것만 선택 | `2, 4`     |
| `zip()`       | 같은 위치끼리 묶음   | `(1, 'a')` |
| `enumerate()` | 번호를 붙임       | `(0, 'a')` |

```text
map       → 변환
filter    → 선택
zip       → 묶기
enumerate → 번호 붙이기
```
