import cv2
import os

def video_to_images(input_video, output_folder):
    cap = cv2.VideoCapture(input_video)
    success, frame = cap.read()
    count = 0
    while success:
        image_path = os.path.join(output_folder, f"frame_{count:04d}.png")
        cv2.imwrite(image_path, frame)

        success, frame = cap.read()
        count += 1
    cap.release()

if __name__ == "__main__":
    input_video_path = "q1.mp4"
    output_folder_path = "q1_images"

    video_to_images(input_video_path, output_folder_path)

