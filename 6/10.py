def aaa(a):
    if a<=1:
        return 1
    return aaa(a-1)+aaa(a-2)

for i in range(40):
    print(aaa(i))