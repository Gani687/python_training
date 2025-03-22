
import glob
import os
import sys
def get_max_filename(path):
    def file(directory):
        file_sizes = {}
        for item in glob.glob(os.path.join(directory, "*")):
            if os.path.isfile(item):
                file_sizes[item] = os.path.getsize(item)
            elif os.path.isdir(item):
                file_sizes.update(file(item))
        return file_sizes

    
    all_files = file(path)
    if all_files:
        return max(all_files, key=all_files.get)  
    else:
        return "No files f ound in the specified path."

if __name__ == "__main__":
    search_path = r"."  
    print("Largest file:", get_max_filename(search_path))

