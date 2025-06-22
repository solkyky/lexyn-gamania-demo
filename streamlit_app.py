import streamlit as st
import requests

st.set_page_config(page_title="Lexyn Context Guard Demo")

st.title("🛡️ Lexyn Context Guard Demo")
st.subheader("語境安全檢測工具")

user_input = st.text_area("請輸入欲分析的語句：", height=200)

if st.button("立即分析"):
    if not user_input.strip():
        st.warning("請先輸入語句")
    else:
        with st.spinner("正在分析中..."):
            try:
                # 連線到 FastAPI 後端 API
                api_url = "https://lexyn-gamania-demo.onrender.com/analyze"
                response = requests.post(api_url, json={"text": user_input})
                
                if response.status_code == 200:
                    result = response.json()
                    st.success("分析完成！")
                    st.markdown(f"**語句原文：** {result['input']}")
                    st.markdown(f"**風險等級：** {result['risk_level']}")
                    st.markdown(f"**建議改寫：** {result['rewritten']}")
                else:
                    st.error(f"API 錯誤（狀態碼 {response.status_code}）：{response.text}")
            except Exception as e:
                st.error(f"連線錯誤：{e}")
