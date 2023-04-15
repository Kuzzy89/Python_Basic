first = int(input())
end = int(input())
magic_num = int(input())

count = 0
is_found = False

for i in range(first, end + 1):
    for j in range(first, end + 1):
        count += 1

        if i + j == magic_num:
            print(f"Combination N:{count} ({i} + {j} = {magic_num})")
            is_found = True
            break

    if is_found:
        break
if not is_found:
    print(f"{count} combinations - neither equals {magic_num}")
