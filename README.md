# Valorant_bot
Valorant bot for deathmatch and training created for educational purposes


## How to start

#### 1. Make virtual enviroment

Mac OS:

> python -m venv venv

> source venv/bin/activate

Windows:

python -m venv venv
(in default terminal, not in powershell)
venv\Scripts\activate

#### 2. Install requirements.txt

> pip install -r requirements.txt


## How to test

You need to run *predict_video.py* in *src* folder.

> python src/predict_video.py

Also you can chage video for test.

You need write here path for your video.

> cap = connect_video("videos/video_example_1.mp4")