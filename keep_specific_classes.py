import os

path="/path/of/txt/folder/" # give the path of txt folder
for file in os.listdir(path):

    with open(os.path.join(path,file), "r") as f: #read the lines of txt files
        lines = f.readlines()
        
        with open(os.path.join(path,file), "w") as f:
            for line in lines:
                if line.startswith("1"): # if the line starts with 1 it will not remove but if it starts 
                    #except 1 it removes that line
                    f.write(line)
                    print("-------------")
    
