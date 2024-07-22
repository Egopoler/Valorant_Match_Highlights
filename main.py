from src.video_indexing import get_video_indexes, make_padding, connect_video
from src.video_maker import make_video, make_timelines
from src.change_device import get_device
import cv2
from ultralytics import YOLO
import numpy as np


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python main.py input_path output_path, use default values")

        mydevice = get_device()
        
        cap = connect_video("videos/video_example_1.mp4")

        model = YOLO("models/valmodel1.pt") 

        print("Model loaded")

        # To check if model is loaded correctly and video is working
        # time.sleep(2)

        indexes = get_video_indexes(model=model, cap=cap, mydevice=mydevice)

        print("default indexes:", indexes)
        pad_indexes = make_padding(indexes)
        print("indexes after padding:", pad_indexes)
        time_lines = make_timelines(pad_indexes)
        
        make_video("videos/video_example_1.mp4", "output/output_video.mp4", time_lines)
    else:
        mydevice = get_device()

        # I choose this video in data_videos folder for example, you can load your own video
        cap = connect_video(sys.argv[1])

        model = YOLO("models/valmodel1.pt") 

        print("Model loaded")

        # To check if model is loaded correctly and video is working
        # time.sleep(2)

        indexes = get_video_indexes(model=model, cap=cap, mydevice=mydevice)

        print("default indexes:", indexes)
        pad_indexes = make_padding(indexes)
        print("indexes after padding:", pad_indexes)
        time_lines = make_timelines(pad_indexes)

        make_video(sys.argv[1], sys.argv[2], time_lines)