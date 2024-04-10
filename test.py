def swap_case(s):
    str = s
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                str[i] = s[i].lower()
            else:
                str[i] = s[i].upper()
    return s

if __name__ == '__main__':
    s = input()
    # print(s)
    result = swap_case(s)
    print(result)