import os
import sys

def rename_files_sequentially(directory):
    if not os.path.isdir(directory):
        raise ValueError(f"Invalid directory: {directory}")

    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        if not files:
            print("No files found")
            return

        for idx, filename in enumerate(files, start=1):
            old_path = os.path.join(directory, filename)
            new_name = f"{idx:03d}_{filename}"
            new_path = os.path.join(directory, new_name)
            
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_name}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    try:
        rename_files_sequentially(directory)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
