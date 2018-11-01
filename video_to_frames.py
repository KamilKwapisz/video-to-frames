import cv2
from moviepy.editor import VideoFileClip
from time import time


video_file = 'teledysk.mp4'
clip = VideoFileClip(video_file)
duration = clip.duration
actual_time: float = 0.0
cap = cv2.VideoCapture(video_file)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
frames: int = 24
fps_counter: int = 0

timer_start = time()
if cap.isOpened():
    while actual_time <= duration:
        actual_time = time() - timer_start
        ret, frame = cap.read()
        if fps_counter % frames == 0:
            cv2.imwrite(f"frames/frame{fps_counter}.jpg", frame)
            print(fps_counter)
        fps_counter += 1
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
