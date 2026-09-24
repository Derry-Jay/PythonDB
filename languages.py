from pymysql import Connection


class Languages:
    def __init__(self, cn: Connection):
        self.dc = cn

    def put(self):
        try:
            db = self.dc.cursor()
            print(db.execute(
                "CREATE TABLE 'languages' IF NOT EXISTS ('language_id' INT UNSIGNED NOT NULL AUTO_INCREMENT,"
                "'language' VARCHAR(45) NOT NULL, PRIMARY KEY ('language_id'), UNIQUE INDEX 'language_id_UNIQUE' ("
                "'language_id' ASC) VISIBLE)"))
            print(db.execute('select distinct Language from countrylanguage order by Language'))
            for ele in db.fetchall():
                query = "insert into languages (language) values " + str(ele)
                print(query)
                print(db.execute(query))
            self.dc.commit()
        except Exception as e:
            print(e)
