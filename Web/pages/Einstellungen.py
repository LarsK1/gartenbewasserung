from Web.standart import *


def einstellungen():
	datenbank_einstellungen = st.container().form("Datenbank")
	datenbank_einstellungen.subheader("Datenbankeinstellungen")
	konfiguration = load_configuration()
	host = datenbank_einstellungen.text_input("Host", help="URL des Datenbankservers", value=konfiguration["database"]["host"])
	user = datenbank_einstellungen.text_input("Benutzername", placeholder=konfiguration["database"]["username"])
	password = datenbank_einstellungen.text_input("Passwort", type="password", value=konfiguration["database"]["password"])
	databasename = datenbank_einstellungen.text_input("Datenbank", value=konfiguration["database"]["databasename"])
	bt = datenbank_einstellungen.form_submit_button("Speichern")
	if bt:
		konfiguration["database"]["host"] = host
		konfiguration["database"]["user"] = user
		konfiguration["database"]["password"] = password
		konfiguration["database"]["databasename"] = databasename
		save_configuration(konfiguration)
		st.info("Die Einstellungen wurden erfolgreich gespeichert!")


seiteneinstellung("Einstellungen")
startSetup()
auth()
if st.session_state["authentication_status"]:
	einstellungen()
	sidebar()
	st.session_state["authenticator"].logout('Abmelden', 'sidebar')
