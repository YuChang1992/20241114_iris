# 在終端機安裝 pip install streamlit

# streamlit hello
# 跳出註冊畫面直接按Enter

# 參考
# https://docs.streamlit.io/develop/quick-reference/cheat-sheet

import numpy as np
import pandas as pd
import streamlit as st


# # 文字輸出
# st.title("Fixed width text")
# st.header("My header")
# st.text("Fixed width text")
# st.write("123")
# st.write("## 123")  # 一個#代表標題一，最多到六個

# # 表格輸出
# a = np.array([10,20,30,40])
# st.write(a)

# df = pd.DataFrame({"name":["JOE","ALEX","JANE"],"age":[19,20,21]})
# st.write(df)
# st.table(df)  # 網頁表格

# st.info("456")  # 提示重要信息


# 核取方塊
st.write("核取方塊")
cb = st.checkbox("是否為本國人")  # 名稱
if cb:
    st.info("是")
else:
    st.info("否")


# 選項按鈕
st.write("選項按鈕")
rb = st.radio("性別", ["男性","女性","第三性"])
st.info(rb)


# 下拉選單
st.write("下拉選單")
se = st.selectbox("縣市",["台北","新北","桃園","新竹","苗栗"])
st.info(se)

se2 = st.selectbox("學歷",["高中","高職","大學","碩士","博士"],key="se2")
st.info(se2)


# 按鈕
st.write("按鈕")
# def check():
#     st.text("123456")
# btn = st.button("喜歡")
# btn2 = st.button("不喜歡",key="btn2")
# if btn:
#     st.info("喜歡")
#     # check()
# elif btn2:
#     st.info("不喜歡")

# t = " "
# btn = st.button("喜歡")
# btn2 = st.button("不喜歡",key="btn2")
# if btn:
#     t = "喜歡"
# elif btn2:
#     t = "不喜歡"
# st.info(t)

def get_user_btn():
    btn = st.button("喜歡")
    btn2 = st.button("不喜歡", key="btn2")

    if btn:
        return "喜歡"
    elif btn2:
        return "不喜歡"
    else:
        return "未選擇"

t = get_user_btn()

st.info(t)


# 滑桿
st.write("滑桿")
num = st.slider("選擇數量",2,20,step=2)
st.info(num)


# 側邊欄
st.write("側邊欄")
se3 = st.sidebar.selectbox("年齡",[18,19,20,21,22],key="se3")
st.sidebar.info(se3)


# 分欄
cols = st.columns(4)
with cols[0]:
    n0 = st.number_input("000",key="n0")
with cols[1]:
    n1 = st.number_input("111",key="n1")
with cols[2]:
    n2 = st.number_input("222",key="n2")
with cols[3]:
    n3 = st.number_input("333",key="n3")
sum = n0+n1+n2+n3
st.write(n0,n1,n2,n3)
st.info(sum)