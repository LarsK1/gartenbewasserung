import pandas
import streamlit as st
import yaml
import streamlit_authenticator as stauth


def auth():
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
    name, authentication_status, username = st.session_state["authenticator"].login('Anmelden', 'main')
    st.session_state["authentication_status"] = authentication_status
    st.session_state["authenticator"] = st.session_state["authenticator"]
    if authentication_status == False:
        st.error('Benutzername oder Passwort falsch')
    elif authentication_status == None:
        st.warning('Bitte gib deine Anmeldedaten ein')

def sidebar():
    st.sidebar.checkbox("Steuerung durch KI", False)

def zonen():
    st.subheader("Aktive Zonen")
    st.table(pandas.DataFrame())
    st.subheader("Neue Zone hinzufügen")
    with st.form("NeueZone", clear_on_submit=True):
        name = st.text_input("Name der Zone")
        typ = st.selectbox("Art der Zone", ["Rasen", "Blumenbeet", "Gemüsebeet", "Sonstiges"])
        submitted = st.form_submit_button("anlegen")



st.set_page_config("Zonen - Gartensteuerung", "https://static.blumagine.de/blatt.png", menu_items={"About": "(c) Lars Kusch"})
st.title('# Zonen')
auth()
if st.session_state["authentication_status"]:
    zonen()
    sidebar()
    st.session_state["authenticator"].logout('Abmelden', 'sidebar')

