# streamlit-experiments
Hacking with Streamlit on whatever I find interesting.

## Gotchas

1) Virtualenv Location
-------------------

You can't run this with a virtualenv set within the top level of your repo.

Do something like this:

    python3 -m venv ~/streamlitenv
    source ~/streamlitenv/ve/activate


Not this:

    cd repo/
    pyvenv ve 
    source ve/bin/activate


