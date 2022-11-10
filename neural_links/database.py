import mysql.connector

config = {
  "user": "u885894041_jarvis",
  "password": "Xxxth77deu.",
  "host": "sql717.main-hosting.eu",
  "database": "u885894041_jarvis",
  "raise_on_warnings": True
}
cnx = mysql.connector.connect(**config)

def get_from_memory(frase):
  cur = cnx.cursor()
  cur.execute("SELECT * FROM learning WHERE user='{}'".format(frase).lower())
  result = cur.fetchall()
  for item in result:
    return item[1]
  cnx.close()

def learning_now(user, jarvis):
  cur = cnx.cursor()
  sql = "INSERT INTO learning (user, jarvis) VALUES (%s, %s)"
  val = (str(user), str(jarvis))
  cur.execute(sql, val)
  cnx.commit()
  cnx.close()

def listening_all_time(user, jarvis):
  cur = cnx.cursor()
  sql = "INSERT INTO listening (user, jarvis) VALUES (%s, %s)"
  val = (str(user), str(jarvis))
  cur.execute(sql, val)
  cnx.commit()
  cnx.close()
  