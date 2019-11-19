import streamlit as st
import pyttsx3

# PyTTSX examples:
# https://pyttsx3.readthedocs.io/en/latest/engine.html#examples

def start_engine():
    return pyttsx3.init()

def stop_engine(engine):
    engine.endLoop()

def speak_it(text):
    engine = start_engine()
    engine.say(text)
    #engine.startLoop(False)
    engine.runAndWait()
    engine.stop()

st.header("Text to Speech Toy")

text = st.empty()

value = ""
if st.button("Clear"):
    value = ""

inp = text.text_area("Speak the text written in this box.", value)

if st.button("Speak"):
    st.write("Speaking")
    speak_it(inp)


if st.button("Rate"):
    st.write("Current Speaking Rate is ")
    speak_it('My current speaking rate is ' + str(rate))
