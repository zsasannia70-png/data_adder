import os
import datetime
import argparse

def rename_files_with_date(directory):
    """
    Prefixes all files in the given directory with today's date (YYYY-MM-DD).
    """
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    today = datetime.date.today().strftime("%Y-%m-%d")
    
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    for filename in files:
        # Avoid double-prefixing if the script is run multiple times
        if filename.startswith(today):
            print(f"Skipping '{filename}' (already prefixed)")
            continue
            
        old_path = os.path.join(directory, filename)
        new_filename = f"{today}-{filename}"
        new_path = os.path.join(directory, new_filename)
        
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")
        except Exception as e:
            print(f"Error renaming {filename}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prefix files in a folder with today's date.")
    parser.add_argument("directory", help="The path to the folder containing files to rename.")
    args = parser.parse_args()
    
    rename_files_with_date(args.directory)
