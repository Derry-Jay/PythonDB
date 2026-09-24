from pymysql import Connection
class Continents:
    def __init__(self, cn: Connection):
        self.dc = cn
    def put(self):
        try:
            db = self.dc.cursor()
            print(db.execute("CREATE TABLE IF NOT EXISTS continents ('continent_id' INT UNSIGNED NOT NULL "
                             "AUTO_INCREMENT,'continent' VARCHAR(15) NOT NULL,'surface_area' DECIMAL(10,2) NOT NULL,"
                             "'population' INT NOT NULL,'life_expectancy' DECIMAL(3,1) NULL,'population_density' INT "
                             "GENERATED ALWAYS AS (population / surface_area) VIRTUAL,'gnp' DECIMAL(10,2) NOT NULL,"
                             "'gnp_old' DECIMAL(10,2) NULL,'gnp_change' DECIMAL(10,2) GENERATED ALWAYS AS (gnp - "
                             "gnp_old) VIRTUAL,PRIMARY KEY ('continent_id')) COMMENT = 'Surface Area is in sq. "
                             "Km\nLife Expectancy is in yrs\nPopulation Density is in per sq. Km'"))
            print(db.execute(
                'SELECT Continent, SUM(SurfaceArea), CAST(SUM(Population) AS UNSIGNED), AVG(LifeExpectancy), SUM(GNP), '
                'SUM(GNPOld) FROM country GROUP BY Continent ORDER BY Continent'))
            for ele in db.fetchall():
                print(ele)
                query = ("insert into continents (continent, surface_area, population, life_expectancy, gnp, gnp_old) "
                     "values (%s, %s, %s, %s, %s, %s)")
                print(query)
                print(db.execute(query, ele))
            self.dc.commit()
        except Exception as e:
            print(e)