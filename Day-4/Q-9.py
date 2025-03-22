import os
def split(file, partition):
    file_size = os.path.getsize(file)
    chunk_size = file_size // partition

    with open(file, 'rb') as input:
        for i in range(partition):

            partition_name = f"{file}_part{i+1}"


            with open(partition_name, 'wb') as partition_file:
                if i == partition - 1:

                    partition_file.write(input.read())
                else:
                    partition_file.write(input.read(chunk_size))
                
            print(f"Generated: {partition_name}")

original_file = r"C:/Users/K Ganesh Sai/handson/text.txt"
n = 4

split(original_file, n)