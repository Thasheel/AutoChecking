fp = open("details.txt", "r")
malefile = open("male.txt", "w")
femalefile = open("female.txt", "w")
others = open("others.txt", "w")
for line in fp:
    words=line.split( )
    if words[1]=="F":
        femalefile.write(line)
    if words[1]=="M":
        malefile.write(line)
    if words[1]=="O":
        others.write(line)

fp.close()


