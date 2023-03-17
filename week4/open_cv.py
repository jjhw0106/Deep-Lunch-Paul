# import numpy as np
import cv2


# 경로에서 파일 읽기
# imageSrc = cv2.imread("C:/Users/jjhw0/Documents/Python/Image/ailee.jpg", cv2.IMREAD_UNCHANGED)
# 상대경로 오류 -> 현재경로가 open_cv가 아닌 작업경로가 기준이 된다.
# os.getcwd() -> 터미널 경로 확인
imageSrc = cv2.imread("week4/Image/ailee.jpg", cv2.IMREAD_UNCHANGED)
# =>왜 image/ailee로하면 에러가 나는지? 

# 이미지파일 윈도우로 띄우기
# cv2.imshow("original image", imageSrc)

### 이미지 사이즈 조절 ###
# 이미지를 축소하여 새로운 픽셀에 색상을 할당해주어야 하기 때문에
# 보간법을 통해 픽셀의 색상을 추정해야 한다. -> interpolation 속성.
cv2.imshow("original size", imageSrc)

# 1. 절대크기
# smallImg = cv2.resize(grayImg, dsize=(800,200), interpolation=cv2.INTER_AREA)

# 2. 상대크기
# dsize 기준으로 fx, fy가 각각 x와 y의 비율을 설정
# dsize가 (0,0)이면 원본과 동일한 크기
smallImg = cv2.resize(imageSrc, dsize=(0,0), fx =0.5, fy = 0.5, interpolation=cv2.INTER_LINEAR)


### 이미지 색상변경 ###
# OpenCV는 기본적으로 색상값을 BGR형태로 저장하고 있다.

# 흑백으로 변경
grayImg = cv2.cvtColor(smallImg, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image", grayImg)

### 특정 색상만 표현(hsv 방식) ###
# hsv로 변경 및 h(색상), s(채도), v(명도) 추출
hsvImg = cv2.cvtColor(smallImg,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsvImg)

# 마스크 설정
mask_skin = cv2.inRange(h,0,30)
mask_lip = cv2.inRange(h,150,200)

# 마스킹
# 두 이미지를 비교하여 마스크에 해당하는 색이 같은 위치에 들어간 부분만 표현
maskedImg = cv2.bitwise_and(hsvImg, hsvImg, mask = mask_skin+mask_lip)
maskedImg = cv2.cvtColor(maskedImg, cv2.COLOR_HSV2BGR)
cv2.imshow('h',maskedImg)

cv2.waitKey(0)
cv2.destroyAllWindows

# 그림 불러오기
# 그림의 rgb값 추출
