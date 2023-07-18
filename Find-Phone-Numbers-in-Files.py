import re
import os
result = []
def search(st):
    r = re.findall(r"\d{3}-\d{3}-\d{4}", st)
    if r:
        for phone_number in r:
            result.append(phone_number)
for folder, subfolders, files in os.walk("Employee"):
    for f in files:
        with open(os.path.join(folder, f), encoding = "utf-8") as my_file:
            text = my_file.read()
            search(text)
print(result)
#%%
