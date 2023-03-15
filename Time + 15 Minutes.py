init_hour = int(input())
init_min = int(input())

init_time = (init_hour * 60) + init_min + 15

hour = init_time // 60
minute = init_time % 60

if hour > 23:
    hour = 0

if minute < 10:
    print(f"{hour}:0{minute}")
else:
    print(f"{hour}:{minute}")
