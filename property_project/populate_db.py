# -*- coding: utf-8 -*-
from property_project.db_models import User, PropertyItem, PropertyType
from property_project import db

# Clear and recreate all tables in db
db.drop_all()
db.create_all()


user_1 = User(username="Peter")

db.session.add(user_1)
db.session.commit()

property_type_1 = PropertyType(type="room")
property_type_2 = PropertyType(type="apartment")
property_type_3 = PropertyType(type="house")

property_type_4 = PropertyType(type="house")


db.session.add(property_type_1)
db.session.add(property_type_2)
db.session.add(property_type_3)
db.session.add(property_type_4)

db.session.commit()


property_item_1 = PropertyItem(rent=100.00, size=10.5,
                                user_id=user_1.id,
                                property_type=property_type_1)

property_item_2 = PropertyItem(rent=350.00, rooms=2, size=35.5,
                                user_id=user_1.id,
                                property_type=property_type_2)

property_item_3 = PropertyItem(rent=1000.00, rooms=3, size=150,
                                user_id=user_1.id,
                                property_type=property_type_3)

property_item_4 = PropertyItem(rent=800.00, rooms=4, size=120, 
                                user_id=user_1.id,
                                property_type=property_type_4)


db.session.add(property_item_1)
db.session.add(property_item_2)
db.session.add(property_item_3)
db.session.add(property_item_4)

db.session.commit()

print("first four entries done!")


