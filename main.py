from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/validate-user', methods=['POST'])
def validate_user():
    username = request.form['user-id']
    password = request.form['user-password']
    verify = request.form['verify-password']
    email = request.form['user-email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20:
        username_error = 'Not a valid username'
        
    if ' ' in username:
        username_error = 'Not a valid username'

    if len(password) < 3 or len(password) > 20:
        password_error = 'Not a valid password'

    if ' ' in password:
        password_error = 'Not a valid password' 

    if len(verify) < 3 or len(verify) > 20:
        verify_error = 'Not a valid password'

    if ' ' in verify:
        verify_error = 'Not a valid password'

    if verify != password:
        verify_error = 'Passwords do not match'

    if len(email) > 0: 
        if len(email) < 3 or len(email) > 40:
            email_error = 'Not a valid email'
    
        elif ' ' in email:
                email_error = 'Not a valid email'

        elif not '@' in email and not '.' in email:
                email_error = 'Not a valid email'

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('Welcome.html', username=username)
    else:
        return render_template('edit.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route("/") 
def index():
    return render_template('edit.html')



app.run()
