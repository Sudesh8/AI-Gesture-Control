import cv2
from ultralytics import YOLO
import numpy as np
import keyboard
from pprint import pprint

# define a video capture object
vid = cv2.VideoCapture(0)
# vid = cv2.VideoCapture(
# r"D:\CODES\Projects\forshorts\src\samples\WIN_20240723_21_03_12_Pro.mp4"
# )


### CONSTANTS
UP_BTN_PRESSED = False
DOWN_BTN_PRESSED = False
pts = np.array([[430, 88], [588, 88], [581, 247], [428, 251]])
pts = pts.reshape((-1, 1, 2))


# model load

model = YOLO("v23.pt")


# font
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (50, 50)

# fontScale
fontScale = 1

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.putText() method


def shorts(IMAGE):
    CLS_NAMES = ["down", "up"]

    data = {"rect": "", "score": "", "names": ""}

    result = model.predict(IMAGE)

    result = result[0]

    rect_list = result.boxes.xyxy

    if len(rect_list) == 0:
        return None
    else:

        score = result.boxes.conf

        # idx = np.argmax(np.array(score))

        try:
            temp_idx = int(result.boxes.cls)
        except Exception as e:
            print(f"ERROR::: {result.boxes.cls}")

        idx = int(result.boxes.cls.tolist()[0])
        # idx = 0

        predName = CLS_NAMES[idx]  # [idx]

        data["rect"] = rect_list

        data["score"] = np.max(score.tolist())

        data["names"] = predName

        print("######")
        pprint(data)
        print("######")

        return data


while True:

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.polylines(frame, [pts], True, (255, 0, 0), 4)

    # model prediction

    data = shorts(IMAGE=frame)
    if data is None:
        print("nonononnoononononoononoononononoononononno")

    else:
        print("----WORING----")
        for sublist in data["rect"]:
            x1, y1, x2, y2 = (
                int(sublist[0]),
                int(sublist[1]),
                int(sublist[2]),
                int(sublist[3]),
            )

            # Drawing rectangel
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)

            CX = int((x1 + x2) // 2)
            CY = int((y1 + y2) // 2)
            cv2.circle(frame, (CX, CY), 10, (255, 255, 0), -1)

            #### TEST PLYGON
            polyTest = cv2.pointPolygonTest(pts, (CX, CY), False)

            if polyTest >= 0:
                if UP_BTN_PRESSED:
                    cv2.circle(frame, (50, 50), 10, (0, 0, 255), -1)
                if DOWN_BTN_PRESSED:
                    cv2.circle(frame, (80, 80), 10, (255, 255, 0), -1)

                # if data["name"]=="down" &

                if data["score"] > 0.60:
                    mytext = f"{data['names']} | {round(data['score']*100,2)}%"
                    frame = cv2.putText(
                        frame,
                        mytext,
                        (x1 + 10, y1 - 10),
                        font,
                        fontScale,
                        color,
                        thickness,
                        cv2.LINE_AA,
                    )

                    if data["names"] == "down":
                        print("down")

                        # scorl the page
                        # keyboard.press_and_release("down")  #

                        if DOWN_BTN_PRESSED:
                            pass
                        else:
                            # keyboard.press_and_release("down")
                            DOWN_BTN_PRESSED = True
                            print("BUTTON_PRESSED---DOWN")
                            # frame = cv2.circle(frame, (50, 50), 3, (0, 0, 255), -1)

                    elif data["names"] == "up":
                        print("up")

                        if UP_BTN_PRESSED:
                            pass
                        else:
                            # keyboard.press_and_release("up")
                            UP_BTN_PRESSED = True
                            print("BUTTON_PRESSED---UP")
                            # cv2.circle(frame, (50, 50), 3, (0, 255, 0), -1)

                    else:
                        pass
            else:
                print(">>> NOT inside polygon")

    cv2.imshow("color image", frame)

    if cv2.waitKey(1) & 0xFF == ord("x"):
        break


vid.release()

cv2.destroyAllWindows()
