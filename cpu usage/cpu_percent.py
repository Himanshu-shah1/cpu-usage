import streamlit as st
import psutil
import pandas as pd
import time

# ---------------- CONFIG ---------------- #
st.set_page_config(page_title="CPU Monitor", layout="wide")

st.title("🖥️ Real-Time CPU Usage Monitor")
st.markdown("### 👨‍💻 Project Created by **Himanshu Shah**")

FRAME_LENGTH = 200

# ---------------- SESSION STATE ---------------- #
if "cpu_perc" not in st.session_state:
    st.session_state.cpu_perc = []

# ---------------- AUTO REFRESH LOOP ---------------- #
placeholder = st.empty()

for _ in range(1000):  # acts like animation frames
    cpu = psutil.cpu_percent()
    st.session_state.cpu_perc.append(cpu)

    # keep last 200 values
    if len(st.session_state.cpu_perc) > FRAME_LENGTH:
        st.session_state.cpu_perc.pop(0)

    # ---------------- UI UPDATE ---------------- #
    with placeholder.container():
        st.subheader(f"Current CPU Usage: {cpu}%")

        df = pd.DataFrame(st.session_state.cpu_perc, columns=["CPU %"])

        # Color logic similar to your code
        if len(st.session_state.cpu_perc) >= 20:
            st.line_chart(df)
        else:
            st.line_chart(df)

    time.sleep(1)
