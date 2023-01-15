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

def geraete():
    st.subheader("Aktive Geräte")
    st.table(pandas.DataFrame())
    st.subheader("Neues Gerät hinzufügen")
    if len(zonen) > 0:

        with st.form("Neues Gerät", clear_on_submit=True):
            typ = st.selectbox("Gerätetyp", ["Sensor", "Magnetventil"])
            zone = st.multiselect("Zugehörige Zone", [1, 2, 3, 4, 5])
            submitted = st.form_submit_button("anlegen")
    else:
        st.warning("Bitte legen Sie erst eine Zone an, bevor Sie Geräte anlegen können.")


zonen = []

st.set_page_config("Geräte - Gartensteuerung", "https://static.blumagine.de/blatt.png", menu_items={"About": "(c) Lars Kusch"})
st.title('# Geräte')
auth()
if st.session_state["authentication_status"]:
    geraete()
    sidebar()
    st.session_state["authenticator"].logout('Abmelden', 'sidebar')

