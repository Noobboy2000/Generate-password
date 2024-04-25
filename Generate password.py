import random

user = random.randint(1000,9000)
print("UserID: @",user)
password = ["WC12*>?@#h&&", "PL56##$5?!!d", "l<<24%$@@tt)","A#cbvZZ%&^12",
            "dftol>?144$%0", "1d@3##>ax$xc", "k19*&AQWb_00", "1__DFG$#2@>b"]

password.__len__()
password.sort()
password = random.choice(password)
print(f"passwords: {password}")
