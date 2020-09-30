from PIL import Image
import numpy as np
import tensorflow as tf
import juanjiNet


def train():
    model_save_path = './checkpoint/mnist.ckpt'

    '''
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')])
    model.load_weights(model_save_path)
    '''

    model = juanjiNet.ResNet18([2, 2, 2, 2])
    model.load_weights(model_save_path)
    return model


def prepic(image_path):
    img = Image.open(image_path)
    img = img.resize((28, 28), Image.ANTIALIAS)
    global img_arr
    img_arr = np.array(img.convert('L'))

    img_arr = 255 - img_arr
    img_arr = img_arr / 255.0
    img_arr = tf.reshape(img_arr, [-1, 28, 28, 1])


def predict():
    x_predict = img_arr
    result = train().predict(x_predict)
    pred = tf.argmax(result, axis=1)
    return pred


def result():
    a = predict()
    return int(a)
