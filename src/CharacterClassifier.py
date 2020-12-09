import tensorflow as tf
import numpy as np

class CharacterClassifier:

    def __init__(self, image_width=28, image_height=28):
        self.model = tf.keras.models.Sequential()
        self.model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(image_width, image_height, 1)))
        self.model.add(tf.keras.layers.MaxPooling2D((2, 2)))
        self.model.add(tf.keras.layers.Flatten())
        self.model.add(tf.keras.layers.Dense(100, activation='relu'))
        self.model.add(tf.keras.layers.Dense(15, activation='softmax'))
        self.model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

    def set_model(self, model):
        self.model = model

    def fit(self, X_train, y_train, epochs=7):
        self.model.fit(X_train, y_train, epochs=epochs)

    def predict(self, x):
        prediction = self.model.predict(x)
        return np.argmax(prediction)