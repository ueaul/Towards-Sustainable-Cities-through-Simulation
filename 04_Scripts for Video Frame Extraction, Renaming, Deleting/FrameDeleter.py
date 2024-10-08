import os

# Specify the path to the folder containing the files to be filtered and deleted
folder_path = r"C:/example_path/train"

def filter_txt_files(folder_path, interval=10):
    """
    Deletes .txt files in the specified folder that are not named in a certain interval (e.g., every 10th file).
    
    Parameters:
    - folder_path: Path to the folder containing the .txt files to be filtered.
    - interval: Interval step for keeping files. Files with numbers divisible by the interval will be kept, others deleted.
    """
    
    # Get a list of all files in the specified folder
    files = os.listdir(folder_path)
    
    # Filter out only .txt files from the list of files in the folder
    txt_files = [f for f in files if f.endswith('.txt')]

    # Loop through each .txt file
    for txt_file in txt_files:
        # Check if the file name starts with 'frame_' (only process files with this prefix)
        if txt_file.startswith('frame_'):
            # Extract the numeric part of the file name (assumes the format 'frame_xxxxxx.txt', where xxxxxx is the number)
            file_number_str = txt_file[6:12]  # Extract characters at position 6-11, which should represent the frame number
            
            try:
                # Convert the extracted string into an integer
                file_number = int(file_number_str)
                
                # If the frame number is not divisible by the specified interval, delete the file
                if file_number % interval != 0:
                    # Create the full path to the file
                    file_path = os.path.join(folder_path, txt_file)
                    
                    # Remove (delete) the file from the folder
                    os.remove(file_path)
                    
                    # Print confirmation that the file was deleted
                    print(f"Gelöscht: {file_path}")  # Deleted: file path
            except ValueError:
                # If the file number is not a valid integer, print an error message (this prevents crashing)
                print(f"Fehler beim Verarbeiten der Datei: {txt_file} - kein gültiger Zahlenwert")  
                # Error processing file: not a valid number
        else:
            # If the file name doesn't start with 'frame_', skip it and print a message
            print(f"Übersprungen (kein 'frame_xxxxxx' Dateiname): {txt_file}")  
            # Skipped (not a 'frame_xxxxxx' filename)

    # After processing all files, print a completion message
    print("Fertig! Alle Dateien in " + str(interval) + "-Schritten wurden behalten.")
    # Done! All files with step interval were kept.

# Call the function to filter and delete .txt files in the folder
filter_txt_files(folder_path)