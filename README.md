# eng2jpn_srv
ほんやくコンニャク～（ドラ〇もん声）  

英語論文をコピペしてグーグル翻訳に投げるとき，改行が入ってめんどくさいときありますよね．  
このWebアプリケーションでは，英文を入力する（改行が入っててもOK）と日本語訳してくれます．  

## 必要なもの
```
python3
pip3
```

## インストール
```
pip3 install bottle
pip3 install googletrans
```

## 動作確認済み環境
Cygwin  

## セットアップ
1. python3 eng2jpn_srv.py
2. ブラウザでlocalhost:8080にアクセス(デフォルトの場合)

## 使い方
1. English欄に英文を入力する．（改行が変に入っててもOK）
2. translate!ボタンをクリック．
3. Japanese欄に日本語訳が出力される．


