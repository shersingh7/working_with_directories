from pathlib import Path

# path = Path("new_dir")
# # create dir
# path.mkdir()
# # create remove
# path.rmdir()

path = Path()

# prints all the files in current dir
for file in path.glob('*.*'):
    print(file)

