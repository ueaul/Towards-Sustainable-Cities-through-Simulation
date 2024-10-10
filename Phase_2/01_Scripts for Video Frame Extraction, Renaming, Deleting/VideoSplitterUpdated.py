import cv2  
import os  
import re 

# Specify the input video path and output folder for extracted frame images
video_path = r"C:/example_path/2023-11-20_07-29_MaVI18.avi" 
output_folder = r"C:/example_path/2023-11-20_07-29_MaVI18"

def extract_frames(video_path, output_folder, frame_interval=150):
    """
    Extract frames from a video at regular intervals and save them as images in the specified folder.
    
    Parameters:
    - video_path: Path to the video file from which to extract frames.
    - output_folder: Directory where the extracted frames will be saved.
    - frame_interval: Interval between frames to be saved (default is every 150th frame).
    """
    
    # Get the video filename from the full path
    video_filename = os.path.basename(video_path)
    
    # Use regex to match the video name to the expected pattern for later naming the frames
    match = re.search(r'(\d{4}-\d{2}-\d{2})_(\d{2}-\d{2})_MaVI(\d+)\.avi', video_filename)
    if not match:
        # If the filename format does not match, show an error and exit
        print("Fehler: Das Format des Videonamens passt nicht zur Erwartung.")  # Error: Video name format does not match expectation
        return
    
    # Extract relevant parts of the video name (date, time, and MaVI number) to be used in naming the frames
    date_part = match.group(1)  # Example: 2023-11-20 (from video filename)
    time_part = match.group(2)  # Example: 07-29 (from video filename)
    ma_vi_number = match.group(3)  # Example: 18 (MaVI number from filename)
    
    # Open the video file using OpenCV
    cap = cv2.VideoCapture(video_path)

    # Check if the video was opened successfully
    if not cap.isOpened():
        print(f"Fehler: Konnte das Video {video_path} nicht öffnen")  # Error: Could not open the video
        return

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Maximale Anzahl der Frames: {total_frames}")  # Maximum number of frames

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_count = 0  # Initialize frame count

    # Loop through the video frame by frame
    while True:
        ret, frame = cap.read()  # Read the next frame
        if not ret:
            # If no more frames are available, exit the loop
            break
        
        # Save every `frame_interval`-th frame
        if frame_count % frame_interval == 0:
            # Format the frame number as a six-digit string (e.g., 000150 for frame 150)
            frame_number_str = f"{frame_count:06d}"
            
            # Create the image filename using the MaVI number, time, and frame number
            image_filename = f"{ma_vi_number}_{time_part}_frame_{frame_number_str}.jpg"
            
            # Define the full path to save the image
            image_path = os.path.join(output_folder, image_filename)
            
            # Save the current frame as an image file
            cv2.imwrite(image_path, frame)
            print(f"Gespeichert: {image_path}")  # Saved: image path

        frame_count += 1  # Increment the frame count
        
        # Stop the loop if we've processed all frames
        if frame_count >= total_frames:
            break

    # Release the video capture object
    cap.release()
    print(f"Extraktion beendet. Alle {frame_interval} Frames wurden im Ordner {output_folder} gespeichert.")  
    # Extraction finished. All frames have been saved.

# Call the function to extract frames from the video
extract_frames(video_path, output_folder)