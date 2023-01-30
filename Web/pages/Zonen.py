import pandas
from Web.standart import *


def zonen():
	st.subheader("Aktive Zonen")
	st.table(pandas.DataFrame())
	st.subheader("Neue Zone hinzufügen")
	with st.form("NeueZone", clear_on_submit=True):
		name = st.text_input("Name der Zone")
		typ = st.selectbox("Art der Zone", ["Rasen", "Blumenbeet", "Gemüsebeet", "Sonstiges"])
		submitted = st.form_submit_button("anlegen")


seiteneinstellung("Zonen")
startSetup()
auth()
if st.session_state["authentication_status"]:
	zonen()
	sidebar()
	st.session_state["authenticator"].logout('Abmelden', 'sidebar')
