from PIL import ImageGrab, ImageOps
import numpy as np
import pyautogui
import time


class Coordinates:
    reply_btn = (480, 570)
    dinosaur = (157, 594)


def restartGame():
    pyautogui.click(Coordinates.reply_btn)
    pyautogui.keyDown('down')


def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print("Jump")
    time.sleep(0.18)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')


def imageGrab():
    box = (Coordinates.dinosaur[0] + 28, Coordinates.dinosaur[1],
           Coordinates.dinosaur[0] + 28 + 60, Coordinates.dinosaur[1] + 5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    array = np.array(grayImage.getcolors())
    print(array.sum())
    return array.sum()


def main():
    restartGame()
    while True:
        if imageGrab() != 547:
            pressSpace()
            time.sleep(0.1)


main()
