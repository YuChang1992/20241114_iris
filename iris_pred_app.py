import streamlit as st

ps = st.navigation(
    [
        st.Page("pages/page1.py", title="鳶尾花品種預測", icon="🌼"),  # path(路徑), title(名稱), (圖示)
        st.Page("pages/page2.py", title="鳶尾花樣本分布", icon="📍")
    ]
)

ps.run()
