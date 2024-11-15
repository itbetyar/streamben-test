import streamlit as st
from PIL import Image

# List of example file paths
examples = [
    "imgs/banana.jpg",
    "imgs/bus.jpg",
    "imgs/arc.jpg"
]

# Dropdown or radio button for selecting examples
st.sidebar.header("Select an example")
selected_example = st.sidebar.radio("Choose an image", examples)

# Display the selected example
if selected_example:
    st.image(Image.open(selected_example), caption=f"Selected: {selected_example}")

# Upload image functionality
st.header("Upload your image")
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])

# Display uploaded image
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")
