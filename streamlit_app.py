import streamlit as st
import random

st.title("Pick 5 random numbers")

start = st.number_input("Start", value=1, step=1)
end = st.number_input("End", value=50, step=1)

if st.button("Pick numbers"):
    start, end = int(start), int(end)
    if end - start + 1 < 5:
        st.error("Range is too small to pick 5 unique numbers.")
    else:
        picks = sorted(random.sample(range(start, end + 1), 5))
        st.success(picks)
