import streamlit as st
import yaml
import streamlit_authenticator as stauth
st.set_page_config("Zonen - Gartensteuerung", "https://static.blumagine.de/blatt.png", menu_items={"About": "(c) Lars Kusch"})
st.title('# Zonen')
if 'authenticator' not in st.session_state:
    with open('../config.yaml') as file:
        config = yaml.load(file, Loader=yaml.SafeLoader)
    st.session_state["authenticator"] = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
st.session_state["authenticator"].login('Anmelden', 'main')
if st.session_state["authentication_status"]:
    st.session_state["authenticator"].logout('Abmelden', 'sidebar')

elif st.session_state["authentication_status"] == False:
    st.error('Benutzername oder Passwort falsch')
elif st.session_state["authentication_status"] == None:
    st.warning('Bitte gib deine Anmeldedaten ein')