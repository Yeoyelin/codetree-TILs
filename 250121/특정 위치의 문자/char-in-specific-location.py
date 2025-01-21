arr = ['L', 'E', 'B', 'R', 'O', 'S']

word = input()

# 해당 문자가 리스트에 없는 경우
if word not in arr:
    print("None")
# 해당 문자가 리스트에 있는 경우
else:
    print(word.index(word))