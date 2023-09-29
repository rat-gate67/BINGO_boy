import streamlit as st

st.title("ビンゴくん mk.1.1")
"---"

# 初期化
if "entered" not in st.session_state:
    st.session_state.entered = []

size = st.toggle("bigger")

entry_number =  st.number_input("No.",1,240,)
st.image(f"source/{entry_number}.png",use_column_width=size)

if st.button("entry"):
    if not entry_number in st.session_state.entered:
        st.session_state.entered.append(entry_number)
    elif entry_number in st.session_state.entered:
        "## 既出"
    else:
        "## エラー"


f"""
## entered number
{st.session_state.entered}
"""
