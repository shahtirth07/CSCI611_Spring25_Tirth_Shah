import os
import shutil

def segregate_files(folder_path):
    jpg_folder = os.path.join(folder_path, 'JPG_Files')
    xml_folder = os.path.join(folder_path, 'XML_Files')
    
    # Create directories if they don't exist
    os.makedirs(jpg_folder, exist_ok=True)
    os.makedirs(xml_folder, exist_ok=True)
    
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            if file.lower().endswith('.jpg'):
                shutil.move(file_path, os.path.join(jpg_folder, file))
            elif file.lower().endswith('.xml'):
                shutil.move(file_path, os.path.join(xml_folder, file))
    
    print("Files segregated successfully.")

# Example usage
folder_path = "Self-Driving Cars.v6-version-4-prescan-416x416.voc/test"  # Change this to your folder path
segregate_files(folder_path)