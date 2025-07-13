# Folder Tree Generator

A simple Python script to generate a visual tree of any folder structure, with support for ignoring specified folders/files using a `.ignoretree` file. Useful for documenting project structures or quickly visualizing directory layouts.

## Features

- Generates a tree view of any directory
- Supports ignoring files/folders via a `.ignoretree` file
- Interactive mode: If no target directory is provided, lets you select from subfolders or enter a custom path
- Customizable output file location

## Requirements

- Python 3.6 or higher

## Usage

### 1. Basic Usage

Generate a tree for a specific folder:

```sh
python generate_tree.py path/to/your/project
```

This will create a `folder_tree.txt` file in the target directory.

### 2. Interactive Mode

If you run the script without arguments:

```sh
python generate_tree.py
```

You will be prompted to select a subfolder or enter a custom path.

### 3. Custom Ignore File or Output File

You can specify a custom ignore file or output file:

```sh
python generate_tree.py path/to/your/project --ignore path/to/.ignoretree --output path/to/output.txt
```

- `--ignore`: Path to a `.ignoretree` file (default: `<target_dir>/.ignoretree`)
- `--output`: Output file name (default: `<target_dir>/folder_tree.txt`)

## .ignoretree Format

- Place each folder or file name to ignore on a separate line.
- Example:
  ```
  __pycache__
  .git
  node_modules
  *.pyc
  ```

## Example Output

```
Current directory: /path/to/your/project

├── src
│   ├── main.py
│   └── utils.py
├── README.md
└── requirements.txt
```

## License

MIT
