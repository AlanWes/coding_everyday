print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_imie1 = name1.lower()
lower_imie2 = name2.lower()

count_t = lower_imie1.count("t")
count_r = lower_imie1.count("r")
count_u = lower_imie1.count("u")
count_e1 = lower_imie1.count("e")
count_t_2 = lower_imie2.count("t")
count_r_2 = lower_imie2.count("r")
count_u_2 = lower_imie2.count("u")
count_e1_1 = lower_imie2.count("e")

count_l = lower_imie2.count("l")
count_o = lower_imie2.count("o")
count_v = lower_imie2.count("v")
count_e2 = lower_imie2.count("e")
count_l_2 = lower_imie1.count("l")
count_o_2 = lower_imie1.count("o")
count_v_2 = lower_imie1.count("v")
count_e2_2 = lower_imie1.count("e")

true_total = count_t + count_r + count_u + count_e1 + count_t_2 + count_r_2 + count_u_2 + count_e1_1
love_total = count_l + count_o + count_v + count_e2 + count_l_2 + count_o_2 + count_v_2 + count_e2_2

love_result = str(true_total) + str(love_total)
if int(love_result) < 10 or int(love_result) > 90:
    print(f"Your score is {love_result}, you go together like coke and mentos.")
elif int(love_result) >= 40 and int(love_result) <= 50:
    print(f"Your score is {love_result}, you are alright together.")
else:
    print(f"Your score is {love_result}.")