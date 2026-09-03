python은 변수 타입,선언 x

[특수기능문자]
특수 기능을 하는 (\n,\,\t 등)문자들을 일반 문자로취급하려면 \를 한개 더 작성한다.
(ex) print('C:\\temp') => C:\temp

문자열 앞에 r-prefix를 쓰면 그건 다 문자열로 취급 
(ex) print(r'C:\temp') => C:\temp

[type]
print(type(int)) => <class 'type'>
print(type(10)) => <class 'int'>

[bool]
print(bool(1.5)) => True
print(bool(2)) => True
print(bool(0)) => False

print(bool("aa")) => True
print(bool(" ")) => True
print(bool("")) => false

[format 매서드]
a = '{0} + {0} = {2}'.format(2,3,2+2) 
{뒤에 번호 대입}
t = 'a = {a}, b = {b}',format(a=10,b=20)
{뒤에 변수 대입}

[f-perfix]
-> f'----'문자열로 {대상:형식}으로 인쇄형식 지정

name = 'young'
age = 10

s = f'{name}, {age+1}'
print (s) => young, 11
print(f'{age:>5} - {age:0>5}') =>   10 - 00010

# 1과. Python 기본 문법 정리

> Python은 **변수 선언 시 타입을 명시하지 않는다.**

---

## 1. 특수 기능 문자 (Escape Sequence)

문자열에서 `\`를 사용하면 특수한 기능을 하는 문자를 표현할 수 있다.

| 표현   | 의미        |
| ---- | --------- |
| `\n` | 줄바꿈       |
| `\t` | 탭         |
| `\\` | `\` 문자 자체 |

### `\`를 일반 문자로 사용하기

특수 기능을 하지 않고 `\` 자체를 출력하려면 `\`를 하나 더 작성한다.

```python
print('C:\\temp')
```

출력:

```text
C:\temp
```

### `r` prefix

문자열 앞에 `r`을 붙이면 **Escape Sequence를 해석하지 않고 그대로 문자열로 취급**한다.

```python
print(r'C:\temp')
```

출력:

```text
C:\temp
```

> `r` = **raw string**
>
> 특히 Windows 경로처럼 `\`가 많이 들어가는 문자열에 유용하다.

---

## 2. `type()`

`type()`은 **값의 자료형을 확인**할 때 사용한다.

```python
print(type(int))
```

출력:

```text
<class 'type'>
```

`int` 자체는 **클래스(class)**이므로 타입이 `type`이다.

```python
print(type(10))
```

출력:

```text
<class 'int'>
```

`10`은 정수이므로 타입이 `int`이다.

### 정리

```text
int        → type
10         → int
"hello"    → str
True       → bool
```

---

## 3. `bool()`

`bool()`은 값을 **True 또는 False로 변환**한다.

### 숫자

```python
print(bool(1.5))  # True
print(bool(2))    # True
print(bool(0))    # False
```

**0은 False**, 0이 아닌 숫자는 True이다.

```text
0          → False
1          → True
-1         → True
1.5        → True
```

### 문자열

```python
print(bool("aa"))  # True
print(bool(" "))   # True
print(bool(""))    # False
```

**빈 문자열 `""`만 False**이고, 문자열 안에 공백이라도 들어 있으면 True이다.

```text
"aa"   → True
" "    → True   # 공백 1개가 들어 있음
""     → False  # 아무것도 없음
```

> ⭐ 기억할 것
>
> `bool()`에서는 **"값이 비어 있으면 False"**라고 생각하면 편하다.
>
> * `0` → False
> * `""` → False
> * `" "` → True

---

## 4. `format()` 메서드

문자열 안에 값을 넣을 때 사용한다.

### 숫자 번호로 값 넣기

```python
a = '{0} + {0} = {2}'.format(2, 3, 2 + 2)
print(a)
```

출력:

```text
2 + 2 = 4
```

`{}` 안의 **번호(index)**가 `.format()`에 전달한 값의 순서를 의미한다.

```text
{0} → 첫 번째 값
{1} → 두 번째 값
{2} → 세 번째 값
```

따라서:

```python
'{0} + {0} = {2}'.format(2, 3, 4)
```

는

```text
2 + 2 = 4
```

가 된다.

---

### 변수 이름으로 값 넣기

```python
t = 'a = {a}, b = {b}'.format(a=10, b=20)

print(t)
```

출력:

```text
a = 10, b = 20
```

`{}` 안에 **변수(키워드) 이름**을 작성할 수도 있다.

```text
{a} → format(a=10)의 10
{b} → format(b=20)의 20
```

> ⚠️ 주의
>
> `format()`은 문자열 뒤에 `.`을 붙여 사용한다.
>
> ```python
> 'a = {a}, b = {b}'.format(a=10, b=20)
> ```

---

## 5. `f-string` (`f` prefix)

문자열 앞에 `f`를 붙이면 문자열 안에 **변수나 표현식의 값을 바로 넣을 수 있다.**

```python
name = 'young'
age = 10

s = f'{name}, {age + 1}'

print(s)
```

출력:

```text
young, 11
```

### 기본 형태

```python
f'{대상}'
```

`{}` 안에 변수나 계산식 등을 넣을 수 있다.

```python
f'{age}'
f'{age + 1}'
f'{name}'
```

---

## 6. f-string의 출력 형식 지정

`{}` 안에서 `:`을 사용하면 **출력 형식**을 지정할 수 있다.

```python
print(f'{age:>5} - {age:0>5}')
```

출력:

```text
   10 - 00010
```

### `:>5`

```python
f'{age:>5}'
```

* 전체 자리: `5`
* `>` : 오른쪽 정렬

```text
"   10"
```

### `:0>5`

```python
f'{age:0>5}'
```

* 전체 자리: `5`
* `>` : 오른쪽 정렬
* 빈 공간을 `0`으로 채움

```text
"00010"
```

### 정리

```text
:>5    → 5자리, 오른쪽 정렬
:0>5   → 5자리, 오른쪽 정렬 + 빈칸을 0으로 채움
```

---

# ⭐ 1과 핵심 암기

```text
type(10)       → <class 'int'>
type(int)      → <class 'type'>

bool(0)        → False
bool(1)        → True
bool("")       → False
bool(" ")      → True

'{0}'.format(10)
→ {0}에 첫 번째 값 대입

'{name}'.format(name='young')
→ {name}에 name 값 대입

f'{name}'
→ 변수 값을 문자열에 바로 삽입

f'{age:>5}'
→ 5자리 오른쪽 정렬

f'{age:0>5}'
→ 5자리 오른쪽 정렬 + 0으로 채움
```
