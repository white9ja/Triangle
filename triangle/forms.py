from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField,DateField,  SelectField, DateField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo
from triangle.models import User, Bio, Skill, Guarrantor, Category
from flask_login import current_user



#This is the form class for User Registration
class UserRegForm(FlaskForm):
    name = StringField('Fullname', validators=[DataRequired(), Length(min=5, max=20, message=('Please ensure to enter your firstname and surname'))])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=11, max=11, message=('Invalid or wrong mobile number, check and try again'))])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20, message=('Please ensure that your Password combination is more than 8 characters'))])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField ('Sign Up')
    def validate_username(self, username):
        username_exist = User.query.filter_by(username = username.data).first()
        if username_exist:
            raise ValidationError('This Username already Exist, Kindly use a different one.')

    def validate_email(self, email):
        email_exist = User.query.filter_by(email = email.data).first()
        if email_exist:
             raise ValidationError('This Email address already Exist, Kindly use a different one.')
    
    def validate_phone(self, phone):
        phone_exist = User.query.filter_by(phone = phone.data).first()
        if phone_exist:
            raise ValidationError('This phone already Exist, Kindly use a different one.')


#This is the form class for Tutors or Teachers Registration
class TutorRegForm(FlaskForm):
    name = StringField('Fullname', validators=[DataRequired(), Length(min=5, max=20, message=('Please ensure to enter your firstname and surname'))])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=11, max=11, message=('Invalid or wrong mobile number, check and try again'))])
    gender = SelectField(
        'Gender',
        [DataRequired()],
        choices=[
            ('', 'Select Gender'),
            ('Male', 'Male'),
            ('Female', 'Female')
        ])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20, message=('Please ensure that your Password combination is more than 8 characters'))])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField ('Sign Up')
    def validate_username(self, username):
        username_exist = User.query.filter_by(username = username.data).first()
        if username_exist:
            raise ValidationError('This Username already Exist, Kindly use a different one.')

    def validate_email(self, email):
        email_exist = User.query.filter_by(email = email.data).first()
        if email_exist:
             raise ValidationError('This Email address already Exist, Kindly use a different one.')
    
    def validate_phone(self, phone):
        phone_exist = User.query.filter_by(phone = phone.data).first()
        if phone_exist:
            raise ValidationError('This phone already Exist, Kindly use a different one.')
class BioForm(FlaskForm):
    about = TextAreaField('about', validators=[DataRequired(), Length(min=5,  message=('Please give details intro about yourself new *'))])
    marital_status = SelectField(
        'Marrital Status',
        [DataRequired()],
        choices=[
            ('', 'Select marrital Status'),
            ('Married', 'Married'),
            ('Single', 'Single'),
            ('Divorsed', 'Divorsed'),
            ('Widow', 'Widow')

        ])
   
    education= SelectField(
        'Highest Education Qualification',
        [DataRequired()],
        choices=[
            ('', 'Select your highest qualification'),
            ('None', 'None'),
            ('SSCE', 'SSCE'),
            ('WAEC', 'WAEC'),
            ('GCE', 'GCE'),
            ('NCE', 'NCE'),
            ('OND', 'OND'),
            ('HND', 'HND'),
            ('BSC', 'BSC'),
            ('BEdu', 'BEdu'),
            ('MSC', 'MSC')
        ])
    religion= SelectField(
        'Religion',
        [DataRequired()],
        choices=[
            ('', 'Select your religion'),
            ('None', 'None'),
            ('Christain', 'Christain'),
            ('Muslim', 'Muslim'),
            ('Traditionalist', 'Traditionalist'),
            ('Atheism', 'Atheism'),
            ('Hinduism', 'Hinduism'),
            ('Buddhism', 'Buddhism'),
            ('Judaism', 'Judaism'),
            
        ])
    city= SelectField(
        'City of Residence',
        [DataRequired()],
        choices=[
            ('', 'select your current location'),
            ('Abia', 'Abia'),
            ('Adamawa', 'Adamawa'),
            ('Akwa Ibom', 'Akwa Ibom'),
            ('Anambra', 'Anambra'),
            ('Bauchi', 'Bauchi'),
            ('Bayelsa', 'Bayelsa'),
            ('Benue', 'Benue'),
            ('Borno', 'Borno'),
            ('Cross River', 'Cross River'),
            ('Delta', 'Delta'),
            ('Ebonyi', 'Ebonyi'),
            ('Edo', 'Edo'),
            ('Ekiti', 'Ekiti'),
            ('Enugu', 'Enugu'),
            ('Gombe', 'Gombe'),
            ('Imo', 'Imo'),
            ('Jigawa', 'Jigawa'),
            ('Kaduna', 'Kaduna'),
            ('Kano', 'Kano'),
            ('Katsina', 'Katsina'),
            ('Kebbi', 'Kebbi'),
            ('Kogi', 'Kogi'),
            ('Kwara', 'Kwara'),
            ('Lagos', 'Lagos'),
            ('Nasarawa', 'Nasarawa'),
            ('Niger', 'Niger'),
            ('Ogun', 'Ogun'),
            ('Ondo', 'Ondo'),
            ('Osun', 'Osun'),
            ('Oyo', 'Oyo'),
            ('Plateau', 'Plateau'),
            ('Rivers', 'Rivers'),
            ('Sokoto', 'Sokoto'),
            ('Taraba', 'Taraba'),
            ('Yobe', 'Yobe'),
            ('Zamfara', 'Zamfara'),
            ('FCT', 'FCT'),
        ])
    address = StringField('Address', validators=[DataRequired(), Length(min=8, max=150, message=('Please enter your address of residence '))])
    date_of_birth  = DateField('Date of birth', validators=[DataRequired()], format='%Y-%m-%d')
    image = FileField('Prefered status photo', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'jfif'])])
    submit = SubmitField ('Submit')



class UpdateImageForm(FlaskForm):
    image = FileField('Prefered status photo', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'jfif'])])
    submit = SubmitField ('Submit')

class SkillForm(FlaskForm):
    skill_name = StringField('Skill / Subject', validators=[DataRequired(), Length(min=3, max=50, message=('Please ensure to enter your skill / subject without abreviation'))])
    submit = SubmitField ('Add') 


class EditSkillForm(FlaskForm):
    skill_name = StringField('Modify Skill / Subject', validators=[DataRequired(), Length(min=3, max=50, message=('Please ensure to enter your skill / subject without abreviation'))])
    submit = SubmitField ('Modify') 

class CategoryForm(FlaskForm):
    category_name = StringField('Class / Exam', validators=[DataRequired(), Length(min=3, max=50, message=('Please ensure to enter  class / Exam as generally known'))])
    submit = SubmitField ('Add') 

class EditCategoryForm(FlaskForm):
    category_name = StringField('Modify Class / Exam', validators=[DataRequired(), Length(min=3, max=50, message=('Please ensure to enter  class / Exam as generally known'))])
    submit = SubmitField ('Modify') 



class EditBioForm(FlaskForm):
    about = TextAreaField('about', validators=[DataRequired(), Length(min=1, message=('Please you have a maximum of 180 characters'))])
    marital_status = SelectField(
        'Marrital Status',
        [DataRequired()],
        choices=[
            ('', 'Select marrital Status'),
            ('Married', 'Married'),
            ('Single', 'Single'),
            ('Divorsed', 'Divorsed'),
            ('Widow', 'Widow')

        ])
   
    education= SelectField(
        'Highest Education Qualification',
        [DataRequired()],
        choices=[
            ('', 'Select your highest qualification'),
            ('None', 'None'),
            ('SSCE', 'SSCE'),
            ('WAEC', 'WAEC'),
            ('GCE', 'GCE'),
            ('NCE', 'NCE'),
            ('OND', 'OND'),
            ('HND', 'HND'),
            ('BSC', 'BSC'),
            ('BEdu', 'BEdu'),
            ('MSC', 'MSC')
        ])
    religion= SelectField(
        'Religion',
        [DataRequired()],
        choices=[
            ('', 'Select your religion'),
            ('None', 'None'),
            ('Christain', 'Christain'),
            ('Muslim', 'Muslim'),
            ('Traditionalist', 'Traditionalist'),
            ('Atheism', 'Atheism'),
            ('Hinduism', 'Hinduism'),
            ('Buddhism', 'Buddhism'),
            ('Judaism', 'Judaism'),
            ('BEdu', 'BEdu'),
            ('MSC', 'MSC')
        ])
    city= SelectField(
        'City of Residence',
        [DataRequired()],
        choices=[
            ('', 'select your current location'),
            ('Abia', 'Abia'),
            ('Adamawa', 'Adamawa'),
            ('Akwa Ibom', 'Akwa Ibom'),
            ('Anambra', 'Anambra'),
            ('Bauchi', 'Bauchi'),
            ('Bayelsa', 'Bayelsa'),
            ('Benue', 'Benue'),
            ('Borno', 'Borno'),
            ('Cross River', 'Cross River'),
            ('Delta', 'Delta'),
            ('Ebonyi', 'Ebonyi'),
            ('Edo', 'Edo'),
            ('Ekiti', 'Ekiti'),
            ('Enugu', 'Enugu'),
            ('Gombe', 'Gombe'),
            ('Imo', 'Imo'),
            ('Jigawa', 'Jigawa'),
            ('Kaduna', 'Kaduna'),
            ('Kano', 'Kano'),
            ('Katsina', 'Katsina'),
            ('Kebbi', 'Kebbi'),
            ('Kogi', 'Kogi'),
            ('Kwara', 'Kwara'),
            ('Lagos', 'Lagos'),
            ('Nasarawa', 'Nasarawa'),
            ('Niger', 'Niger'),
            ('Ogun', 'Ogun'),
            ('Ondo', 'Ondo'),
            ('Osun', 'Osun'),
            ('Oyo', 'Oyo'),
            ('Plateau', 'Plateau'),
            ('Rivers', 'Rivers'),
            ('Sokoto', 'Sokoto'),
            ('Taraba', 'Taraba'),
            ('Yobe', 'Yobe'),
            ('Zamfara', 'Zamfara'),
            ('FCT', 'FCT'),
        ])
    address = StringField('Address', validators=[DataRequired(), Length(min=8, max=150, message=('Please enter your address of residence '))])
    submit = SubmitField ('Submit')


#This is the model class for Rset of Password
class ResetForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    submit = SubmitField ('Login') 


#This is the model class for login
class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField ('Login') 



#This is the model class for login
class GuarrantorForm(FlaskForm):

    gua_one_name = StringField('Guarrantor One Name', validators=[DataRequired(), Length(min=8, max=150, message=('Please ensure to enter your firstname and surname'))])
    gua_one_phone = StringField('Guarrantor One Phone', validators=[DataRequired(), Length(min=11, max=11, message=('Invalid or wrong mobile number, check and try again'))])
    gua_one_address = StringField('Guarrantor One Address', validators=[DataRequired(), Length(min=8, max=150, message=('Please enter your address of residence '))])
    gua_one_card = FileField('Guarrantor One ID Card', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'jfif'])])
    gua_two_name = StringField('Guarrantor Two Name', validators=[DataRequired(), Length(min=8, max=150, message=('Please ensure to enter your firstname and surname'))])
    gua_two_phone = StringField('Guarrantor Two Phone', validators=[DataRequired(), Length(min=11, max=11, message=('Invalid or wrong mobile number, check and try again'))])
    gua_two_address = StringField('Guarrantor Two Address', validators=[DataRequired(), Length(min=8, max=150, message=('Please enter your address of residence '))])
    gua_two_card = FileField('Guarrantor Two ID Card', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'jfif'])])
    submit = SubmitField ('Submit') 



class SearchForm(FlaskForm):
    name = StringField('Search by Subject or Location', validators=[DataRequired(), Length(min=3, max=50, message=('Please ensure to enter your subject or location without abreviation'))])
    submit = SubmitField ('Search') 



class ServiceForm(FlaskForm):
    name = StringField('Class/Examamination e.g SSCE, JAMB', validators=[DataRequired(), Length(min=3, max=50, message=('Please ensure to enter your Class / Exam name'))])
    meeting = StringField(' Number of meeting / section per week', validators=[DataRequired(), Length(min=1, max=1, message=('Invalid or wrong Meeting / Section or Coaching Number Per WeeK, Please enter 1-7'))])
    description = TextAreaField('Description  e.g Number of subject and meeting duration', validators=[DataRequired(), Length(min=3, max=250, message=('Please ensure to enter your Class / Exam name'))])
    available = SelectField(
        'Available to coach now',
        [DataRequired()],
        choices=[
            ('', 'Select Availability status'),
            ('AVAILABLE', 'Available'),
            ('NOT-AVAILABLE', 'Not available'),
            ('BOOKED', 'Booked'),
            ('AVAILABLE NEXT-WEEK', 'Available Next-Week'),
            ('AVAILABLE NEXT-MONTH', 'Available Next-Month'),
            ('ONLINE CLASSES ONLY', 'ONLINE CLASSES ONLY'),
        ])
    price = StringField('Month Price', validators=[DataRequired(), Length(min=3, max=10, message=('Please enter a valid or correct price for your service'))])
    submit = SubmitField ('Add')