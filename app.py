import streamlit as st
import requests

st.set_page_config(page_title="Lexyn 語境分析", layout="centered")

st.title("Lexyn Context Guard Demo")
st.markdown("🛡️ **語境安全檢測工具**")

text_input = st.text_area("請輸入欲分析的語句：", height=200)

if st.button("立即分析"):
    if not text_input.strip():
        st.warning("請先輸入文字。")
    else:
        with st.spinner("分析中，請稍候..."):
            try:
                response = requests.post(
                    "https://lexyn-gamania-demo-mdtq4m2rgdepidjhhnowci.streamlit.app/analyze",
                    json={"text": text_input}
                )
                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ 分析完成")
                    st.markdown(f"**語句風險等級：** `{data['risk_level']}`")
                    st.markdown(f"**建議重寫句子：** {data['rewritten']}")
                else:
                    st.error(f"伺服器回應錯誤：{response.status_code}")
            except Exception as e:
                st.error(f"連線錯誤：{str(e)}")
