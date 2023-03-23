import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

database_hostname = os.getenv("database_hostname")
database_port = os.getenv("database_port")
database_password = os.getenv("database_password")
database_name = os.getenv("database_name")
database_username = os.getenv("database_username")

def get_connection():
  conn = psycopg2.connect(
    host=database_hostname,
    dbname=database_name,
    user=database_username,
    password=database_password,
    port=database_port
  )
  return conn

def init():
  # conexion a base de datos postgresql
  conn = get_connection()
  cur = conn.cursor()

  # crear tablas

  cur.execute("""CREATE TABLE IF NOT EXISTS notes (
    id SERIAL,
    title VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY(id)
  );
  """)

  conn.commit()

  cur.close()
  conn.close()

def create_note(title: str, state: str):
  # conexion a base de datos postgresql
  conn = get_connection()
  cur = conn.cursor()

  # consultas
  cur.execute("""INSERT INTO notes (title, state)
              VALUES (%s, %s) RETURNING *;""", (title, state))

  note = cur.fetchone()
  print(note)

  conn.commit()

  cur.close()
  conn.close()


def get_notes():
  # conexion a base de datos postgresql
  conn = get_connection()
  cur = conn.cursor()

  # consultas
  cur.execute("""SELECT * FROM notes;""")
  notes = cur.fetchall()
  
  print(notes)
  
  conn.commit()

  cur.close()
  conn.close()
  
  return notes
  
  
def get_notes_by_state(state: str):
  # conexion a base de datos postgresql
  conn = get_connection()
  cur = conn.cursor()

  # consultas
  cur.execute(f"SELECT * FROM notes WHERE state = '{state}'")
  notes = cur.fetchall()
  
  print(notes)
  
  conn.commit()

  cur.close()
  conn.close()
  
  return notes
