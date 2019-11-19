import streamlit as st


st.header('Hello (World)(?) in four different RTL languages.')

with st.echo():
    st.markdown('''
    <div dir="rtl">

    ببخشید؟

    مرحبا العالم؟

    שלום בעולם

    ہیلو دنیا
    </div>
    ''', unsafe_allow_html=True)

st.markdown('---')

st.header('Writing RTL in Markdown without any RTL marker.')
# &#x202b;

with st.echo():

    st.markdown('''
    Arabic:  عربى

    Greek: Ελληνικά

    We can often write Ελληνικά and عربى on the same line without a problem.
    ''')

st.markdown('---')

st.header('What happens when we input English in RTL mode?')

with st.echo():

    st.markdown('''&rlm;English backwards?&rlm;''')
    st.markdown('''<div dir="rtl">Maybe this will do it?</div>''', unsafe_allow_html=True)

