# Python - zip, enumerate, unpacking, dict 변환 정리

## 1. `[튜플, 튜플]`을 `dict`로 변환하기

예를 들어 다음과 같은 리스트가 있다고 하자.

```python
x = [('apple', 100), ('banana', 200), ('kiwi', 300)]
```

이것을 dictionary로 바꾸고 싶다면:

```python
dict(x)
```

결과:

```python
{
    'apple': 100,
    'banana': 200,
    'kiwi': 300
}
```

### 왜 가능한가?

`dict()`는 **각 요소가 `[key, value]` 또는 `(key, value)` 형태**라면 dictionary로 변환할 수 있다.

즉,

```text
[
    ('apple', 100),
    ('banana', 200),
    ('kiwi', 300)
]
```

을

```text
key       value
 ↓          ↓
apple     100
banana    200
kiwi      300
```

으로 해석한다.

### ⭐ 핵심

```python
dict([('a', 10), ('b', 20)])
```

↓

```python
{'a': 10, 'b': 20}
```

---

# 2. `zip()`은 무엇인가?

`zip()`은 **여러 Iterable의 같은 위치에 있는 값들을 묶어준다.**

```python
zip(a, b)
```

예:

```python
a = ['apple', 'banana', 'kiwi']
b = [100, 200, 300]

zip(a, b)
```

개념적으로 다음과 같이 묶인다.

```text
apple   100
banana  200
kiwi    300
```

실제로 꺼내보면:

```python
print(list(zip(a, b)))
```

결과:

```python
[
    ('apple', 100),
    ('banana', 200),
    ('kiwi', 300)
]
```

즉,

```python
zip(a, b)
```

↓

```python
('apple', 100)
('banana', 200)
('kiwi', 300)
```

와 같은 **튜플들의 묶음**을 만들어낸다.

---

# 3. `zip()` + `dict()`

여기서 아주 중요한 연결이 나온다.

```python
a = ['apple', 'banana', 'kiwi']
b = [100, 200, 300]

dict(zip(a, b))
```

결과:

```python
{
    'apple': 100,
    'banana': 200,
    'kiwi': 300
}
```

과정을 풀어보면:

### ① `zip()`

```python
zip(a, b)
```

↓

```text
('apple', 100)
('banana', 200)
('kiwi', 300)
```

### ② `dict()`

```python
dict([
    ('apple', 100),
    ('banana', 200),
    ('kiwi', 300)
])
```

↓

```python
{
    'apple': 100,
    'banana': 200,
    'kiwi': 300
}
```

### ⭐ 핵심 공식

```python
dict(zip(keys, values))
```

→ **두 리스트를 dictionary로 합치는 대표적인 방법**

---

# 4. `zip()`에서 길이가 다르면?

기본적으로 **짧은 쪽에 맞춰서 끝난다.**

```python
a = ['a', 'b', 'c']
b = [1, 2]

print(list(zip(a, b)))
```

결과:

```python
[('a', 1), ('b', 2)]
```

`c`는 짝이 없기 때문에 사용되지 않는다.

```text
a       b
↓       ↓
a       1
b       2
c       없음  ← 사용 안 됨
```

---

# 5. `enumerate()`는 무엇인가?

`enumerate()`는 Iterable을 순회하면서 **인덱스와 값을 함께 제공**한다.

```python
enumerate(iterable)
```

예:

```python
x = ['apple', 'banana', 'kiwi']

print(list(enumerate(x)))
```

결과:

```python
[
    (0, 'apple'),
    (1, 'banana'),
    (2, 'kiwi')
]
```

즉,

```text
원래 값
apple
banana
kiwi

        ↓ enumerate()

(0, apple)
(1, banana)
(2, kiwi)
```

---

# 6. `enumerate()` + for

실제로는 이렇게 사용하는 경우가 많다.

```python
x = ['apple', 'banana', 'kiwi']

for i, value in enumerate(x):
    print(i, value)
```

결과:

```text
0 apple
1 banana
2 kiwi
```

여기서 중요한 것은 `enumerate()`가 만든 것이 **튜플**이라는 점이다.

```text
(0, 'apple')
(1, 'banana')
(2, 'kiwi')
```

그리고

```python
for i, value in ...
```

에서 각각 자동으로 unpacking된다.

```text
(0, 'apple')
 ↓       ↓
 i     value
```

---

# 7. `enumerate()`의 시작 번호 바꾸기

기본 시작 번호는 `0`이다.

```python
enumerate(x)
```

↓

```text
0 apple
1 banana
2 kiwi
```

시작 번호를 지정할 수도 있다.

```python
enumerate(x, 1)
```

↓

```text
1 apple
2 banana
3 kiwi
```

예:

```python
for i, value in enumerate(x, 1):
    print(i, value)
```

---

# 8. `zip()`과 `enumerate()`의 차이

둘 다 **튜플을 만들어낸다는 점** 때문에 헷갈릴 수 있다.

하지만 역할이 다르다.

### zip

**여러 Iterable을 서로 묶는다.**

```python
a = ['A', 'B', 'C']
b = [10, 20, 30]

list(zip(a, b))
```

↓

```python
[('A', 10), ('B', 20), ('C', 30)]
```

```text
A ── 10
B ── 20
C ── 30
```

### enumerate

**하나의 Iterable에 인덱스를 붙인다.**

```python
a = ['A', 'B', 'C']

list(enumerate(a))
```

↓

```python
[(0, 'A'), (1, 'B'), (2, 'C')]
```

```text
0 ── A
1 ── B
2 ── C
```

### ⭐ 한 줄 암기

```text
zip       → 여러 개를 묶음
enumerate → 번호를 붙임
```

---

# 9. Unpacking과 같이 생각하기

`zip()`과 `enumerate()`를 이해하려면 **unpacking**도 같이 알아야 한다.

다음 튜플이 있다고 하자.

```python
x = ('apple', 100)
```

이것을:

```python
a, b = x
```

라고 하면

```text
a → 'apple'
b → 100
```

이 된다.

이것이 **unpacking**이다.

그래서:

```python
for a, b in zip(x, y):
    ...
```

같은 코드가 가능한 것이다.

예:

```python
x = ['apple', 'banana', 'kiwi']
y = [100, 200, 300]

for name, price in zip(x, y):
    print(name, price)
```

`zip()`이:

```text
('apple', 100)
('banana', 200)
('kiwi', 300)
```

을 만들어주고,

```python
name, price = ('apple', 100)
```

처럼 자동으로 unpacking되는 것이다.

---

# 10. `[튜플, 튜플] → dict`와 `zip()`의 관계

이 부분이 가장 중요하다.

### 이미 튜플 형태라면

```python
x = [
    ('apple', 100),
    ('banana', 200),
    ('kiwi', 300)
]

dict(x)
```

바로 가능하다.

---

### 리스트가 따로 있다면

```python
names = ['apple', 'banana', 'kiwi']
prices = [100, 200, 300]
```

먼저 `zip()`으로 튜플을 만든다.

```python
zip(names, prices)
```

↓

```text
('apple', 100)
('banana', 200)
('kiwi', 300)
```

그 다음 `dict()`로 변환한다.

```python
dict(zip(names, prices))
```

↓

```python
{
    'apple': 100,
    'banana': 200,
    'kiwi': 300
}
```

### 따라서

```text
[튜플, 튜플, 튜플]
        ↓
      dict()
        ↓
      dict
```

반면

```text
[키, 키, 키] + [값, 값, 값]
        ↓
      zip()
        ↓
[튜플, 튜플, 튜플]
        ↓
      dict()
        ↓
      dict
```

---

# 11. `dict(enumerate())`

이것도 자주 나오는 형태다.

```python
x = ['apple', 'banana', 'kiwi']

dict(enumerate(x))
```

결과:

```python
{
    0: 'apple',
    1: 'banana',
    2: 'kiwi'
}
```

왜냐하면:

```python
enumerate(x)
```

↓

```text
(0, 'apple')
(1, 'banana')
(2, 'kiwi')
```

그리고 `dict()`가 이것을:

```text
key → value
```

로 해석하기 때문이다.

```text
0 → apple
1 → banana
2 → kiwi
```

### ⭐ 이것도 암기

```python
dict(enumerate(x))
```

→ **인덱스를 key로 사용하는 dictionary 생성**

---

# 12. `zip()`을 3개 이상 사용

`zip()`은 여러 개도 묶을 수 있다.

```python
name = ['A', 'B', 'C']
age = [20, 21, 22]
score = [90, 80, 70]

list(zip(name, age, score))
```

결과:

```python
[
    ('A', 20, 90),
    ('B', 21, 80),
    ('C', 22, 70)
]
```

즉,

```text
(A, 20, 90)
(B, 21, 80)
(C, 22, 70)
```

---

# 13. ⭐ 전체 연결 관계

이 네 가지를 하나의 흐름으로 이해하면 된다.

```text
                Iterable
                   │
        ┌──────────┴──────────┐
        ↓                     ↓
      zip()               enumerate()
        │                     │
        ↓                     ↓
 여러 Iterable을           인덱스 추가
 같은 위치끼리 묶음
        │                     │
        ↓                     ↓
 (a,1), (b,2), ...       (0,a), (1,b), ...
        │                     │
        └──────────┬──────────┘
                   ↓
                tuple
                   │
                   ↓
             unpacking 가능
             a, b = (a, 1)
                   │
                   ↓
                dict()
                   │
                   ↓
                dictionary
```

---

# 14. ⭐ 시험에서 자주 나오는 패턴

### ① 리스트 → 딕셔너리

```python
x = [('a', 1), ('b', 2)]

dict(x)
```

결과:

```python
{'a': 1, 'b': 2}
```

---

### ② 두 리스트 → 딕셔너리

```python
a = ['a', 'b', 'c']
b = [1, 2, 3]

dict(zip(a, b))
```

결과:

```python
{'a': 1, 'b': 2, 'c': 3}
```

---

### ③ 리스트에 번호 붙이기

```python
x = ['a', 'b', 'c']

list(enumerate(x))
```

결과:

```python
[(0, 'a'), (1, 'b'), (2, 'c')]
```

---

### ④ 번호를 key로 하는 dict

```python
dict(enumerate(x))
```

결과:

```python
{0: 'a', 1: 'b', 2: 'c'}
```

---

### ⑤ zip + for + unpacking

```python
a = ['A', 'B', 'C']
b = [10, 20, 30]

for x, y in zip(a, b):
    print(x, y)
```

결과:

```text
A 10
B 20
C 30
```

---

### ⑥ enumerate + for + unpacking

```python
a = ['A', 'B', 'C']

for i, x in enumerate(a):
    print(i, x)
```

결과:

```text
0 A
1 B
2 C
```

---

# ⭐ 최종 암기표

| 코드                         | 의미                    |
| -------------------------- | --------------------- |
| `dict([('a',1), ('b',2)])` | 튜플 리스트 → dict         |
| `zip(a,b)`                 | a와 b를 같은 위치끼리 묶음      |
| `list(zip(a,b))`           | zip 결과를 리스트로 확인       |
| `enumerate(a)`             | a에 인덱스를 붙임            |
| `list(enumerate(a))`       | enumerate 결과를 리스트로 확인 |
| `dict(zip(a,b))`           | 두 리스트 → dict          |
| `dict(enumerate(a))`       | 인덱스 → 값 형태의 dict      |
| `for x,y in zip(a,b)`      | 두 데이터를 동시에 순회         |
| `for i,x in enumerate(a)`  | 인덱스와 값을 동시에 순회        |
| `a,b = (1,2)`              | unpacking             |

## 🔥 진짜 핵심

```text
zip
→ 여러 개를 같은 위치끼리 묶는다.

enumerate
→ 인덱스와 값을 묶는다.

unpacking
→ 묶여 있는 값을 변수 여러 개로 나눈다.

dict
→ (key, value) 형태의 데이터를 dictionary로 만든다.
```

따라서 다음 코드를 보면:

```python
dict(zip(a, b))
```

무조건 이렇게 머릿속에서 풀어보면 된다.

```text
a = ['A', 'B', 'C']
b = [10, 20, 30]

       zip
        ↓
('A', 10)
('B', 20)
('C', 30)

       dict
        ↓
{'A': 10, 'B': 20, 'C': 30}
```

그리고:

```python
dict(enumerate(a))
```

는:

```text
a = ['A', 'B', 'C']

    enumerate
        ↓
(0, 'A')
(1, 'B')
(2, 'C')

       dict
        ↓
{0: 'A', 1: 'B', 2: 'C'}
```

이렇게 생각하면 된다.
