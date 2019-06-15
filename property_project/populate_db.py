
## vs. Schafer tutorial!
#from sqlalchemy import create_engine 
#from sqlalchemy.orm import sessionmaker

# import sql alchemy classes 
from property_project.db_models import User, PropertyItem, PropertyType #,PropertyAddress
from property_project import db #, bcrypt ## C. Schafer LOGIN # fuer Passwort hashing!

## in __init__.py aufrufen + db.drop_all() an Anfang setzen!!!

    ## Database leeren ==> db.drop_all()  vs. db.create_all() => Umkehrung??
        ### Wichtig vgl. Video 4 ==> unterschiedlicher database-Zugriff 
            ## db. => vor allen commands!!!

    #### TO DO: Infos fuer jeded Kategorie in Tuple-Liste packen und adding()/commiting()
    ## in Schleife!!


    ## User:
#db.drop_all()
##To create the initial database, just import the db object from an interactive 
##      Python shell and run the SQLAlchemy.create_all() method to create the tables and database


db.drop_all() ## Eintraege, die ueber Formular geschehen erhalten??!!?
db.create_all()

# bcrypt.generate_password_hash('hunter2')
user_1 = User (username ="Peter")#, password = bcrypt.generate_password_hash("123").decode('utf-8')) 
#, email = "Peter@pan.de",password = "123")#bcrypt.generate_password_hash("123"))

#print(user_1)
db.session.add(user_1)
db.session.commit()

property_type_1 = PropertyType(type = "room") ## jede Kategorie muss nur einmal in category-db auftauchen!
# wie abfragen, ob es sie schon gibt/ Ueberbevoelkerung verhindern??
property_type_2 = PropertyType(type = "apartment")
property_type_3 = PropertyType(type = "house")

property_type_4 = PropertyType(type = "house")



db.session.add(property_type_1)
db.session.add(property_type_2)
db.session.add(property_type_3)
db.session.add(property_type_4)

db.session.commit()

# address_1 = PropertyAddress(post_code="123456")
# address_2 = PropertyAddress(post_code="123")
# db.session.add(address_1)
# db.session.add(address_2)
# db.session.commit()

#print(property_type_1)
#session.commit()

property_item_1 = PropertyItem(rent = 100.00, size = 10.5, user_id = user_1.id, 
                property_type = property_type_1) ## user_id => automatisch setzen?!

property_item_2 = PropertyItem(rent = 350.00, rooms = 2, size = 35.5, user_id = user_1.id,
                property_type = property_type_2)

property_item_3 = PropertyItem(rent = 1000.00, rooms = 3, size = 150, user_id = user_1.id,
                property_type = property_type_3)

property_item_4 = PropertyItem(rent = 800.00, rooms = 4, size = 120, user_id = user_1.id,
                property_type = property_type_4)

#print(property_item_1)
db.session.add(property_item_1)
db.session.add(property_item_2)
db.session.add(property_item_3)
db.session.add(property_item_4)

db.session.commit()

print("first four entries done!")

