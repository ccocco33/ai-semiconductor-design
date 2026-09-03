Iterable
여기 iterable 타입들 정리한거 이미지 넣고싶음

*set 은 중복제거함
{1,2,1,3} 이렇게 넣으면 {1,2,3}됨 (단, 순서는 모름)

insert(번호, item) : 위치에 '추가'
append(item):item 끝에 추가
add(): set 에서 추가 (위치 지정 x)

set의 item과 dict의 key는 유니크 해야함.
=> list, set, dict 사용 불가(수정가능하니까) / tupple 은 가능

[pack, unpack]
a = 2,3,4,5
=> a = (2,3,4,5) 알아서 pack 해서 튜플로 만든다.

이걸 이용해 swap 가능
=> a,b = b,a

iterable 타입은 모두 unpack가능
*a 로 사용
set - 순서 보장 x
dict - key 값만 unpack됨

부분 unpack
t = (10, 20, 30, 40, 50)
a, *b = t
a, *_, e, f = t

container 변환 함수
str(),tuple(),list(),dict(),set()
* dict는 key,value 쌍으로 받아야함

[lookup table]
n = 10
t = ('LOW', 'HIGH')
print(t[n >= 0])

d = {False : 'LOW', True : 'HIGH'}
print(d[n >= 0])

[range 함수]
range(stop) *stop보다 작을때까지
range(start,stop) 
range(start,stop,step)

# 1과. Iterable & 자료형 정리

## 1. Iterable

**Iterable(이터러블)**이란 `for`문 등을 통해 **하나씩 꺼낼 수 있는 객체**를 말한다.

대표적인 Iterable:

```text
str
list
tuple
set
dict
range
```

> 💡 `dict`를 순회하면 **key가 하나씩 나온다.**

### Iterable 자료형 비교

| 자료형     | 순서 | 중복       | 수정 | 특징            |
| ------- | -- | -------- | -- | ------------- |
| `str`   | O  | O        | X  | 문자열           |
| `tuple` | O  | O        | X  | 수정 불가능        |
| `list`  | O  | O        | O  | 가장 자유로운 자료형   |
| `set`   | X  | X        | O  | 중복 제거         |
| `dict`  | O* | Key 중복 X | O  | `key : value` |

* Python 3.7+에서는 `dict`가 **입력된 순서를 유지**한다.

---

# 2. Set

`set`은 **중복을 허용하지 않는 자료형**이다.

```python
s = {1, 2, 1, 3}

print(s)
```

출력:

```text
{1, 2, 3}
```

중복된 `1`이 자동으로 제거된다.

> ⚠️ `set`은 **인덱스로 위치를 지정할 수 없다.**
>
> ```python
> s[0]  # ❌
> ```

또한 set은 **순서를 기준으로 사용하면 안 된다.**

---

# 3. 값 추가 메서드

자료형에 따라 값을 추가하는 방법이 다르다.

### `list.insert()`

원하는 **위치에 추가**한다.

```python
a = [1, 2, 3]

a.insert(1, 10)

print(a)
```

출력:

```text
[1, 10, 2, 3]
```

형식:

```python
list.insert(위치, item)
```

---

### `list.append()`

리스트의 **맨 뒤에 추가**한다.

```python
a = [1, 2, 3]

a.append(10)

print(a)
```

출력:

```text
[1, 2, 3, 10]
```

형식:

```python
list.append(item)
```

---

### `set.add()`

set에 값을 추가한다.

```python
s = {1, 2, 3}

s.add(10)

print(s)
```

출력:

```text
{1, 2, 3, 10}
```

`set`은 위치가 없기 때문에 **위치를 지정해서 추가할 수 없다.**

```text
list.insert() → 원하는 위치에 추가
list.append() → 마지막에 추가
set.add()     → 위치 지정 없이 추가
```

---

# 4. Set의 item & Dict의 key

`set`의 원소와 `dict`의 key는 **중복될 수 없다.**

### Set

```python
{1, 2, 1, 3}
```

→

```python
{1, 2, 3}
```

### Dict

```python
d = {
    'a': 10,
    'a': 20
}
```

key가 중복되면 마지막 값이 남는다.

```python
{'a': 20}
```

---

## ⭐ Hashable

`set`의 원소와 `dict`의 key는 **hashable한 객체**여야 한다.

대표적으로:

```text
가능 ✅
int
float
str
tuple (단, 내부 원소도 hashable해야 함)

불가능 ❌
list
set
dict
```

예:

```python
s = {[1, 2]}       # ❌
d = {[1, 2]: 10}   # ❌
```

`list`, `set`, `dict`는 **수정 가능한(mutable) 객체**이기 때문에 set의 원소나 dict의 key로 사용할 수 없다.

반면:

```python
s = {(1, 2)}       # ✅
d = {(1, 2): 10}   # ✅
```

`tuple`은 수정할 수 없기 때문에 사용할 수 있다.

> ⚠️ 단, `tuple` 안에 `list` 같은 unhashable 객체가 들어 있으면 안 된다.
>
> ```python
> s = {(1, [2, 3])}  # ❌
> ```

---

# 5. Packing

여러 값을 하나의 변수에 묶는 것을 **Packing**이라고 한다.

```python
a = 2, 3, 4, 5
```

Python은 이를 자동으로 tuple로 묶는다.

```python
a = (2, 3, 4, 5)
```

즉,

```python
a = 2, 3, 4, 5

print(type(a))
```

→

```text
<class 'tuple'>
```

---

# 6. Unpacking

하나의 Iterable에 들어 있는 값을 **여러 변수로 나누어 받는 것**을 Unpacking이라고 한다.

```python
a = (2, 3, 4)

x, y, z = a

print(x)  # 2
print(y)  # 3
print(z)  # 4
```

---

## ⭐ Swap

Unpacking을 이용하면 두 변수의 값을 쉽게 교환할 수 있다.

```python
a = 10
b = 20

a, b = b, a
```

결과:

```text
a → 20
b → 10
```

실제로는 다음과 같은 과정으로 생각할 수 있다.

```python
a, b = (b, a)
```

오른쪽에서 `(b, a)`를 먼저 Packing하고, 왼쪽에서 Unpacking한다.

---

# 7. `*`를 이용한 Unpacking

`*`를 사용하면 **여러 개의 값을 하나의 변수로 받을 수 있다.**

```python
t = (10, 20, 30, 40, 50)

a, *b = t
```

결과:

```text
a → 10
b → [20, 30, 40, 50]
```

`*b`가 나머지 값을 모두 받아서 **list로 만든다.**

---

## 부분 Unpacking

```python
t = (10, 20, 30, 40, 50)

a, *b = t
```

```text
a → 10
b → [20, 30, 40, 50]
```

또는:

```python
a, *_, e, f = t
```

결과:

```text
a → 10
e → 40
f → 50
_ → [20, 30]
```

여기서 `_`는 **사용하지 않을 값을 받는 변수로 흔히 사용**한다.

> ⭐ `*`를 사용한 변수는 한 번의 unpacking에서 **하나만 존재할 수 있다.**

```python
a, *b, *c = t  # ❌
```

---

# 8. Iterable Unpacking

Iterable이라면 unpacking할 수 있다.

```python
a, b, c = [1, 2, 3]
a, b, c = (1, 2, 3)
a, b, c = {1, 2, 3}
a, b, c = "ABC"
```

### Dict는 주의!

`dict`를 unpacking하면 **key만 나온다.**

```python
d = {'a': 10, 'b': 20}

x, y = d
```

결과:

```text
x → 'a'
y → 'b'
```

`value`는 나오지 않는다.

```text
list   → item
tuple  → item
set    → item
str    → 문자
dict   → key
```

---

# 9. Container 변환 함수

자료형을 다른 자료형으로 변환할 수 있다.

```python
str()
tuple()
list()
dict()
set()
```

예:

```python
a = [1, 2, 3]

print(tuple(a))
print(set(a))
```

결과:

```text
(1, 2, 3)
{1, 2, 3}
```

---

## `dict()` 변환

`dict()`는 **key-value 쌍** 형태의 Iterable을 받아야 한다.

```python
a = [('a', 10), ('b', 20)]

d = dict(a)

print(d)
```

결과:

```text
{'a': 10, 'b': 20}
```

즉,

```text
('a', 10) → key='a', value=10
('b', 20) → key='b', value=20
```

> ⭐ `dict()`는 각각의 원소가 **2개의 값으로 구성된 쌍**이어야 한다.

---

# 10. Lookup Table

조건에 따라 값을 선택할 때 **Lookup Table**을 사용할 수 있다.

예를 들어:

```python
n = 10

t = ('LOW', 'HIGH')

print(t[n >= 0])
```

`n >= 0`의 결과는 `True`이다.

Python에서:

```text
False → 0
True  → 1
```

따라서:

```python
t[True]
```

는

```python
t[1]
```

과 같고,

```text
'HIGH'
```

가 출력된다.

---

## Dict를 이용한 Lookup Table

```python
n = 10

d = {
    False: 'LOW',
    True: 'HIGH'
}

print(d[n >= 0])
```

`n >= 0` → `True`

따라서:

```python
d[True]
```

→

```text
'HIGH'
```

### 정리

```text
조건 결과
False → 0
True  → 1
```

따라서 조건에 따라 값을 선택할 때:

```python
t[조건]
```

또는

```python
d[조건]
```

처럼 사용할 수 있다.

> ⭐ Lookup Table은 `if`문을 간단하게 표현할 때 유용하다.

---

# 11. `range()`

`range()`는 **일정한 범위의 정수들을 만들어 주는 객체**이다.

대표적인 형태는 3가지이다.

```python
range(stop)

range(start, stop)

range(start, stop, step)
```

---

## `range(stop)`

`0`부터 `stop` **미만**까지 생성한다.

```python
range(5)
```

→

```text
0, 1, 2, 3, 4
```

즉:

```text
0 ≤ 값 < 5
```

---

## `range(start, stop)`

`start`부터 `stop` **미만**까지 생성한다.

```python
range(2, 5)
```

→

```text
2, 3, 4
```

즉:

```text
2 ≤ 값 < 5
```

---

## `range(start, stop, step)`

`step`만큼 증가하면서 생성한다.

```python
range(1, 10, 2)
```

→

```text
1, 3, 5, 7, 9
```

### 감소도 가능

`step`을 음수로 만들면 감소한다.

```python
range(5, 0, -1)
```

→

```text
5, 4, 3, 2, 1
```

---

# ⭐ `range()` 핵심

```text
range(stop)
→ 0부터 stop 미만

range(start, stop)
→ start부터 stop 미만

range(start, stop, step)
→ start부터 stop 미만까지 step만큼 이동
```

**항상 `stop`은 포함되지 않는다.**

```python
range(5)
```

```text
0 1 2 3 4
          ↑
       5는 포함 X
```

---

# ⭐ 1과 핵심 암기

```text
[Iterable]
str, list, tuple, set, dict, range
→ 하나씩 꺼낼 수 있음

[Set]
중복 X
순서에 의존 X
add()로 추가
set의 원소는 hashable 해야 함

[Dict]
key 중복 X
dict를 unpacking하면 key만 나옴
key는 hashable 해야 함

[Packing]
a = 1, 2, 3
→ a = (1, 2, 3)

[Unpacking]
a, b, c = (1, 2, 3)

[Swap]
a, b = b, a

[* Unpacking]
a, *b = (1, 2, 3, 4)
→ a = 1
→ b = [2, 3, 4]

[Container 변환]
str()
list()
tuple()
set()
dict()

[Lookup Table]
False → 0
True  → 1

[range]
range(stop)
range(start, stop)
range(start, stop, step)

→ stop은 항상 포함하지 않음
```
