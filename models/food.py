from init import db
# This is one of the places where the init items are imported

from marshmallow import fields

# the class Food uses Sqlalchemy to create a table structure with column names and data types.
class Food(db.model):
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    type = db.Column(db.String)
    date = db.Column(db.Date)
    # wine_id
    # user_id


# Marshmallow ma converts these data types into db readable format via the Schema and with the use of marshmallow fields each column item can be retrieved by the controller on a Model View Control (MVC) structure.
class FoodSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'type', 'date')