from keras.models import load_model
import numpy as np
import cv2
import serial  


model = load_model('hola/keras_Model.h5')


ser = serial.Serial('COM6', 9600)  

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
cap = cv2.VideoCapture(0)
classes = ['H', 'O', 'L', 'FONDO', 'A']

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (224, 224))
    image_array = np.asarray(imgS)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    indexVal = np.argmax(prediction)

    cv2.putText(img, str(classes[indexVal]), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
    print(classes[indexVal])

    cv2.imshow('PERLA 2.1', img)
    cv2.waitKey(1)

    
    if classes[indexVal] == 'H':
        ser.write(b'h')
    if classes[indexVal] =='O':
        ser.write(b'o')
    if classes[indexVal] =='L':
        ser.write(b'l')
    if classes[indexVal] =='A':
        ser.write(b'a')        