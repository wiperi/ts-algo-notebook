import os
import sys
import argparse

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


    # Check if there are more than 10 targets and ask for user confirmation
    if len(targets) > 10:
        print("Modification list:")
        print('\n'.join(targets))
        print('Total:', len(targets))
        proceed = input('Do you want to continue? (yes/no): ').strip().lower()
        if proceed != 'yes':
            print('Operation cancelled.')
            sys.exit(0)

    for file_path in targets:
        with open(file_path, 'a', encoding='utf-8') as f:
            print(f"Appending export to {file_path}")
            f.write('\nexport {}')
                

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Append 'export' to TypeScript files that don't have it.")
    parser.add_argument("src_dir", help="Source directory to search for TypeScript files.")
    args = parser.parse_args()
    
    src_directory = args.src_dir
    print('Scanning dir: \n', src_directory)
    
    append_export_to_ts_files(src_directory)
