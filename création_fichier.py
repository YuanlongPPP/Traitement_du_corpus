import os

# Define the project structure with files and directories
project_structure = [
    "PROJECT/bin",
    "PROJECT/data/raw",
    "PROJECT/data/clean",
    "PROJECT/figures",
    "PROJECT/scripts/process",
    "PROJECT/scripts/plot",
    "PROJECT/src/model1",
    "PROJECT/src/model2",
    "PROJECT/src/model3",
    "PROJECT/LICENSE",
    "PROJECT/Makefile",
    "PROJECT/readme.md"
]

# Create the directories and files
for path in project_structure:
    if '.' in os.path.basename(path):  # if the path is a file
        with open(path, 'w') as f:
            if "LICENSE" in path:
                f.write("MIT License\n\nCopyright (c) 2024\n")
            elif "readme.md" in path:
                f.write("# Project Title\n\nA brief description of the project.\n")
            elif "Makefile" in path:
                f.write("# Makefile content\n")
    else:  # if the path is a directory
        os.makedirs(path, exist_ok=True)
        gitkeep_path = os.path.join(path, ".gitkeep")
        with open(gitkeep_path, 'w') as f:
            pass

print("Project structure with files and .gitkeep files created successfully!")

