import os

# Specify the folder path containing the files to be renamed
folder_path = r"C:/example_path/train"

def rename_images(folder_path):
    """
    Renames .jpg and .txt files in the given folder.
    For each file that starts with 'frame_' and follows the pattern 'frame_xxxxxx', it:
    - Adds 16 to the frame number (in this case, no addition is done as per the code).
    - Formats the frame number to a six-digit string.
    - Adds a prefix ('5_19-55_') to the filename.
    """

    # Iterate over all files in the specified folder
    for filename in os.listdir(folder_path):

        # Handle .jpg image files with 'frame_' prefix
        if filename.endswith('.jpg') and filename.startswith('frame_'):
            # Extract the frame number from the filename
            frame_number = int(filename.split('_')[1].split('.')[0])  # Extract number between 'frame_' and '.jpg'
            
            # Add 16 to the frame number (no addition is actually done here)
            new_frame_number = frame_number  # In the original code, no actual addition of 16 occurs
            
            # Format the new frame number as a six-digit string (e.g., '32' -> '000032')
            new_frame_number_str = f"{new_frame_number:06d}"
            
            # Create the new filename with the prefix "5_19-55_" (adjust as needed)
            new_filename = f"5_19-55_frame_{new_frame_number_str}.jpg"
            
            # Get the full paths for the old and new filenames
            old_file = os.path.join(folder_path, filename)  # Full path to the current file
            new_file = os.path.join(folder_path, new_filename)  # Full path for the renamed file
            
            # Rename the file using os.rename() function
            os.rename(old_file, new_file)
            
            # Print confirmation of renaming
            print(f'Renamed: {filename} -> {new_filename}')

        # Handle .txt files with 'frame_' prefix (similar to the .jpg block)
        if filename.endswith('.txt') and filename.startswith('frame_'):
            # Extract the frame number from the filename
            frame_number = int(filename.split('_')[1].split('.')[0])  # Extract number between 'frame_' and '.txt'
            
            # Add 16 to the frame number (no addition is actually done here)
            new_frame_number = frame_number  # No actual addition of 16 in the original code
            
            # Format the new frame number as a six-digit string (e.g., '32' -> '000032')
            new_frame_number_str = f"{new_frame_number:06d}"
            
            # Create the new filename with the prefix "5_19-55_" (adjust as needed)
            new_filename = f"5_19-55_frame_{new_frame_number_str}.txt"
            
            # Get the full paths for the old and new filenames
            old_file = os.path.join(folder_path, filename)  # Full path to the current file
            new_file = os.path.join(folder_path, new_filename)  # Full path for the renamed file
            
            # Rename the file using os.rename() function
            os.rename(old_file, new_file)
            
            # Print confirmation of renaming
            print(f'Renamed: {filename} -> {new_filename}')

# Call the function to rename images and text files in the specified folder
rename_images(folder_path)