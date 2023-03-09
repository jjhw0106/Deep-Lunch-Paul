import cv2
# 파이썬 버전 3.7 - 3.10 사이만 지원``
import mediapipe as mp

videoSrc = "C:/Users/jjhw0/Desktop/programming/assets/cv2_assets/before.mp4"
cap = cv2.VideoCapture(videoSrc)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow('videoSrc', frame)


# mp_face_detection = mp.solutions.face_detection
# mp_drawing = mp.solutions.drawing_utils
# drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius = 1)
# with mp_face_detection.FaceDetection(
#     min_detection_confidence=0.5, model_selection=0) as face_detection:
#   for name, image in short_range_images.items():
#     # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
#     results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

#     # Draw face detections of each face.
#     print(f'Face detections of {name}:')
#     if not results.detections:
#       continue
#     annotated_image = image.copy()
#     for detection in results.detections:
#       mp_drawing.draw_detection(annotated_image, detection)
#     resize_and_show(annotated_image)

cv2.waitKey(5)
# mp_drawing = mp.solutions.drawing_utils