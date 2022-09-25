from flask_login import UserMixin
from datastore_entity import DatastoreEntity, EntityValue
import datetime
class Party:
    def __init__(self,
                 name,
                 game,
                 proficiency,
                 lat,
                 lng):
        self.name = name
        self.game = game
        self.proficiency = proficiency
        self.lat = lat
        self.lgn = lng

class User(DatastoreEntity, UserMixin):
    username = EntityValue(None)
    password = EntityValue(None)
    status = EntityValue (1)
    data_created = EntityValue(datetime.datetime.utcnow())