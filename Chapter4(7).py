def compute_grade():
    score = input('Enter score - ')
    try:
        score = float(score)
    except:
        print('Bad score')

    if score > 1.0:
        print('Bad Score')
    else:
        if 1.0 >= score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        elif score > 0.6:
            print('F')


compute_grade()
