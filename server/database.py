# imported by Flash_Server.py 

#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import MySQLdb as master_db

UNKNOW_DATABASE_ERR = 1049
MASTER_DATABASE = "project_B_db3"

create_master_tbl = """ CREATE TABLE IF NOT EXISTS img_tbl (
			       ID integer PRIMARY KEY AUTO_INCREMENT,
                               dev_name text,
                               timestamp text,
                               file_path text
                               );"""

insert_query_master_tbl = """ INSERT INTO img_tbl (
				    dev_name,
                                    timestamp, 
                                    file_path
                                 ) VALUES (%s,%s,%s)"""


def create_database(master_db_name):
	
	try:
		conn = master_db.connect("localhost","root","Newuser123")
		cursor = conn.cursor()
		master_db_query = "CREATE DATABASE IF NOT EXISTS " + master_db_name
		cursor.execute("SET sql_notes = 0; ")
		cursor.execute(master_db_query)
		cursor.execute("SET sql_notes = 1; ")
	
		conn = master_db.connect("localhost","root","Newuser123",master_db_name,use_unicode=True, charset="utf8")
		return conn
	except master_db.Error as err:
                print(err)

	return None

def create_database_connection(master_db_name):
	
	try:	
		# Open database connection
		conn = master_db.connect("localhost","root","Newuser123",master_db_name,use_unicode=True, charset="utf8")
		return conn

	except master_db.Error as err:

		print(err)
		if err.args[0] == UNKNOW_DATABASE_ERR :
			conn = create_database(master_db_name)
			return conn
	return None

def create_master_table(conn,create_tbl):
	try:
		cursor = conn.cursor()
		cursor.execute("SET sql_notes = 0; ")
		cursor.execute(create_tbl)
		cursor.execute("SET sql_notes = 1; ")
	except master_db.Error as err:
                print(err)

def db_insert_single_records(conn,row_data):
	try:
		cursor = conn.cursor()
		cursor.execute(insert_query_master_tbl,row_data)
	except master_db.Error as err:
		print(err)

def db_insert_multiple_records(conn,row_data):
        try:
                cursor = conn.cursor()
                cursor.executemany(insert_query_master_tbl,row_data)
        except master_db.Error as err:
                print(err)

def db_save_records(conn):
	try:
		conn.commit()
		conn.close()
	except master_db.Error as err:
                print(err)


def main_file(project_secret_key,  project_secret_ts,new_file_path):
		print("Create Database script !!!")
		conn = create_database_connection( MASTER_DATABASE )
		create_master_table( conn, create_master_tbl )
		db_insert_single_records(conn,[project_secret_key,  project_secret_ts,new_file_path] )
		db_save_records(conn)
		return

