import cv2
import os

def images_to_video(input_folder, output_video, frame_rate):
    images = [img for img in os.listdir(input_folder) if img.endswith(".png")]
    images.sort()
    image_path = os.path.join(input_folder, images[0])
    img = cv2.imread(image_path)
    height, width, _ = img.shape

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(output_video, fourcc, frame_rate, (width, height))

    for image in images:
        image_path = os.path.join(input_folder, image)
        frame = cv2.imread(image_path)
        video_writer.write(frame)

    video_writer.release()

if __name__ == "__main__":
    input_images_folder_path = "q1_images"
    output_video_path = "q1_images/q1_video.mp4"
    desired_frame_rate = 30  

    images_to_video(input_images_folder_path, output_video_path, desired_frame_rate)

# import cv2
# import os

# def images_to_video(input_folder, output_video, frame_rate):
#     images = [img for img in os.listdir(input_folder) if img.endswith(".png")]
#     images.sort()

#     # Check if there are any images in the folder
#     if not images:
#         print(f"No images found in {input_folder}")
#         return

#     image_path = os.path.join(input_folder, images[0])
#     img = cv2.imread(image_path)

#     # Check if the first image is successfully read
#     if img is None:
#         print(f"Error reading the first image: {image_path}")
#         return

#     height, width, _ = img.shape

#     fourcc = cv2.VideoWriter_fourcc(*"mp4v")
#     video_writer = cv2.VideoWriter(output_video, fourcc, frame_rate, (width, height))

#     for image in images:
#         image_path = os.path.join(input_folder, image)
#         frame = cv2.imread(image_path)

#         # Check if the current image is successfully read
#         if frame is None:
#             print(f"Error reading the image: {image_path}")
#             continue

#         video_writer.write(frame)

#     video_writer.release()

# if __name__ == "__main__":
#     input_images_folder_path = "q1_images"
#     output_video_path = "q1_images/q1_video.mp4"
#     desired_frame_rate = 30  

#     images_to_video(input_images_folder_path, output_video_path, desired_frame_rate)
