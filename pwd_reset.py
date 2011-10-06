import web
import os
from web import form
web.config.smtp_server = 'email.somewhere.com'
to_address = 'foo@foo'
from_address = 'foo@foo'

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
			link = '0.0.0.0:8080/%s' % (f['username'].value)
			my_message = 'To reset your password please follow this link %s' % (link)
			web.sendmail(from_address, to_address, 'Password Reset', my_message)
			return 'Thanks.  Check your email.'
		

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
			#return 'sudo python /home/ncigf/drc/chpass.py %s %s' % (f['username'].value,f['password'].value)
			return 'Password has been reset. %s' % (foo) 

if __name__ == "__main__": app.run()
