import os
import shutil
import argparse

def copy_files_with_extension(src_dir: str, dest_dir: str, extension: str):

    tasks = []

    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(extension):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)
                tasks.append((src_file, dest_file))

    # Prompt user with the content of the task list
    print("\nThe following files will be copied:")
    for src_file, dest_file in tasks:
        print(f"{src_file} -> {dest_file}")

    # Ask user if they are sure to continue
    proceed = input("\nDo you want to proceed with copying these files? (yes/no): ").strip().lower()
    if proceed != 'yes':
        print("Operation cancelled.")
        return
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Finish task and print
    for src_file, dest_file in tasks:
        shutil.copy2(src_file, dest_file)
        print(f"Copied {src_file} to {dest_file}")

    print("\nAll files have been copied.")
                
                

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy files with a specific extension to a destination directory.")
    parser.add_argument("src_dir", help="Source directory to search for files.")
    parser.add_argument("--extensions", "-e", required=True, help="File extension to look for.")
    parser.add_argument("--path", "-p", required=True, help="Destination directory to copy files to.")
    
    args = parser.parse_args()
    copy_files_with_extension(args.src_dir, args.path, args.extensions)
