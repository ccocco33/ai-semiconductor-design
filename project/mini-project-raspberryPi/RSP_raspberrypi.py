
# 현재 문제점
# 학습한 이미지는 전체(배경까지 있는) 이미지를 기준으로 학습
# -> 이 코드는 손만 따로 떼써 판별 하다보니 낮은 신뢰도 또는 인식을 못하는 문제 발생
# =========================================================
# 1. 모듈 로딩
# =========================================================

import tflite_runtime.interpreter as tflite
from cvzone.HandTrackingModule import HandDetector

import numpy as np
import time
import cv2


# =========================================================
# 2. LiteRT 모델 설정
# =========================================================

modelPath = "best.tflite"

# modelPath = "best_int8.tflite"
# modelPath = "best_w8a32.tflite"

print("model path:", modelPath)

interpreter = tflite.Interpreter(
    model_path=modelPath
)

interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print(input_details)
print(output_details)

input_index = input_details[0]["index"]
output_index = output_details[0]["index"]

input_dtype = input_details[0]["dtype"]
output_dtype = output_details[0]["dtype"]

# 기존 모델 구조: (1,3,320,320)
height = input_details[0]["shape"][2]
width = input_details[0]["shape"][3]

print("model input shape:", (height, width))


# =========================================================
# 3. 기본 설정
# =========================================================

ansToText = {
    0: "scissors",
    1: "rock",
    2: "paper"
}

colorList = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255)
]

IMG_SIZE = 320

CONF_TH = 0.4
IOU_TH = 0.45


# =========================================================
# 4. 게임 및 배경 설정
# =========================================================

# 손 2개 탐지 후 가위바위보 인식 시간
GESTURE_RECOGNITION_TIME = 0.5

# 결과 표시 시간
RESULT_DISPLAY_TIME = 2.0

# BGR 색상
P1_BG_COLOR = (0, 255, 255)      # 노란색
P2_BG_COLOR = (144, 238, 144)    # 연두색
DRAW_BG_COLOR = (255, 0, 0)      # 파란색

BG_ALPHA = 0.45

# 손 Bounding Box 여백
HAND_OFFSET = 20


# =========================================================
# 5. HandDetector 설정
# =========================================================

# 3명 이상 감지 여부도 확인하기 위해 4개로 설정
detector = HandDetector(
    maxHands=4,
    detectionCon=0.5
)


# =========================================================
# 6. Letterbox
# =========================================================

def letterbox(
    img,
    new_shape=(320, 320),
    color=(114, 114, 114)
):

    h, w = img.shape[:2]

    nh, nw = new_shape

    r = min(nw / w, nh / h)

    new_w = int(w * r)
    new_h = int(h * r)

    resized = cv2.resize(
        img,
        (new_w, new_h)
    )

    pad_w = nw - new_w
    pad_h = nh - new_h

    pad_x = pad_w // 2
    pad_y = pad_h // 2

    padded = cv2.copyMakeBorder(
        resized,
        pad_y,
        pad_y,
        pad_x,
        pad_x,
        cv2.BORDER_CONSTANT,
        value=color
    )

    return padded, r, pad_x, pad_y


# =========================================================
# 7. YOLO 모델 입력 처리
# =========================================================

def makeModelInput(img):

    img_rgb = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2RGB
    )

    img_lb, r, pad_x, pad_y = letterbox(
        img_rgb,
        (IMG_SIZE, IMG_SIZE)
    )

    img = img_lb.astype(np.float32) / 255.0

    img = np.expand_dims(
        img,
        axis=0
    )

    img = np.transpose(
        img,
        (0, 3, 1, 2)
    )

    return img, r, pad_x, pad_y


# =========================================================
# 8. 손 crop 이미지에서 가위바위보 탐지
# =========================================================
# =========================================================
# 8. 손 crop 이미지에서 가위바위보 탐지
# =========================================================
def processCrop(crop, interpreter, input_details, output_details):

    # 이미지가 비어 있는 경우
    if crop is None or crop.size == 0:
        print("None img")
        return None

    # BGR -> RGB
    crop = cv2.cvtColor(
        crop,
        cv2.COLOR_BGR2RGB
    )

    # 이미지 크기 고정
    crop = cv2.resize(
        crop,
        (320, 320),
        interpolation=cv2.INTER_AREA
    )

    # Float32 변환 및 정규화
    crop = crop.astype(np.float32) / 255.0

    # HWC -> CHW
    crop = np.transpose(
        crop,
        (2, 0, 1)
    )

    # 배치 차원 추가
    crop = np.expand_dims(
        crop,
        axis=0
    )

    print(
        "processCrop input shape:",
        crop.shape
    )

    # 모델 입력
    interpreter.set_tensor(
        input_details[0]["index"],
        crop
    )

    # 추론
    interpreter.invoke()

    # 모델 출력
    output = interpreter.get_tensor(
        output_details[0]["index"]
    )

    # 출력 형태:
    # (1, 7, 2100)
    #
    # 배치 차원 제거
    # (7, 2100)
    raw = output[0]

    # (7, 2100) -> (2100, 7)
    raw = raw.transpose()

    # 클래스 점수 추출
    # 앞의 4개: bounding box 정보
    # 뒤의 3개: scissors, rock, paper
    class_scores = raw[:, 4:]

    # 각 탐지 후보의 최고 클래스 점수
    confidence = np.max(
        class_scores,
        axis=1
    )

    # 각 탐지 후보의 클래스 번호
    class_ids = np.argmax(
        class_scores,
        axis=1
    )

    # 가장 높은 confidence를 가진 후보 선택
    best_index = np.argmax(
        confidence
    )

    best_confidence = float(
        confidence[best_index]
    )

    best_class_id = int(
        class_ids[best_index]
    )

    # 신뢰도 임계값
    CONFIDENCE_THRESHOLD = 0.25

    # 신뢰도가 낮으면 인식 실패
    if best_confidence < CONFIDENCE_THRESHOLD:
        print("Low reliability: ",best_confidence)
        return None

    # 결과를 딕셔너리로 반환
    result = {
        "class_id": best_class_id,
        "confidence": best_confidence
    }

    print(
        "Detection result:",
        result
    )

    return result


# =========================================================
# 9. 손 Bounding Box를 이용한 crop
# =========================================================

def cropHand(frame, hand):

    x, y, w, h = hand["bbox"]

    frame_h, frame_w = frame.shape[:2]

    # Offset 적용
    x1 = max(0, x - HAND_OFFSET)
    y1 = max(0, y - HAND_OFFSET)

    x2 = min(frame_w, x + w + HAND_OFFSET)
    y2 = min(frame_h, y + h + HAND_OFFSET)

    crop = frame[y1:y2, x1:x2]

    return crop, (x1, y1, x2, y2)


# =========================================================
# 10. 화면 텍스트 출력
# =========================================================

def drawText(
    frame,
    text,
    position,
    font_scale=0.6,
    color=(255, 255, 255),
    thickness=2
):

    cv2.putText(
        frame,
        text,
        position,
        cv2.FONT_HERSHEY_SIMPLEX,
        font_scale,
        color,
        thickness
    )


# =========================================================
# 11. HandDetector Bounding Box 그리기
# =========================================================

def drawHandBox(
    frame,
    bbox,
    color=(255, 255, 255),
    label=""
):

    x1, y1, x2, y2 = bbox

    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        color,
        2
    )

    if label != "":

        drawText(
            frame,
            label,
            (x1, max(y1 - 8, 15)),
            0.45,
            color,
            2
        )


# =========================================================
# 12. 배경 색상 적용
# =========================================================

def applyBackgroundColor(
    frame,
    hand_boxes,
    mode="split",
    split_x=None,
    bg_color=None
):

    h, w = frame.shape[:2]

    overlay = frame.copy()

    # 손 영역 마스크
    hand_mask = np.zeros(
        (h, w),
        dtype=np.uint8
    )

    for bbox in hand_boxes:

        x1, y1, x2, y2 = bbox

        x1 = max(0, x1)
        y1 = max(0, y1)

        x2 = min(w, x2)
        y2 = min(h, y2)

        hand_mask[y1:y2, x1:x2] = 255

    # 좌우 분할
    if mode == "split":

        if split_x is None:

            split_x = w // 2

        overlay[:, :split_x] = P1_BG_COLOR

        overlay[:, split_x:] = P2_BG_COLOR

    # 단일 결과 색상
    elif mode == "winner":

        overlay[:, :] = bg_color

    # 원본 영상과 혼합
    blended = cv2.addWeighted(
        frame,
        1 - BG_ALPHA,
        overlay,
        BG_ALPHA,
        0
    )

    background_mask = (hand_mask == 0)

    frame[background_mask] = blended[background_mask]

    return frame


# =========================================================
# 13. 승패 판정
# =========================================================

def checkWinner(p1_gesture, p2_gesture):

    if p1_gesture == p2_gesture:

        return "무승부"

    if p1_gesture == "scissors":

        if p2_gesture == "paper":

            return "P1 승리"

        return "P2 승리"

    elif p1_gesture == "rock":

        if p2_gesture == "scissors":

            return "P1 승리"

        return "P2 승리"

    elif p1_gesture == "paper":

        if p2_gesture == "rock":

            return "P1 승리"

        return "P2 승리"

    return "판정 오류"


# =========================================================
# 14. 카메라 설정
# =========================================================

cap = cv2.VideoCapture(0)

cap.set(
    cv2.CAP_PROP_FRAME_WIDTH,
    320
)

cap.set(
    cv2.CAP_PROP_FRAME_HEIGHT,
    240
)

cap.set(
    cv2.CAP_PROP_BUFFERSIZE,
    1
)

cv2.namedWindow(
    "cam",
    cv2.WINDOW_NORMAL
)

cv2.resizeWindow(
    "cam",
    320 + 40,
    240 + 60
)


# =========================================================
# 15. 게임 상태 변수
# =========================================================

recognition_start = None

result_text = ""

result_time = None

result_bg_color = None

result_detections = []

result_hand_boxes = []

startTime = time.time()


# =========================================================
# 16. 메인 루프
# =========================================================

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:

        break

    frame_height, frame_width = frame.shape[:2]

    # -----------------------------------------------------
    # 1. HandDetector로 손 탐지
    # -----------------------------------------------------

    hands, _ = detector.findHands(
        frame,
        draw=False
    )

    # 왼쪽 -> 오른쪽 정렬
    hands = sorted(
        hands,
        key=lambda hand: hand["center"][0]
    )

    player_count = len(hands)

    # 손 Bounding Box 정보
    hand_boxes = []

    for hand in hands:

        x, y, w, h = hand["bbox"]

        x1 = max(0, x - HAND_OFFSET)
        y1 = max(0, y - HAND_OFFSET)

        x2 = min(
            frame_width,
            x + w + HAND_OFFSET
        )

        y2 = min(
            frame_height,
            y + h + HAND_OFFSET
        )

        hand_boxes.append(
            (x1, y1, x2, y2)
        )


    # =====================================================
    # 2. 결과 표시 중
    # =====================================================

    if result_text != "":

        elapsed_result = time.time() - result_time

        # 결과 배경 적용
        applyBackgroundColor(
            frame,
            result_hand_boxes,
            mode="winner",
            bg_color=result_bg_color
        )

        # 결과 텍스트
        drawText(
            frame,
            result_text,
            (10, 140),
            0.45,
            (255, 255, 255),
            2
        )

        # 결과 당시 손 영역 표시
        for bbox in result_hand_boxes:

            drawHandBox(
                frame,
                bbox,
                (255, 255, 255)
            )

        # 2초 경과
        if elapsed_result >= RESULT_DISPLAY_TIME:

            result_text = ""

            result_time = None

            result_bg_color = None

            result_detections = []

            result_hand_boxes = []

            recognition_start = None


    # =====================================================
    # 3. 일반 게임 상태
    # =====================================================

    else:

        # -------------------------------------------------
        # 플레이어 없음
        # -------------------------------------------------

        if player_count == 0:

            recognition_start = None

            drawText(
                frame,
                "Waiting for players...",
                (10, 30),
                0.6,
                (0, 255, 255),
                2
            )


        # -------------------------------------------------
        # 플레이어 1명
        # -------------------------------------------------

        elif player_count == 1:

            recognition_start = None

            drawText(
                frame,
                "Player 1 detected",
                (10, 30),
                0.6,
                (0, 255, 255),
                2
            )


        # -------------------------------------------------
        # 플레이어 2명
        # -------------------------------------------------

        elif player_count == 2:

            # P1, P2
            p1_hand = hands[0]
            p2_hand = hands[1]

            p1_bbox = hand_boxes[0]
            p2_bbox = hand_boxes[1]

            # 중간 X 좌표
            split_x = (
                p1_hand["center"][0]
                + p2_hand["center"][0]
            ) // 2

            # 좌우 배경 적용
            applyBackgroundColor(
                frame,
                hand_boxes,
                mode="split",
                split_x=split_x
            )

            # ---------------------------------------------
            # 손 탐지 후 인식 시작
            # ---------------------------------------------

            if recognition_start is None:

                recognition_start = time.time()

                # 0.5초 동안 인식
                # 이후 판정 진행

            elapsed_recognition = (
                time.time() - recognition_start
            )

            remaining = (
                GESTURE_RECOGNITION_TIME
                - elapsed_recognition
            )

            # ---------------------------------------------
            # 0.5초 인식
            # ---------------------------------------------

            if remaining > 0:

                drawText(
                    frame,
                    "Recognizing gesture...",
                    (20, 90),
                    0.55,
                    (0, 255, 255),
                    2
                )

                drawText(
                    frame,
                    f"{remaining:.1f} sec",
                    (100, 120),
                    0.55,
                    (0, 255, 255),
                    2
                )

            # ---------------------------------------------
            # 0.5초 후 판정
            # ---------------------------------------------

            else:
                print("let's start")

                # P1 손 crop
                p1_crop, p1_crop_bbox = cropHand(
                    frame,
                    p1_hand
                )
                # print("p1_cropHand: ",p1_crop, " / p1_crop_bbox: ",p1_crop_bbox)

                # P2 손 crop
                p2_crop, p2_crop_bbox = cropHand(
                    frame,
                    p2_hand
                )
                # print("p2_cropHand: ",p1_crop, " / p2_crop_bbox: ",p1_crop_bbox)

                # YOLO 가위바위보 분류
                p1_result = processCrop(
                    p1_crop,
                    interpreter,
                    input_details,
                    output_details
                )
                print("p1_result type:", p1_result)
                p2_result = processCrop(
                    p2_crop,
                    interpreter,
                    input_details,
                    output_details
                )
                print("p2_result type:", p2_result)
                # -----------------------------------------
                # 손은 탐지되었으나 분류 실패
                # -----------------------------------------

                if (
                    p1_result is None
                    or p2_result is None
                ):

                    result_text = "Gesture recognition failed"

                    result_bg_color = (0, 0, 0)

                else:

                    # 클래스 -> 손 모양
                    p1_gesture = ansToText[
                        p1_result["class_id"]
                    ]

                    p2_gesture = ansToText[
                        p2_result["class_id"]
                    ]

                    # 승패 판정
                    result = checkWinner(
                        p1_gesture,
                        p2_gesture
                    )

                    # 결과 색상
                    if result == "P1 승리":

                        result_bg_color = P1_BG_COLOR

                    elif result == "P2 승리":

                        result_bg_color = P2_BG_COLOR

                    elif result == "무승부":

                        result_bg_color = DRAW_BG_COLOR

                    else:

                        result_bg_color = (0, 0, 0)

                    # 결과 텍스트
                    result_text = (
                        f"P1: {p1_gesture} | "
                        f"P2: {p2_gesture} | "
                        f"{result}"
                    )

                # 판정 당시 손 영역 저장
                result_hand_boxes = [
                    tuple(bbox)
                    for bbox in hand_boxes
                ]

                result_detections = []

                # 결과 표시 시작
                result_time = time.time()


        # -------------------------------------------------
        # 플레이어 3명 이상
        # -------------------------------------------------

        else:

            recognition_start = None

            drawText(
                frame,
                "Only 2 players allowed",
                (10, 30),
                0.6,
                (0, 0, 255),
                2
            )


    # =====================================================
    # 4. 손 Bounding Box 표시
    # =====================================================

    # 결과 표시 중
    if result_text != "":

        for bbox in result_hand_boxes:

            drawHandBox(
                frame,
                bbox,
                (255, 255, 255)
            )

    # 일반 화면
    else:

        for i, hand in enumerate(hands):

            x, y, w, h = hand["bbox"]

            x1 = max(0, x - HAND_OFFSET)
            y1 = max(0, y - HAND_OFFSET)

            x2 = min(
                frame_width,
                x + w + HAND_OFFSET
            )

            y2 = min(
                frame_height,
                y + h + HAND_OFFSET
            )

            bbox = (x1, y1, x2, y2)

            if i == 0:

                label = "P1 (LEFT)"
                box_color = (0, 255, 255)

            elif i == 1:

                label = "P2 (RIGHT)"
                box_color = (144, 238, 144)

            else:

                label = f"Hand {i + 1}"
                box_color = (255, 255, 255)

            drawHandBox(
                frame,
                bbox,
                box_color,
                label
            )


    # =====================================================
    # 5. FPS 표시
    # =====================================================

    curTime = time.time()

    fps = 1 / max(
        curTime - startTime,
        1e-6
    )

    startTime = curTime

    drawText(
        frame,
        f"FPS: {fps:.1f}",
        (20, 50),
        0.6,
        (0, 255, 255),
        2
    )


    # =====================================================
    # 6. 카메라 화면 출력
    # =====================================================

    cv2.imshow(
        "cam",
        frame
    )

    key = cv2.waitKey(10)

    if key == ord("q"):

        break


# =========================================================
# 7. 종료
# =========================================================

cap.release()

cv2.destroyAllWindows()