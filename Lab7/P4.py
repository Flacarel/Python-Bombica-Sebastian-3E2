import os
import sys
from collections import defaultdict

def count_files_by_extension(directory):
    if not os.path.isdir(directory):
        raise ValueError(f"Invalid directory: {directory}")

    extension_counts = defaultdict(int)

    try:
        files = os.listdir(directory)
        if not files:
            print("Directory is empty")
            return extension_counts

        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                _, ext = os.path.splitext(file)
                extension_counts[ext] += 1

    except Exception as e:
        print(f"Error accessing directory: {e}")
    
    return extension_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    try:
        extension_counts = count_files_by_extension(directory)
        if extension_counts:
            for ext, count in extension_counts.items():
                print(f"{ext if ext else 'No Extension'}: {count}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
