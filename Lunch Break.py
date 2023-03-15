from math import ceil

show = str(input())
duration_episode = int(input())
duration_break = int(input())

lunch_time = duration_break * 1/8
relax_time = duration_break * 1/4

break_left = duration_break - lunch_time - relax_time

diff = abs(break_left - duration_episode)
round_diff = ceil(diff)
if break_left >= duration_episode:
    print(f"You have enough time to watch {show} and left with {round_diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {show}, you need {round_diff} more minutes.")



