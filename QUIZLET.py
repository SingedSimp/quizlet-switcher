with open("vocab.txt", "r") as f: # open vocab.txt in reading mode
    lines = f.readlines() # get an array of the contents of the file
    f.close() # close the file to avoid accidental uses
ll = [] # Initialize a new array to add the strings to
for line in lines: # for each line in the file
    line = line.strip("\n").split(" - ") # strip the newlines from the text, and split it into two arrays.
    ll.append(f"{line[1]} - {line[0]}\n") # add the arrays backwards to reverse the order

with open("newvocab.txt", "w+") as f: # open a text file, make it if needed ("+")
    for l in ll: # for line in the sorted lines
        f.write(l) # write the line to the file