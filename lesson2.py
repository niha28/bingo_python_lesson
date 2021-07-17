# プログラミングの基礎である計算とデータの形を学ぶ
# 文字列と数字が違うものということだけしっかり伝えてください．

# データの形による出力の差
# pythonでは数字と文字は別々なもの
print(1)
# 数字の場合は計算される
print(1+2+3)
# 文字の場合はそのまま出る
print("1+2+3")

# 四則演算に関する演算子
# 和差積商ができる
print(3-2+1)
A = 3*2+(3-5)/2
print(A)
# 割り算のあまり
print(3%2)
# 割り算の切り捨て
print(7//3)
# 乗算
print(3**5)

# inputで入力された値は文字列
"""
print("足し算をするよ")
x = input("好きな数字を入力してね")
y = input("もう一つ好きな数字を入力してね")
print(x + y)
"""

print("足し算をするよ")
x = input("好きな数字を入力してね")
y = input("もう一つ好きな数字を入力してね")
# intで数字に変換できる
x = int(x)
y = int(y)
print(x+y)

import tkinter

def tashizan():
    mozi1 = entry1.get()
    mozi2 = entry2.get()
    x = int(mozi1)
    y = int(mozi2)
    button["text"] = x+y


root = tkinter.Tk()
root.title("keisan")

# 画面サイズを設定する
root.geometry("800x600")

label = tkinter.Label(root, text="Lets tashizan")
label.place(x=200, y=100)

entry1 = tkinter.Entry(width=10)
entry1.place(x=10, y=10)
entry2 = tkinter.Entry(width=10)
entry2.place(x=100, y=10)

button = tkinter.Button(text="tashizan", command=tashizan)
button.place(x=50, y=50)
root.mainloop()




