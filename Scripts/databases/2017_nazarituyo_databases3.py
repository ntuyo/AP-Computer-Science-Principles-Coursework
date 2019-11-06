import pymysql

connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='world',
                             autocommit=True)

cursor = connection.cursor()
sql = 'ALTER TABLE world.country MODIFY COLUMN Continent varchar(35);'
cursor.execute(sql)

sql = "select * from country where name like '%stan';"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    country_name_org = row[1]
    country_name_new = row[1]
    country_size = len(country_name_new)
    country_replace = 'zurg'
    search_size = len('stan')
    country_name_new = country_name_new[0:country_size - search_size] + country_replace
    print(country_name_new)
    update_sql = 'update country set name = "' + country_name_new + '" where name = "' + country_name_org + '"'
    print(update_sql)
    cursor.execute(update_sql)

zurg_languages = ['buzz_sucks', 'ihatewoody', 'nomorewendy']  # make your list of Zurg's languages
sql = "SELECT * FROM " + " world.Countrylanguage"
cursor.execute(sql)  # Runs whatever you put in quotations
results = cursor.fetchall()
for row in results:
    import random
    country_lang_org = row[1]
    country_lang_new = row[1]
    country_size = len(country_lang_new)
    random_lang = random.SystemRandom()
    country_lang_replace = random_lang.choice(zurg_languages)
    country_lang_new_new = country_lang_replace
    print(country_lang_new)
    update_sql = 'update country set name = "' + country_lang_new + '" where name = "' + country_lang_org + '"'
    print(update_sql)
    cursor.execute(update_sql)

cursor.close()
connection.close()
