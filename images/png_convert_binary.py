import io
import os
import sys
import glob
import base64
import PySimpleGUpythonI as sg

# コードに変換したい画像を指定
fname = sg.popup_get_file('week1.text1.PNG')

# コードの保存先フォルダ指定
save_path = sg.popup_get_folder('images')

# 読み込んだ画像をコードに変換
# base64のbytesデータ
c = base64.encodestring(open(fname, 'rb').read())
print('コード文字数:', len(c))

# basenameでファイル名を取得して、splitextで名前と拡張子に分割
# titleとextに代入（アンパック）
title, ext = os.path.splitext(os.path.basename(fname))
print('画像ファイル名:', title)
print('拡張子:', ext)

# テキストファイルに保存
with open(save_path + "/" + str(title) +str("_base64") + '.txt', "wb") as f:
    f.write(c)
