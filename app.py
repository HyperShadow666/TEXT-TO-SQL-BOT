import streamlit as st
from model import generate_sql

# Sidebar setup
with st.sidebar:
    st.markdown("### About SQL-y")
    st.write("SQL-y is a chatbot powered by Transformer that can assist you with SQL queries.")
    st.write("Feel free to SQL-y your desired promps")
    st.markdown("---")  # Add a horizontal line for separation
    st.write("*Made by:*")
    st.write("⦿ Houda Moudni")
    st.write("⦿ Chadi Mountassir")

# Columns for logo and title
image_column, title_column = st.columns([1, 2]) 
with image_column:
    st.image("./static/logo.jpg", use_column_width=True)  # Adjust the width ratio as needed
with title_column:
    st.title("SQL-y")
    st.caption("A SQLBot powered by Transformer")


prompt = st.chat_input('pass your prompt here')



# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you?"}]

# Display chat messages in a container to keep the input field at the bottom
chat_container = st.container()

with chat_container:
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

# Process user input and response
if prompt:
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Generate SQL response
    response = generate_sql(prompt)

    # Add assistant message to session state
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)

