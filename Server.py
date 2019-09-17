import keras
import cv2
import numpy as np

"""
Подключение обученной модели нейронной сети
"""
model = keras.models.load_model('SavedModels/model.h5')
model.compile('adam', 'categorical_crossentropy', metrics=['accuracy'])

"""
Функция предобработки изображения
"""
def preprocess(image):
    image = cv2.resize(image, (128, 72))
    if len(image.shape) == 3 and image.shape[-1] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        image = np.expand_dims(image, -1)
    elif len(image.shape) == 3 and image.shape[-1] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2GRAY)
        image = np.expand_dims(image, -1)
    if len(image.shape) == 2:
        image = np.expand_dims(image, -1)
    return image

"""
Функция аналитической обработки изображения. Данная функция предобрабатывает изображение, классифицирует с помощью
обученной модли нейронной сети и возвращает значение True в том случае, если на изображении был распознан огонь. В ином 
случае функция вернет значение False.
"""
def serv(image):
    x = preprocess(image)
    x_mass = [x]
    x_mass = np.array(x_mass)
    predictions = model.predict(x_mass)
    verdict = predictions.argmax()
    if verdict == 0:
        return True
    else:
        return False
