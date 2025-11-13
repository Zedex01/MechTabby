from pathlib import Path
from tkinter import Tk, filedialog
from datetime import datetime
import json
import subprocess
from PIL import Image
import os



def main():
    #Prompt for input dir name
    input_dir_path = Path(get_dir())

    #Make sure input folder exists
    if not input_dir_path.exists():
        print("No directory found @: ", input_dir_path)
        exit()

    # Get the name of the working dir
    input_dir_name = input_dir_path.name

    #Get the parent dir path
    parent_path = input_dir_path.parent
    #Create a name for the output dir
    output_dir_name = input_dir_name + " Fixed"
    #Create the path for the output dir
    output_dir_path = parent_path / output_dir_name

    log_file = parent_path / "log.txt"

    #safely create output dir:
    output_dir_path.mkdir(parents=True, exist_ok = True)

    cnt = 0
    err_cnt = 0

    file_cnt = 0

    log_file.open("a").write(f"\n === {datetime.now()} ===")


    #Get # of files to be converted:
    for file in input_dir_path.rglob("*"):
        if file.exists() and file.suffix != ".json":
            file_cnt += 1

    print("Starting...")
    #Go through each child item recursivly:
    for json_file in input_dir_path.rglob("*.json"):
        #print(":=====: ",json_file.name)
        
        #Find corresponding media file:
        media_file = json_file.with_suffix("").with_suffix("")
        #print("media_file: ", media_file.name)

        #Load the metadata json to be readable
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        #Extract photo taken time:
        ts = int(data["photoTakenTime"]["timestamp"])
        #Reformat timestamp to datetime
        dt = datetime.fromtimestamp(ts)
        cnt += 1

        #Create file output path fore media file
        output_path = output_dir_path / media_file.name

        #Only run subprocess if file does not exist in output:
        if not output_path.exists():
            print("Building Command: ", media_file.name)
            print("datetime: ", str(dt))

            #Build command for updating creation date
            cmd = [
                "exiftool",
                "-DateTimeOriginal=" + dt.strftime("%Y:%m:%d %H:%M:%S"),
                "-DateTimeDigitized=" + dt.strftime("%Y:%m:%d %H:%M:%S"),
                "-FileModifyDate<" + dt.strftime("%Y:%m:%d %H:%M:%S"),
                "-FileCreateDate<" + dt.strftime("%Y:%m:%d %H:%M:%S"),
                "-FileAccessDate<" + dt.strftime("%Y:%m:%d %H:%M:%S"),
                "-o", str(output_path), str(media_file)
            ]
          

            #run cmd and change file exifdata
            try:
                res = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(res.stdout)
            
            except subprocess.CalledProcessError as e:

                err_cnt += 1

                #note The old suffix
                old_suffix = media_file.suffix
                print("Old Suffix: ", old_suffix)

                #Find the correct suffix:
                with Image.open(media_file) as img:
                    format = img.format
                    print(f"Image format for {media_file}: {format}")

                #Note the new suffix
                new_suffix = "." + format
                print("New Suffix: ", new_suffix)

                #Change medida file name
                new_media_file_path = media_file.with_suffix(new_suffix)

                #Change json file name
                str_json_path = str(json_file)
                
                new_json_file_path = Path(str_json_path.replace(old_suffix, new_suffix))


                print("New media file Name: ", new_media_file_path.name)
                print("New json file Name: ", new_json_file_path.name)
                media_file.rename(new_media_file_path)
                json_file.rename(new_json_file_path)

            #One final for all update:
            cmd = [
                "exiftool", "-FileCreateDate<DateTimeOriginal", "-FileModifyDate<DateTimeOriginal", "*"
                ]
            
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            finished_cnt = len(list(output_dir_path.rglob("*")))


    print("Total Files to Move: ", file_cnt)
    print("Total Files Made: ", finished_cnt)
    
    print("Conversion Errors: ", err_cnt)



# === Functions === 
def get_dir() -> str:
    #Prompt user for input folder and return the path
    root = Tk()
    root.withdraw()

    input_folder = filedialog.askdirectory(title="Select input folder")
    if not input_folder:
        print("Not valid")
        return None

    return input_folder
    

if __name__ == "__main__":
    main()




