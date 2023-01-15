import streamlit as st

if st.session_state["authentication_status"]:
    st.session_state["authenticator"].logout('Abmelden', 'sidebar')
    st.title('Einstellungen')
elif st.session_state["authentication_status"] == False:
    st.error('Benutzername oder Passwort falsch')
elif st.session_state["authentication_status"] == None:
    st.warning('Bitte gib deine Anmeldedaten ein')