from pymysql import Connection


class GovernmentForms:
    def __init__(self, cn: Connection):
        self.dc = cn

    def put(self):
        try:
            db = self.dc.cursor()
            print(db.execute(
                "CREATE TABLE government_types IF NOT EXISTS ('government_type_id' INT UNSIGNED NOT NULL AUTO_INCREMENT, "
                "'government_type' VARCHAR(45) NOT NULL, PRIMARY KEY ('government_type_id'), UNIQUE INDEX "
                "'government_type_id_UNIQUE' ('government_type_id' ASC) VISIBLE)"))
            print(db.execute('select distinct GovernmentForm from country order by GovernmentForm'))
            for ele in db.fetchall():
                print(db.execute("insert into government_types (government_type) values (%s)", ele))
            self.dc.commit()
        except Exception as e:
            print(e)
