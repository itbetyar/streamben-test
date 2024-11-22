import streamlit as st


if "counter" not in st.session_state:
    st.session_state.counter = 0

# Define actions
def increment():
    st.session_state.counter += 1

def reset():
    st.session_state.counter = 0

#* #######################################################

st.title('Hello')

st.divider()
col1, col2 = st.columns([1,1])

my_radio = col1.radio("Válassz:", options=["Egyik", "Másik", "Harmadik"])
col2.write(f"Radio választás: {my_radio}")
if my_radio == "Egyik":
    col2.write("A radio az egyik-en áll!")
st.divider()


coll1, coll2 = st.columns([1,1])

my_dropdown = coll1.selectbox("Válasszál", options=["Item A", "Item B", "Item C"])
coll2.write(f"Dropdown választás: {my_dropdown}")

st.divider()
st.write("Alább megjelenik a kép ha a radio a \"masik\" állásban van és a dropdown az Item B-n áll")
if my_radio == "Másik" and my_dropdown == "Item B":
    st.image("kep.jpg", width=300)
else:
    st.markdown("<div style='height:190px;'></div>", unsafe_allow_html=True)
st.divider()

# Display counter value
st.write(f"Counter value: {st.session_state.counter}")

# Buttons to modify session state
st.button("Increment", on_click=increment)
st.button("Reset", on_click=reset)