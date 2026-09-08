6과 사용자 정의함수와 parameter

def 함수이름(parameter list): 함수 본문
return

global

다양한 함수 parameter
위치-키워드(pPK,pPKd): 위치나 키워드
위치 전용(pP):/ 앞의 파라미터는 모두 위치 전용 ex) abs(pP,/)
키워드 전용(pK,pKd): * 이후에 위치함
가변-위치(*pVP): 0개이상의 임의의 개수위치 파라미터 지정,tuple로 묶어서 전달
가변 키워드(**pVK): 파라미터에는 dict로 묶어서 전달

# 6과. 사용자 정의 함수와 Parameter

## 1. 사용자 정의 함수

사용자가 직접 만드는 함수를 **사용자 정의 함수(User Defined Function)**라고 한다.

기본 형태:

```python
def 함수이름(parameter_list):
    함수 본문
```

예:

```python
def add(a, b):
    return a + b
```

호출:

```python
print(add(10, 20))
```

출력:

```text
30
```

---

# 2. Parameter와 Argument

함수를 정의할 때 사용하는 변수를 **Parameter(매개변수)**라고 한다.

```python
def add(a, b):
    return a + b
```

여기서:

```text
a, b → parameter
```

함수를 호출할 때 실제로 전달하는 값을 **Argument(인자)**라고 한다.

```python
add(10, 20)
```

여기서:

```text
10, 20 → argument
```

### 정리

```text
함수 정의
def add(a, b):
          ↑
      parameter

함수 호출
add(10, 20)
     ↑  ↑
   argument
```

---

# 3. `return`

`return`은 함수의 **결과를 호출한 곳으로 돌려준다.**

```python
def add(a, b):
    return a + b
```

```python
x = add(10, 20)

print(x)
```

결과:

```text
30
```

`return`을 만나면 **함수의 실행이 종료**된다.

```python
def func():
    print(1)
    return
    print(2)

func()
```

출력:

```text
1
```

`return` 뒤의 `print(2)`는 실행되지 않는다.

---

## `return`이 없는 경우

```python
def func():
    print('hello')
```

이 함수는 값을 반환하지 않는다.

실제로는 `None`을 반환한다.

```python
x = func()

print(x)
```

출력:

```text
hello
None
```

---

# 4. `global`

함수 내부에서 **전역 변수(global variable)**를 수정하려면 `global`을 사용한다.

```python
x = 10

def func():
    global x
    x = 20

func()

print(x)
```

출력:

```text
20
```

---

## `global`이 필요한 이유

함수 밖에 있는 변수:

```python
x = 10
```

함수 안에서 단순히:

```python
def func():
    x = 20
```

라고 하면 **새로운 지역 변수 `x`**를 만드는 것이다.

```text
전역 x → 10

함수 내부 x → 20
```

둘은 서로 다른 변수이다.

반면:

```python
def func():
    global x
    x = 20
```

라고 하면 전역 변수 `x` 자체를 수정한다.

> ⭐
>
> ```text
> 함수 안에서 전역 변수의 값을 읽는 것
> → 보통 global 필요 없음
>
> 함수 안에서 전역 변수에 새로운 값을 대입
> → global 필요
> ```

---

# 5. 다양한 함수 Parameter

Python에서는 parameter의 종류에 따라 **어떤 방식으로 argument를 전달할 수 있는지** 제한할 수 있다.

크게 다음과 같이 구분한다.

```text
위치-키워드 Parameter
위치 전용 Parameter
키워드 전용 Parameter
가변-위치 Parameter
가변-키워드 Parameter
```

---

# 6. 위치-키워드 Parameter

가장 기본적인 parameter이다.

```python
def func(a, b=10):
    ...
```

위치 또는 키워드 방식으로 값을 전달할 수 있다.

### 위치로 전달

```python
func(1, 2)
```

### 키워드로 전달

```python
func(a=1, b=2)
```

둘 다 가능하다.

---

## 기본값 Parameter

```python
def func(a, b=10):
    return a + b
```

`b`를 전달하지 않으면 기본값 `10`이 사용된다.

```python
func(5)
```

→

```text
15
```

---

# 7. 위치 전용 Parameter

`/` 앞에 있는 parameter는 **위치로만 전달**할 수 있다.

```python
def func(a, b, /):
    return a + b
```

가능:

```python
func(10, 20)
```

불가능:

```python
func(a=10, b=20)  # ❌
```

즉:

```text
/ 앞의 parameter
→ 위치 전용
→ keyword 사용 불가능
```

---

## 예시

Python의 `abs()`와 같은 일부 내장 함수도 위치 전용 parameter를 사용한다.

개념적으로:

```python
abs(x, /)
```

처럼 생각할 수 있다.

따라서:

```python
abs(-10)
```

은 가능하지만,

```python
abs(x=-10)
```

은 사용할 수 없다.

---

# 8. 키워드 전용 Parameter

`*` 뒤에 오는 parameter는 **키워드로만 전달**할 수 있다.

```python
def func(*, a, b):
    return a + b
```

가능:

```python
func(a=10, b=20)
```

불가능:

```python
func(10, 20)  # ❌
```

즉:

```text
* 이후의 parameter
→ 키워드 전용
```

---

## 기본값도 가능

```python
def func(*, a=10, b=20):
    return a + b
```

```python
func()
func(a=30)
func(a=30, b=40)
```

모두 가능하다.

---

# 9. 위치 전용 + 위치/키워드 + 키워드 전용

세 종류를 한 번에 사용할 수도 있다.

```python
def func(a, b, /, c, d=10, *, e, f=20):
    ...
```

구조:

```text
a, b
 ↓
위치 전용

c, d
 ↓
위치 또는 키워드

e, f
 ↓
키워드 전용
```

예:

```python
func(1, 2, 3, e=5)
```

가능하다.

---

# 10. 가변-위치 Parameter `*pVP`

`*`를 붙인 parameter는 **0개 이상의 위치 argument를 받을 수 있다.**

```python
def func(*args):
    print(args)
```

호출:

```python
func(1, 2, 3, 4)
```

결과:

```text
(1, 2, 3, 4)
```

전달된 값들이 **tuple로 묶여서** parameter에 들어간다.

```python
def func(*args):
    print(type(args))
```

결과:

```text
<class 'tuple'>
```

---

## 0개도 가능

```python
func()
```

결과:

```text
()
```

즉:

```text
*args
→ 0개 이상의 위치 argument
→ tuple로 묶어서 전달
```

---

## 일반 Parameter와 같이 사용

```python
def func(a, *args):
    print(a)
    print(args)
```

호출:

```python
func(10, 20, 30, 40)
```

결과:

```text
10
(20, 30, 40)
```

첫 번째 값은 `a`가 받고, 나머지는 `args`가 받는다.

---

# 11. 가변-키워드 Parameter `**pVK`

`**`를 붙인 parameter는 **0개 이상의 키워드 argument**를 받을 수 있다.

```python
def func(**kwargs):
    print(kwargs)
```

호출:

```python
func(a=10, b=20, c=30)
```

결과:

```text
{'a': 10, 'b': 20, 'c': 30}
```

전달된 값들이 **dict로 묶여서** parameter에 들어간다.

```python
def func(**kwargs):
    print(type(kwargs))
```

결과:

```text
<class 'dict'>
```

즉:

```text
**kwargs
→ 0개 이상의 키워드 argument
→ dict로 묶어서 전달
```

---

# 12. `*args`와 `**kwargs` 비교

| Parameter  | 전달 방식        | 내부 자료형  |
| ---------- | ------------ | ------- |
| `*args`    | 위치 argument  | `tuple` |
| `**kwargs` | 키워드 argument | `dict`  |

예:

```python
def func(*args, **kwargs):
    print(args)
    print(kwargs)
```

호출:

```python
func(1, 2, 3, a=10, b=20)
```

결과:

```text
(1, 2, 3)
{'a': 10, 'b': 20}
```

---

# 13. Parameter 종류 전체 정리

```text
def func(a, b=10, /, c=20, *args, d=30, **kwargs):
    ...
```

각각의 의미:

```text
a, b
→ 위치 전용
→ / 앞

c
→ 위치 + 키워드
→ 일반 parameter

*args
→ 가변 위치
→ tuple

d
→ 키워드 전용
→ * 뒤

**kwargs
→ 가변 키워드
→ dict
```

---

# ⭐ Parameter 문법 핵심

```text
/ 앞
→ 위치 전용

일반 parameter
→ 위치 + 키워드

* 뒤
→ 키워드 전용

*args
→ 가변 위치
→ tuple

**kwargs
→ 가변 키워드
→ dict
```

### 한눈에 보기

```text
def func(
    a, b,       # 위치 전용
    /,
    c, d=10,    # 위치 + 키워드
    *args,      # 가변 위치
    e, f=20,    # 키워드 전용
    **kwargs    # 가변 키워드
):
    ...
```

---

# ⭐ 6과 핵심 암기

```text
[함수]

def 함수이름(parameter):
    함수 본문

return
→ 결과 반환
→ 함수 종료

global
→ 함수 내부에서 전역 변수에 대입할 때 사용
```

```text
[Parameter]

위치 전용
→ / 앞

위치-키워드
→ 일반 parameter

키워드 전용
→ * 뒤

가변-위치
→ *args
→ tuple

가변-키워드
→ **kwargs
→ dict
```

```text
[가변 Parameter]

*args
→ 위치 argument 여러 개
→ tuple로 받음

**kwargs
→ keyword argument 여러 개
→ dict로 받음
```

### ⭐ `/`와 `*`만 기억해도 큰 틀을 잡을 수 있다.

```text
        /
        ↓
[위치 전용] | [위치 + 키워드] | [키워드 전용]
                              ↑
                              *
```
