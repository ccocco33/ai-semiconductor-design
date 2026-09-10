import 해올거 해오기
↓
데이터 적기
(x_input,labels ...)
↓
min, max scaler 선언 해주기
↓
model 정의 하기
(dense 에서 actiation 설정 가능, 아래에서 설명)
↓
model compile(= 모델을 어떤 방식으로 학습시킬지 설정하는것)
(=optimizer,learning_rate, loss, metrics 정해주기, 아래에 각각 설명함)
↓
학습하기
(x_input, labels가지고 학습, epochs로 횟수정하기)
↓
plot
(그래프 그리기, 그냥 있으면 보기 좋음)
↓
min max scaler하면서 사용한식 함수 만들기
(우리가 넣어볼 데이터도 앞에서 훈련 시킬때 쓴 값 형태로 만들어 주는 거)
↓
traning 을 한 결과로 test
↓
결과 프린트! 끝!


# activation : 신경망 한층에서 계산한 결과를 한번 변환해주는 함수
(ex)Dense(1, activation='sigmoid')
입력
 ↓
Dense가 계산
 ↓
계산 결과 z
 ↓
sigmoid 함수
 ↓
최종 출력

(1) Sigmoid : 출력 범위 0~1, 이진 분류에서 사용
(2) Softmax : 출력의 합 1, 여러가지중 한개를 선택하는 다중 분류에서 사용
(3) ReLU : 음수 -> 0 , 양수 -> 그대로 , 은닉층에서 사용
(4) tanh : 출력 범위: -1~1

# optimizer : loss를 줄이기 위해 가중치(weight)를 어떻게 수정할지 정하는 방법
(ex)
(1) SGD : 경사 하강법(현재 gradient(기울기)를 보고 weight(가중치)를 조금씩 수정하는 방법)
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)
-> learning_rate : 한번 수정할 때 얼마나 크게 움직일지 결정

(2) Adam : * 가장 많이 사용 , 현재 gradient(기울기)만 보는게 아니라 이전 gradient(기울기)들의 정보도 이용해서 각 가중치를 얼마나 움직일지 조절
optimizer=tf.keras.optimizers.Adam(learning_rate=0.001)

(3) RMSprop: learning_rate를 조절하면서 학습

# loss : 모델의 예측이 정답과 얼마나 다른지를 숫자로 나타내는 함수
(ex)
(1) Mean Squared Error (MSE) : 예측값과 정답의 차이를 제곱해서 평균 , 주로 Regression(회귀) 에 사용
loss='mean_squared_error'  / loss=tf.keras.losses.MeanSquaredError()

(2) Binary Crossentropy : 0 또는 1을 분류하는 이진 분류
loss='binary_crossentropy' / Dense(1, activation='sigmoid')

(3) Categorical Crossentropy : 여러 개의 클래스를 분류할 때 사용 and 정답이 one-hot형태
예시. 고양이 강아지 말 3개중 하나를 선택하는 문제, 정답은 one-hot 형태 *one-hot : 한개만 1, 나머지 0  / [0,0,1]
고양이 -> [1,0,0]
강아지 -> [0,1,0]
말 -> [0,0,1]
loss='categorical_crossentropy'

(4) Sparse Categorrical Crossentropy : 여러 클래스를 분류할 때 사용 and 결과를 숫자 하나로 표현
예시. 
고양이 -> 0
강아지 -> 1
말 -> 2
loss='sparse_categorical_crossentropy'

# metrics : 학습을 잘하고있는지 확인하기위한 지표 / 그냥 사람이 확인하기위해 사용하는것 / 모델학습에 연관 없음 
(ex)
(1) Accuracy : 전체중 정답을 맞힌 비율 / 정확도
metrics=['accuracy']
(2) Precision : 모델이 1 이라고 예측한것중 실제로 1 인 비율
metrics=['precision']
(3) Recall : 실제로 1인 것들 중 모델이 얼마나 찾아냈는가
metrics=['recall']
(4) AUC : 0과 1을 얼마나 잘 구분하는지를 평가하는 지표
metrics=['AUC']

                 compile()
                    │
       ┌────────────┼────────────┐
       ↓            ↓            ↓
   optimizer      loss        metrics
       │            │            │
       ↓            ↓            ↓
  어떻게 고칠까?  얼마나 틀렸나?  얼마나 잘했나?
       │            │            │
      SGD          MSE         Accuracy
      Adam         BCE         Precision
      RMSprop      CCE         Recall
                   SCCE        AUC