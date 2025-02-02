import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(page_icon="📝")

st.title('SAKURI（サクリ）')
st.subheader('〜サクサク原稿クリエイト〜')

st.write('',unsafe_allow_html=True)
st.write("""
SAKURI(サクリ)は原稿を作成するための原稿作成ツールです。
<br><br>
##### ＜原稿作成手順＞

**[1]ベース原稿を作成して複製する**

原稿内の変更する情報は【例：[?職種名?]】のようにマークアップしてください。
         
<font color="red">複製する原稿本数は一番左に増やす原稿本数を記載してください。</font>
         
※ダウンロード時に一番左の複製数の列は削除されています。<br><br>""",unsafe_allow_html=True)


st.write("""**[2]複製した原稿のマークアップした箇所を置換する。**

置換の指示はエクセル上で行います。
エクセルはフォーマットを用いてください。

シート名は「原稿」と「変換指示」の２シートです。
         
「原稿」のシートには[1]で作成した複製した情報を貼り付けてください。
         
<font color="red">「変換指示」のシートの１行目には変換前の情報【例：[?職種名?]】を入力してください。
         
「変換指示」のシートの２行目以降には変換後の情報を入力してください。</font>
         
""",unsafe_allow_html=True)