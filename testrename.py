

# this works run it any put any files into test and they will be renamed appropriately with 4 leading zeros


import os
#"""
#Renames the multiple file within the same directory with appending number
#"""
path = 'test'
files = os.listdir(path)
i = 1

for file in files:
    filename, file_extension = os.path.splitext(file)
    num=str(i).zfill(5)
    os.rename(os.path.join(path, file), os.path.join(path, str('G') + str(num) + file_extension))
    #num = num.zfill(5)
    i = i+1