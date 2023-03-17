# CONCEPTION
- 동영상을 프레임 단위로 불러와 이미지 별 로직을 수행한 뒤 화면을 보여줌

# 1. 영상 불러오기
``` python
videoSrc = "C:/Users/jjhw0/Desktop/programming/assets/cv2_assets/before.mp4"
cap = cv2.VideoCapture(videoSrc)
 ```

# 2. 사이즈 조절하기
## 2-1. 카메라(캠)일 경우
- 영상 프레임을 읽기 전 사이즈 조절
    ``` python
    # 원본 파일의 사이즈
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print('w=',w, 'h=',h)
    # resize할 해상도 set
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 360)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    while True:
        retval, frame = cap.read()
        
        if not retval:
            break

        cv2.imshow("resized frame", resized_frame)
        cv2.waitKey(24) # 동영상의 프레임만큼 waitKey에 넣어줘야 동영상을 제대로 읽어온다
    
    cap.release() 
    ```

## 2-2 동영상파일일 경우
- 동영상 파일의 frame을 한 장씩 read -> resize -> show 실행한다.
- waitKey() : waitKey는 입력을 기다리거나, 매개변수에 들어간 숫자ms만큼 delay를 준다.
- 여기서 영상의 프레임만큼 숫자를 주는 의미는 1초당 24프레임의 속도로 영상을 틀어 준다는 의미 
- => Question (24ms만큼의 delay를 주는 것과 1초에 24프레임을 준다는게 어찌 같은말인지?)
- 작은 숫자를 주면 영상이 빨라지고, 큰 숫자를 주면 영상이 느려짐
    ``` python 
    while True:
        retval, frame = cap.read()
        if not retval:
            break
        resized_frame = cv2.resize(frame, (180,320), interpolation=cv2.INTER_CUBIC)
        cv2.imshow("resized frame", resized_frame)
        cv2.waitKey(24) # 동영상의 프레임만큼 waitKey에 넣어줘야 동영상을 제대로 읽어온다
    
    cap.release() 
    ```