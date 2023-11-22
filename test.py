import os

source = os.walk("dataset_copy")

for res in source:
    print(res)

print("==========")
source = os.walk("dataset_copy") # 因為迭代器在遍歷一次後就會指向末尾，再次遍歷時就不會返回任何內容。
for folder, subfolders, files in source:
    print(folder)
    for subfolder in subfolders:
        print(f'{folder} 的子資料夾 {subfolder}')
    for file in files:
        print(f'{folder} 的檔案有 {file}.')

print("==========")
ids = next(os.walk("dataset_copy/train/Images"))
print(ids)
print("No. of images = ", len(ids[2]))

