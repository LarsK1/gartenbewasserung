import streamlit as st
import yaml
import streamlit_authenticator as stauth

with open('../config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Anmelden', 'main')

st.session_state["authenticator"] = authenticator
if authentication_status:
    authenticator.logout('Abmelden', 'sidebar')
    st.title('Startseite')
elif authentication_status == False:
    st.error('Benutzername oder Passwort falsch')
elif authentication_status == None:
    st.warning('Bitte gib deine Anmeldedaten ein')

