import cv2 
import os 
import re 

# Specify the path to the input video and the output folder for frame images
video_path = r"C:/example_path/2024-04-11_19-55_MaVI5.avi" 
output_folder = r"C:/example_path/2024-04-11_19-55_MaVI5"

# Frame extraction parameters
frame_interval = 100  # Interval between frames to be saved (every 100th frame)
org_start = 10460  # Original starting frame number for half-frame calculation
half_frame = org_start // 2  # Calculate half of the original starting frame
start_frame = org_start - half_frame  # Adjusted starting frame
end_frame = 1 + 10860 - half_frame  # Adjusted ending frame

# On Babett's laptop the frames did not match the exported frames from the CVAT software when shifting the starting frame of the video extraction based on the deisred intervals.
# Babett is unsure, why this was the case. However, shifting the start and end frame by half of the amount that the start of the video extraction was shifted by originally, fixed the error.

def extract_frames(video_path, output_folder, frame_interval, start_frame, end_frame):
    """
    Extract frames from a video between specified start and end frames at regular intervals,
    and save them as images in the output folder.

    Parameters:
    - video_path: Path to the video file.
    - output_folder: Folder where extracted frames will be saved.
    - frame_interval: Interval between frames to be saved.
    - start_frame: The frame number at which to start extraction.
    - end_frame: The frame number at which to stop extraction.
    """
    
    # Get the video filename from the full path
    video_filename = os.path.basename(video_path)
    
    # Use regex to match the video name to the expected pattern for later frame naming
    match = re.search(r'(\d{4}-\d{2}-\d{2})_(\d{2}-\d{2})_MaVI(\d+)\.avi', video_filename)
    if not match:
        print("Fehler: Das Format des Videonamens passt nicht zur Erwartung.")  # Error: Video name format does not match expectation
        return
    
    # Extract relevant parts of the video name (date, time, and MaVI number) to be used in naming frames
    date_part = match.group(1)  # Example: 2024-04-11 (date from video filename)
    time_part = match.group(2)  # Example: 19-55 (time from video filename)
    ma_vi_number = match.group(3)  # Example: 5 (MaVI number from filename)
    
    # Open the video file using OpenCV
    cap = cv2.VideoCapture(video_path)

    # Check if the video was opened successfully
    if not cap.isOpened():
        print(f"Fehler: Konnte das Video {video_path} nicht öffnen")  # Error: Could not open video
        return

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Maximale Anzahl der Frames: {total_frames}")  # Maximum number of frames

    # Ensure the end_frame is within the total frames of the video
    if end_frame is None or end_frame > total_frames:
        end_frame = total_frames

    # Validate that the start frame is less than the end frame and non-negative
    if start_frame >= end_frame or start_frame < 0:
        print("Fehler: Ungültiger Start- oder Endframe-Wert.")  # Error: Invalid start or end frame value
        return

    # Create the output folder if it doesn't already exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_count = 0  # Initialize frame count to keep track of current frame number
    saved_frame_count = 0  # Track how many frames were saved
    
    # Set the starting position of the video to the desired start_frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    # Loop through the video frames until the end_frame is reached
    while frame_count < end_frame:
        ret, frame = cap.read()  # Read the next frame from the video
        if not ret or frame_count >= end_frame:
            # If no more frames or if we exceed the end_frame, exit the loop
            break
        
        # Save frames at the specified interval
        if frame_count >= start_frame and (frame_count - start_frame) % frame_interval == 0:
            # Adjust the frame number by adding half_frame and format it as a six-digit string
            frame_number_str = frame_count + half_frame
            frame_number_str = f"{frame_number_str:06d}" 
            
            # Create the image filename using the MaVI number, time, and frame number
            image_filename = f"{ma_vi_number}_{time_part}_frame_{frame_number_str}.jpg"
            # Define the full path to save the image
            image_path = os.path.join(output_folder, image_filename)
            
            # Save the current frame as an image
            cv2.imwrite(image_path, frame)
            print(f"Gespeichert: {image_filename}")  # Print a message when a frame is saved
            saved_frame_count += 1  # Increment the count of saved frames

        frame_count += 1  # Increment the frame count

    # Release the video capture object to free up resources
    cap.release()
    print(f"Extraktion beendet. {saved_frame_count} Frames wurden im Ordner {output_folder} gespeichert.")  
    # Extraction finished. Print how many frames were saved.

# Call the function to extract frames from the video
extract_frames(video_path, output_folder, frame_interval, start_frame, end_frame)