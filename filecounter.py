import os
import glob

# Set path to the root directory 
root_path = input("Insert location the map U want to have scanned example: C:/Users/{user}/{map}/: ")

# Initialize variables to keep track of file counts
total_file_count = 0
file_counts = {}


#Dicionary in dictionary

subfolder = {
    "extensions" : {
        ".docx" : 0,
        ".png" : 0,
        ".ini" : 0,
        ".pptx" : 0,
        ".xlxs" : 0,
        ".exe" : 0,
        ".jpeg" : 0,
        ".bat" : 0,
        ".dll" : 0,
        ".txt" : 0
    },

}

 
# Iterate through all subfolders in the root directory using os.walk

for root, dirs, files in os.walk(root_path):
    # Get the current subfolder name
    subfolder = root.split("/")[-1]
    # Initialize a count for each file type
    file_counts[subfolder] = {}
    # Iterate through all files in the subfolder using glob
    for file in glob.glob(os.path.join(root, "*")):
    # Check if the file is a regular file (not a directory)
        if os.path.isfile(file):
            total_file_count += 1
        
        # Get the file extension
            extension = file.split(".")[-1]
        
        # If the extension is not in the dictionary, add it
            if extension not in file_counts[subfolder]:
                file_counts[subfolder][extension] = 1
        # If the extension is already in the dictionary, increase the count by 1
            else:
                file_counts[subfolder][extension] += 1



# Print the total file count
print(f"There are a total of {total_file_count} files.\n")
# Print the file counts for each subfolder
for subfolder, counts in file_counts.items():
    print(f"In the subfolder: {subfolder} are {counts}")
#for extensions in subfolder:
#    print(f"There are {subfolder} .{extension} files")

    



