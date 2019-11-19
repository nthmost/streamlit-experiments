import os

import streamlit as st
import pandas as pd

DATADIR = os.path.join(os.path.expanduser('~'), 'Desktop/DATA/')

CODEBOOK = "Big5_codebook.txt"
DATAFILE = "Big5_data_small.csv"


with open(os.path.join(DATADIR, DATAFILE)) as fh:
    df = pd.read_csv(fh)
    st.write(df)

