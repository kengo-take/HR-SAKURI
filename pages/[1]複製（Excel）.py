import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(page_icon="📝")
st.header('複製（Excel）')

# ファイルアップロード
st.error('※Excelファイルの場合はコチラ')
uploaded_files = st.file_uploader('複製する原稿をアップロードしてください。', type=["xlsx", "xls"])

# ファイルがアップロードされた場合
if uploaded_files is not None:
    try:
        df = pd.read_excel(uploaded_files)
        st.success("ファイルが正常に読み込まれました。")
        st.write(df)
    except Exception as e:
        st.error(f"エラー: {e}")
 
    # 簡単なデータ処理
    processed_df = df.loc[df.index.repeat(df[df.columns[0]])]
    processed_df = processed_df.drop(df.columns[0], axis = 1)

 
    # 処理結果をCSVとしてダウンロード
    csv = processed_df.to_csv(index = False).encode('utf-8')
    st.download_button(
        label="複製した原稿をダウンロードする",
        data=csv,
        file_name='processed_data.csv',
        mime='text/csv',
    )