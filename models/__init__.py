#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == "db":
	import models.engine.db_storage
	storage = models.engine.db_storage.DBStorage()
	storage.reload()

else:
	import models.engine.file_storage
	storage = models.engine.file_storage.FileStorage()
	storage.reload()
