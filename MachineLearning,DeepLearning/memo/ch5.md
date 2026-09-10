# 5과. Multi Layer Perceptron (MLP)

## 1. MNIST Classification

MNIST는 손글씨 숫자 `0~9` 이미지 데이터셋이다.

- 이미지 하나의 크기: `28 × 28`
- 클래스: `0~9` → 총 10개
- 학습 데이터: `60,000개`
- 테스트 데이터: `10,000개`

```python
(train_data, train_labels), (test_data, test_labels) = mnist.load_data()
```

### 데이터 구조

```text
train_data  → (60000, 28, 28)
train_labels → (60000,)

test_data   → (10000, 28, 28)
test_labels → (10000,)
```

`train_data[i]`와 `train_labels[i]`는 서로 대응한다.

```text
train_data[i]   → 이미지
train_labels[i] → 그 이미지의 정답
```

---

## 2. Min-Max Scaling

MNIST의 픽셀값은 원래 `0~255` 범위이다.

```python
train_data = train_data / 255.0
test_data = test_data / 255.0
```

그러면 픽셀값이 `0~1` 범위로 변환된다.

```text
0   → 0.0
127 → 약 0.498
255 → 1.0
```

신경망 학습을 안정적으로 하기 위해 입력값의 크기를 조정한다.

---

# 3. Multi Layer Perceptron (MLP)

## 의미

**Multi Layer Perceptron = 여러 층으로 구성된 퍼셉트론**

단순한 구조:

```text
입력 → 출력
```

MLP:

```text
입력
 ↓
Hidden Layer
 ↓
Hidden Layer
 ↓
출력
```

즉 퍼셉트론을 여러 층으로 쌓은 구조이다.

---

## 4. MNIST에서의 MLP 구조

주석을 해제하면:

```python
model = tf.keras.models.Sequential([
    tf.keras.Input(shape=(28,28)),
    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(256, activation='sigmoid'),
    tf.keras.layers.Dense(256, activation='sigmoid'),

    tf.keras.layers.Dense(10, activation='softmax')
])
```

구조는:

```text
28 × 28
   ↓
Flatten
   ↓
784
   ↓
Dense(256)
   ↓
Dense(256)
   ↓
Dense(10)
   ↓
Softmax
   ↓
0~9 각각의 확률
```

---

# 5. Sequential

```python
tf.keras.models.Sequential([...])
```

Layer를 순서대로 쌓아 모델을 만드는 방법이다.

```text
Layer 1
   ↓
Layer 2
   ↓
Layer 3
```

---

# 6. Input

```python
tf.keras.Input(shape=(28,28))
```

모델에 들어오는 데이터의 형태를 지정한다.

MNIST 이미지 하나가:

```text
28 × 28
```

이므로 `shape=(28,28)`이다.

---

# 7. Flatten

```python
tf.keras.layers.Flatten()
```

2차원 데이터를 1차원으로 펼친다.

```text
28 × 28
   ↓
784
```

예를 들어:

```text
[[1,2,3],
 [4,5,6]]
```

↓

```text
[1,2,3,4,5,6]
```

MNIST에서는:

```text
28 × 28 = 784
```

따라서 Flatten 이후에는 이미지 하나가 784개의 입력값이 된다.

---

# 8. Dense

```python
tf.keras.layers.Dense(256, activation='sigmoid')
```

`Dense(256)`은 **뉴런 256개를 가진 층**이다.

각 뉴런은 이전 층의 모든 출력과 연결된다.

```text
784개의 입력
      ↓
┌───────────────────┐
│ Dense(256)        │
│                   │
│ ● ● ● ● ... ●     │
│   256개의 뉴런     │
└───────────────────┘
      ↓
256개의 출력
```

### 왜 256개를 사용하는가?

`784 → 10`으로 바로 분류하는 것보다 중간에 많은 뉴런을 두면 입력의 여러 패턴을 조합하고 변환할 수 있다.

개념적으로:

```text
픽셀 정보
   ↓
특징/패턴
   ↓
더 복잡한 특징
   ↓
숫자 분류
```

따라서:

```text
784 → 10
```

보다

```text
784 → 256 → 256 → 10
```

처럼 Hidden Layer를 추가하면 더 복잡한 패턴을 학습할 수 있다.

단, 뉴런과 층을 무조건 많이 추가하는 것이 항상 좋은 것은 아니다.

---

# 9. Hidden Layer

입력층과 출력층 사이에 있는 층이다.

```text
Input
  ↓
Hidden Layer  ← Dense(256)
  ↓
Hidden Layer  ← Dense(256)
  ↓
Output        ← Dense(10)
```

Hidden Layer는 입력 데이터를 여러 단계로 변환하고 특징을 조합하는 역할을 한다.

---

# 10. Activation Function

Dense에서 계산한 값을 그대로 다음 층으로 보내지 않고 활성화 함수를 적용할 수 있다.

```python
Dense(256, activation='sigmoid')
```

여기서 `sigmoid`가 활성화 함수이다.

---

## Sigmoid

수식:

```text
sigmoid(x) = 1 / (1 + e^(-x))
```

입력값을 `0~1` 사이의 값으로 변환한다.

대표적인 값:

```text
-5 → 약 0.007
 0 → 0.5
+5 → 약 0.993
```

즉:

```text
작은 음수 → 0에 가까움
0         → 0.5
큰 양수    → 1에 가까움
```

Sigmoid의 중요한 역할은 단순히 값을 `0~1`로 만드는 것뿐만 아니라 **비선형성**을 제공하는 것이다.

비선형성이 있어야 여러 층을 쌓았을 때 복잡한 패턴을 학습할 수 있다.

---

# 11. Output Layer

```python
tf.keras.layers.Dense(10, activation='softmax')
```

MNIST의 클래스가:

```text
0,1,2,3,4,5,6,7,8,9
```

총 10개이므로 출력 뉴런도 10개이다.

```text
뉴런 0 → 0일 확률
뉴런 1 → 1일 확률
...
뉴런 9 → 9일 확률
```

---

# 12. Softmax

Softmax는 출력값을 확률 형태로 변환한다.

예:

```text
0 → 0.01
1 → 0.02
2 → 0.01
3 → 0.03
4 → 0.02
5 → 0.01
6 → 0.01
7 → 0.85
8 → 0.02
9 → 0.02
```

모든 출력의 합은 `1`이 된다.

```text
0.01 + 0.02 + ... + 0.85 + ... = 1
```

가장 높은 확률을 가진 클래스를 최종 예측값으로 사용한다.

---

# 13. 현재 코드와 MLP 코드의 차이

현재 주석을 유지하면:

```python
Flatten()
Dense(10, activation='softmax')
```

구조:

```text
784 → 10
```

주석을 해제하면:

```python
Flatten()
Dense(256, activation='sigmoid')
Dense(256, activation='sigmoid')
Dense(10, activation='softmax')
```

구조:

```text
784 → 256 → 256 → 10
```

주석 처리된 두 개의 `Dense(256)`이 바로 Hidden Layer이다.

---

# 14. Forward Propagation

입력에서 출력 방향으로 계산하는 과정이다.

```text
입력
 ↓
Dense(256)
 ↓
Dense(256)
 ↓
Dense(10)
 ↓
Softmax
 ↓
예측
```

즉:

```text
Input → Output
```

방향으로 진행된다.

---

# 15. Loss

모델의 예측과 실제 정답이 얼마나 다른지 나타내는 값이다.

예:

```text
실제 정답: 7

모델:
7 → 0.95
```

이면 잘 예측한 것이다.

반대로:

```text
실제 정답: 7

모델:
7 → 0.02
3 → 0.80
```

이면 잘못 예측한 것이다.

이 차이를 Loss로 계산한다.

---

# 16. Compile

```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

모델을 **어떤 방식으로 학습할지 설정**하는 단계이다.

### optimizer

```python
optimizer='adam'
```

Gradient를 이용하여 가중치를 어떻게 수정할지 결정한다.

### loss

```python
loss='sparse_categorical_crossentropy'
```

예측값과 실제 정답 사이의 오차를 계산한다.

MNIST의 정답은:

```text
5
0
4
1
9
...
```

처럼 숫자 하나로 표현되어 있으므로 `sparse_categorical_crossentropy`를 사용한다.

### metrics

```python
metrics=['accuracy']
```

학습 결과를 확인하기 위한 지표이다.

Accuracy:

```text
맞힌 개수 / 전체 개수
```

---

# 17. Backpropagation

**역전파**

모델이 예측한 후 Loss가 계산되면, 그 오차를 출력층에서 입력 방향으로 전달하면서 각 가중치가 Loss에 얼마나 영향을 주는지 계산한다.

```text
Forward

입력
 ↓
Layer 1
 ↓
Layer 2
 ↓
Output
 ↓
Loss
```

Loss가 계산된 후:

```text
Backpropagation

Loss
 ↓
Output
 ↓
Layer 2
 ↓
Layer 1
```

방향으로 오차 정보를 전달한다.

---

# 18. Gradient

각 가중치를 조금 변경했을 때 Loss가 얼마나 변하는지를 나타내는 정보이다.

쉽게:

> "이 가중치를 어느 방향으로 얼마나 바꿔야 Loss가 줄어드는가?"

를 알려주는 정보라고 생각하면 된다.

---

# 19. Optimizer와 Backpropagation의 관계

둘은 같은 것이 아니다.

```text
Forward Propagation
        ↓
       예측
        ↓
     Loss 계산
        ↓
Backpropagation
        ↓
Gradient 계산
        ↓
Optimizer
        ↓
가중치 수정
```

### Backpropagation

→ Gradient를 계산하기 위해 오차를 역방향으로 전달

### Gradient

→ 가중치를 어느 방향으로 수정해야 하는지 알려주는 정보

### Optimizer

→ Gradient를 이용해서 실제 가중치를 수정

---

# 20. model.fit()

```python
history = model.fit(
    train_data,
    train_labels,
    epochs=5
)
```

실제 학습을 시작하는 함수이다.

기본적인 학습 흐름:

```text
Training Data
     ↓
Forward Propagation
     ↓
예측
     ↓
Loss 계산
     ↓
Backpropagation
     ↓
Gradient 계산
     ↓
Optimizer
     ↓
가중치 수정
     ↓
반복
```

---

# 21. Epoch

```python
epochs=5
```

전체 Training 데이터를 5번 반복해서 학습한다는 의미이다.

```text
1 epoch → 전체 학습 데이터 1회
2 epoch → 전체 학습 데이터 2회
...
5 epoch → 전체 학습 데이터 5회
```

---

# 22. Mini-batch

전체 데이터를 한 번에 처리하지 않고 작은 묶음으로 나누어 학습하는 방법이다.

예를 들어:

```text
Training data
60,000개

       ↓

[1~100]
[101~200]
[201~300]
...
```

`100개`씩 처리한다면 각각이 하나의 batch이다.

```text
100개
 ↓
Forward
 ↓
Loss
 ↓
Backpropagation
 ↓
Gradient
 ↓
가중치 수정
```

그리고 다음 batch를 처리한다.

---

# 23. Epoch와 Batch 관계

예를 들어:

```text
Training data = 60,000개
batch_size = 100
```

이라면:

```text
60,000 ÷ 100 = 600 batches
```

따라서:

```text
1 epoch
= 600개의 batch를 모두 처리
```

`epochs=5`라면:

```text
600 × 5 = 3,000번의 batch 처리
```

가 일어난다.

---

# 24. Validation

Validation은 **학습 중인 모델이 새로운 데이터에서도 잘 작동하는지 확인하기 위한 데이터**이다.

Training:

```text
Training Data
     ↓
모델 학습
     ↓
가중치 수정
```

Validation:

```text
Validation Data
     ↓
현재 모델 평가
     ↓
잘 학습되고 있는지 확인
```

예:

```python
model.fit(
    train_data,
    train_labels,
    epochs=5,
    validation_split=0.2
)
```

Training 데이터의 20%를 validation에 사용한다.

---

# 25. Training / Validation / Test

세 데이터를 구분한다.

```text
Training
→ 모델을 실제로 학습

Validation
→ 학습 중 모델 상태 확인

Test
→ 학습이 끝난 최종 모델의 성능 평가
```

전체적인 개념:

```text
Training Data
     ↓
 ┌───┴────┐
 ↓        ↓
Train   Validation
 ↓        ↓
학습     확인

학습 완료
     ↓
Test Data
     ↓
최종 성능 평가
```

---

# 26. Underfitting

**Underfitting = 과소적합**

모델이 학습 데이터를 충분히 학습하지 못한 상태이다.

```text
Train 성능 낮음
Test/Validation 성능 낮음
```

원인 예:

- 모델이 너무 단순함
- 학습이 부족함
- 학습 시간이 너무 짧음

비유:

```text
공부를 거의 안 함
 ↓
연습문제도 못 품
 ↓
새로운 문제도 못 품
```

---

# 27. Overfitting

**Overfitting = 과적합**

Training 데이터를 너무 잘 외워서 새로운 데이터에서는 성능이 떨어지는 상태이다.

예:

```text
Train accuracy      → 99~100%
Validation accuracy → 점점 감소
```

비유:

```text
연습문제와 답을 통째로 외움
 ↓
연습문제 → 매우 잘 맞힘
 ↓
새로운 문제 → 잘 못 품
```

---

# 28. Underfit / Overfit

`underfit`, `underfitting`은 거의 같은 의미이다.

```text
underfit / underfitting
→ 과소적합 상태/현상

overfit / overfitting
→ 과적합 상태/현상
```

---

# 29. Test

```python
model.evaluate(test_data, test_labels)
```

학습이 끝난 모델을 Test 데이터로 평가한다.

```text
학습
 ↓
최종 모델
 ↓
Test Data
 ↓
예측
 ↓
Test Labels와 비교
 ↓
Loss / Accuracy
```

---

# 30. %%time

```python
%%time
model.evaluate(test_data, test_labels)
```

Jupyter Notebook에서 해당 셀의 실행 시간을 측정한다.

모델의 학습 기능과는 직접적인 관계가 없다.

---

# 31. 전체 흐름

```text
MNIST 데이터
     ↓
28×28 이미지
     ↓
/255.0
     ↓
0~1 범위로 정규화
     ↓
Flatten
28×28 → 784
     ↓
┌─────────────────────┐
│        MLP          │
│                     │
│ 784 → 256 → 256 → 10│
└─────────────────────┘
     ↓
Softmax
     ↓
0~9 확률
     ↓
예측
     ↓
Loss 계산
     ↓
Backpropagation
     ↓
Gradient
     ↓
Optimizer(Adam)
     ↓
가중치 수정
     ↓
Mini-batch 반복
     ↓
Epoch 반복
     ↓
Validation으로 학습 상태 확인
     ↓
학습 완료
     ↓
Test Data
     ↓
최종 평가
```

---

# 32. 핵심 용어 한 줄 정리

| 용어 | 의미 |
|---|---|
| MLP | 여러 층의 퍼셉트론으로 구성된 신경망 |
| Layer | 신경망의 한 층 |
| Hidden Layer | 입력과 출력 사이의 중간층 |
| Dense | 이전 층의 모든 뉴런과 연결된 층 |
| Flatten | 2차원 데이터를 1차원으로 펼침 |
| Activation | 뉴런의 출력에 적용하는 함수 |
| Sigmoid | 값을 0~1 사이로 변환하는 비선형 함수 |
| Softmax | 여러 클래스의 출력값을 확률 형태로 변환 |
| Forward Propagation | 입력 → 출력 방향의 계산 |
| Loss | 예측과 정답의 차이를 나타내는 값 |
| Backpropagation | Loss의 영향을 뒤에서 앞으로 계산하는 과정 |
| Gradient | 가중치를 어느 방향으로 바꿀지 알려주는 정보 |
| Optimizer | Gradient를 이용해 가중치를 수정 |
| Epoch | 전체 학습 데이터를 한 번 학습 |
| Batch | 한 번에 처리하는 데이터 묶음 |
| Mini-batch | 전체 데이터를 작은 batch로 나누어 학습 |
| Validation | 학습 중 모델 성능을 확인하는 데이터 |
| Test | 학습 완료 후 최종 성능을 확인하는 데이터 |
| Underfitting | 모델이 충분히 학습하지 못한 상태 |
| Overfitting | 학습 데이터를 너무 외워 새로운 데이터에 약해진 상태 |
| `model.fit()` | 모델을 학습시키는 함수 |
| `model.evaluate()` | 모델의 성능을 평가하는 함수 |

---

## 핵심 구조

```text
MLP
→ 모델의 구조

Backpropagation
→ 모델을 학습시키는 과정

Optimizer
→ Gradient를 이용해 가중치를 수정하는 방법

Validation
→ 학습 중 잘 배우고 있는지 확인

Test
→ 학습이 끝난 후 최종 시험

Underfitting
→ 너무 못 배움

Overfitting
→ 너무 외움

Mini-batch
→ 데이터를 작은 묶음으로 나누어 학습
```
