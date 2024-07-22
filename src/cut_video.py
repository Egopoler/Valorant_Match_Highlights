import cv2
import os
import shutil


def clear_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)

def save_frames(video_path, output_folder, interval):

    # Создаем папку для сохранения кадров, если она не существует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    else:
        clear_folder(output_folder)


    # Открываем видео
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Ошибка открытия видеофайла")
        return

    # Получаем количество кадров в секунду (fps) и общее количество кадров
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Вычисляем количество кадров для заданного интервала времени
    frame_interval = int(fps * interval)

    frame_count = 0
    saved_frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_frame_count += 1

        frame_count += 1

    cap.release()
    print(f"Сохранено {saved_frame_count} кадров в папку {output_folder}")

# Пример использования
video_path = "videos/video_example_1.mp4"
output_folder = "output_frames"
interval = 1  # Интервал в секундах

save_frames(video_path, output_folder, interval)
