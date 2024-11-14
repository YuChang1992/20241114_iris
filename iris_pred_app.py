import streamlit as st

ps = st.navigation(
    [
        st.Page("pages/page1.py", title="IRIS品種預測", icon="🌼"),  # path(路徑), title(名稱), (圖示)
        st.Page("pages/page2.py", title="IRIS樣本分布", icon="📍")
    ]
)

ps.run()