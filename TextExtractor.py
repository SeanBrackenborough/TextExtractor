import pytesseract as pytesseract
from PIL import ImageGrab, Image
from pynput.mouse import Listener
import cv2
from GUI import Fullscreen

def on_click(x, y, _, pressed):
    # TODO Do this without global variables
    global mouse_pressed, mouse_released
    print('{} at {}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        mouse_released = x, y
        # End listener if we capture a release
        return False
    else:
        mouse_pressed = x, y
    return x, y


def text_extractor():
    # Listener for capturing press and release to simulate click and drag
    with Listener(on_click=on_click) as listener:
        listener.join()

    img = ImageGrab.grab(bbox=(mouse_pressed[0], mouse_pressed[1], mouse_released[0], mouse_released[1]))
    img.save("sc.png")
    cv_img = cv2.imread("sc.png")

    # Convert to grayscale for more accurate text detection
    grey = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("sc_grey.png", grey)

    # TODO How to package this up as a standalone app
    # TODO Currently have to: install tesseract, addd to PATH and include the following line
    pytesseract.pytesseract.tesseract_cmd = "D:\Program Files (x86)\Tesseract-OCR\\tesseract.exe"

    # Convert image to text
    text = pytesseract.image_to_string(Image.open("sc_grey.png"))
    print(text)

    # TODO Clean up png images at the end


if __name__ == '__main__':
    # screen = Fullscreen()
    text_extractor()
