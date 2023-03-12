import cv2
# 파이썬 버전 3.7 - 3.10 사이만 지원``
import mediapipe as mp

videoSrc = "C:/Users/jjhw0/Desktop/programming/assets/cv2_assets/before.mp4"
cap = cv2.VideoCapture(videoSrc)

# 1. 카메라(캠)일 경우
# 영상 프레임을 읽기 전 사이즈 조절
# w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# print('w=',w, 'h=',h)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 360)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,640)
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# 동영상파일일 경우d
# 영상 프레임을 읽어온 후 사이즈 조절
# flow : 영상을 프레임단위로 Read -> Resize -> resize된 이미지를 한장씩 보여줌
while True:
    retval, frame = cap.read()
    if not retval:
        break
    resized_frame = cv2.resize(frame, (180,320), interpolation=cv2.INTER_CUBIC)
    cv2.imshow("resized frame", resized_frame)
    cv2.waitKey(5) # 동영상의 프레임만큼 waitKey에 넣어줘야 동영상을 제대로 읽어온다
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap.release()

# mp_drawing = mp.solutions.drawing_utils