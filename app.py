#app ui

import streamlit as st

from utils import generate_script 

#styling
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: blue;
    color: white;
}
div.stButton > button:hover {
    background-color: lime;
    color: white;
}
</style>""", unsafe_allow_html = True)

#create session variable
if 'API_Key' not in st.session_state:
    st.session_state['API_Key'] = ''
st.title('YT Scripting .....##')

#Sidebar to capture openapi api key
st.sidebar.title("API----KEY")
st.session_state['API_Key'] = st.sidebar.text_input("Enter API KEY", type = "password")

#Capture User Inputs
prompt = st.text_input('Video topic', key="prompt")
video_length = st.text_input("expected length", key = "video_length")
creativity = st.slider('Creativity Bar - ( 0 - 1) SCALE', 0.0,1.0,0.2, step =0.1)
submit = st.button("generate script")

if submit:
    if st.session_state['API_Key']:
        search_result, title,script = generate_script(prompt,
                                                video_length,
                                                creativity,
                                                st.session_state['API_Key'])
        st.success("Script Generated ...")

        #Title
        st.subheader("TITLE")
        st.write(title)

        #display script
        st.subheader("Script...")
        st.write(script)                                       

    else:
        st.error("provide correct api key")