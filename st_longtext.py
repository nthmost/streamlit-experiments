import streamlit as st

document = open('/Users/nthmost/epilepsy_set.txt').read()

st.markdown(f'<div style="color: green; font-size: small">{document}</div>',unsafe_allow_html=True)

