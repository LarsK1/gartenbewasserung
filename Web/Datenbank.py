import sqlalchemy.orm

Base = sqlalchemy.orm.declarative_base()


class Daten(Base):
	__tablename__ = "Messdaten"
	id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.Sequence("messdaten_seq"), primary_key=True)
	date = sqlalchemy.Column(sqlalchemy.DateTime())
	sensortyp = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Sensorentypen.id"))
	zone = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Zonen.id"))


ZoneSensoren = sqlalchemy.Table("ZoneSensorenRelation", Base.metadata, sqlalchemy.Column("zone_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("Zonen.id")), sqlalchemy.Column("Sensoren_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("Sensoren.id")))
ZoneAktoren = sqlalchemy.Table("ZoneAktorenRelation", Base.metadata, sqlalchemy.Column("zone_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("Zonen.id")), sqlalchemy.Column("Aktoren_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("Aktoren.id")))


class Sensoren(Base):
	__tablename__ = "Sensoren"
	id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.Sequence("sensoren_seq"), primary_key=True)
	typ = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Sensorentypen.id"))


class Aktoren(Base):
	__tablename__ = "Aktoren"
	id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.Sequence("aktoren_seq"), primary_key=True)
	typ = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Aktorentypen.id"))


class Zonen(Base):
	__tablename__ = "Zonen"
	id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.Sequence("zonen_seq"), primary_key=True)
	name = sqlalchemy.Column(sqlalchemy.Text)
	sensoren = sqlalchemy.orm.relationship('Sensoren', secondary=ZoneSensoren, backref="zonen")
	aktoren = sqlalchemy.orm.relationship('Aktoren', secondary=ZoneAktoren, backref="zonen")


class Aktortypen(Base):
	__tablename__ = "Aktorentypen"
	id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.Sequence("aktortyp_seq"), primary_key=True)
	name = sqlalchemy.Column(sqlalchemy.Text)


class Sensortyp(Base):
	__tablename__ = "Sensorentypen"
	id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.Sequence("sensortyp_seq"), primary_key=True)
	name = sqlalchemy.Column(sqlalchemy.Text)


class Einstellungen(Base):
	__tablename__ = "Einstellungen"
	id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.Sequence("einstellungen_seq"), primary_key=True)
	name = sqlalchemy.Column(sqlalchemy.Text)
	wert = sqlalchemy.Column(sqlalchemy.Boolean)


class Steuerung:
	def __init__(self, benutzername, passwort, host, datenbankname):
		self.engine = sqlalchemy.create_engine(f"postgresql+psycopg2://{benutzername}:{passwort}@{host}:5432/{datenbankname}")
		Base.metadata.bind = self.engine
		Base.metadata.create_all(self.engine)
		self.session = sqlalchemy.orm.Session(self.engine)

		if len(self.session.query(Einstellungen).all()) == 0:
			self.TabellenInitieren()

	def TabellenInitieren(self):
		self.session.add(Einstellungen(name="KI-Steuerung", wert=False))

	def getEinstellungen(self):
		return Einstellungen

	def Tabellenlöschen(self):
		Base.metadata.drop_all(self.engine)

	def Test(self):
		Base.metadata.drop_all(self.engine)
		Base.metadata.create_all(self.engine)
		self.session.query(Einstellungen).all()
