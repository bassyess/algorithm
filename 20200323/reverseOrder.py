words = list(map(str, input().strip().split(',')))
def compare(s1, s2):
    if not s1:
        return True
    if not s2:
        return False
    for i in range(min(len(s1), len(s2))):
        # if ord(s1[i])>ord(s2[i]):
        #     return True
        # elif ord(s1[i])<ord(s2[i]):
        #     return False
        if s1[i]>s2[i]:
            return True
        elif s1[i]<s2[i]:
            return False
    return True if len(s1)<len(s2) else False
for i in range(len(words)):
    for j in range(i+1, len(words)):
        if compare(words[j], words[i]):
            words[i], words[j] = words[j], words[i]
print(",".join(words))
