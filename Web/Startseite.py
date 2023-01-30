import pandas
from Datenbank import *

from standart import *


def gesamt_widget():
	reihe1, reihe2, reihe3 = st.columns(3)
	reihe1.metric("Temperatur", "30°C", 2)
	reihe2.metric("Niederschlag", "5mm/h", -1)
	reihe3.metric("Ø Bodentemperatur", "12°C", "-5°C")


def bewaesserungs_verlauf():
	st.subheader("Letze Bewässerungsmenge")
	st.table(pandas.read_sql(st.session_state["Datenbank"].session.query(Zonen).statement, st.session_state["Datenbank"].engine))
	#st.bar_chart(pandas.read_csv(r"C:\Users\Lars-\Downloads\Mappe2.CSV", sep=";", ), x="Datum", y="Wassermenge")


def geplannte_bewaesserungen():
	st.subheader("Nächste Bewässerung")
	#st.table(pandas.read_csv(r"C:\Users\Lars-\Downloads\Mappe3.CSV", sep=";", ))



seiteneinstellung("Startseite")
startSetup()
auth()
if st.session_state["authentication_status"]:
	sidebar()
	gesamt_widget()
	bewaesserungs_verlauf()

	geplannte_bewaesserungen()
	st.session_state["authenticator"].logout('Abmelden', 'sidebar')
