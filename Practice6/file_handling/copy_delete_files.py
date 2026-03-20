# copy_delete_files.py

import shutil
import os

# Copy file
shutil.copy("sample.txt", "backup.txt")

print("File copied!")

# Delete safely
if os.path.exists("backup.txt"):
    os.remove("backup.txt")
    print("File deleted!")
else:
    print("File not found")