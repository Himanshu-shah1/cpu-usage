import streamlit as st
import pandas as pd
import random
import time

# ---------------- CONFIG ---------------- #
st.set_page_config(page_title="CPU Monitor", layout="wide")

st.title("🖥️ CPU Usage Monitor (Demo)")

FRAME_LENGTH = 200

# ---------------- SESSION STATE ---------------- #
if "cpu_perc" not in st.session_state:
    st.session_state.cpu_perc = []

placeholder = st.empty()

# ---------------- LOOP ---------------- #
for _ in range(200):  # simulate real-time
    cpu = random.randint(0, 100)  # demo CPU values

    st.session_state.cpu_perc.append(cpu)

    if len(st.session_state.cpu_perc) > FRAME_LENGTH:
        st.session_state.cpu_perc.pop(0)

    with placeholder.container():
        st.subheader(f"Current CPU Usage: {cpu}%")
        df = pd.DataFrame(st.session_state.cpu_perc, columns=["CPU %"])
        st.line_chart(df)

    time.sleep(1)

# ---------------- FOOTER ---------------- #
st.markdown(
    "<hr><p style='text-align:center;color:gray;font-size:14px;'>Project Created by <b>Himanshu Shah</b></p>",
    unsafe_allow_html=True
)
