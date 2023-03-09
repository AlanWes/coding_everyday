row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

choice = [int(x) for x in position]
x = choice[0]
y = choice[1]
x_int = int(x - 1)  #number
y_int = int(y - 1)  #lane

map_row = map[y_int]
map_row[x_int] = 'X'

print(f"{row1}\n{row2}\n{row3}")