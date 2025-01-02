import os

def count_lines(directory: str) -> int:
    total_lines = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.ts'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = sum(1 for _ in f)
                        print(lines, file_path)
                        total_lines += lines
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return total_lines

if __name__ == "__main__":
    directory = "./src"  # 修改为目标目录
    print(f"Total lines of code: {count_lines(directory)}")
