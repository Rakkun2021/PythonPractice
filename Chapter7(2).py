fname = input('Enter file name: ')
fhand = open(fname)
count = 0
total = 0
try:
    fhand = open(fname)
except:
    print('File not found', fname)
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'): continue
    col_pos = line.find(':')
    number = line[col_pos + 1:]
    confidence = float(line(number)
    count = count + 1
    avg = confidence / count
    print('Average Spam confidence: ', avg)
