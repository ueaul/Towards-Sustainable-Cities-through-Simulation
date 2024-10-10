#%%
import cv2
import numpy as np
import glob


#%%
def enhance_contrast(frame):
    # Convert to grayscale if not already
    if len(frame.shape) == 3 and frame.shape[2] == 3:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Enhance contrast using histogram equalization
    equalized = cv2.equalizeHist(frame)
    return equalized

def process_video(input_path, output_path, target_fps):
    # Open the input video
    cap = cv2.VideoCapture(input_path)
    
    # Get original frame rate and dimensions
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Calculate frame skipping interval
    frame_interval = int(original_fps / target_fps)
    
    # VideoWriter object for the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for MPEG-4
    out = cv2.VideoWriter(output_path, fourcc, target_fps, (frame_width, frame_height), isColor=False)
    
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Process every nth frame based on frame_interval
        if frame_count % frame_interval == 0:
            # Enhance contrast
            enhanced_frame = enhance_contrast(frame)
            
            # Write the processed frame to the output video
            out.write(enhanced_frame)
        
        frame_count += 1
    
    # Release everything
    cap.release()
    out.release()
    cv2.destroyAllWindows()


#%%
def process_all_videos(input_folder, output_folder, target_fps):
    # Ensure output directory exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Get list of video files in the input directory
    video_files = glob.glob(os.path.join(input_folder, "*.avi"))
    
    for video_file in video_files:
        # Extract the file name and create the output path
        file_name = os.path.basename(video_file)
        output_file = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".mp4")
        
        # Process the video
        process_video(video_file, output_file, target_fps)
        print(f"Processed: {video_file} -> {output_file}")


#%%
input_folder = "Input"    # Folder containing input videos
output_folder = "Output"  # Folder to save processed videos
target_fps = 15 

process_all_videos(input_folder, output_folder, target_fps)

# %%
