9과 제어문, 반복문

if 조건식: 수행문  - 조건식이 참이면 수행문 실행
if ~else,if~elif~else

pass문 : 고의로 비워두는것

for 문
for target in iterable: 수행문  - iterable에서 item을 순차적으로 target에 전달후 수행문 수행, item이 소진될때까지 반복
(ex) for i ,x in enumerate('ABCD'):
        print(i,x)
    ->결과
    0 A
    1 B
    2 C
    3 D

이중for문, for~else 문 (for 의 반복이 break으로 중단되면 else문 실행 x)
break,continue
break : 반복을 중지하고 loop 탈출
continue: 나머지 코드 수행을 그만두고 다시 for로 돌아간다.

while문
while 조건식: 수행문
(ex)
while True:
    i = input()
    if i !='X':
        print('Error')
    elif i =='X':
        print('Exit')
        break

# 9과. 제어문, 반복문

# 1. 제어문

제어문은 프로그램의 **실행 흐름을 제어**하는 문법이다.

대표적으로:

```text
조건문 → if
반복문 → for, while
```

---

# 2. if 문

조건식이 `True`이면 수행문을 실행한다.

```python
if 조건식:
    수행문
```

예:

```python
age = 20

if age >= 20:
    print('성인')
```

결과:

```text
성인
```

---

# 3. if ~ else

조건식이 참이면 `if`의 수행문을 실행하고,
거짓이면 `else`의 수행문을 실행한다.

```python
if 조건식:
    수행문1
else:
    수행문2
```

예:

```python
n = 10

if n > 0:
    print('양수')
else:
    print('0 또는 음수')
```

---

# 4. if ~ elif ~ else

여러 조건을 순서대로 검사할 때 사용한다.

```python
if 조건식1:
    수행문1
elif 조건식2:
    수행문2
elif 조건식3:
    수행문3
else:
    수행문4
```

예:

```python
score = 85

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')
```

결과:

```text
B
```

> ⭐ `if → elif → elif → else`는 **위에서부터 검사하며 처음으로 True가 된 블록 하나만 실행**된다.

---

# 5. pass 문

`pass`는 **아무 동작도 하지 않는 문장**이다.

즉, 문법적으로 수행문이 필요한 자리를 일부러 비워둘 때 사용한다.

```python
if n > 0:
    pass
```

주로 아직 구현하지 않은 부분을 임시로 만들어 놓을 때 사용한다.

```python
def func():
    pass
```

> ⭐ `pass`는 반복을 건너뛰는 것이 아니다.
> **그냥 아무것도 하지 않는다.**

---

# 6. for 문

`for`문은 Iterable의 요소를 **순서대로 하나씩 꺼내면서 반복**한다.

기본 형태:

```python
for target in iterable:
    수행문
```

동작:

```text
iterable에서 item 하나 꺼냄
        ↓
target에 전달
        ↓
수행문 실행
        ↓
다음 item
        ↓
item이 모두 소진될 때까지 반복
```

예:

```python
for x in [10, 20, 30]:
    print(x)
```

결과:

```text
10
20
30
```

---

# 7. for + enumerate()

`enumerate()`를 사용하면 **인덱스와 값을 동시에** 얻을 수 있다.

```python
for i, x in enumerate('ABCD'):
    print(i, x)
```

결과:

```text
0 A
1 B
2 C
3 D
```

### 동작

```text
enumerate('ABCD')
        ↓
(0, 'A')
(1, 'B')
(2, 'C')
(3, 'D')
```

그리고

```python
for i, x in ...
```

에서 튜플이 자동으로 unpacking된다.

```text
i ← 인덱스
x ← 값
```

> ⭐ `enumerate()` = **인덱스 + 값**

---

# 8. 이중 for문

`for`문 안에 또 다른 `for`문을 넣을 수 있다.

이를 **중첩 반복문**, **이중 for문**이라고 한다.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

결과:

```text
0 0
0 1
1 0
1 1
2 0
2 1
```

### 실행 구조

```text
i = 0
 ├─ j = 0
 └─ j = 1

i = 1
 ├─ j = 0
 └─ j = 1

i = 2
 ├─ j = 0
 └─ j = 1
```

> ⭐ 바깥쪽 `for`가 한 번 실행될 때마다 안쪽 `for`가 **끝까지 모두 실행**된다.

---

# 9. for ~ else 문

Python의 `for`문에는 `else`를 붙일 수 있다.

```python
for target in iterable:
    수행문
else:
    수행문
```

중요한 점은:

**반복이 정상적으로 끝나면 `else`가 실행된다.**

반대로 `break`로 반복이 중단되면 `else`는 실행되지 않는다.

### 정상적으로 반복 종료

```python
for i in range(3):
    print(i)
else:
    print('반복 종료')
```

결과:

```text
0
1
2
반복 종료
```

### break로 중단

```python
for i in range(3):
    print(i)
    if i == 1:
        break
else:
    print('반복 종료')
```

결과:

```text
0
1
```

`break`로 반복이 중단되었기 때문에 `else`가 실행되지 않는다.

> ⭐ `for ~ else`의 핵심:
>
> **break 없이 정상 종료 → else 실행**
> **break로 종료 → else 실행 X**

---

# 10. break

`break`는 현재 반복문을 **즉시 종료하고 반복문 밖으로 빠져나간다.**

```python
for i in range(10):
    if i == 3:
        break
    print(i)
```

결과:

```text
0
1
2
```

`i == 3`이 되는 순간 `break`가 실행되어 반복문이 종료된다.

### 핵심

```text
break
 ↓
현재 loop 종료
 ↓
loop 밖으로 탈출
```

---

# 11. continue

`continue`는 **현재 반복에서 남은 수행문을 건너뛰고 다음 반복으로 이동**한다.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

결과:

```text
0
1
3
4
```

`i == 2`일 때:

```text
continue
   ↓
현재 반복의 나머지 코드 건너뜀
   ↓
다음 반복
```

### break와 비교

```text
break
→ 반복문 자체를 종료

continue
→ 현재 반복만 건너뛰고 다음 반복
```

---

# 12. while 문

`while`문은 **조건식이 True인 동안 계속 반복**한다.

기본 형태:

```python
while 조건식:
    수행문
```

예:

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

결과:

```text
0
1
2
3
4
```

동작:

```text
조건 검사
 ↓
True → 수행문 실행
 ↓
다시 조건 검사
 ↓
True → 수행문 실행
 ↓
...
 ↓
False → 반복 종료
```

> ⭐ `for`는 **Iterable의 요소를 순회**할 때 많이 사용하고,
> `while`은 **조건이 유지되는 동안 반복**할 때 많이 사용한다.

---

# 13. while True + break

`while True`는 조건이 항상 `True`이므로 **무한 반복**이 된다.

따라서 일반적으로 특정 조건에서 `break`를 사용하여 종료한다.

```python
while True:
    i = input()

    if i != 'X':
        print('Error')
    elif i == 'X':
        print('Exit')
        break
```

실행 예:

```text
A
Error
B
Error
X
Exit
```

`X`가 입력되면:

```text
break
 ↓
while 반복 종료
```

---

# 14. 위 코드는 조금 더 간단하게 만들 수 있다

현재 코드:

```python
while True:
    i = input()

    if i != 'X':
        print('Error')
    elif i == 'X':
        print('Exit')
        break
```

여기서는 `i != 'X'`와 `i == 'X'`가 서로 반대 조건이므로 `else`를 사용하면 된다.

```python
while True:
    i = input()

    if i != 'X':
        print('Error')
    else:
        print('Exit')
        break
```

더 간단하게 작성하면:

```python
while True:
    i = input()

    if i == 'X':
        print('Exit')
        break

    print('Error')
```

이 형태가 특히 읽기 쉽다.

```text
X인가?
 ↓
Yes → Exit → break
 ↓ No
Error
 ↓
다시 입력
```

---

# 15. for와 while 비교

| 구분    | for                  | while               |
| ----- | -------------------- | ------------------- |
| 기본 기준 | Iterable 순회          | 조건식                 |
| 반복 횟수 | Iterable에 따라 결정      | 조건에 따라 결정           |
| 대표 형태 | `for x in iterable:` | `while condition:`  |
| 종료    | Iterable 소진          | 조건이 False           |
| 무한 반복 | 가능하지만 일반적이지 않음       | `while True`로 쉽게 구현 |

예를 들어 리스트를 순회한다면:

```python
for x in [1, 2, 3]:
    print(x)
```

조건이 만족되는 동안 반복한다면:

```python
while x < 10:
    print(x)
    x += 1
```

---

# 16. ⭐ 핵심 암기

### 조건문

```text
if
→ 조건이 True면 실행

if ~ else
→ True / False 두 경우

if ~ elif ~ else
→ 여러 조건 중 하나 선택
```

### pass

```text
pass
→ 아무것도 하지 않음
→ 문법적으로 수행문이 필요할 때 사용
```

### for

```python
for target in iterable:
    수행문
```

→ Iterable의 요소를 하나씩 꺼내 반복

### enumerate

```python
for i, x in enumerate(iterable):
```

→ **인덱스 + 값**

### break / continue

```text
break
→ 반복문 자체 종료

continue
→ 현재 반복만 건너뛰고 다음 반복
```

### for ~ else

```text
정상적으로 반복 종료 → else 실행
break로 반복 종료   → else 실행 X
```

### while

```python
while 조건식:
    수행문
```

→ 조건식이 `True`인 동안 반복

### 무한 반복

```python
while True:
    ...
    break
```

→ `break`가 실행될 때까지 반복
