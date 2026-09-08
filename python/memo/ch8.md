8과 Comprehensions

비교연산자
==,!=
is,is not : 객체의 id() 비교
in,not in
<,>,<=,>=
x if c else y : 조건식 c가 참이면 결과는 x, 거짓이면 y

논리연산자
not and or

all(it): it 의 모든 item들이 다 ture면 ture
any(it): it의 item들중 하나라고 true면 ture

gernerator Expression
(expression for target in iterable)
(ex) b = (x for x in t)

+ filter 기능
(expression for target in iterable if expression if ...)
(ex) b = (x*x for x in t if x >0 and x % 3)

Comprehensions: generator expression 을 이용해 container생성
list Comprehension: [expression for target in iterable if...]
set Comprehension: {expression for target in iterable if ...}
dict Comprehension: {key: value for target in iterable if ...}

다차원list 생성하는 표준식: a = [[] for i range(4)]

# 8과. Comprehensions

## 1. 비교 연산자

조건을 비교해서 `True` 또는 `False`를 만드는 연산자이다.

| 연산자      | 의미          | 예            |
| -------- | ----------- | ------------ |
| `==`     | 같다          | `a == 10`    |
| `!=`     | 같지 않다       | `a != 10`    |
| `is`     | 같은 객체인지 비교  | `a is b`     |
| `is not` | 다른 객체인지 비교  | `a is not b` |
| `in`     | 포함되어 있는지    | `x in t`     |
| `not in` | 포함되어 있지 않은지 | `x not in t` |
| `<`      | 작다          | `a < 10`     |
| `>`      | 크다          | `a > 10`     |
| `<=`     | 작거나 같다      | `a <= 10`    |
| `>=`     | 크거나 같다      | `a >= 10`    |

### `is`와 `==`의 차이

`==`는 **값이 같은지** 비교하고,

`is`는 **같은 객체인지(`id`)** 비교한다.

```python
a = [1, 2]
b = [1, 2]
c = a

print(a == b)   # True
print(a is b)   # False

print(a is c)   # True
```

```text
a == b  → 값이 같음
a is b  → 서로 다른 객체

a is c  → 같은 객체를 가리킴
```

> ⭐ 일반적으로 **값 비교는 `==`**, 객체 동일성 비교는 `is`를 사용한다.

---

# 2. 조건식 (삼항 연산자)

Python에서는 다음과 같은 형태로 간단한 조건문을 표현할 수 있다.

```python
x if c else y
```

의미:

```text
조건 c가 True  → x
조건 c가 False → y
```

예:

```python
a = 10

result = '양수' if a > 0 else '음수 또는 0'

print(result)
```

결과:

```text
양수
```

일반적인 `if`문으로 표현하면:

```python
if a > 0:
    result = '양수'
else:
    result = '음수 또는 0'
```

> ⭐ `x if c else y`
> → **조건이 참이면 x, 거짓이면 y**

---

# 3. 논리 연산자

논리 연산자는 여러 조건을 조합할 때 사용한다.

```text
not
and
or
```

| 연산자   | 의미              |
| ----- | --------------- |
| `not` | 반대              |
| `and` | 모두 True여야 True  |
| `or`  | 하나라도 True면 True |

### not

```python
not True
```

→ `False`

```python
not False
```

→ `True`

### and

```python
True and True    # True
True and False   # False
False and True   # False
False and False  # False
```

→ **둘 다 True여야 True**

### or

```python
True or True     # True
True or False    # True
False or True    # True
False or False   # False
```

→ **하나라도 True면 True**

---

# 4. all()

```python
all(iterable)
```

Iterable의 **모든 요소가 참(True)** 이면 `True`를 반환한다.

```python
print(all([True, True, True]))
# True

print(all([True, False, True]))
# False
```

숫자를 이용하면:

```python
print(all([1, 2, 3]))
# True

print(all([1, 0, 3]))
# False
```

### 핵심

```text
all → 모두 True인가?
```

```python
all(x > 0 for x in [1, 2, 3])
```

→ 모든 `x`가 0보다 큰지 검사

결과:

```text
True
```

---

# 5. any()

```python
any(iterable)
```

Iterable의 요소 중 **하나라도 참(True)** 이면 `True`를 반환한다.

```python
print(any([False, False, True]))
# True

print(any([False, False, False]))
# False
```

### 핵심

```text
any → 하나라도 True인가?
```

예:

```python
x = [1, 3, 5, 8]

print(any(n % 2 == 0 for n in x))
```

→ 짝수가 하나라도 있는지 검사

결과:

```text
True
```

---

# 6. Generator Expression

Generator Expression은 **generator를 만드는 표현식**이다.

기본 형태:

```python
(expression for target in iterable)
```

예:

```python
t = (1, 2, 3, 4, 5)

b = (x for x in t)
```

여기서 `b`는 리스트가 아니라 **generator 객체**이다.

```python
print(b)
```

→ generator 객체가 출력된다.

값을 꺼내려면:

```python
print(list(b))
```

결과:

```text
[1, 2, 3, 4, 5]
```

---

# 7. Generator Expression + 조건

`if`를 추가하면 조건에 맞는 값만 생성할 수 있다.

기본 형태:

```python
(expression for target in iterable if condition)
```

예:

```python
t = (-3, -2, -1, 0, 1, 2, 3)

b = (x * x for x in t if x > 0)

print(list(b))
```

결과:

```text
[1, 4, 9]
```

### 동작

```text
x > 0인 값만 선택
       ↓
1, 2, 3
       ↓
x * x 적용
       ↓
1, 4, 9
```

조건을 여러 개 사용할 수도 있다.

```python
b = (
    x * x
    for x in t
    if x > 0 and x % 3 == 0
)
```

→ `x > 0`이고 `3의 배수`인 값만 제곱한다.

---

# 8. Comprehension

**Comprehension**은 Iterable을 이용해서 새로운 Container를 간결하게 생성하는 문법이다.

대표적으로:

```text
List Comprehension
Set Comprehension
Dictionary Comprehension
```

이 있다.

> ⚠️ Generator Expression 자체는 **generator를 생성**하고,
> Comprehension은 **container를 생성**한다.

---

# 9. List Comprehension

기본 형태:

```python
[expression for target in iterable]
```

조건을 추가하면:

```python
[expression for target in iterable if condition]
```

예:

```python
a = [x * x for x in range(1, 6)]

print(a)
```

결과:

```text
[1, 4, 9, 16, 25]
```

일반적인 `for`문으로 작성하면:

```python
a = []

for x in range(1, 6):
    a.append(x * x)
```

List Comprehension을 사용하면:

```python
a = [x * x for x in range(1, 6)]
```

---

## 조건 추가

```python
a = [x for x in range(10) if x % 2 == 0]

print(a)
```

결과:

```text
[0, 2, 4, 6, 8]
```

→ 짝수만 선택한다.

---

# 10. Set Comprehension

기본 형태:

```python
{expression for target in iterable}
```

예:

```python
a = {x * x for x in range(1, 6)}

print(a)
```

결과:

```text
{1, 4, 9, 16, 25}
```

Set이므로 **중복은 제거**된다.

```python
a = {x % 3 for x in range(10)}

print(a)
```

결과:

```text
{0, 1, 2}
```

---

# 11. Dictionary Comprehension

기본 형태:

```python
{key: value for target in iterable}
```

예:

```python
a = {x: x * x for x in range(1, 6)}

print(a)
```

결과:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

즉,

```text
key   → x
value → x * x
```

이다.

조건도 추가할 수 있다.

```python
a = {x: x * x for x in range(10) if x % 2 == 0}

print(a)
```

결과:

```text
{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

---

# 12. Generator Expression vs Comprehension

형태가 거의 똑같기 때문에 구분하는 것이 중요하다.

### Generator Expression

```python
(x * x for x in range(5))
```

→ **generator 생성**

### List Comprehension

```python
[x * x for x in range(5)]
```

→ **list 생성**

### Set Comprehension

```python
{x * x for x in range(5)}
```

→ **set 생성**

### Dictionary Comprehension

```python
{x: x * x for x in range(5)}
```

→ **dict 생성**

### 한눈에 비교

| 문법                     | 결과        |
| ---------------------- | --------- |
| `(expression for ...)` | Generator |
| `[expression for ...]` | List      |
| `{expression for ...}` | Set       |
| `{key: value for ...}` | Dict      |

> ⭐ **괄호 모양으로 결과를 구분하는 것이 핵심**

---

# 13. 다차원 List 생성

2차원 리스트를 만들 때 다음과 같이 작성할 수 있다.

```python
a = [[] for i in range(4)]
```

결과:

```python
[[], [], [], []]
```

즉, 빈 리스트 `[]`를 4개 생성한다.

---

## ⚠️ `[[ ] ] * 4`와의 차이

다음 코드는 주의해야 한다.

```python
a = [[]] * 4
```

겉으로 보면:

```text
[[], [], [], []]
```

처럼 보이지만 **같은 리스트 객체를 4번 참조**한다.

따라서:

```python
a[0].append(10)
```

을 실행하면:

```text
[[10], [10], [10], [10]]
```

이 된다.

반면:

```python
a = [[] for i in range(4)]
```

에서는 각각 **서로 다른 빈 리스트**가 생성된다.

```python
a[0].append(10)
```

결과:

```text
[[10], [], [], []]
```

> ⭐ 다차원 리스트를 독립된 리스트로 만들 때는
> **`[[] for i in range(4)]`** 형태를 사용한다.

---

# 14. Comprehension 기본 패턴

Comprehension은 다음 구조를 기억하면 된다.

```text
[결과식 for 변수 in 반복대상 if 조건]
```

예:

```python
[x * 2 for x in t if x > 0]
```

순서대로 읽으면:

```text
t에서
 ↓
x를 하나씩 꺼내고
 ↓
x > 0이면
 ↓
x * 2를 결과에 넣는다
```

---

# ⭐ 핵심 암기

### 비교

```text
== / !=  → 값 비교
is / is not → 객체 동일성 비교
in / not in → 포함 여부
```

### 조건식

```python
x if c else y
```

```text
c가 True  → x
c가 False → y
```

### 논리

```text
not → 반대
and → 모두 True
or  → 하나라도 True
```

### all / any

```text
all → 전부 True인가?
any → 하나라도 True인가?
```

### Generator

```python
(expression for target in iterable)
```

→ generator

### Comprehension

```python
[expression for target in iterable if ...]
```

→ list

```python
{expression for target in iterable if ...}
```

→ set

```python
{key: value for target in iterable if ...}
```

→ dict

### 가장 중요한 형태

```text
Generator → ( )
List       → [ ]
Set        → { }
Dict       → {key: value}
```

### 다차원 List

```python
[[] for i in range(4)]
```

→ **서로 독립된 빈 리스트 4개**
