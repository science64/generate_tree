import os
import argparse

def load_ignores(ignore_path):
    if not os.path.exists(ignore_path):
        return set()
    with open(ignore_path, 'r') as f:
        return set(line.strip() for line in f if line.strip())

def build_tree(root, ignore_set, prefix=''):
    entries = []
    try:
        items = sorted(os.listdir(root))
    except Exception:
        return entries

    folders = [item for item in items if os.path.isdir(os.path.join(root, item))]
    files = [item for item in items if os.path.isfile(os.path.join(root, item))]

    for i, folder in enumerate(folders):
        if folder in ignore_set:
            continue
        is_last = (i == len(folders) - 1 and not files)
        entries.append(f"{prefix}{'└── ' if is_last else '├── '}{folder}")
        deeper_prefix = prefix + ('    ' if is_last else '│   ')
        entries += build_tree(os.path.join(root, folder), ignore_set, deeper_prefix)

    for j, file in enumerate(files):
        entries.append(f"{prefix}{'└── ' if j == len(files) - 1 else '├── '}{file}")

    return entries

def main():

    parser = argparse.ArgumentParser(description="Generate a folder tree for a given directory.")
    parser.add_argument('target_dir', nargs='?', default=None, help='Target directory to generate the tree for (optional)')
    parser.add_argument('--ignore', default=None, help='Path to .ignoretree file (default: <target_dir>/.ignoretree)')
    parser.add_argument('--output', default=None, help='Output file name (default: <target_dir>/folder_tree.txt)')
    args = parser.parse_args()

    # If target_dir is not provided, prompt user to select from subfolders or enter a path
    if not args.target_dir:
        cwd = os.getcwd()
        subfolders = [f for f in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, f))]
        print("No target directory provided.")
        if not subfolders:
            print("No subfolders found in the current directory. Please enter a folder path.")
            target_dir = input("Enter the path to the target directory: ").strip()
        else:
            print("Select a folder to generate the tree for:")
            for idx, folder in enumerate(subfolders, 1):
                print(f"  {idx}. {folder}")
            print(f"  {len(subfolders)+1}. Enter a custom path")
            while True:
                choice = input(f"Enter your choice (1-{len(subfolders)+1}): ").strip()
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(subfolders):
                        target_dir = os.path.abspath(os.path.join(cwd, subfolders[choice-1]))
                        break
                    elif choice == len(subfolders)+1:
                        target_dir = input("Enter the path to the target directory: ").strip()
                        target_dir = os.path.abspath(target_dir)
                        break
                print("Invalid choice. Please try again.")
    else:
        target_dir = os.path.abspath(args.target_dir)

    ignore_file = args.ignore if args.ignore else os.path.join(target_dir, '.ignoretree')
    output_file = args.output if args.output else os.path.join(target_dir, 'folder_tree.txt')

    ignore_folders = load_ignores(ignore_file)
    tree_lines = [f"Current directory: {target_dir}", ""]
    tree_lines += build_tree(target_dir, ignore_folders)

    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write('\n'.join(tree_lines))

    print(f"Folder tree saved to {output_file}")

if __name__ == "__main__":
    main()
