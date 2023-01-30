import streamlit as st
import streamlit_authenticator as stauth
import yaml
from Datenbank import Steuerung


def load_configuration(pfad="../config.yaml"):
	with open(pfad) as file:
		return yaml.load(file, Loader=yaml.SafeLoader)


def save_configuration(config, pfad="../config.yaml"):
	with open(pfad, 'w') as file:
		yaml.dump(config, file, default_flow_style=False)


@st.experimental_singleton
def datenbank(benutzername,  passwort, host, datenbankname):
	if "Datenbank" not in st.session_state:
		st.session_state["Datenbank"] = Steuerung(benutzername, passwort, host, datenbankname)


def startSetup():
	config = load_configuration()
	datenbank(config["database"]["username"], config["database"]["password"], config["database"]["host"], config["database"]["databasename"])



def auth():
	if 'authenticator' not in st.session_state:
		config = load_configuration("../config.yaml")
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
	if not authentication_status:
		st.error('Benutzername oder Passwort falsch')
	elif authentication_status is None:
		st.warning('Bitte gib deine Anmeldedaten ein')


def sidebar():
	if "ki-steuerung" in st.session_state:
		st.sidebar.checkbox("Steuerung durch KI", st.session_state["ki-steuerung"], key="ki-steuerung", on_change=sidebar_aenderung_button_ki)
	else:
		st.sidebar.checkbox("Steuerung durch KI", False, key="ki-steuerung", on_change=sidebar_aenderung_button_ki)

def sidebar_aenderung_button_ki():
	st.session_state["Datenbank"].getEinstellungen()


def seiteneinstellung(titel: str):
	st.set_page_config(f"{titel} - Gartensteuerung", "https://static.blumagine.de/blatt.png", menu_items={"About": "© 2023 Blumagine"})
	st.title(f"# {titel}")
	hide_streamlit_style = """
				<style>
				#MainMenu {visibility: hidden;}
				footer {visibility: hidden;}
				footer:after {
					content:'© 2023 Blumagine'; 
					visibility: visible;
					display: block;
					position: relative;
					padding: 5px;
					top: 2px;
				}
				</style>
				"""
	st.markdown(hide_streamlit_style, unsafe_allow_html=True)


