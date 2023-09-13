import cv2

def extract_frames(video_path):
    # Open video file
    video_capture = cv2.VideoCapture(video_path)
    count = 0
    success, frame = video_capture.read()

    while success:
           # Save the frame with the appropriate count
            cv2.imwrite(f"frame{count}.jpg", frame)

            # Read the next frame
            success, frame = video_capture.read()

            count += 1

if __name__ == '__main__':
    video_path = "C:\\Users\\Admin\\PycharmProjects\\project_1\\openCV.mp4"
    extract_frames(video_path)
