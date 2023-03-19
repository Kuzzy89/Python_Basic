n = int(input())
word = input()

strings = []
cont_strings = []

for i in range(n):
    current_string = input()
    strings.append(current_string)

    if word in current_string:
        cont_strings.append(current_string)

# for i in range(len(strings) - 1, -1, -1):
#     element = strings[i]
#     if word not in element:
#         strings.remove(element)
print(strings)
print(cont_strings)