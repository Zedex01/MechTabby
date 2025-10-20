from pathlib import Path
import os

sandbox_path = Path(r'C:/Users/mmoran/Desktop/Sandbox/D/Point Clouds')
#create new dir:
##dir_new = sandbox_path / "TestDir"
##dir_new.mkdir(exist_ok=True)

'''
#New file and dir:
# Create a file within a directory (the directory must exist first)
directory = Path("my_folder")
directory.mkdir(exist_ok=True)
file_in_dir_path = directory / "another_file.txt" # Using the forward slash operator for path concatenation
with file_in_dir_path.open("w") as f:
    f.write("Content for the file in the folder.")
'''
print("Starting...")
for i in range (190201,190400):
    dir = sandbox_path / str(i) 
    dir.mkdir(exist_ok=True)
    file_path = dir / "file.txt"
    with file_path.open("w") as f:
        f.write(f"This is file with info: {i}")

print("Done!")