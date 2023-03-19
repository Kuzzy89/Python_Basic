tail = input()
body = input()
head = input()

vse = [tail, body, head]

vse[0], vse[2] = vse[2], vse[0]
print(vse)

