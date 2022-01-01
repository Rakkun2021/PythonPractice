score = input('Enter Score -')
# noinspection PyBroadException
try:
    score = float(score)
except:
    print('Bad Score')
    quit()                             #Assign Variables; Assign Correct Data types; Describe the process; Print.
if 0.0 <= score <= 1.0:
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    elif score < 0.6:
        print('F')
else:
    if score > 1.0:
        print('Bad Score')
