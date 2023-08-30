import os
import cv2
import dlib

def extract_faces(frames_dir):
    # Create a "frames_with_boxes" directory within the frames directory
    frames_with_boxes_dir = os.path.join(frames_dir, "frames_with_boxes")
    os.makedirs(frames_with_boxes_dir, exist_ok=True)
    
    # Create a "faces" directory within the frames directory
    faces_dir = os.path.join(frames_dir, "faces")
    os.makedirs(faces_dir, exist_ok=True)
    
    # Load the dlib face detection model
    detector = dlib.get_frontal_face_detector()
    
    # List all frame files in the frames directory
    frame_files = [f for f in os.listdir(frames_dir) if f.endswith(".jpg")]
    
    # Loop through frame files
    for frame_file in frame_files:
        frame_path = os.path.join(frames_dir, frame_file)
        frame = cv2.imread(frame_path)
        
        # Convert frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = detector(gray_frame)
        
            # Calculate padding relative to the bounding box size
    padding_factor_bounding_box = 0.1  # Adjust this factor based on your preference

    # Loop through frame files
    for frame_file in frame_files:
        frame_path = os.path.join(frames_dir, frame_file)
        frame = cv2.imread(frame_path)
        frame_with_boxes = frame.copy()

        # Draw bounding boxes on the frame with boxes
        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()

            # Calculate padding for the bounding box
            padding_x = int(w * padding_factor_bounding_box)
            padding_y = int(h * padding_factor_bounding_box)

            # Adjust coordinates with padding
            x1 = max(x - padding_x, 0)
            y1 = max(y - padding_y, 0)
            x2 = min(x + w + padding_x, frame.shape[1])
            y2 = min(y + h + padding_y, frame.shape[0])

            # Draw bounding box on the frame with boxes
            cv2.rectangle(frame_with_boxes, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Save the frame with bounding boxes
        frame_with_boxes_path = os.path.join(frames_with_boxes_dir, f"{frame_file[:-4]}_with_boxes.jpg")
        cv2.imwrite(frame_with_boxes_path, frame_with_boxes)

        
        # Iterate through detected faces
        for face_num, face in enumerate(faces):
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            # Calculate padding relative to the bounding box size
            padding_factor = 0.5  # Adjust this factor based on your preference
            padding_x = int(w * padding_factor)
            padding_y = int(h * padding_factor)
    
            # Calculate cropping boundaries with padding
            x1 = max(x - padding_x, 0)
            y1 = max(y - padding_y, 0)
            x2 = min(x + w + padding_x, frame.shape[1])
            y2 = min(y + h + padding_y, frame.shape[0])
            
            # Crop and save the face in the "faces" directory
            face_image = frame[y1:y2, x1:x2]
            face_filename = os.path.join(faces_dir, f"{frame_file[:-4]}_face_{face_num}.jpg")
            cv2.imwrite(face_filename, face_image)
    
    return frames_with_boxes_dir, faces_dir, "Frames with bounding boxes and faces saved in separate directories."
