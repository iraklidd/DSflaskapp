import psycopg2



class pgsqlcn:

  def __init__(self):
    try:
      connection = psycopg2.connect(user = "username",
                                    password = "",
                                    host = "198.199.1.1",
                                    port = "5432",
                                    database = "pgsql")
      cursor = connection.cursor()
      # Print PostgreSQL Connection properties
      # print ( connection.get_dsn_parameters(),"\n")

      # Print PostgreSQL version
      cursor.execute("SELECT version();")
      record = cursor.fetchone()
      # print("You are connected to - ", record,"\n")

    except (Exception, psycopg2.Error) as error :
      # print ("Error while connecting to PostgreSQL", error)
      self.cstatus = 'pgsql db connection error'
    finally:
      #closing database connection.
      if(connection):
        self.cstatus = 'pgsql db connection ok'
        self.cursor = cursor
        self.connection = connection

  def connf(self):
    print(self.cstatus)
    return self.cursor


  def dconnf(self):
      print("disconnected")
      self.cursor.close()
      self.connection.close()
      print("disconnected2")





