from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.models import Film, Actors


class FilmSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Film
        exclude = ['id']
        load_instance = True


class ActorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Actors
        load_instance = True
