import cv2
import os

def capture_images(output_folder, num_images=10):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    cap = cv2.VideoCapture(0)  
    if not cap.isOpened():
        print("Error while opening Cam.")
        return
    for _ in range(num_images):
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Webcam Feed", frame)
        image_path = os.path.join(output_folder, f"captured_frame_{_ + 1}.png")
        cv2.imwrite(image_path, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    output_folder_path = "q2_output"
    number_of_images_to_capture = 10
    capture_images(output_folder_path, number_of_images_to_capture)
