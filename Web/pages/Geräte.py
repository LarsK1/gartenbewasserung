import streamlit as st
st.set_page_config("Geräte - Gartensteuerung", "https://static.blumagine.de/blatt.png", menu_items={"About": "(c) Lars Kusch"})

if st.session_state["authentication_status"]:
    st.session_state["authenticator"].logout('Abmelden', 'sidebar')
    st.title('Geräte')
elif st.session_state["authentication_status"] == False:
    st.error('Benutzername oder Passwort falsch')
elif st.session_state["authentication_status"] == None:
    st.warning('Bitte gib deine Anmeldedaten ein')