
import streamlit as st
import anthropic
import os

st.set_page_config(page_title="Chatbot WiData", page_icon="🤖")

# Gestione API key: Streamlit Cloud usa st.secrets
# In locale usa la variabile d'ambiente
if "ANTHROPIC_API_KEY" in st.secrets:
    os.environ["ANTHROPIC_API_KEY"] = st.secrets["ANTHROPIC_API_KEY"]

client = anthropic.Anthropic()

SYSTEM = "Sei l'assistente di WiData Srl, startup IoT di Sassari."

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.title("⚙️ Impostazioni")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
    if st.button("🗑️ Nuova chat"):
        st.session_state.messages = []
        st.rerun()

st.title("🤖 Chatbot WiData")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Scrivi un messaggio..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        risposta = ""
        placeholder = st.empty()
        with client.messages.stream(
            model="claude-haiku-4-5-20251001",
            max_tokens=500,
            temperature=temperature,
            system=SYSTEM,
            messages=st.session_state.messages
        ) as stream:
            for text in stream.text_stream:
                risposta += text
                placeholder.markdown(risposta + "▌")
        placeholder.markdown(risposta)

    st.session_state.messages.append({"role": "assistant", "content": risposta})
