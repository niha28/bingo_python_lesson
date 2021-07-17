# ifについて学び、条件分岐を理解する

# if 条件式: で条件式がTrueであればプログラムが実行される
# Trueはあっている，Falseは間違っているということ
if True:
    print("Hello,Warld")
if False:
    print("Hello,Warld")

# ==で一致しているかどうか
x = 3
if x == 3:
    print("xは3です")

# elif 条件式: と else: で複数の条件分岐を記述することができる
y = 4

if y == 2:
    print("yは2です")
elif y == 3:
    print("2でなければyは3です")
else:
    print("yは2でも3でもないです")

# 様々な条件式
# 値の大小を比較する:<, >, <=, >=, ==, !=
z = 108

if 1 <= z <= 100:
    z = z * 5
    print(z)
elif z == 108:
    print("煩悩バンザイ")
elif z != 0:
    print(False)
else:
    print("ぎょえええええ")

# and, or, notで複数の条件式を指定できる
a = 50
b = 0
if 0<=a<=50 and b==0:
    print("aは0以上50以下で，bは0です")

if a == 50:
    if b == 0:
        print("aは50，bは0です")



# 作品例:じゃんけんゲームV2

import random

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




