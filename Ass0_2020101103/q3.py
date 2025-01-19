import cv2
import numpy as np

def chroma_keying(foreground_video_path, background_video_path, output_path, color_key=(0, 255, 0)):
    foreground_cap = cv2.VideoCapture(foreground_video_path)
    background_cap = cv2.VideoCapture(background_video_path)
    width = int(foreground_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(foreground_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, 30.0, (width, height))

    while True:
        ret_foreground, frame_foreground = foreground_cap.read()
        ret_background, frame_background = background_cap.read()

        if not ret_foreground or not ret_background:
            break
        frame_background = cv2.resize(frame_background, (width, height))

        hsv = cv2.cvtColor(frame_foreground, cv2.COLOR_BGR2HSV)
        lower_bound = np.array([40, 40, 40])
        upper_bound = np.array([80, 255, 255])

        mask = cv2.inRange(hsv, lower_bound, upper_bound)
        inv_mask = cv2.bitwise_not(mask)
        foreground = cv2.bitwise_and(frame_foreground, frame_foreground, mask=inv_mask)
        background = cv2.bitwise_and(frame_background, frame_background, mask=mask)
        result = cv2.add(foreground, background)
        out.write(result)
        cv2.imshow('Chroma Keying', result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    foreground_cap.release()
    background_cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    foreground_video_path = "foreground.mp4"
    background_video_path = "background.mp4"
    output_video_path = "Final_output.mp4"

    chroma_keying(foreground_video_path, background_video_path, output_video_path)
