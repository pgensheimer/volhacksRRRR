#r->R
import fileinput

#this function replaces lowercases r with capital Rs
def rReplace(filein):
    output = filein.replace("r","R")
    return output



if __name__ == "__main__":
    fileR = input("Please enter file: ")
    rfile = "R" + fileR
    writer = open(rfile, "w")
    reader = open(fileR, "r")
    
    filein = reader.read()
    
    nl = rReplace(filein)
    print("Your new file is: "+ rfile)
    writer.write(nl)
    
    writer.close()
    reader.close()
