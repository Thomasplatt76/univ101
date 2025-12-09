import webbrowser
import streamlit as st
import pandas as pd
import io
from supabase import create_client

button_clicked = False

# ---------------------------------------
# CONNECT TO SUPABASE
# ---------------------------------------
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
BUCKET = st.secrets["SUPABASE_BUCKET"]
FILE_PATH = st.secrets["SUPABASE_FILE"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------------------------------------
# DOWNLOAD EXCEL FILE FROM STORAGE
# ---------------------------------------
file_bytes = supabase.storage.from_(BUCKET).download(FILE_PATH)

df = pd.read_excel(io.BytesIO(file_bytes))


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
