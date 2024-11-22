import os
import sys

def calculate_total_size(directory):
    total_size = 0

    if not os.path.isdir(directory):
        raise ValueError(f"Invalid directory: {directory}")

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                total_size += os.path.getsize(file_path)
            except Exception as e:
                print(f"Error accessing {file_path}: {e}")
    
    return total_size

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    try:
        total_size = calculate_total_size(directory)
        print(f"Total size: {total_size} bytes")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
