import webbrowser
import streamlit as st
import pandas as pd
button_clicked = False

df = pd.read_excel(r"C:\Users\thoma\Documents\Semester 1\UNIV 101\Final Project Data.xlsx")
prompt_list = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))

for x in prompt_list.values():
    print(x)

st.title("UNIV 101 Time Capsule")
selected_prompt = st.selectbox("✨Select Prompt", prompt_list.values())
selected_row = row = df[df.iloc[:, 1] == selected_prompt]

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
    color: inherit !important;         /* keep text normal color */
    text-decoration: underline !important;
    text-decoration-color: #4DA3FF !important;  /* blue underline */
    text-underline-offset: 3px;        /* spacing between text + underline */
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="always-blue-underline">
        <h6>{f"✍️ {label}"}:   🔗<a href="{talk_link}" target="_blank">{talk_text}</a></h6>
    </div>
    """,
    unsafe_allow_html=True
)
