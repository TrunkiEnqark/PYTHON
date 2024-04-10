if __name__ == '__main__':
    s = input()
    cnt = [(0, ' ')] * 26
    # print(cnt[25][0])
    for i in range(len(s)):
        idx = ord(s[i]) - ord('a')
        # print(idx)
        cnt[idx] = (cnt[idx][0] + 1, s[i])
    cnt.sort(reverse=True)
    for i in range(3):
        print(cnt[i][0], cnt[i][1])