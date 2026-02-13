from pathlib import Path
import shutil
source = Path.home() / "Downloads"
docu_dest = Path.home()/"OneDrive"/"Documents"
img_dest = Path.home()/"OneDrive"/"Pictures"
vid_dest = Path.home()/"Videos"


for file in source.iterdir():
    if file.is_file() and file.suffix.lower() in [".pdf",".txt",".docx",".doc",".xlsx",".xls",".csv",".ppt",".pptx"]:
        dest_path = docu_dest / file.name
        if dest_path.exists():
            print(f"{file} already exists. Skipping")
        else:
            shutil.move(file,docu_dest)
            print(f"Successfull Moved{file} to {docu_dest}")
    
    if file.is_file() and file.suffix.lower() in [".jpeg",".jpg",".png",".gif",".heif",".heic",".raw"]:
        dest_path = img_dest / file.name
        if dest_path.exists():
            print(f"{file} already exists. Skipping")           
        else:
            shutil.move(file,img_dest)
            print(f"Successfull Moved{file} to {img_dest}")
            
    if file.is_file() and file.suffix.lower() in [".mp4",".mov",".avi",".mkv",".webm"]:
        dest_path = vid_dest / file.name
        if dest_path.exists():
            print(f"{file} already exists. Skipping") 
           
        else:
            shutil.move(file,vid_dest)
            print(f"Successfull Moved{file} to {vid_dest}")
            
print("Success!!")