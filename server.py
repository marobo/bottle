import time, calendar
import sqlite3
import pygal
from  bottle import route, get, post, request, response, route, run, template, redirect, os, time, static_file # or route
AUTHENTICATE_SECRET ="sjfkjslfjs" ####cookie responde password ho kodigu ne'e;;;;;;

@route("/pie/")
def pie():
	multipie_chart = pygal.Pie()
	multipie_chart.title = 'Browser usage by version in February 2012 (in %)'
	multipie_chart.add('IE', [5.7, 10.2, 2.6, 1])
	multipie_chart.add('Firefox', [.6, 16.8, 7.4, 2.2, 1.2, 1, 1, 1.1, 4.3, 1])
	multipie_chart.add('Chrome', [.3, .9, 17.1, 15.3, .6, .5, 1.6])
	multipie_chart.add('Safari', [4.4, .1])
	multipie_chart.add('Opera', [.1, 1.6, .1, .5])
	return multipie_chart.render()
			
@route('/pie1/')
def pie1():
    return template('template/pie.html')	
	

@get('/')
def index(username="MUNDU"):
    return template('template/index.html', naran=username,)

@route('/admin/')
def admin(username="todos"):
	username = user_is_authenticated('/admin/')
	return template('template/admin.html', naran=username,)
		

@route('/images/')
def images():
	return template('template/images.html')

@route('/login1/')
def login1():
	return template('template/login1.html')
	

@route('/kalkulator/')
def kalkulator():
    return template('template/kalkulator.html')
	
	
@get('/konaba/')
def konaba():
	localtime = time.asctime(time.localtime(time.time()))
	cal = calendar.month(2015,5)
	return template('template/konaba.html', cal=cal, localtime=localtime )
	

	
###########==========upload images=======####
@get('/upload1/')
def upload1():
	connection = sqlite3.connect("test.db")
	entries = connection.execute("SELECT id, category, upload FROM upload")
	return template('template/upload1.html', entries=entries)

@get('/upload/')
def upload():
	user_is_authenticated('/upload/')
	connection = sqlite3.connect("test.db")
	entries = connection.execute("SELECT id, category, upload FROM upload")
	return template('template/upload.html', entries=entries)
	
@get('/upload/foun/')
def upload_foun():
    user_is_authenticated('/upload/foun/')
    return template('template/upload_foun.html', category="", upload="", sala="")
	
@post('/upload/foun/')
def kria_upload_foun():
	category = request.forms.get('category')
	upload = request.files.get('upload')
	name, ext = os.path.splitext(upload.filename)
	if ext not in ('.png', '.jpg', '.jpeg', '.JPG', '.gif'):


		return "File extension not allowed."
	

	save_path = "static/upload/"####{category}".format(category=category)
	if not os.path.exists(save_path):
	    os.makedirs(save_path)

	file_path = "{category}/{upload}".format(category=save_path, upload=upload.filename)

	upload.save(file_path)

	connection = sqlite3.connect("test.db")
	connection.execute("INSERT INTO upload( category, upload) VALUES ( '{category}', '{upload}')".format(category=category, upload=upload.filename))

	connection.commit()
	id=connection.execute('SELECT last_insert_rowid()').next()[0]
	connection.close()
	entries= [( id, category, upload.filename )]
	return template("template/upload.html", entries=entries)
	
#===========delete upload===========	
@get('/upload/hamos/<id>/')
def upload_hamos(id=id):
	connection =sqlite3.connect('test.db')
	connection.execute("DELETE from upload WHERE id={id}".format(id=id))
	connection.commit()
	connection.close()
	return upload()	
	
##======troka upload=======	
@get('/upload/troka/<id>/')
def upload_troka(id=id):
	connection = sqlite3.connect('test.db')
	query = "SELECT id, category, upload FROM upload WHERE id = {id}".format(id=id)
	entries = connection.execute(query)
	entry = entries.next()
	category= entry[1]
	upload.filename = entry[2]
	return template('template/upload_foun.html', category=category, upload=upload.filename)

@post('/upload/troka/<id>/')
def upload_troka(id=id):
	category = request.forms.get('category')
	upload = request.files.get('upload')
	name, ext = os.path.splitext(upload.filename)
	if ext not in ('.png', '.jpg', '.jpeg', '.JPG', '.gif'):
		return "File extension not allowed."
	
	save_path = "static/upload/"##====={category}".format(category=category)
	if not os.path.exists(save_path):
	    os.makedirs(save_path)

	file_path = "{category}/{upload}".format(category=save_path, upload=upload.filename)
	upload.save(file_path)
	connection = sqlite3.connect('test.db')
	query = "UPDATE upload set category='{category}', upload='{upload}' WHERE id={id}".format( category=category, upload=upload.filename, id=id)
	entries = connection.execute(query)
	connection.commit()
	entries = [(id, category, upload.filename)]
	return template('template/upload.html', entries = entries)
#======================================================
#----------koding upload images to'o iha ne'e-----------------	

#######================================================
#---------koding upload videos--------------------------
@get('/videos1/')
def videos1():
	connection = sqlite3.connect("test.db")
	entries = connection.execute("SELECT id, category, upload FROM videos")
	return template('template/videos1.html', entries=entries)

@get('/videos/')
def videos():
	user_is_authenticated('/videoas/')
	connection = sqlite3.connect("test.db")
	entries = connection.execute("SELECT id, category, upload FROM videos")
	return template('template/videos.html', entries=entries)
	
@get('/videos/foun/')
def videos_foun():
    user_is_authenticated('/videos/foun/')
    return template('template/videos_foun.html', category="", upload="", sala="")
	
@post('/videos/foun/')
def kria_videos_foun():
	category = request.forms.get('category')
	upload = request.files.get('upload')
	name, ext = os.path.splitext(upload.filename)
	if ext not in ('.MP4', '.mp4', '.flv', '.WMV', '.mpg', '.avi'):
		return "File extension not allowed."
	save_path = "static/videos/"####{category}".format(category=category)
	if not os.path.exists(save_path):
	    os.makedirs(save_path)

	file_path = "{category}/{upload}".format(category=save_path, upload=upload.filename)
	upload.save(file_path)
	connection = sqlite3.connect("test.db")
	connection.execute("INSERT INTO videos( category, upload) VALUES ( '{category}', '{upload}')".format(category=category, upload=upload.filename))

	connection.commit()
	id=connection.execute('SELECT last_insert_rowid()').next()[0]
	connection.close()
	entries= [( id, category, upload.filename )]
	return template("template/videos.html", entries=entries)
	
#===========delete upload VIDEO===========	
@get('/videos/hamos/<id>/')
def videos_hamos(id=id):
	connection =sqlite3.connect('test.db')
	connection.execute("DELETE from videos WHERE id={id}".format(id=id))
	connection.commit()
	connection.close()
	return videos()	
	
##======troka videos=======	
@get('/videos/troka/<id>/')
def videos_troka(id=id):
	connection = sqlite3.connect('test.db')
	query = "SELECT id, category, upload FROM videos WHERE id = {id}".format(id=id)
	entries = connection.execute(query)
	entry = entries.next()
	category= entry[1]
	upload.filename = entry[2]
	return template('template/videos_foun.html', category=category, upload=upload.filename)

@post('/videos/troka/<id>/')
def videos_troka(id=id):
	category = request.forms.get('category')
	upload = request.files.get('upload')
	name, ext = os.path.splitext(upload.filename)
	if ext not in ('.MP4', '.mp4', '.flv', '.WMV', '.mpg', '.avi'):
		return "File extension not allowed."
	
	save_path = "static/videos/"##====={category}".format(category=category)
	if not os.path.exists(save_path):
	    os.makedirs(save_path)

	file_path = "{category}/{upload}".format(category=save_path, upload=upload.filename)
	upload.save(file_path)
	connection = sqlite3.connect('test.db')
	query = "UPDATE videos set category='{category}', upload='{upload}' WHERE id={id}".format( category=category, upload=upload.filename, id=id)
	entries = connection.execute(query)
	connection.commit()
	entries = [(id, category, upload.filename)]
	return template('template/videos.html', entries = entries)
#======================================================
#----------koding upload video to'o iha ne'e----------


@get('/music1/')
def music1():
	connection = sqlite3.connect("test.db")
	entries = connection.execute("SELECT id, category, upload FROM music")
	return template('template/music1.html', entries=entries)

@get('/music/')
def music():
	user_is_authenticated('/music/')
	connection = sqlite3.connect("test.db")
	entries = connection.execute("SELECT id, category, upload FROM music")
	return template('template/music.html', entries=entries)
	
@get('/music/foun/')
def music_foun():
    user_is_authenticated('/music/foun/')
    return template('template/music_foun.html', category="", upload="", sala="")
	
@post('/music/foun/')
def kria_music_foun():
	category = request.forms.get('category')
	upload = request.files.get('upload')
	name, ext = os.path.splitext(upload.filename)
	if ext not in ('.mp3', '.MP3'):
		return "File extension not allowed."
	save_path = "static/audios/"####{category}".format(category=category)
	if not os.path.exists(save_path):
	    os.makedirs(save_path)

	file_path = "{category}/{upload}".format(category=save_path, upload=upload.filename)
	upload.save(file_path)
	connection = sqlite3.connect("test.db")
	connection.execute("INSERT INTO music( category, upload) VALUES ( '{category}', '{upload}')".format(category=category, upload=upload.filename))

	connection.commit()
	id=connection.execute('SELECT last_insert_rowid()').next()[0]
	connection.close()
	entries= [( id, category, upload.filename )]
	return template("template/music.html", entries=entries)
	
#===========delete upload musik===========	
@get('/music/hamos/<id>/')
def videos_hamos(id=id):
	connection =sqlite3.connect('test.db')
	connection.execute("DELETE from music WHERE id={id}".format(id=id))
	connection.commit()
	connection.close()
	return music()	
	
##======troka videos=======	
@get('/music/troka/<id>/')
def music_troka(id=id):
	connection = sqlite3.connect('test.db')
	query = "SELECT id, category, upload FROM music WHERE id = {id}".format(id=id)
	entries = connection.execute(query)
	entry = entries.next()
	category= entry[1]
	upload.filename = entry[2]
	return template('template/music_foun.html', category=category, upload=upload.filename)

@post('/music/troka/<id>/')
def music_troka(id=id):
	category = request.forms.get('category')
	upload = request.files.get('upload')
	name, ext = os.path.splitext(upload.filename)
	if ext not in ('.mp3', '.MP3'):
		return "File extension not allowed."
	
	save_path = "static/audios/"##====={category}".format(category=category)
	if not os.path.exists(save_path):
	    os.makedirs(save_path)

	file_path = "{category}/{upload}".format(category=save_path, upload=upload.filename)
	upload.save(file_path)
	connection = sqlite3.connect('test.db')
	query = "UPDATE music set category='{category}', upload='{upload}' WHERE id={id}".format( category=category, upload=upload.filename, id=id)
	entries = connection.execute(query)
	connection.commit()
	entries = [(id, category, upload.filename)]
	return template('template/music.html', entries = entries)
#======================================================
##-------------koding upload musik to'o iha ne'e-------
	#################################
	################LOGIN############;;;

@get('/login/') 
def login():
	if 'destination' in request.query: #;;;;authenticated husu ba query atu hatudu nia dalan....
		destination = request.query['destination']
	else:
		destination='/'  #;;;;detination hatudu dalan ba pagina ne'ebe ita atu visita....
	return template('template/login.html', username="", password="", sala="", destination=destination)

	
@post('/login/') 
def authenticate():
	username = request.forms.get('username')
	password = request.forms.get('password')
	destination = request.forms.get('destination')
	if check_login(username, password):
		response.set_cookie("account", username, path='/', secret=AUTHENTICATE_SECRET)
		return redirect(destination)
	else:
		return template('template/login.html', username=username, password=password, sala="Username ka password sala...! Kontaktu ony (670) 78150465", destination="")
	####################################
	#======DEFINE DESTINATION===========
					
def user_is_authenticated(destination=None):
	username = request.get_cookie("account", secret=AUTHENTICATE_SECRET)
	if not username:
		if destination:
			return redirect('/login/?destination={destination}'.format(destination=destination))
		else:
			return template('/login/')
	else: 
		return username
	
	
		#=====cookie nia funsaun atu rai dados ne'ebe ita hatama ba 
			#=====username ho password se bainhira ita la sig-out maka password ne'ebe ita hatama nafatin iha ita nia web nia laran.....
def check_login(username, password):
	if not username or not password:
		return False
		
	else:
		connection = sqlite3.connect("test.db")
		entries = connection.execute("SELECT username FROM user WHERE username='{username}' AND password='{password}'".format(username=username, password=password))	
	
	if entries.fetchone():
		return True
	else:
		return False
		
###########################
#=============LOG OUT======
@get('/logout/')
def logout():
	reset() # drop the cookie
	
def reset():
	response.delete_cookie("account", path="/")
	return redirect('/')
	
	###########################	
	#=============USER=========
@get('/user1/') 
def user1():
	user_is_authenticated('/user1/')
	connection = sqlite3.connect("test.db")#####ligasaun ho data base##########
	entries = connection.execute("SELECT id, username, password, first_name, last_name, gender, birthday, district, email, phone_number FROM user")
	return template('template/user1.html',entries = entries)

@get('/user1/<id>/')
def user_entry(id=id):
		connection = sqlite3.connect("test.db")
		query = "SELECT id, username, password, first_name, last_name, gender, birthday, district, email, phone_number FROM user WHERE id = {id}".format(id=id)
		
		entries = connection.execute(query)
		
		return template('template/user1.html', entries=entries)
		
@get('/user/') 
def user():
	connection = sqlite3.connect("test.db")
	entries = connection.execute("SELECT id, username, password, first_name, last_name, gender, birthday, district, email, phone_number FROM user")
	return template('template/user.html',entries = entries)

@get('/user/foun/') 
def user_foun():
	username = user_is_authenticated('/user/foun/')
	return template('template/user_foun.html', username="", password="", first_name="", last_name="", gender="", birthday="", district="", email="", phone_number="", sala="")
	
	
@get('/user/<id>/')
def user_entry(id=id):
		connection = sqlite3.connect("test.db")
		query = "SELECT id, username, password, first_name, last_name, gender, birthday, district, email, phone_number FROM user WHERE id = {id}".format(id=id)
		entries = connection.execute(query)
		return template('template/user.html', entries=entries)
		
			
@get('/user/hamos/<id>/')
def user_hamos(id=id):
	connection = sqlite3.connect("test.db")
	connection.execute("DELETE FROM user WHERE id={id}".format(id=id))
	connection.commit()
	connection.close()
	return user1()
	
@get('/user/troka/<id>/')
def kria_user_uluk(id=id):
	connection = sqlite3.connect("test.db")
	query = "SELECT id, username, password, first_name, last_name, gender, birthday, district, email, phone_number FROM user WHERE id = {id}".format(id=id)
	entries = connection.execute(query)
	entry=entries.next()
	
	username = entry[1]	      
	password = entry[2]
	first_name = entry[3]					
	last_name = entry[4]	
	gender = entry[5] 
	birthday = entry[6] 
	district = entry[7] 
	email = entry[8]
	phone_number = entry[9]
	return template('template/user_foun.html',username=username, password=password, first_name=first_name, last_name=last_name, gender=gender, birthday=birthday, district=district, email=email, phone_number=phone_number, sala="")
	
@post('/user/troka/<id>/')
def kria_user_ikus(id=id):
	username = request.forms.get('username')
	password = request.forms.get('password')
	first_name= request.forms.get('first_name')
	last_name = request.forms.get('last_name')
	gender = request.forms.get('gender')
	birthday = request.forms.get('birthday')
	district = request.forms.get('district')
	email = request.forms.get('email')
	phone_number = request.forms.get('phone_number')
	
	username = unicode(username, 'utf-8')
	password = unicode(password, 'utf-8')
	first_name = unicode(first_name, 'utf-8')
	last_name = unicode(last_name, 'utf-8')
	gender = unicode(gender, 'utf-8')
	birthday = unicode(birthday, 'utf-8')
	district = unicode(district, 'utf-8')
	email = unicode(email, 'utf-8')
	phone_number = unicode(phone_number, 'utf-8')
	
	if check_user(username, password, first_name, last_name, gender, birthday, district, email, phone_number):
		connection = sqlite3.connect("test.db")
		query = "UPDATE user SET username = ?, password = ?, first_name = ?, last_name = ?, gender = ?, birthday = ?, district = ?, email = ?, phone_number = ? WHERE id=?;"
		args = (username, password, first_name, last_name, gender, birthday, district, email, phone_number, id)
		connection.execute(query, args)
		connection.commit()
		entries = [(id, username, password, first_name, last_name, gender, birthday, district, email, phone_number)]
	
		return template('template/user1.html', entries=entries,) 
	else:
		return template('template/user_foun.html',username=username, password=password, first_name=first_name, last_name=last_name, gender=gender, birthday=birthday, district=district, email=email, phone_number=phone_number, sala="Dadus sala...!",)
	
@post('/user/foun/')
def kria_user_foun():
	username = request.forms.get('username')
	password = request.forms.get('password')
	first_name = request.forms.get('first_name')
	last_name = request.forms.get('last_name')
	gender = request.forms.get('gender')
	birthday = request.forms.get('birthday')
	district = request.forms.get('district')
	email = request.forms.get('email')
	phone_number = request.forms.get('phone_number')

	username = unicode (username, 'utf-8')
	password = unicode (password, 'utf-8')
	first_name = unicode (first_name, 'utf-8')
	last_name = unicode (last_name, 'utf-8')
	gender = unicode (gender, 'utf-8')
	birthday = unicode (birthday, 'utf-8')
	district = unicode (district, 'utf-8')
	email = unicode (email, 'utf-8')
	phone_number = unicode (phone_number, 'utf-8')
	if check_user( username, password, first_name, last_name, gender, birthday, district, email, phone_number ):
		connection = sqlite3.connect("test.db")
		try:
			query =  "INSERT INTO user( username, password, first_name, last_name, gender, birthday, district, email, phone_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
			args = ( username, password, first_name, last_name, gender, birthday, district, email, phone_number )
			connection.execute(query, args)
			connection.commit()
		
			id=connection.execute('SELECT last_insert_rowid()').next()[0]

			connection.close()
		
			entries= [(id,username,password,first_name,last_name,gender,birthday,district,email,phone_number)]
		
			return template('template/user1.html', entries=entries,)
		except sqlite3.IntegrityError, e:
			return template('template/user_foun.html',username=username, password=password, first_name=first_name, last_name=last_name, gender=gender, birthday=birthday, district=district, email=email, phone_number=phone_number, sala="Dadus sala...!")
	else:
			return template('template/user_foun.html',username=username, password=password, first_name=first_name, last_name=last_name, gender=gender, birthday=birthday, district=district, email=email, phone_number=phone_number, sala="Dadus sala...!",)

def check_user(username, password, first_name, last_name, gender, birthday, district, email, phone_number):
	if not username:
		return False
	elif not password:
		return False
	elif not first_name:
		return False
	elif not last_name:
		return False
	elif not gender:
		return False
	elif not birthday:
		return False
	elif not district:
		return False
	elif not email:
		return False
	elif not phone_number:
		return False
	else: 
		return True
	
	##########################################
	#==================NOTICIA================

@get('/noticia/') 
def noticia():
	user_is_authenticated('/noticia/')
	connection = sqlite3.connect("test.db")
	entries = connection.execute("SELECT id, naran, email, mensajen FROM noticia")
	return template('template/noticia.html',entries=entries)
		
@get('/noticia/foun/') 
def noticia_foun():
	user_is_authenticated('/noticia/foun/')
	return template('template/noticia_foun.html',naran="", email="", mensajen="", sala="")
	
@post('/noticia/foun/') 
def kria_noticia_foun():
	naran = request.forms.get('naran')
	email = request.forms.get('email')
	mensajen = request.forms.get('mensajen')
	
	naran = unicode(naran, 'utf-8')
	email = unicode(email, 'utf-8')
	mensajen = unicode(mensajen, 'utf-8')
	
	if check_noticia_foun(naran, email, mensajen):
		connection = sqlite3.connect("test.db")
		query = "INSERT  INTO noticia (naran, email, mensajen) VALUES (?, ?, ?)"
		args = (naran, email, mensajen)
		connection.execute(query, args)
		connection.commit()
		id = connection.execute('SELECT last_insert_rowid()').next()[0]
		connection.close()
		entries = [(id, naran, email, mensajen)]
		
		return template('template/noticia.html', entries=entries,)
	else:
		return template('template/noticia_foun.html',naran=naran,
													email=email,
													mensajen=mensajen,
													sala="Kodigu ita hatama sala, Favor koko fali !!!")

def check_noticia_foun(naran, email, mensajen):
	if not naran:
		return False
	elif not email:
		return False
	elif not mensajen:
		return False	
	else: 
		return True
						


@get('/noticia/<id>/')
def noticia_entry(id=id):
		connection = sqlite3.connect("test.db")
		query = "SELECT id, naran, email, mensajen FROM noticia WHERE id={id}".format(id=id)
		entries = connection.execute(query)
		return template('template/noticia.html', entries=entries,)

@get('/noticia/hamos/<id>/')
def noticia_hamos(id=id):
	connection = sqlite3.connect("test.db")
	connection.execute("DELETE FROM noticia WHERE id={id}".format(id=id))
	connection.commit()
	connection.close()
	
	return noticia()
		
@get('/noticia/troka/<id>/')
def kria_noticia_uluk(id=id):
	connection = sqlite3.connect("test.db")
	query = "SELECT id, naran, email, mensajen FROM noticia WHERE id = {id}".format(id=id)
	entries = connection.execute(query)
	entry=entries.next()
	
	naran=entry[1]
	email=entry[2]
	mensajen=entry[3]
	
	return template('template/noticia_foun.html',naran=naran, email=email, mensajen=mensajen, sala="")
	
@post('/noticia/troka/<id>/')
def kria_noticia_ikus(id=id):
	naran = request.forms.get('naran')
	email = request.forms.get('email')
	mensajen = request.forms.get('mensajen')
	
	naran = unicode(naran, 'utf-8')
	email = unicode(email, 'utf-8')
	mensajen = unicode(mensajen, 'utf-8')
	
	if check_noticia(naran, email, mensajen):
		connection = sqlite3.connect("test.db")
		query = "UPDATE noticia SET naran=?, email=?, mensajen=? WHERE id=?;"
		args = (naran, email, mensajen, id)
		connection.execute(query, args)
		connection.commit()
	
		entries = [(id, naran, email, mensajen)]
	
		return template('template/noticia.html', entries=entries,) 
	else:
		return template('template/noticia_foun.html',naran=naran, email=email, mensajen=mensajen)

		
def check_noticia(naran, email, mensajen):
	if not naran:
		return False
	elif not email:
		return False
	elif not mensajen:
		return False
	else: 
		return True	

	
@get('/noticia1/') 
def noticia1():
	connection = sqlite3.connect("test.db")
	entries = connection.execute("SELECT id, naran, email, mensajen FROM noticia")
	return template('template/noticia1.html', entries=entries)
	 
@get('/noticia1/<id>/')
def noticia1_entry(id=id):
		connection = sqlite3.connect("test.db")
		query = "SELECT id, naran, email, mensajen FROM noticia WHERE id={id}".format(id=id)
		entries = connection.execute(query)
		return template('template/noticia1.html', entries=entries,)

									
	##################################		
	#=============BLOG================

@get('/blog/') 
def blog():
	user_is_authenticated('/blog/')
	connection = sqlite3.connect("test.db")
	entries = connection.execute("SELECT id, title, body FROM blog")
	return template('template/blog.html',entries = entries)
	
@get('/blog/foun/') 
def blog_foun():
	user_is_authenticated('/blog/foun/')
	return template('template/blog_foun.html', title="", body="", sala="")
	
@post('/blog/foun/') 
def kria_blog_foun():
	title = request.forms.get('title')
	body = request.forms.get('body')
	
	title = unicode(title, 'utf-8')
	body = unicode(body, 'utf-8')
	
	if check_blog_foun(title, body):
	
		connection=sqlite3.connect("test.db")
		query = "INSERT  INTO  blog (title, body) VALUES (?, ?)"
		args = (title, body)
		connection.execute(query, args)
		connection.commit()
		id = connection.execute('SELECT last_insert_rowid()').next()[0]
		connection.commit()
		connection.close()
		
		entries = [(id, title, body)]
		
		return template('template/blog.html', entries=entries,)
	else:
		return template('template/blog_foun.html',title=title, body=body, sala="Kodigu ita hatama sala, Favor koko fali !!!",)

def check_blog_foun(title, body,):
	if  title=="":
		return False
	elif body=="":
		return False
	else: 
		return True


@get('/blog1/') 
def blog1():
	connection = sqlite3.connect("test.db")
	entries = connection.execute("SELECT id, title, body FROM blog")
	return template('template/blog1.html',entries = entries)


@get('/blog1/<id>/')
def blog1_entry(id=id):
		connection = sqlite3.connect("test.db")
		query = "SELECT id, title, body FROM blog WHERE id = {id}".format(id=id)
		entries = connection.execute(query)
		return template('template/blog1.html', entries=entries,)
	

@get('/blog/<id>/')
def blog_entry(id=id):
		connection = sqlite3.connect("test.db")
		query = "SELECT id, title, body FROM blog WHERE id = {id}".format(id=id)
		entries = connection.execute(query)
		return template('template/blog.html', entries=entries,)
		
			
@get('/blog/hamos/<id>/')
def blog_hamos(id=id):
	connection = sqlite3.connect("test.db")
	connection.execute("DELETE FROM blog WHERE id={id}".format(id=id))
	connection.commit()
	connection.close()
	return blog()
	
@get('/blog/troka/<id>/')
def kria_blog_uluk(id=id):
	connection = sqlite3.connect("test.db")
	query = "SELECT id, title, body FROM blog WHERE id = {id}".format(id=id)
	entries = connection.execute(query)
	entry=entries.next()
	
	title=entry[1]
	body=entry[2]
	
	return template('template/blog_foun.html',title=title, body=body, sala="")
	
@post('/blog/troka/<id>/')
def kria_blog_ikus(id=id):
	title = request.forms.get('title')
	body = request.forms.get('body')
	
	title = unicode(title, 'utf-8')
	body = unicode(body, 'utf-8')
	
	if check_blog(title, body):
		connection = sqlite3.connect("test.db")
		query = "UPDATE blog SET title=?, body=? WHERE id=?;"
		args = (title, body, id)
		connection.execute(query, args)
		connection.commit()
		entries = [(id, title, body)]
	
		return template('template/blog.html', entries=entries,) 
	else:
		return template('template/blog_foun.html',title=title, body=body, sala="Dadus sala...!",)
		
def check_blog(title, body,):
	if not title:
		return False
	elif not body:
		return False
	else: 
		return True	


###############=======Import filepath:path========########	
@route('/static/<filepath:path>')
def static(filepath):
    return static_file(filepath, root='static/')


run(host='0.0.0.0',port=8003, reloader=True, debug=True)
