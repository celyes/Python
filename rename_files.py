import os
def rename_files():
    files = os.listdir(r"C:\Users\Celyes\Desktop\OMAC\prank")
    current_path = os.getcwd()
    os.chdir(r"C:\Users\Celyes\Desktop\OMAC\prank")
    for file_name in files:
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print file_name
    os.chdir(current_path)
rename_files()