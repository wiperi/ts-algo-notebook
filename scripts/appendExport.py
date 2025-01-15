import os
import sys

def append_export_to_ts_files(path: str):
    if os.path.isfile(path):
        files = [path]
    else:
        files = []
        for root, _, filenames in os.walk(path):
            if 'node_modules' in root:
                print(f"Skipping directory: {root}")
                continue
            for filename in filenames:
                if filename.endswith('.ts'):
                    files.append(os.path.join(root, filename))
    
    targets = []
    
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'export' not in content:
            targets.append(file_path)


    if len(targets) > 10:
        print("Modification list:")
        print('\n'.join(targets))
        print('Total: ', len(targets))
        if input('Do you want to continue? y/n\n') == 'n':
            print('Aborted')
            sys.exit(0)

    for file_path in targets:
        with open(file_path, 'a', encoding='utf-8') as f:
            print(f"Appending export to {file_path}")
            f.write('\nexport {}')
                

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python appendExport <directory>")
        sys.exit(1)
    
    # Get the directory from the command line argument
    src_directory = sys.argv[1]
    print('Scanning dir: \n', src_directory)
    
    append_export_to_ts_files(src_directory)