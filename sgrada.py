floor = int(input())
flat_per_floor = int(input())

flat_number = 0
flat_name = ""

for floor_n in range(floor, 0, -1):
    print()
    for flat_n in range(flat_per_floor):

        flat_number = floor_n + flat_n

        if floor_n == floor:
            flat_name = f"L{flat_number}{flat_n}"

        elif floor_n % 2 == 0:
            flat_name = f"O{flat_number}{flat_n}"

        elif floor_n % 2 != 0:
            flat_name = f"A{flat_number}{flat_n}"

        print(flat_name, end=" ")

