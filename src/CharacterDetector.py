import cv2

class CharacterDetector:

    def detect_bounding_boxes(self, path_to_image):
        self.bounding_boxes = []
        image = cv2.imread(path_to_image)

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        threshold = cv2.adaptiveThreshold(blurred_image, 255, 1, 1, 11, 2)
        contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 50:
                [x, y, w, h] = cv2.boundingRect(contour)
                bounding_box = []
                bounding_box.append(x)
                bounding_box.append(y)
                bounding_box.append(x + w)
                bounding_box.append(y + h)
                self.bounding_boxes.append(bounding_box)