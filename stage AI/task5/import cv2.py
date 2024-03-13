import cv2
import face_recognition

# Load pre-trained face detection model (Haar cascades)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load sample image with multiple faces
image_path = 'sample_image.jpg'
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces using Haar cascades
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Iterate over detected faces and draw rectangles around them
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the image with detected faces
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Load sample image for face recognition
image_path_2 = 'sample_image_2.jpg'
known_image = face_recognition.load_image_file(image_path_2)
known_encoding = face_recognition.face_encodings(known_image)[0]  # Encode known face

# Load another image to recognize faces
unknown_image = face_recognition.load_image_file('unknown_image.jpg')
unknown_encodings = face_recognition.face_encodings(unknown_image)

# Compare encodings to recognize faces
for unknown_encoding in unknown_encodings:
    results = face_recognition.compare_faces([known_encoding], unknown_encoding)
    if results[0]:
        print("Face Recognition: This is a known face.")
    else:
        print("Face Recognition: This is an unknown face.")
