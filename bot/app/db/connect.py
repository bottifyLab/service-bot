from orator import DatabaseManager, Schema, Model

DATABASES = {
    'sqlite3': {
        'foreign_keys': True,
        'driver': 'sqlite',
        'database': 'data/data.sqlite'
    }
}

#DATABASES = {
#    'postgres': {
#        'driver': 'postgres',
#       'host': 'localhost',
#        'database': 'mydb',
#        'user': 'ben',
#        'password': 'ben',
#        'prefix': ''
#    }
#}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)