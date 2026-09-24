from pymysql import connect

from government_forms import GovernmentForms
# from continents import Continents
# from regions import Regions

# from languages import Languages

con = connect(host='localhost',user='root',database='world',password='admin')

if __name__ == "__main__":
    # Languages(con).put()
    # Continents(con).put()
    # Regions(con).put()
    GovernmentForms(con).put()
