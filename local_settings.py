
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "9ffa0342-669e-4987-a2d1-791244859c6c2d4f4fd4-4a7c-4080-834e-b1d435ca476740cbf9e6-9902-47cb-80f3-8c2008f9026f"
NEVERCACHE_KEY = "a6e9f501-9d86-4c4c-aaf8-ff107732ff2b3da394c7-7c29-487f-b37d-547521cbd2a85a117052-a604-4e07-a0fe-48c7bb4acbdd"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
