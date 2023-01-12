from flask import Flask, render_template, request, redirect
import imaplib
import email

# Create a Flask app
app = Flask(__name__)

# Define a route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for the login page
@app.route('/login', methods=['POST'])
def login():
    # Get the email and password from the form
    email = request.form['email']
    password = request.form['password']

    # Connect to the email server
    mail = imaplib.IMAP4_SSL('imap.example.com')

    # Login
    mail.login(email, password)

    # Select the inbox
    mail.select('inbox')

    # Search for all emails and retrieve the first one
    status, messages = mail.search(None, 'ALL')
    if status == 'OK':
        data = []
        for message in messages[0].split():
            # Fetch the email
            status, data_temp = mail.fetch(message, '(RFC822)')
            if status == 'OK':
                # Parse the email
                msg = email.message_from_bytes(data_temp[0][1])
                subject = msg['Subject']
                sender = msg['From']
                for part in msg.walk():
                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get('Content-Disposition') is None:
                        continue
                    filename = part.get_filename()
                    if filename is not None:
                        data.append({'Subject': subject, 'From': sender, 'Attachment': filename})
        # Close the mailbox
        mail.close()

        # Return the emails and attachments as a table
        return render_template('emails.html', data=data)
    else:
        # Return an error message if the login failed
        return redirect('/')

# Run the app
if __name__ == '__main__':
    app.run(port=8000)

