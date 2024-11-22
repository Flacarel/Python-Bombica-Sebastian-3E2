import os
import sys

def find_files(directory, extension):
    if not os.path.isdir(directory):
        raise ValueError(f"Invalid directory: {directory}")
    if not extension.startswith('.'):
        raise ValueError(f"Invalid extension: {extension}")
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(extension)]

def print_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            print(f"\n{file_path}:\n{file.read()}")
    except Exception as e:
        print(f"Error: {file_path}: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python P1.py <directory> <extension>")
        sys.exit(1)

    directory = sys.argv[1]
    extension = sys.argv[2]

    try:
        files = find_files(directory, extension)
        if not files:
            print("No files found")
            return
        for file in files:
            print_file_contents(file)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
