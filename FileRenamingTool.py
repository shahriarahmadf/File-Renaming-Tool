# FileRenamingTool V1.1
# Important Note:
# The source folder must be on the same drive as the python code file.
# The renamed files will go to the same folder as the FileRenamingTool.py file is.
# So it is advised that the FileRenamingTool.py is put in the same folder as the source.

import os
Src = input('Enter source of the files: ')
name = input('What do you want to replace the filename with? YOURINPUT001 is the format: ')

list = os.listdir(Src)
print(list)
for i in range (0,len(list)):
    print(list[i])
    ren = name + str(i) + ".jpg"
    des = Src + list[i]
    os.rename(des,ren)

print('Your work is done. Please check.')

#Developed by - Shahriar Ahmad Fahim E-mail:shahriarahmadf@gmail.com