import cv2
import os
import tempfile
import shutil

def extract_frames(video_path, frame_rate=2):
    # Create a temporary directory named "temp_frames"
    temp_dir = "temp_frames"
    os.makedirs(temp_dir, exist_ok=True)
    
    # Get the video file name without extension
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    
    # Create a directory for frames within the temp directory
    frames_dir = os.path.join(temp_dir, video_name)
    
    # Handle existing directory by adding a number suffix
    dir_suffix = 1
    while os.path.exists(frames_dir):
        frames_dir = os.path.join(temp_dir, f"{video_name}_{dir_suffix}")
        dir_suffix += 1
    
    os.makedirs(frames_dir)
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file")
        return
    
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    interval = int(fps / frame_rate)
    
    frame_number = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_number % interval == 0:
            frame_filename = os.path.join(frames_dir, f"frame_{frame_number:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
        
        frame_number += 1
    
    cap.release()
    print(f"Extracted {frame_number} frames at {frame_rate} frames per second")
    
    return frames_dir


# # Example usage
# video_path = "/home/hpcap/Desktop/Project_ai_06/Testdata/aagfhgtpmv.mp4"
# frames_dir_temp = extract_frames(video_path, frame_rate=2)
# print(f"Frames are saved in: {frames_dir}")


# result_dir, result_message = extract_faces(frames_dir)
# print(result_message)
