# importを使いGUIに出力する
# pythonで様々なものが作成可能ということを伝えてください．もし作品があればそれを見せてください．
# pythonが楽しそうだと思ってもらいたいです

# インポートで機能を追加できる
import tkinter

root = tkinter.Tk()
root.title("画面にもじを表示する")

# 画面サイズを設定する
root.geometry("800x600")

label = tkinter.Label(root, text="test")
label.place(x=200, y=100)

root.mainloop()

"""
1行ごとに一緒にプログラムしていき，結果に対して説明をすることを考えています．
説明のあと自分で少し内容を変えたプログラムを書いてもらってください．
もしも，時間が余ったりしましたらテーマに沿った課題を与えてください．
"""