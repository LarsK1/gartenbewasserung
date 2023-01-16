import pandas
import streamlit as st
import streamlit_authenticator as stauth
import yaml


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


def gesamt_widget():
	reihe1, reihe2, reihe3 = st.columns(3)
	reihe1.metric("Temperatur", "30°C", 2)
	reihe2.metric("Niederschlag", "5mm/h", -1)
	reihe3.metric("Ø Bodentemperatur", "12°C", "-5°C")


def bewaesserungs_verlauf():
	st.subheader("Letze Bewässerungsmenge")
	st.bar_chart(pandas.read_csv(r"C:\Users\Lars-\Downloads\Mappe2.CSV", sep=";", ), x="Datum", y="Wassermenge")


def geplannte_bewaesserungen():
	st.subheader("Nächste Bewässerung")
	st.table(pandas.read_csv(r"C:\Users\Lars-\Downloads\Mappe3.CSV", sep=";", ))


def sidebar():
	st.sidebar.checkbox("Steuerung durch KI", False)


st.set_page_config("Startseite - Gartensteuerung", "https://static.blumagine.de/blatt.png", menu_items={"About": "(c) Lars Kusch"})
st.title('# Startseite')
auth()
if st.session_state["authentication_status"]:
	sidebar()
	gesamt_widget()
	bewaesserungs_verlauf()
	geplannte_bewaesserungen()
	st.session_state["authenticator"].logout('Abmelden', 'sidebar')
