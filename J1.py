R = int(input("number of regular boxes:"))
S = int(input("number of small boxes:"))

total_reg = 8 * R
total_small = 3 * S

total_cupckeas = total_reg + total_small

leftover = total_cupckeas - 28

print("the total number of cupcakes left over is:", leftover)