# Valorant Match Highlights 

This project provides a script to process a Valorant match recording and extract only those moments where players are visible. This allows you to record your gameplay and reduce a long video to only the moments where you are in combat with other players.

## Table of Contents
- [Installation](#installation)
  - [Windows](#windows)
  - [Mac](#mac)
- [Usage](#usage)
  - [Windows](#windows-1)
  - [Mac](#mac-1)
- [Script Execution](#script-execution)

## Installation

### Windows
(Also you can just run script for windows, go to Usage->Windows and script install all libraries to venv)

1. Create a virtual environment:

(Use the default terminal, not PowerShell)
   
> python -m venv venv

2. Activate the virtual environment:

>venv\Scripts\activate

3. Install the necessary libraries:

If you have cuda install pytorch with it

you this to check: https://pytorch.org/get-started/locally/

for example

> pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

Then install requirements

> pip install -r requirements.txt



### Mac

1. Create a virtual environment:

> python -m venv venv

2. Activate the virtual environment:

> source venv/bin/activate

3. Install requirements.txt

> pip3 install -r requirements.txt


## Usage


### Windows

After installing the virtual environment and the necessary libraries, you can run the main script:


> python main.py input_path output_path

Or you can use the provided runner script:


> ./runner_for_windows.sh input_path output_path

### Mac

After installing the virtual environment and the necessary libraries, you can run the main script:

> python main.py input_path output_path

## Script Execution

The main.py script processes the input video, extracts only the moments where players are visible, and saves the result to the specified output path. The script takes two arguments: the path to the input video and the path to the output video.

Example usage:


> python main.py path/to/input_video.mp4 path/to/output_video.mp4

Or using the runner script on Windows:


> ./runner_for_windows.sh path/to/input_video.mp4 path/to/output_video.mp4


for test I upload video in videos/video_example_1.mp4, you can save it to output folder

> python main.py videos/video_example_1.mp4 output/output_video.mp4