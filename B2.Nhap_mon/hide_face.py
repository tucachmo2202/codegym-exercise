from facenet_pytorch import MTCNN
import cv2

# Khởi tạo mô hình
mtcnn = MTCNN(thresholds= [0.65, 0.65, 0.65] ,keep_all=True)
print("Khoi tao model detection")

# Hàm dự đoán vị trí mặt từ ảnh
def detect_image(model, image):
    boxes, _ = model.detect(image)
    return boxes

# Đọc video từ OpenCV    
video_path = "/home/manhas/Videos/video_phong_van.mp4"
video_capture = cv2.VideoCapture(video_path)
assert video_capture.isOpened(), print("wrong path video")
while(video_capture.isOpened()):
    ret, frame = video_capture.read()
    h,w = frame.shape[:2]
    if not ret:
        break
    boxes = detect_image(mtcnn, frame)
    if boxes is None:
        continue
    for box in boxes:
        face_image = frame[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
#        face_image *= 0
        frame[int(box[1]):int(box[3]), int(box[0]):int(box[2])] = cv2.GaussianBlur(face_image,(w//7|1,h//7|1),0)
#        face_image = cv2.blur(face_image,(15,15))
    cv2.imshow("face", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()

