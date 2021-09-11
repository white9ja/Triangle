from datetime import datetime
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from triangle import db, login_manager, app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.filter_by(id=user_id).first()   


class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    secret_key = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(255), nullable=True)
    gender = db.Column(db.String(255), nullable=True)
    online = db.Column(db.String(255), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    role = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(255), nullable=True)
    state_of_origin = db.Column(db.String(255), nullable=True)
    country = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    date_of_birth =db.Column(db.String(255), nullable=True)
    image = db.Column(db.String(255), nullable=True, default='default.jpg')
    tutor_image = db.Column(db.String(255), nullable=True, default='default.jpg')
    pro_status = db.Column(db.String(255), nullable=True, default= 0)
    online_status = db.Column(db.String(255), nullable=True, default= 0)
    bio_status = db.Column(db.String(255), nullable=True, default= 0)
    guarrantor_status = db.Column(db.String(255), nullable=True, default= 0)
    skill_status = db.Column(db.String(255), nullable=True, default= 0)
    subject_status = db.Column(db.String(255), nullable=True, default= 0)
    verify_status = db.Column(db.String(255), nullable=True, default= 0)
    activated_status = db.Column(db.String(255), nullable=True, default= 0)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())


 


class Bio(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255), nullable=True)
    about = db.Column(db.String(1000), nullable=True)
    email = db.Column(db.String(255), unique=True, nullable=True)
    marital_status = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(255), nullable=True)
    role = db.Column(db.String(255), nullable=True)
    education = db.Column(db.String(255), nullable=True)
    gender = db.Column(db.String(255), nullable=True)
    online = db.Column(db.String(255), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    religion = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(255), nullable=True)
    country = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    date_of_birth =db.Column(db.String(255), nullable=True)
    image = db.Column(db.String(255), nullable=True, default='default.jpg')
    tutor_image = db.Column(db.String(255), nullable=True, default='default.jpg')
    pro_status = db.Column(db.String(255), nullable=True, default= 0)
    online_status = db.Column(db.String(255), nullable=True, default= 0)
    bio_status = db.Column(db.String(255), nullable=True, default= 0)
    guarrantor_status = db.Column(db.String(255), nullable=True, default= 0)
    skill_status = db.Column(db.String(255), nullable=True, default= 0)
    subject_status = db.Column(db.String(255), nullable=True, default= 0)
    verify_status = db.Column(db.String(255), nullable=True, default= 0)
    activated_status = db.Column(db.String(255), nullable=True, default= 0)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())



class Skill(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    skill_status = db.Column(db.String(255), nullable=True, default= 0)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime())
    activated_status = db.Column(db.String(255), nullable=True, default= 0)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

class Category(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    category_status = db.Column(db.String(255), nullable=True, default= 0)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime())
    activated_status = db.Column(db.String(255), nullable=True, default= 0)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())


class Guarrantor(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=True)
    gua_one_name = db.Column(db.String(255), nullable=True)
    gua_one_phone = db.Column(db.String(255), nullable=True)
    gua_one_address = db.Column(db.String(255), nullable=True)
    gua_one_card = db.Column(db.String(255), nullable=True)
    gua_two_name = db.Column(db.String(255), nullable=True)
    gua_two_phone = db.Column(db.String(255), nullable=True)
    gua_two_address = db.Column(db.String(255), nullable=True)
    gua_two_card = db.Column(db.String(255), nullable=True)
    verify_status = db.Column(db.String(255), nullable=True, default= 0)
    activated_status = db.Column(db.String(255), nullable=True, default= 0)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())




class Service(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    meeting = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    available = db.Column(db.String(255), nullable=True)
    duration = db.Column(db.String(255), nullable=True)
    price = db.Column(db.String(255), nullable=True)
    week_price = db.Column(db.String(255), nullable=True)
    incase = db.Column(db.String(255), nullable=True)
    class_status = db.Column(db.String(255), nullable=True, default= 0)
    meeting_count = db.Column(db.String(255), nullable=True, default= 0)
    class_count = db.Column(db.String(255), nullable=True, default= 0)
    count = db.Column(db.String(255), nullable=True, default= 0)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime())
    activated_status = db.Column(db.String(255), nullable=True, default= 0)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())