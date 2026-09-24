from pymysql import Connection


class Regions:
    def __init__(self, cn: Connection):
        self.dc = cn

    def put(self):
        try:
            db = self.dc.cursor()
            print(db.execute("CREATE TABLE IF NOT EXISTS regions ('region_id' INT UNSIGNED NOT NULL AUTO_INCREMENT, "
                             "'continent_id' INT UNSIGNED NOT NULL, 'region' VARCHAR(30) NOT NULL, 'surface_area' "
                             "DECIMAL(10,2) NOT NULL, 'population' INT(10) ZEROFILL NOT NULL, 'life_expectancy' "
                             "DECIMAL(3,1) NULL, 'population_density' INT GENERATED ALWAYS AS (population / "
                             "surface_area) VIRTUAL, 'gnp' DECIMAL(10,2) NOT NULL, 'gnp_old' DECIMAL(10,2) NULL, "
                             "'gnp_change' DECIMAL(10,2) GENERATED ALWAYS AS (gnp - gnp_old) VIRTUAL, PRIMARY KEY ("
                             "'region_id'), UNIQUE INDEX 'region_id_UNIQUE' ('region_id' ASC) VISIBLE, CONSTRAINT "
                             "'fk_regions_continents' FOREIGN KEY ('continent_id') REFERENCES 'world'.'continents' ("
                             "'continent_id') ON DELETE CASCADE ON UPDATE CASCADE) COMMENT = 'Surface Area is in sq. "
                             "Km\nLife Expectancy is in yrs\nPopulation Density is in per sq. Km'"))
            print(db.execute(
                'SELECT Region, SUM(SurfaceArea), CAST(SUM(Population) AS UNSIGNED), AVG(LifeExpectancy), SUM(GNP), '
                'SUM(GNPOld) FROM country GROUP BY Region ORDER BY Region'))
            for ele in db.fetchall():
                print(ele)
                print(db.execute("SELECT Continent FROM country WHERE Region LIKE %s", (f"%{ele[0]}%",)))
                e1 = db.fetchone() or tuple()
                print(db.execute("SELECT continent_id FROM continents WHERE continent LIKE %s",
                                 (f"%{e1[0]}%",)))
                query = (
                    "insert into regions (continent_id, region, surface_area, population, life_expectancy, gnp, gnp_old) "
                    "values (%s, %s, %s, %s, %s, %s, %s)")
                print(query)
                e2 = db.fetchone() or tuple()
                print(db.execute(query, (*e2, *ele)))
            self.dc.commit()
        except Exception as e:
            print(e)
