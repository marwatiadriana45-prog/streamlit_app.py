import streamlit as st
import random
import pandas as pd

st.title("Prize → Random Number Picker")

st.subheader("Number range")
start = st.number_input("Start of range", value=1, step=1)
end = st.number_input("End of range", value=100, step=1)

st.subheader("Prizes")
st.write("Enter one prize per line (example: 1st Prize, 2nd Prize, etc.)")

default_prizes = "\n".join([f"Prize {i}" for i in range(1, 11)])
prize_text = st.text_area("Prize names", value=default_prizes, height=200)

unique_numbers = st.checkbox("Use unique numbers (no repeats)", value=True)

if st.button("Pick numbers for prizes"):
    start_i, end_i = int(start), int(end)

    prizes = [p.strip() for p in prize_text.splitlines() if p.strip()]

    if not prizes:
        st.error("Please enter at least one prize name.")
        st.stop()

    range_size = end_i - start_i + 1
    if range_size <= 0:
        st.error("End of range must be greater than or equal to start.")
        st.stop()

    if unique_numbers and range_size < len(prizes):
        st.error(
            f"Range is too small for unique picks. "
            f"You have {len(prizes)} prizes but only {range_size} numbers available."
        )
        st.stop()

    # Pick numbers
    if unique_numbers:
        picks = random.sample(range(start_i, end_i + 1), len(prizes))
    else:
        picks = [random.randint(start_i, end_i) for _ in prizes]

    results = pd.DataFrame({"Prize": prizes, "Number": picks})

    st.success("Done!")
    st.dataframe(results, use_container_width=True)
