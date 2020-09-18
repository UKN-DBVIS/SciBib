"""

DB_Controller for the scibib database

"""
from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.dialects.mysql import TINYINT, MEDIUMTEXT, ENUM, DATETIME, YEAR, INTEGER
from flask_security import UserMixin, RoleMixin
from datetime import datetime

# See https://github.com/pallets/flask-sqlalchemy/issues/589#issuecomment-361075700
class SQLAlchemy(_BaseSQLAlchemy):
    def apply_pool_defaults(self, app, options):
        super(SQLAlchemy, self).apply_pool_defaults(app, options)
        options["pool_pre_ping"] = True


db = SQLAlchemy()

class Authors(db.Model, SerializerMixin):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    surname = db.Column(db.String(255))
    forename = db.Column(db.String(255))
    cleanname = db.Column(db.String(255))


class Authors_publications(db.Model, SerializerMixin):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer())
    publication_id = db.Column(db.Integer())
    position = db.Column(db.Integer())

class Categories(db.Model, SerializerMixin):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    parent_id = db.Column(db.Integer())
    lft = db.Column(db.Integer())
    rght = db.Column(db.Integer())
    description = db.Column(db.String(255))


class Categories_publications(db.Model, SerializerMixin):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    category_id = db.Column(db.Integer())
    publication_id = db.Column(db.Integer())

#
# class Chairs(db.Model, SerializerMixin):
#     id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
#     name = db.Column(db.String(255))
#
# class Chairs_publications(db.Model, SerializerMixin):
#     id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
#     chair_id = db.Column(db.Integer())
#     publication_id = db.Column(db.Integer())

# class Copyrights(db.Model, SerializerMixin):
#     id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
#     name = db.Column(db.String(255))
#     disclaimer = db.Column(MEDIUMTEXT)
#     created = db.Column(DATE)
#     modified = db.Column(DATE)

class Documents(db.Model, SerializerMixin):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    publication_id = db.Column(db.Integer())
    visible = db.Column(TINYINT)
    remote = db.Column(TINYINT)
    filename = db.Column(db.String(255))
    description = db.Column(db.String(255))

# class Documents2(db.Model, SerializerMixin):
#     id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
#     publication_id = db.Column(db.Integer())
#     visible = db.Column(TINYINT)
#     remote = db.Column(TINYINT)
#     filename = db.Column(db.String(255))
#     description = db.Column(db.String(255))

# class Keywords(db.Model, SerializerMixin):
#     id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
#     publication_id = db.Column(db.Integer())
#     name = db.Column(db.String(255))

class Keywords(db.Model, SerializerMixin):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)

class Keywords_publication(db.Model, SerializerMixin):
    keyword_id = db.Column(db.Integer(), db.ForeignKey('keywords.id'), primary_key=True)
    publication_id = db.Column(db.Integer(), db.ForeignKey('publications.id'), primary_key=True)

class Posts(db.Model, SerializerMixin):
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    body = db.Column(db.String(255))
    created = db.Column(DATETIME)
    modified = db.Column(DATETIME)

class Publications(db.Model, SerializerMixin):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    address = db.Column(MEDIUMTEXT)
    booktitle = db.Column(db.String(255))
    chapter = db.Column(db.Integer())
    edition = db.Column(db.String(255))
    editor = db.Column(db.String(255))
    howpublished = db.Column(MEDIUMTEXT)
    institution = db.Column(db.String(255))
    journal = db.Column(db.String(255))
    month = db.Column(db.String(3))
    note = db.Column(MEDIUMTEXT)
    number = db.Column(db.String(255))
    organization = db.Column(db.String(255))
    pages = db.Column(db.String(255))
    school = db.Column(db.String(255))
    series = db.Column(db.String(255))
    title = db.Column(db.String(255))
    volume = db.Column(db.String(255))
    url = db.Column(db.String(255))
    doi = db.Column(db.String(255))
    year = db.Column(YEAR)
    citename = db.Column(db.String(255), unique=True)
    publisher = db.Column(db.String(255))
    published = db.Column(TINYINT)
    submitted = db.Column(TINYINT)
    public = db.Column(TINYINT)
    created = db.Column(db.DateTime, default=datetime.now())
    modified = db.Column(db.DateTime, default=datetime.now())
    copyright_id = db.Column(db.Integer(), index=True)
    type = db.Column(ENUM("Inproceedings", "Article", "Techreport", "Inbook",
                                         "Book", "Booklet", "Conference", "Incollection",
                                         "Manual", "Masterthesis", "Misc", "PhDThesis",
                                         "Proceedings", "Unpublished"))
    thumb = db.Column(db.String(255))
    mainfile = db.Column(MEDIUMTEXT)
    publicationdate = db.Column(db.Date, index=True)
    kops = db.Column(db.String(255))
    other = db.Column(db.TEXT)
    abstract = db.Column(MEDIUMTEXT)

# class Users(db.Model, UserMixin):
#     id = db.Column(CHAR, primary_key=True)
#     username = db.Column(db.String(255))
#     email = db.Column(db.String(255))
#     password = db.Column(db.String(255))
#     first_name = db.Column(db.String(50))
#     last_name = db.Column(db.String(50))
#     token = db.Column(db.String(255))
#     token_expires = db.Column(DATETIME)
#     api_token = db.Column(db.String(255))
#     activation_date = db.Column(DATETIME)
#     tos_date = db.Column(DATETIME)
#     active = db.Column(TINYINT)
#     is_superuser = db.Column(TINYINT)
#     role = db.Column(db.String(255))
#     created = db.Column(DATETIME)
#     modified = db.Column(DATETIME)

roles_users = db.Table('roles_users',
                      db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
                      db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Users_publication(db.Model, SerializerMixin):
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), primary_key=True)
    publication_id = db.Column(db.Integer(), db.ForeignKey('publications.id'), primary_key=True)

class role(db.Model, RoleMixin):
    __tablename__ = "role"
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))

    users = db.relationship("users", secondary="roles_users",
                            backref=db.backref("users"))

# class roles_users(db.Model, SerializerMixin):
#     # user_id = db.Column(db.Integer(), primary_key=True)
#     # role_id = db.Column(db.Integer(), primary_key=True)
#     user_id = db.Column(db.Integer(), db.ForeignKey('users2.id'), primary_key=True)
#     role_id = db.Column(db.Integer(), db.ForeignKey('role.id'), primary_key=True)

# class roles_users(db.Model):
#     __tablename__ = 'roles_users'
#
#     # id = db.Column(db.Integer(), primary_key=True)
#     user_id = db.Column(db.Integer(), db.ForeignKey('users2.id'), primary_key=True)
#     role_id = db.Column(db.Integer(), db.ForeignKey('role.id'), primary_key=True)

class users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    token = db.Column(db.String(255))
    token_expires = db.Column(DATETIME)
    api_token = db.Column(db.String(255))
    activation_date = db.Column(DATETIME)
    tos_date = db.Column(DATETIME)
    active = db.Column(TINYINT)
    is_superuser = db.Column(TINYINT)
    created = db.Column(DATETIME)
    modified = db.Column(DATETIME)
    roles = db.relationship('role', secondary="roles_users",
                            backref=db.backref('roles', lazy='dynamic'))

