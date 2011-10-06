import web
import os
from web import form

render = web.template.render('templates/')

urls = (
	'/','index',
	'/(.*)','reset_pwd'
)

app = web.application(urls, globals())

chpass = form.Form(
    form.Textbox('username',
		form.notnull),
    form.Password('password',
		form.notnull),
    form.Password('password_again',
		form.notnull),
    form.Button('Submit'),
    validators = [form.Validator("Passwords didn't match.", lambda i: i.password == i.password_again)]
)

userform = form.Form(
    form.Textbox('username',
		form.notnull),
)

class index:
	def GET(self):
		f = userform()
		return render.formtest(f)

	def POST(self):
		f = userform()
		if not f.validates():
			return render.formtest(f)
		else:
			raise web.seeother('/%s' % (f['username'].value)) 
		

class reset_pwd:
	def GET(self, name):
		f = chpass()
		f['username'].value = name
		return render.formtest(f) 

	def POST(self, name):
		f = chpass()
		if not f.validates():
			return render.formtest(f)
		else:
			foo = os.system('sudo python chpass.py %s %s' % (f['username'].value,f['password'].value))	
			return 'Password has been reset. %s' % (foo) 

if __name__ == "__main__": app.run()
