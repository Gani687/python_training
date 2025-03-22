import os

def process_files(source_dir, output_filepath):
    
    try:
        with open(output_filepath, "w", encoding="utf-8") as output_file:
            for root, _, files in os.walk(source_dir):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    try:
                        with open(file_path, "r", encoding="utf-8") as input_file:
                            output_file.write(f"--- File content: {file_path} ---\n")
                            output_file.writelines(input_file.readlines())
                            output_file.write("\n\n")
                    except IOError as e:
                        print(f"Error reading {file_path}: {e}")
                    except UnicodeDecodeError:
                        print(f"Non-text file skipped: {file_path}")
    except Exception as e:
        print(f"An error occurred while writing to {output_filepath}: {e}")


source_directory = "C:/Users/K Ganesh Sai/handson"
output_file = "output.txt"

process_files(source_directory, output_file)
print(f"Content from all files has been written to {output_file}.")