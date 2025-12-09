import requests
import io
import pandas as pd
import streamlit as st

@st.cache_data
def load_excel():
    url = "https://raw.githubusercontent.com/Thomasplatt76/univ101/main/Final%20Project%20Data.xlsx"
    response = requests.get(url)
    return pd.read_excel(io.BytesIO(response.content))

df = load_excel()

button_clicked = False
prompt_list = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))

st.title("UNIV 101 Time Capsule")

selected_prompt = st.selectbox("✨Select Prompt", prompt_list.values())
selected_row = df[df.iloc[:, 1] == selected_prompt]

st.write("#### 📘Prompt")
st.write(f"{selected_row.iloc[0,2]}")

st.write("#### ✍️My Response")
st.write(f"{selected_row.iloc[0,3]}")

st.write("#### 🧑‍🏫Teachers Response")
st.write(f"{selected_row.iloc[0,4]}")

talk_text = selected_row.iloc[0,6]
talk_link = selected_row.iloc[0,5]
label = selected_row.iloc[0,7]

st.markdown("""
<style>
.always-blue-underline a {
    color: inherit !important;
    text-decoration: underline !important;
    text-decoration-color: #4DA3FF !important;  /* blue underline */
    text-underline-offset: 3px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="always-blue-underline">
        <h6>✍️ {label}: 🔗 <a href="{talk_link}" target="_blank">{talk_text}</a></h6>
    </div>
    """,
    unsafe_allow_html=True
)
