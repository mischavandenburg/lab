import os

def combine_markdown_files(output_file='combined_document.md'):
    with open(output_file, 'w') as outfile:
        for root, _, files in os.walk('.'):
            for file in files:
                if file.endswith('.md') and file != output_file:
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, 'r') as infile:
                            outfile.write(f"\n\n# Content from: {filepath}\n\n")
                            outfile.write(infile.read())
                        print(f"Added: {filepath}")
                    except IOError as e:
                        print(f"Error reading file {filepath}: {e}")

if __name__ == "__main__":
    combine_markdown_files()
    print("Markdown files combined into combined_document.md")
