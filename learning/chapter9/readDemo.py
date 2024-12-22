import os


script_dir = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(script_dir,"input.txt")

f = open(filePath)

data = f.read()
print(data)

f.close()