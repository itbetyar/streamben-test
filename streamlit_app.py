import streamlit as st

st.title("IT Betyár Streamlit minta")
st.subheader("I am a subheader!")

st.write("Sima write elem")
st.write("Ezt a sort a github codespace-ben hoztam létre")

st.text(" Ez egy sima **text**, mint ilyen a csillagok nem \"bold-olnak\" semmit")
st.markdown("---")

st.markdown("[Google link](https://www.google.com)")

st.image("kep.jpg", caption="Valami", width=150)

st.audio("zene.mp3")
