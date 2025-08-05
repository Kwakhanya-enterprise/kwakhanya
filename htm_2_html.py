import os

# Replace this with the root folder you want to start from
root_folder = "."

for foldername, subfolders, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.endswith(".htm"):
            old_path = os.path.join(foldername, filename)
            new_filename = filename[:-4] + ".html"
            new_path = os.path.join(foldername, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} -> {new_path}")
