import streamlit as st
import yaml
import streamlit_authenticator as stauth


def auth():
	if 'authenticator' not in st.session_state:
		with open('../config.yaml') as file:
			config = yaml.load(file, Loader=yaml.SafeLoader)
		st.session_state["authenticator"] = stauth.Authenticate(config['credentials'], config['cookie']['name'], config['cookie']['key'], config['cookie']['expiry_days'], config['preauthorized'])
	name, authentication_status, username = st.session_state["authenticator"].login('Anmelden', 'main')
	st.session_state["authentication_status"] = authentication_status
	st.session_state["authenticator"] = st.session_state["authenticator"]
	if authentication_status == False:
		st.error('Benutzername oder Passwort falsch')
	elif authentication_status == None:
		st.warning('Bitte gib deine Anmeldedaten ein')


def sidebar():
	st.sidebar.checkbox("Steuerung durch KI", False)


def einstellungen():
	datenbank = st.container()
	datenbank.subheader("Datenbankeinstellungen")
	datenbank.text_input("Host", help="URL des Datenbankservers")
	datenbank.text_input("Benutzername")
	datenbank.text_input("Passwort", type="password")
	datenbank.text_input("Datenbank")


st.set_page_config("Einstellungen - Gartensteuerung", "https://static.blumagine.de/blatt.png", menu_items={"About": "(c) Lars Kusch"})
st.title('# Einstellungen')
auth()
if st.session_state["authentication_status"]:
	einstellungen()
	sidebar()
	st.session_state["authenticator"].logout('Abmelden', 'sidebar')
