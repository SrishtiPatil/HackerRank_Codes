def minion_game(string):
    SScore, KScore =0, 0
    string = list(string.lower())
    n = len(string)
    vowels = 'aeiou'
    for i in range(n):
        if string[i] in vowels:
            KScore+= n-i
        else:
            SScore+=n-i
    if SScore>KScore:
        print("Stuart",SScore)
    elif KScore>SScore:
        print("Kevin",KScore)
    else:
        print("Draw")

