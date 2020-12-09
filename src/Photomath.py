from CharacterClassifier import *
from CharacterDetector import *
from Solver import *
import cv2
import os
from keras.models import load_model


class Photomath:

    def __init__(self, character_detector, character_classifier, solver, number_of_classes=15, image_width=28, image_height=28):
        self.character_detector = character_detector
        self.character_classifier = character_classifier
        self.solver = solver
        self.number_of_classes = number_of_classes
        self.image_width = image_width
        self.image_height = image_height

    def load_data(self, directory_in_str, label, X_train, y_train):
        directory = os.fsencode(directory_in_str)
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            path = directory_in_str + '/' + filename
            img = cv2.imread(path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.resize(img, (self.image_width, self.image_height), interpolation=cv2.INTER_AREA)
            if X_train is None:
                X_train = img.reshape((1, self.image_width, self.image_height))
                y_train = np.array(label).reshape((1,))
            else:
                X_train = np.append(X_train, img.reshape((1, self.image_width, self.image_height)))
                y_train = np.append(y_train, np.array(label).reshape((1,)))
        return X_train, y_train

    def train_model(self, path_to_train_data, save_model=False):
        for i in range(self.number_of_classes):
            if i == 0:
                X_train, y_train = self.load_data(path_to_train_data + str(i), i, None, None)
            else:
                X_train, y_train = self.load_data(path_to_train_data + str(i), i, X_train, y_train)
        X_train = X_train.reshape(
            (int(len(X_train) / (self.image_width * self.image_height)), self.image_width, self.image_height))
        X_train = X_train.reshape((X_train.shape[0], self.image_width, self.image_height, 1))

        # X_train, y_train = shuffle(X_train, y_train)
        self.character_classifier.fit(X_train, y_train)

        if save_model:
            self.character_classifier.model.save('trained_model.h5')

    def load_classification_model(self, path_to_model):
        self.character_classifier.set_model(load_model(path_to_model))

    def calculate(self, path_to_image):
        self.character_detector.detect_bounding_boxes(path_to_image)

        image = cv2.imread(path_to_image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.character_detector.bounding_boxes.sort(key=lambda x: x[0])
        expression = ""

        for bounding_box in self.character_detector.bounding_boxes:
            cropped_image = image[bounding_box[1]:bounding_box[3], bounding_box[0]:bounding_box[2]]
            cropped_image = cv2.resize(cropped_image, (self.image_width, self.image_height), interpolation=cv2.INTER_AREA)
            cropped_image = cropped_image.reshape((1, self.image_width, self.image_height))
            cropped_image = cropped_image.reshape((cropped_image.shape[0], self.image_width, self.image_height, 1))
            y = self.character_classifier.predict(cropped_image)
            if y == 10:
                expression += '+'
            elif y == 11:
                expression += '-'
            elif y == 12:
                expression += '*'
            elif y == 13:
                expression += '/'
            elif y == 14:
                expression += '('
            elif y == 15:
                expression += ')'
            else:
                expression += str(y)
        self.expression = expression
        solver = Solver()
        try:
            solution = solver.solve(expression)
        except:
            solution = 'Wrong expression'
        return solution