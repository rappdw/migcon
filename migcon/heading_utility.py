import argparse
import json

from collections import defaultdict
from pathlib import Path


def generate_replacement_template(source: Path, target: Path):
    # read the input file
    with open(source, "r") as f:
        lines = f.readlines()
    structure = defaultdict(list)
    for line in lines:
        file, heading = line.split(".md:")
        structure[f'{file}.md'].append((heading, heading))
    with open(target, "w") as f:
        json.dump(structure, f, indent=4)


def execute_replacement(source: Path, target: Path):
    # read the input json file
    with open(source, "r") as f:
        structure = json.load(f)
    for file, changes in structure.items():
        target_file = target / file
        if not target_file.exists():
            print(f"Warning: {target_file} doesn't exist")
            continue
        # read the file
        with open(target_file, "r") as f:
            data = f.read()
        try:
            for change in changes:
                old, new = change
                if data.find(old) == -1:
                    print(f"Warning: {old} not found in {file}. Content has changed, re-examine your change file")
                else:
                    data = data.replace(old, new)
        except ValueError as e:
            print(f"Error: {e} on file: {target_file}")

        # write the file
        with open(target_file, "w") as f:
            f.write(data)


def main():
    # create an argument parser that accepts to arguments a heading change input file and an output directory
    parser = argparse.ArgumentParser(description="Convert a Confluence export to Jupyter Book")
    parser.add_argument("source", help="Source Directory or File")
    parser.add_argument("target", help="Target directory or File")
    # add an optional argument to specify the function to perform
    parser.add_argument("-f", "--function", help="Function to perform", choices=["generate", "execute"], default="generate")
    args = parser.parse_args()

    source = Path(args.source).expanduser()
    target = Path(args.target).expanduser()
    if not source.exists():
        print("Input heading change file doesn't exist")
        return

    # based on the function argument, call the appropriate function
    if args.function == "generate":
        generate_replacement_template(source, target)
    elif args.function == "execute":
        execute_replacement(source, target)


if __name__ == '__main__':
    main()
