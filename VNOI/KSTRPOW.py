string_1 = input()
string_2 = input()
times = int(input())

i = 0
calc_times = 0
while i + len(string_1) - 1 < len(string_2):
    print(string_2[i:i + len(string_1)])
    if string_2[i:i + len(string_1)] != string_1:
        print("NO");
        exit()
    i += len(string_1)
    calc_times += 1
    
if calc_times == times:
    print("YES")
else:
    print("NO")