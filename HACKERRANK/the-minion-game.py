if __name__ == '__main__':
    s = input()
    stuart, kevin = 0, 0
    n = len(s)
    for i in range(n):
        if s[i] in "AOEUI":
            kevin += n - i
        else:
            stuart += n - i
    
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")