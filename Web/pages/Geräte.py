import pandas
from Web.standart import *

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

seiteneinstellung("Geräte")
startSetup()
auth()
if st.session_state["authentication_status"]:
	geraete()
	sidebar()
	st.session_state["authenticator"].logout('Abmelden', 'sidebar')
