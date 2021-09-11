import os
import random
import secrets
from datetime import datetime
from datetime import date
from flask import render_template, request, session, logging, url_for, redirect, flash, request
from triangle import app, db, bcrypt
from triangle.forms import UserRegForm, LoginForm, TutorRegForm, ResetForm, BioForm, SkillForm,UpdateImageForm, EditBioForm, EditSkillForm, SearchForm, GuarrantorForm,CategoryForm, EditCategoryForm,ServiceForm
from flask_login import login_user, current_user, logout_user, login_required
from triangle.models import User,Bio, Skill, Guarrantor, Category, Service
from sqlalchemy import or_





  # this is a function to upload the Guarrantor one ID Card
def gua_one_cardd(gua_one_card):
  random_hex = secrets.token_hex(8)
  _, f_ext = os.path.splitext(gua_one_card.filename)
  picture_fn = random_hex + f_ext
  picture_path = os.path.join(app.root_path, 'static/user_uploads', picture_fn)
  gua_one_card.save(picture_path)
  return picture_fn
  


# this is a function to upload the Guarrantor two ID Card
def gua_two_cardd(gua_two_card):
  random_hex = secrets.token_hex(8)
  _, f_ext = os.path.splitext(gua_two_card.filename)
  picture_fn = random_hex + f_ext
  picture_path = os.path.join(app.root_path, 'static/user_uploads', picture_fn)
  gua_two_card.save(picture_path)
  return picture_fn


# this is a function to upload the user Prfile Picture 
def save_image(image):
  random_hex = secrets.token_hex(8)
  _, f_ext = os.path.splitext(image.filename)
  picture_fn = random_hex + f_ext
  picture_path = os.path.join(app.root_path, 'static/user_uploads', picture_fn)
  image.save(picture_path)
  return picture_fn








# #This is the function to post image in the post field
# def post_image(post_img):
#   random_hex = secrets.token_hex(8)
#   _, f_ext = os.path.splitext(post_img.filename)
#   picture_fn = random_hex + f_ext
#   picture_path = os.path.join(app.root_path, 'static/user_uploads', picture_fn)
#   post_img.save(picture_path)
#   return picture_fn


#This is the default route
@app.route('/')
def index ():
  return render_template('/index.html',title='Welcome')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user)
      next_page = request.args.get('next')
      return redirect (next_page) if next_page else redirect (url_for('home'))
    else:
         flash(f'Incorrect or wrong Email / Password Combination!', 'danger')
  return render_template('/login.html',title='Login', form=form)



#This is the user registration route
@app.route('/reg', methods=['GET', 'POST'])
def reg():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = UserRegForm()
  if form.validate_on_submit():
      hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(name=form.name.data, email=form.email.data, password=hashed_password, phone=form.phone.data, role= 'User')
      db.session.add(user)
      db.session.commit()
      # flash(f'Account Created for {form.username.data} Successfully !', 'success')
      login_user(user)
      return redirect (url_for('home'))
  return render_template('register.html', title = 'Register', form=form)



#This is the Tutor registration route
@app.route('/tutor_reg', methods=['GET', 'POST'])
def tutor_reg():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = TutorRegForm()
  if form.validate_on_submit():
      hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(name=form.name.data, email=form.email.data, password=hashed_password, phone=form.phone.data, gender=form.gender.data, role= 'Tutor')
      db.session.add(user)
      db.session.commit()
      # flash(f'Account Created for {form.username.data} Successfully !', 'success')
      login_user(user)
      return redirect (url_for('home'))
  return render_template('tutor_reg.html', title = 'Register', form=form)


#This is the Home route
@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
  form = SearchForm()
  if form.validate_on_submit():
    page = request.args.get('page', 1, type=int)
    #.with_entities(Bio.id, Bio.email, Bio.city, Bio.role, Skill.skill_name, Bio.image).distinct()
    #teachers = db.session.query(Bio.city, Skill.skill_name).join(Bio).join(Skill).filter(Bio.email == Skill.email).filter(Bio.city.like(f'%{form.name.data}%')).paginate(page = page,  per_page=3)
    # teachers = db.session.query(Bio).filter(Bio.city.like(f'%{form.name.data}%')).order_by(Bio.created_at.desc()).paginate(page = page,  per_page=3) 
    teachers = (Bio).query.join(Skill, Bio.email == Skill.email ).join(Category, Bio.email == Category.email ).filter(or_(Skill.skill_name.like(f'%{form.name.data}%'),
      Bio.city.like(f'%{form.name.data}%'),
      Category.category_name.like(f'%{form.name.data}%'))).distinct().paginate(page = page,  per_page=3)
      
    # teachers= Skill.query.filter_by(skill_name= form.name.data, location= form.location.da).order_by(Workers.completed_at.desc()).paginate(page = page,  per_page=3)
    if teachers:
      return render_template('/home.html', title='Search', teachers = teachers, form=form)
    else:
      return 'No recent found'
      
  else:
    page = request.args.get('page', 1, type=int)
    tutors = User.query.filter_by(role= "Tutor").order_by(User.created_at.desc()).paginate(page = page,  per_page=3)
    return render_template('/home.html', title='home',form=form, tutors = tutors)



#This is the Password Reset route
@app.route('/forget_password')
def password ():
  form = ResetForm()
  return render_template('/password.html',title='Reset-password', form = form)


#This is the Home route
@app.route('/user_detail/<email>')
@login_required
def detail (email):
  user = User.query.get(email)
  users = User.query.filter_by(email = email).first()
  categorys = Category.query.filter_by(email=email)
  skills = Skill.query.filter_by(email=email)
  bios = Bio.query.filter_by(email = email)
  image = url_for('static', filename='user_uploads/' + str(users.image))
  return render_template('/detail.html',title='user-detail', bios = bios, skills = skills, categorys=categorys, image =image)


@app.route('/profile')
@login_required
def profile ():
  categorys = Category.query.filter_by(email = current_user.email)
  skills = Skill.query.filter_by(email = current_user.email)
  bios = Bio.query.filter_by(email = current_user.email)
  image = url_for('static', filename='user_uploads/' + str(current_user.image))
  return render_template('/profile.html',title='user-detail', bios = bios, skills = skills, categorys= categorys, image =image)



#This is the default route
@app.route('/bio', methods=['GET', 'POST'])
@login_required
def bio ():
  form = BioForm()
  if form.validate_on_submit():
    photo = save_image(form.image.data)
    current_user.image = photo
    current_user.bio_status = 1
    current_user.city = form.city.data
    bio = Bio(email=current_user.email, about=form.about.data, date_of_birth=form.date_of_birth.data, marital_status=form.marital_status.data,religion=form.religion.data,address=form.address.data,city=form.city.data,education=form.education.data,image=photo, gender = current_user.gender, phone =current_user.phone,role= current_user.role, user_id=random.randint(0,999), bio_status=1)
    db.session.add(bio)
    db.session.commit()
    return redirect (url_for('guarrantor'))
 
  return render_template('bio.html', title = 'Bio Completed', form=form)



#This is the update bio infor form
@app.route('/editbio/<int:bio_id>/update',methods=['GET', 'POST'])
@login_required
def editbio(bio_id):
  form = EditBioForm()
  # specials = Posts.query.filter_by(email= current_user.email)
  bios = Bio.query.get(bio_id)
  if form.validate_on_submit():
    bios.about = form.about.data
    bios.marital_status = form.marital_status.data
    bios.city = form.city.data
    bios.education = form.education.data
    bios.religion = form.religion.data
    bios.address = form.address.data
    db.session.commit()
    flash(f'Updated Successfully !', 'success')
    return redirect (url_for('detail', bio_id = bios.id))
  elif request.method == 'GET':
    form.about.data = bios.about
    form.marital_status.data = bios.marital_status
    form.city.data = bios.city
    form.address.data = bios.address
    form.education.data = bios.education
    form.religion.data = bios.religion
  return render_template('editbio.html', title = 'Modified Successfully',  form=form, bio_id = bios.id)




@app.route('/updateimage/<email>/update',methods=['GET', 'POST'])
@login_required
def updateimage(email):
   form = UpdateImageForm()
   if form.validate_on_submit():

    if form.image.data:
      picture_shot = save_image(form.image.data)  
      update_post = Bio.query.filter_by(email=current_user.email).first()
    
      current_user.image = picture_shot
      update_post.image = current_user.image
      db.session.commit()
      #flash('Profile Image Updated Successfully!', 'success')
    return redirect (url_for('detail'))
   else:

    # image = url_for('static', filename='user_uploads/' + str(current_user.fc_image))
    return render_template('/updateimage.html', title='Update File', form = form)

@app.route('/skill', methods=['GET', 'POST'])
@login_required
def skill():
  skills = Skill.query.filter_by(email = current_user.email)
  form = SkillForm()
  if form.validate_on_submit():
      skill = Skill(email=current_user.email, skill_name=form.skill_name.data, skill_status= 1)
      current_user.skill_status = 1 
      db.session.add(skill)
      db.session.commit()
      flash(f'Skill Added Successfully !', 'success')
     
      return redirect (url_for('profile'))
  return render_template('skill.html', title = 'Skill', form=form, skills = skills)



#This is the update skill infor form
@app.route('/editskill/<int:skill_id>/update',methods=['GET', 'POST'])
@login_required
def editskill(skill_id):
  skill = Skill.query.get(skill_id)
  form = EditSkillForm()
  skills = Skill.query.filter_by(email= current_user.email)
  if form.validate_on_submit():

    skill.skill_name = form.skill_name.data
   
    db.session.commit()
    flash(f'Updated Successfully !', 'success')
    return redirect (url_for('skill', skill_id = skill.id, email = current_user.email))
  elif request.method == 'GET':
    form.skill_name.data = skill.skill_name
  return render_template('editskill.html', title = 'Modified Successfully',  form=form, skills = skills)



#This is the route to delete your previous post by id
@app.route('/skills/<int:skill_id>/delete', methods=['GET', 'skill'])
@login_required
def del_skill(skill_id):
  skill = Skill.query.get(skill_id)
  db.session.delete(skill)
  db.session.commit()
  flash(f'skill Deleted Successfully !', 'success')
  return redirect (url_for('skill'))


#this is the route to add class or examination
@app.route('/category', methods=['GET', 'POST'])
@login_required
def cate():
  categorys = Category.query.filter_by(email = current_user.email)
  form = CategoryForm()
  if form.validate_on_submit():
      category = Category(email=current_user.email, category_name=form.category_name.data, category_status= 1)
      current_user.pro_status = 1 
      db.session.add(category)
      db.session.commit()
      flash(f'Class Added Successfully !', 'success')
     
      return redirect (url_for('profile'))
  return render_template('category.html', title = 'Category', form=form, categorys = categorys)


#This is the update category infor form
@app.route('/editcategory/<int:category_id>/update',methods=['GET', 'POST'])
@login_required
def editcate(category_id):
  category = Category.query.get(category_id)
  form = EditCategoryForm()
  categorys = Category.query.filter_by(email= current_user.email)
  if form.validate_on_submit():

    category.category_name = form.category_name.data
   
    db.session.commit()
    flash(f'Updated Successfully !', 'success')
    return redirect (url_for('cate', category_id = category.id, email = current_user.email))
  elif request.method == 'GET':
    form.category_name.data = category.category_name
  return render_template('editcategory.html', title = 'Modified Successfully',  form=form, categorys = categorys)



#This is the route to delete your previous class or exam  by id
@app.route('/categorys/<int:category_id>/delete', methods=['GET', 'POST'])
@login_required
def del_category(category_id):
  cat = Category.query.get(category_id)
  db.session.delete(cat)
  db.session.commit()
  flash(f'category Deleted Successfully !', 'success')
  return redirect (url_for('cate'))


#this is the guarrantor route
@app.route('/guarrantor', methods=['GET', 'POST'])
@login_required
def guarrantor ():
  form = GuarrantorForm()
  if form.validate_on_submit():
    gua_one_idcard = gua_one_cardd(form.gua_one_card.data)
    gua_two_idcard = gua_two_cardd(form.gua_one_card.data)
    current_user.guarrantor_status = 1
    gua= Guarrantor(email=current_user.email, gua_one_name=form.gua_one_name.data, gua_one_phone=form.gua_one_phone.data, gua_one_address=form.gua_one_address.data, gua_one_card=gua_one_idcard, gua_two_name=form.gua_two_name.data, gua_two_phone=form.gua_two_phone.data,gua_two_address=form.gua_two_address.data,gua_two_card=gua_two_idcard)
    db.session.add(gua)
    db.session.commit()
    return redirect (url_for('profile'))
 
  return render_template('guarrantor.html',title='Guarrantor Form', form = form)




#This is the default route
@app.route('/schedule/<email>')
@login_required
def schedule (email):
  user = User.query.get(email)
  users = User.query.filter_by(email=email)
  bios = Bio.query.filter_by(email = email)
  services = Service.query.filter_by(email=email)

  # image = url_for('static', filename='user_uploads/' + str(users.image))
  return render_template('/schedule.html',title='Schedule', services = services, bios =bios, users = users)



#This is the default route
@app.route('/services/<email>')
@login_required
def service (email):
  user = User.query.get(email)
  users = User.query.filter_by(email=email)
  bios = Bio.query.filter_by(email = email)
  services = Service.query.filter_by(email=email)
  # image = url_for('static', filename='user_uploads/' + str(users.image))
  return render_template('/services.html',title='My Schedule', services = services, bios =bios, users = users)



@app.route('/add_service/<email>', methods=['GET', 'POST'])
def add_service (email):
  user = User.query.get(current_user.email)
  users = User.query.filter_by(email=current_user.email)
  bios = Bio.query.filter_by(email = current_user.email)
  form = ServiceForm()
  if form.validate_on_submit():
    serve = Service(email=current_user.email, name=form.name.data, description=form.description.data, meeting=form.meeting.data,available=form.available.data,price=form.price.data)
    db.session.add(serve)
    db.session.commit()
    return redirect (url_for('service', bios = bios, email =current_user.email))
  return render_template('/add_service.html',title='Add Service', form =form, bios =bios, users = users)

#This is the logout route
@app.route('/logout', methods=['GET', 'POST'])
def logout():
  logout_user()
  return redirect(url_for('index'))