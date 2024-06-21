import cv2
from ultralytics import YOLO
import numpy as np
import mss
import torch


def get_optimal_size(sct):
    monitor = sct.monitors[1]  # Может отличаться в зависимости от вашего устройства
    monitor_width = monitor["width"]
    monitor_height = monitor["height"]
    return {"top": monitor_width // 40, "left": monitor_height // 40, "width": monitor_width // 40 * 19 , "height": monitor_height // 40 * 19} 


def get_device():
    """
    Returns the device to be used for computations.

    Returns:
        str: The device to be used for computations. Possible values are "mps", "cuda", or "cpu".
    """
    if torch.backends.mps.is_available():
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"

mydevice = get_device()



model = YOLO("models/valmodel1.pt")
print("Model loaded")


sct = mss.mss()

region = get_optimal_size(sct)

while True:
    
    screenshot = sct.grab(region)
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    results = model(frame, device=mydevice)

    result = results[0]

    bboxes = np.array(result.boxes.xyxy.cpu(), dtype="int")
    classes = np.array(result.boxes.cls.cpu(), dtype="int")
    print(bboxes)
    
    for cls,bbox in zip(classes, bboxes):
        x1, y1, x2, y2 = bbox
        if cls == 0:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, model.names[cls], (x1, y1 - 10), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 2)
        
    
    cv2.imshow("Img", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    

cv2.destroyAllWindows()









