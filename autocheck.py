fp = open("details.txt", "r")
malefile = open("male.txt", "w")
femalefile = open("female.txt", "w")
others = open("others.txt", "w")
for line in fp:
    words=line.split( )
