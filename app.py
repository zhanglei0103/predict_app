import streamlit as st

st.set_page_config(page_title="文本回显工具", page_icon="📝")

st.title("📝 文本回显工具")

# 获取用户输入
user_input = st.text_input("请输入任意文本：", placeholder="在这里输入...")

# 输出显示
if user_input:
    st.success("输出结果：")
    st.info(user_input)