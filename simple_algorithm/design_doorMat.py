n, m = map(int, input().split(" ")) # 7, 21


get_half = (n // 2)
side_man = (m - 3)//2 # 9 9
middle_man = 1#m-(side_man * 2)
rev_middle_man = (n - 2)
rev_side_man = (get_half) # = 3 33-(11*)
print(rev_middle_man)
side_belt = (m - n)//2 # = 3
# 21 - 

for i in range(get_half):
    print((side_man * '-').ljust(side_man-3)+(middle_man * '.|.').center(1)+(side_man * '-').rjust(side_man-3))
    side_man -= 3
    middle_man += 2

print((side_belt * '-').ljust(side_belt-3)+("WELCOME").center(middle_man)+(side_belt * '-').rjust(side_belt-3))

for i in range(get_half):
    print((rev_side_man * '-').ljust(rev_side_man)+(rev_middle_man*'.|.').center(1)+(rev_side_man*'-').rjust(rev_side_man))
    rev_side_man += 3
    rev_middle_man -= 2