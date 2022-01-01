fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
for line in fhand:
    line = line.upper()
    line = line.rstrip()
    print('Line: ', line)
