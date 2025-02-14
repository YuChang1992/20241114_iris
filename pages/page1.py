import streamlit as st
import pandas as pd
import joblib

st.title("鳶尾花品種預測")

# 載入模型
knn = joblib.load("model/KNN.joblib")
lr = joblib.load("model/LR.joblib")
rf = joblib.load("model/RF.joblib")
svm = joblib.load("model/SVM.joblib")

m = st.sidebar.selectbox("### 請選擇模型:",("KNN","LogisticRegression","RandomForest","SVM"))
if m == "KNN":
    model = knn
elif m == "LogisticRegression":
    model = lr
elif m == "RandomForest":
    model = rf
elif m == "SVM":
    model = svm

# 佈置元件
df = pd.read_csv("iris.csv")
se1 = st.slider("### 花萼長度(cm):",float(df["sepal.length"].min() - 0.5) ,  # 抓sepal.length欄位最小值當滑桿的起點
                float(df["sepal.length"].max() + 0.5),  # 最大值當滑桿的終點
                float(df["sepal.length"].mean()))  # 平均值當滑桿的中間點

se2 = st.slider("### 花萼寬度(cm):",float(df["sepal.width"].min() - 0.5) ,
                float(df["sepal.width"].max() + 0.5),
                float(df["sepal.width"].mean()))

se3 = st.slider("### 花瓣長度(cm):",float(df["petal.length"].min() - 0.5) ,
                float(df["petal.length"].max() + 0.5),
                float(df["petal.length"].mean()))

se4 = st.slider("### 花瓣寬度(cm):",float(df["petal.width"].min() - 0.5) ,
                float(df["petal.width"].max() + 0.5),
                float(df["petal.width"].mean()))

st.image("iris.png")

# 進行預測
labels = ["Setosa", "Versicolor", "Virginica"]
if st.button("進行預測"):
    X = [[se1,se2,se3,se4]]
    y = model.predict(X)
    # st.write(y)
    st.write("### 預測結果",labels[y[0]])
