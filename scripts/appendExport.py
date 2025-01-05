import os
import sys

def append_export_to_ts_files(path: str):
    if os.path.isfile(path):
        files = [path]
    else:
        files = []
        for root, _, filenames in os.walk(path):
            for filename in filenames:
                if filename.endswith('.ts'):
                    files.append(os.path.join(root, filename))
    
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'export' not in content:
            with open(file_path, 'a', encoding='utf-8') as f:
                print(f"Appending export to {file_path}")
                f.write('\nexport {}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python appendExport <directory>")
        sys.exit(1)
    
    # Get the directory from the command line argument
    src_directory = sys.argv[1]
    print(src_directory)
    
    append_export_to_ts_files(src_directory)