Aim: program to prasent all small and capital vowel in string.
s = input()
n = len(s)
for i in range(n):
    if s[i] == "a" or s[i]== "A" and s[i] == "e" or s[i] == "E" and s[i] == "i" or s[i] == "I" and s[i] == "u" or s[i] == "U" and s[i] == "o" or s[i] == "O" :
        print(s)
        break
    else:
        print("not accept")
else:
    pass
