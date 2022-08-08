
import os



def solider(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().splitlines()

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}.{format}")
            i +=1 

solider("C:\Users\skeer\Desktop\Python3.0\Exercises\solider","C:\Users\skeer\Desktop\Python3.0\Exercises\solider\test.txt", "txt")