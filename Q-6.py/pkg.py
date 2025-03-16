import os 
import datetime

class File():
    def __init__(self, directory):
        self.directory = directory
        
    
    def __repr__(self):
        return self.directory
    

    def getMaxSize(directory, index):
        max_size = 0
        largest_files = []
        for dirpath, dirname, files in os.walk(str(directory)):
            for file in files:
                file_path = os.path.join(dirpath, file)
                file_name = os.path.basename(file_path)
                file_size = os.path.getsize(file_path)
            
                if file_size>max_size:
                    max_size = file_size
                    
                    largest_files.append(file)

        # Sort by size in descending order
        largest_files = sorted(largest_files, key=lambda x: os.path.getsize(os.path.join(str(directory), x)), reverse=True)
        return largest_files[:index]