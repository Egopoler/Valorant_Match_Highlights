import cv2
from ultralytics import YOLO
import numpy as np
import torch
import time





def somebody_here(frame, model, mydevice="cpu"):
    results = model(frame, device=mydevice)

    result = results[0]

    bboxes = np.array(result.boxes.xyxy.cpu(), dtype="int")
    return len(bboxes) != 0


def connect_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if cap.isOpened():
        return cap
    print("Error: Could not open video")
    exit(0)


def get_video_info(cap):
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    video_length = total_frames // fps
    return int(fps), total_frames, int(video_length)



def make_padding(indexes, pad=1):
    pad_indexes = set()
    for index in indexes:
        for p in range(0, pad + 2):
            if index - p + 1 >= 1:
                pad_indexes.add(index - p + 1)
    return list(pad_indexes)


def close_player_bars(frame, height, width):
    start_x = int(0.15 * width)
    end_x = int(0.85 * width)
    start_y = int(0 * height)
    end_y = int(0.15 * height)
    cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (0, 0, 0), -1)

def close_map(frame, height, width):
    start_x = int(0 * width)
    end_x = int(0.25 * width)
    start_y = int(0 * height)
    end_y = int(0.4 * height)
    cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (0, 0, 0), -1)

def close_gun(frame, height, width):
    start_x = int(0.58 * width)
    end_x = int(1 * width)
    start_y = int(0.58 * height)
    end_y = int(1 * height)
    cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (0, 0, 0), -1)

def get_video_indexes(model, cap, mydevice="cpu"):
    
    ret, frame = cap.read()
    fps, total_frames, video_length = get_video_info(cap)
    indexes = set()
    index = 1
    height, width, _ = frame.shape
    while ret:

        close_player_bars(frame, height, width)
        close_map(frame, height, width)
        close_gun(frame, height, width)
        if somebody_here(frame, model, mydevice) and total_frames > index:
            indexes.add(index//fps)
            
        index += 1

        #cv2.imshow("Img", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
        ret, frame = cap.read()
        

    cap.release()
    cv2.destroyAllWindows()
    return list(indexes)





