import os
import datetime
import sys

def add_date_to_filenames(folder_path):
    """Prefixes all files in the specified folder with today's date (YYYY-MM-DD)."""
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    today = datetime.date.today().strftime("%Y-%m-%d")
    
    # List all files in the directory
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        
        # Only rename files (skip directories)
        if os.path.isfile(old_path):
            new_filename = f"{today}-{filename}"
            new_path = os.path.join(folder_path, new_filename)
            
            # Avoid renaming if the file already has the date prefix
            if not filename.startswith(today):
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {filename} -> {new_filename}")
                except Exception as e:
                    print(f"Failed to rename {filename}: {e}")
            else:
                print(f"Skipping {filename} (already has date prefix)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python add_date.py <folder_path>")
    else:
        add_date_to_filenames(sys.argv[1])
