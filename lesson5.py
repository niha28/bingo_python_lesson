# 関数の使い方を学び作品をまとめる

# 引数がある
def tashizan(x, y):
    print(x+y)

tashizan(1, 2)

# 戻り値がある
def name():
    return "須貝元"

print(name())

# 関数外の変数を扱う場合globalで定義する
li =[]
def add_list(new):
    global li
    li.append(new)
    return li

new_li = add_list(3)
print(new_li)



import random
def janken():
    T = [None, "グー", "チョキ", "パー"]

    print("じゃんけんをします")
    print("1:グー\n2:チョキ\n3:パー")
    a = input("あなた:")

    your = int(a)
    enemy = random.randint(1, 3)

    win = "あなたの勝ち!!"
    lose = "あなたの負け!!"
    dorw ="あいこ!!"

    if your == enemy:
        judge = dorw

    elif your == 1:
        if enemy == 2:
            judge = win
        elif enemy ==3:
            judge = lose

    elif your == 2:
        if enemy == 3:
            judge = win
        elif enemy ==1:
            judge = lose

    elif your == 3:
        if enemy == 1:
            judge = win
        elif enemy ==2:
            judge = lose

    print(f"あなたの手は{T[your]}です\n")
    print(f"敵の手は{T[enemy]}です\n")
    print(f"結果は{judge}")

janken()

