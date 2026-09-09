# 2과. Linear Regression & Keras

## 1. Perceptron

Perceptron은 입력값에 Weight를 곱하고 Bias를 더한 뒤, Activation Function을 적용하여 출력값을 만드는 기본적인 인공신경망 구조이다.

### Perceptron 수식

$$
y = \sigma\left(\sum_{i=1}^{N} w_i x_i + b\right)
$$

- $x_i$ : 입력값
- $w_i$ : Weight(가중치)
- $b$ : Bias(편향)
- $\sigma$ : Activation Function
- $y$ : 출력값

### 계산 과정

```text
Input X
   ↓
X × W
   ↓
Σ (모두 더하기)
   ↓
+ Bias
   ↓
Activation Function
   ↓
Output

예:

X = np.array([1,2,3])
W = np.array([4,5,6])
B = 10

mul = W * X
s = np.sum(mul) + B

y = np.float32(s > 10)
W * X
= [4, 10, 18]

sum
= 32

+ B
= 42

42 > 10
→ True
→ 1.0
2. Linear Regression

Linear Regression(선형 회귀)은 입력과 출력의 관계를 직선으로 나타내고, 데이터에 가장 잘 맞는 직선을 찾는 방법이다.

기본 Hypothesis
$$ H(x) = Wx + B $$
$x$ : Input
$W$ : Weight
$B$ : Bias
$H(x)$ : 모델의 예측값

예를 들어 나이로 혈압을 예측한다면:

AGE
 ↓
H(x) = Wx + B
 ↓
혈압 예측값
3. Hypothesis

Hypothesis는 입력값을 이용하여 결과를 예측하는 함수이다.

def Hypothesis(x):
    return W*x + B

즉,

$$ H(x)=Wx+B $$

이다.

중요한 점은 W와 B를 처음부터 알고 있는 것이 아니라 학습을 통해 찾아간다는 것이다.

처음
W, B를 임의의 값으로 설정
        ↓
Hypothesis로 예측
        ↓
Cost 계산
        ↓
Gradient 계산
        ↓
W, B 수정
        ↓
반복
        ↓
좋은 W, B 찾기
4. Cost Function

모델의 예측값이 실제 정답과 얼마나 차이가 나는지를 측정하는 함수이다.

2과에서는 **Mean Squared Error(MSE)**를 사용한다.

MSE
$$ MSE = \frac{1}{N}\sum_{i=1}^{N}(H(x_i)-y_i)^2 $$
$H(x_i)$ : 예측값
$y_i$ : 실제 정답
$N$ : 데이터 개수

Python:

def Cost():
    return np.mean((Hypothesis(x_input) - labels)**2)
Cost의 의미
Cost가 크다
→ 예측이 정답과 많이 다르다

Cost가 작다
→ 예측이 정답과 가깝다

따라서 머신러닝의 목표는

Cost를 최소화하는 W와 B를 찾는 것

이다.

5. Gradient

Gradient는 Cost를 줄이기 위해 Weight와 Bias를 어느 방향으로 변경해야 하는지 알려주는 값이다.

grad_w, grad_b = Gradient(x_input, labels)

Gradient를 이용하여 W와 B를 업데이트한다.

W -= learning_rate * grad_w
B -= learning_rate * grad_b
6. Gradient Descent

Gradient Descent(경사 하강법)는 Gradient를 이용하여 Cost가 작아지는 방향으로 Parameter를 반복해서 수정하는 방법이다.

Parameter 업데이트
$$ W = W - \alpha \frac{\partial Cost}{\partial W} $$ $$ B = B - \alpha \frac{\partial Cost}{\partial B} $$
$W$ : Weight
$B$ : Bias
$\alpha$ : Learning Rate
Gradient : Cost의 변화 방향
핵심

Gradient는 Cost가 증가하는 방향을 알려주기 때문에,

현재 위치
   ↓
Gradient 방향의 반대 방향으로 이동
   ↓
Cost 감소

하게 된다.

7. Learning Rate

Learning Rate는 한 번의 학습에서 Parameter를 얼마나 크게 변경할지를 결정한다.

learning_rate = 0.005
너무 큰 경우
너무 크게 이동
→ 최솟값을 지나칠 수 있음
→ 학습이 불안정해질 수 있음
너무 작은 경우
조금씩 이동
→ 학습 속도가 느림

따라서 적절한 Learning Rate를 설정해야 한다.

8. Epoch

Epoch는 학습을 반복하는 횟수이다.

epochs = 5000

개념적으로:

1회
Hypothesis → Cost → Gradient → W/B 수정

2회
Hypothesis → Cost → Gradient → W/B 수정

3회
...

5000회

반복하면서 Cost를 줄여나간다.

9. Optimize Hypothesis

Optimize Hypothesis는

Cost가 최소가 되도록 Hypothesis의 Parameter인 W와 B를 최적의 값으로 찾아가는 것

을 의미한다.

전체 과정:

W, B 초기화
    ↓
Hypothesis
H(x) = Wx + B
    ↓
예측
    ↓
Cost 계산
    ↓
Gradient 계산
    ↓
W, B 업데이트
    ↓
반복
    ↓
Cost 감소
    ↓
최적의 W, B
    ↓
Optimized Hypothesis

즉,

$$ \boxed{\text{Cost를 최소화하는 } W,B \text{를 찾는다}} $$

가 핵심이다.

10. 혈압 예측 Linear Regression

예제에서는 나이(AGE)를 이용하여 혈압을 예측한다.

x_input = np.array([
    25,25,25,
    35,35,35,
    45,45,45,
    55,55,55,
    65,65,65,
    73,73,73
])

labels = np.array([
    118,125,130,
    118,126,123,
    120,124,130,
    122,125,130,
    127,130,130,
    125.5,130,138
])

입력:

AGE

출력:

BLOOD PRESSURE

구조:

AGE
 ↓
H(x) = Wx + B
 ↓
혈압

학습을 통해 AGE와 혈압의 관계를 가장 잘 나타내는 W와 B를 찾는다.

11. Multi-variable Linear Regression

입력 변수가 하나가 아니라 여러 개라면 Multi-variable Linear Regression이 된다.

예:

AGE
BMI
Weight
Exercise
    ↓
   모델
    ↓
혈압
Hypothesis

입력이 N개라면:

$$ H(x) = W_1x_1 + W_2x_2 + \cdots + W_Nx_N + B $$

즉,

N-variable = 입력 변수가 N개

이다.

12. Multi-output Linear Regression

출력이 여러 개일 수도 있다.

예:

AGE
BMI
 ↓
모델
 ├──→ HIGH
 └──→ LOW

이 경우 출력이 2개이다.

Input
→ HIGH
→ LOW

즉,

M-output = 출력이 M개

이다.

13. N-variable, M-output Linear Regression

Multi-variable과 Multi-output을 합친 일반적인 형태이다.

N개의 입력
     ↓
   Model
     ↓
M개의 출력

예제에서는:

Input = 2개
AGE
BMI

Output = 2개
HIGH
LOW

따라서

N = 2
M = 2

이다.

구조:

AGE ───┐
       ├──→ HIGH
BMI ───┤
       └──→ LOW
14. N-variable, M-output의 Hypothesis

입력이 여러 개이고 출력도 여러 개인 경우 각 출력마다 입력들의 Weight와 Bias를 이용하여 계산한다.

예를 들어 입력이 2개이고 출력이 2개라면:

$$ H_1 = W_{11}x_1 + W_{21}x_2 + B_1 $$ $$ H_2 = W_{12}x_1 + W_{22}x_2 + B_2 $$

즉,

          HIGH
         ↗
AGE ─────┤
         │
BMI ─────┤
         │
         └────→ LOW

각 출력마다 Weight와 Bias가 존재한다.

Parameter 개수

입력 2개 × 출력 2개:

Weight = 2 × 2 = 4개
Bias   = 2개
----------------
총 Parameter = 6개
15. Min-Max Scaling

입력값의 범위를 0~1 사이로 변환하는 방법이다.

x_min = np.min(x_input, axis=0)
x_max = np.max(x_input, axis=0)

x_input = (x_input-x_min)/(x_max-x_min)

공식:

$$ x' = \frac{x-x_{min}}{x_{max}-x_{min}} $$

예를 들어:

AGE : 25 ~ 73
BMI : 22 ~ 30

각각을 대략

0 ~ 1

범위로 변환한다.

사용하는 이유

입력 변수들의 값의 크기가 서로 크게 차이나는 경우 학습을 안정적으로 진행하는 데 도움을 준다.

16. Keras

앞에서는 Hypothesis, Cost, Gradient, Parameter 업데이트를 직접 작성했다.

def Hypothesis(x):
    ...

def Cost():
    ...

def Gradient(x, y):
    ...

W -= learning_rate * grad_w
B -= learning_rate * grad_b

하지만 입력과 출력이 많아지면 직접 구현하기가 복잡해진다.

Keras를 사용하면 이러한 과정을 간단하게 구현할 수 있다.

17. Keras Model 정의
model = tf.keras.models.Sequential([
    tf.keras.Input(shape=(2,)),
    tf.keras.layers.Dense(2)
])
Sequential

레이어를 순서대로 쌓아서 모델을 구성하는 방식이다.

Input
 ↓
Dense
 ↓
Output
Input(shape=(2,))

입력 변수가 2개라는 뜻이다.

AGE
BMI

즉:

shape=(2,)

→ 입력 데이터 하나당 값이 2개 들어온다.

Dense(2)

출력 뉴런을 2개 만든다는 뜻이다.

HIGH
LOW

따라서:

Input(2)
   ↓
Dense(2)
   ↓
Output(2)

이다.

18. Keras의 compile()
model.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.1),
    loss='mean_squared_error'
)

compile()은 모델을 어떤 방식으로 학습할지 설정하는 단계이다.

Loss
loss='mean_squared_error'

앞에서 배운 MSE Cost와 같은 개념이다.

예측값
  ↓
정답과 비교
  ↓
MSE 계산
  ↓
Loss
Optimizer
optimizer=tf.keras.optimizers.SGD(learning_rate=0.1)

Gradient Descent를 이용하여 Weight와 Bias를 업데이트하는 방법을 설정한다.

즉 앞에서 직접 작성했던:

W -= learning_rate * grad_w
B -= learning_rate * grad_b

와 같은 학습 과정을 Keras가 처리한다.

19. Keras의 fit()
history = model.fit(
    x_input,
    labels,
    epochs=1000
)

fit()은 실제 학습을 수행한다.

개념적으로 Keras가 다음 과정을 반복한다.

Input
 ↓
Prediction
 ↓
Loss 계산
 ↓
Gradient 계산
 ↓
Weight / Bias 업데이트
 ↓
반복

epochs=1000이면 이 학습을 1000번 반복한다.

20. history
history = model.fit(...)

학습 과정에서 발생한 Loss 등의 기록을 저장한다.

history.history['loss']

를 이용하면 Epoch별 Loss를 확인할 수 있다.

예:

Epoch 1    → Loss 500
Epoch 2    → Loss 300
Epoch 3    → Loss 180
...
Epoch 1000 → Loss 10

Loss가 감소하고 있다면 모델이 점점 데이터를 잘 맞추고 있다는 의미이다.

21. Loss Graph
loss = history.history['loss']
epochs = range(1, len(loss)+1)

plt.plot(epochs, history.history['loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()

학습이 진행되면서 Loss가 어떻게 변화하는지 그래프로 확인한다.

이상적인 경우:

Loss
 ↑
 │\
 │ \
 │  \
 │   \
 │    \____
 │
 └────────────→ Epoch

Loss가 점점 감소하여 안정되는 형태가 좋다.

22. predict()

학습이 끝난 모델을 이용하여 새로운 데이터를 예측할 때 사용한다.

H_x = model.predict(x_input)

또는 새로운 데이터를 넣어서:

model.predict(x_test)

를 사용할 수 있다.

23. 새로운 데이터 예측

예제:

x_test = tf.constant([
    [50.0, 25.0]
], dtype=tf.float32)

이는

AGE = 50
BMI = 25

인 새로운 데이터를 의미한다.

하지만 학습할 때 Min-Max Scaling을 사용했기 때문에 새로운 데이터도 똑같이 Scaling해야 한다.

def predict(x):
    return model.predict(
        (x-x_min)/(x_max-x_min)
    )

따라서:

새로운 데이터
[50, 25]
    ↓
Min-Max Scaling
    ↓
[Scaling된 AGE, Scaling된 BMI]
    ↓
학습된 Model
    ↓
[예측 HIGH, 예측 LOW]
24. 2과 전체 흐름
                    Perceptron
                        ↓
                 Wx + B 계산
                        ↓
               Linear Regression
                        ↓
                  Hypothesis
                  H(x) = Wx + B
                        ↓
                   Cost Function
                       (MSE)
                        ↓
                    Gradient
                        ↓
                Gradient Descent
                        ↓
                  W, B 업데이트
                        ↓
                      반복
                        ↓
                Optimized Hypothesis
                        ↓
              Multi-variable Linear
                    Regression
                        ↓
              Multi-output Linear
                    Regression
                        ↓
             N-variable, M-output
                        ↓
                     Keras
                        ↓
              ┌─────────┴─────────┐
              ↓                   ↓
           compile()           fit()
         Loss/Optimizer          학습
              │                   │
              └─────────┬─────────┘
                        ↓
                    predict()
                        ↓
                      예측
25. 핵심 개념 정리
개념	의미
Input	모델에 넣는 데이터
Label	실제 정답
Weight	입력의 영향력을 조절하는 값
Bias	전체적인 값을 조절하는 값
Hypothesis	예측을 위한 함수
Cost / Loss	예측이 얼마나 틀렸는지 나타내는 값
MSE	대표적인 Cost 계산 방법
Gradient	Cost를 줄이기 위한 방향을 알려주는 값
Gradient Descent	Gradient를 이용해 Parameter를 수정하는 방법
Learning Rate	한 번에 수정하는 크기
Epoch	학습 반복 횟수
Parameter	학습되는 Weight와 Bias
Min-Max Scaling	입력값을 0~1 범위로 변환
Dense	입력과 출력을 연결하는 Keras Layer
Optimizer	Parameter를 업데이트하는 방법
compile()	Loss와 Optimizer 등을 설정
fit()	모델을 실제로 학습
predict()	학습된 모델로 예측
26. 가장 중요한 개념

2과의 핵심은 다음 한 문장으로 정리할 수 있다.

머신러닝은 데이터를 이용하여 Cost를 최소화하도록 Weight와 Bias를 학습하고, 그 결과로 데이터를 잘 예측하는 Hypothesis를 만드는 과정이다.

그리고 Keras에서는 이 과정을 직접 구현하는 대신:

Hypothesis
Cost
Gradient
Parameter Update

를 Keras의

Dense
Loss
Optimizer
fit()

를 통해 쉽게 구현할 수 있다.

2과의 발전 과정
1 Variable + 1 Output
        ↓
      Wx + B
        ↓
Linear Regression
        ↓
Multi-variable
        ↓
Multi-output
        ↓
N-variable + M-output
        ↓
      Keras