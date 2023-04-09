import os

import sys

if (len(sys.argv) < 2):
    print("Usage: python generate_tts.py <input file>")
    exit(1)

file= open(sys.argv[1], "r")

# write in a new file the content of the old file after 100 lines
j=0
i=0
if os.path.exists("./segments"):
    os.system("rm -rf ./segments")
os.mkdir("./segments")
filename="./segments/segment"+str(j)+".txt"
write = open(filename, "w")

for line in file:
    line.replace("“", "")
    line.replace("”", "")
    line.replace("’", "'")
    line.replace("‘", "")
    line.replace("…", ",")
    line.replace("–", ",")
    line.replace("—", ",")
    line.replace(")", ",")
    line.replace("(", ",")
    write.write(line)
    i+=1
    if i==200:
        write.close()
        i=0
        j+=1
        filename="./segments/segment"+str(j)+".txt"
        write = open(filename, "w")

write.close()
file.close()
