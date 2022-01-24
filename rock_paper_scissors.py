import random


user_input = input("Georgian(Qartulad) / English:  1 or 2?  ")

data = {
    '1': "MAKRATELI",
    '2': "CHA",
    '3': "QAGALDI"
}
data_eng = {
    '1': "scissors",
    '2': "rock",
    '3': "paper"
}
# number = random.choice(range(1,4))
points = 15

your_poin = 0
comp_point = 0


if user_input == "1":
    print("gamarjoba,  shen tamashob jeirans da aucilebelia daimaxsovro, rom tamashistvis aucilebelia sityvierad chawero mnishvnelobebi")
    print(" MAKRATELI / makrateli")
    print(" CHA / cha")
    print(" QAGALDI / qagaldi")
    print("Tamashob sul 15 raunds, ")
    print("===================================================================================================================================")
    while True:
        if points > 0:
            com_num =str(random.choice(range(1,4)))
            usr_num =str(input("kompiuterma gaaketa archevani, axla sheni jeria???  >>>  "))
            print(">>> ---------------------------------------------------------------")
            if com_num == "1" and usr_num.lower() == "makrateli":
                print(f" Comp - {data[com_num]} /  shen - {usr_num}")
                your_poin += 0
                comp_point += 0
                print(f"comp-{comp_point}  /  shen-{your_poin}  darcha {points} xeli")

            elif com_num == "1" and usr_num.lower() == "cha":
                print(f" Comp - {data[com_num]} /  shen - {usr_num}")
                your_poin += 1
                comp_point += 0
                print(f"comp-{comp_point}  /  shen-{your_poin} darcha {points} xeli")

            elif com_num == "1" and usr_num.lower() == "qagaldi":
                print(f" Comp - {data[com_num]} /  shen - {usr_num}")
                your_poin += 0
                comp_point += 1
                print(f"comp-{comp_point}  /  shen-{your_poin} darcha {points} xeli")

            elif com_num == "2" and usr_num.lower() == "makrateli":
                print(f" Comp - {data[com_num]} /  shen - {usr_num}")
                your_poin += 0
                comp_point += 1
                print(f"comp-{comp_point}  /  shen-{your_poin} darcha {points} xeli")

            elif com_num == "2" and usr_num.lower() == "cha":
                print(f" Comp - {data[com_num]} /  shen - {usr_num}")
                your_poin += 0
                comp_point += 0
                print(f"comp-{comp_point}  /  shen-{your_poin}  darcha {points} xeli")

            elif com_num == "2" and usr_num.lower() == "qagaldi":
                print(f" Comp - {data[com_num]} /  shen - {usr_num}")
                your_poin += 1
                comp_point += 0
                print(f"comp-{comp_point}  /  shen-{your_poin}  darcha {points} xeli")

            elif com_num == "3" and usr_num.lower() == "makrateli":
                print(f" Comp - {data[com_num]} /  shen - {usr_num}")
                your_poin += 1
                comp_point += 0
                print(f"comp-{comp_point}  /  shen-{your_poin}  darcha {points} xeli")

            elif com_num == "3" and usr_num.lower() == "cha":
                print(f" Comp - {data[com_num]} /  shen - {usr_num}")
                your_poin += 0
                comp_point += 1
                print(f"comp-{comp_point}  /  shen-{your_poin}  darcha {points} xeli")

            elif com_num == "3" and usr_num.lower() == "qagaldi":
                print(f" Comp - {data[com_num]} /  shen - {usr_num}")
                your_poin += 0
                comp_point += 0
                print(f"comp-{comp_point}  /  shen-{your_poin}  darcha {points} xeli")

        elif points == 0:
            print("----------------------------------------------------------------------------")
            print(f"tamashi morcha, shedegi Comp-{comp_point} da shen-{your_poin}")
        points -= 1
elif user_input == "2":
    print("Hello, you are playing popular game rock paper scissors, provide in lower letter ")
    print(" rock")
    print(" paper")
    print(" scissors")
    print("you have 15 rounds, ")
    print("===================================================================================================================================")
    while True:
        if points > 0:
            com_num =str(random.choice(range(1,4)))
            usr_num =str(input("computer already chose , now it is your turn???  >>>  "))
            print(">>> ---------------------------------------------------------------")
            if com_num == "1" and usr_num.lower() == "scissors":
                print(f" comp - {data_eng[com_num]} /  you - {usr_num}")
                your_poin += 0
                comp_point += 0
                print(f"comp-{comp_point}  /  you-{your_poin}  left {points} round")

            elif com_num == "1" and usr_num.lower() == "rock":
                print(f" comp - {data_eng[com_num]} /  you - {usr_num}")
                your_poin += 1
                comp_point += 0
                print(f"comp-{comp_point}  /  you-{your_poin} left {points} round")

            elif com_num == "1" and usr_num.lower() == "paper":
                print(f" comp - {data_eng[com_num]} /  you - {usr_num}")
                your_poin += 0
                comp_point += 1
                print(f"comp-{comp_point}  /  you-{your_poin} left {points} round")

            elif com_num == "2" and usr_num.lower() == "scissors":
                print(f" comp - {data_eng[com_num]} /  you - {usr_num}")
                your_poin += 0
                comp_point += 1
                print(f"comp-{comp_point}  /  you-{your_poin} left {points} round")

            elif com_num == "2" and usr_num.lower() == "rock":
                print(f" comp - {data_eng[com_num]} /  you - {usr_num}")
                your_poin += 0
                comp_point += 0
                print(f"comp-{comp_point}  /  you-{your_poin}  left {points} round")

            elif com_num == "2" and usr_num.lower() == "paper":
                print(f" comp - {data_eng[com_num]} /  you - {usr_num}")
                your_poin += 1
                comp_point += 0
                print(f"comp-{comp_point}  /  you-{your_poin}  left {points} round")

            elif com_num == "3" and usr_num.lower() == "scissors":
                print(f" comp - {data_eng[com_num]} /  you - {usr_num}")
                your_poin += 1
                comp_point += 0
                print(f"comp-{comp_point}  /  you-{your_poin}  left {points} round")

            elif com_num == "3" and usr_num.lower() == "rock":
                print(f" comp - {data_eng[com_num]} /  you - {usr_num}")
                your_poin += 0
                comp_point += 1
                print(f"comp-{comp_point}  /  you-{your_poin}  left {points} round")

            elif com_num == "3" and usr_num.lower() == "paper":
                print(f" comp - {data_eng[com_num]} /  you - {usr_num}")
                your_poin += 0
                comp_point += 0
                print(f"comp-{comp_point}  /  you-{your_poin}  left {points} round")

        elif points == 0:
            print("----------------------------------------------------------------------------")
            print(f"Game is over. score: Computer-{comp_point} and you-{your_poin}")
        points -= 1

