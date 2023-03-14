from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# make the pages dynamic with </string:page_name> args
@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_pages(page_name):
    return render_template(page_name)

# create a function to store data received from the contact me form
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email}, {subject}, {message}')


# create a function to store data received from the contact me form into a csv file
def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])  # pass the email parameters directly as a list 

# function for the contact form on webpage to be able to capture and send data to our server
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong!'

# manual way to link all the pages but specifying each page component

# @app.route('/contact.html')
# def contact_me():
#     return render_template('contact.html')

# @app.route('/works.html')
# def my_works():
#     return render_template('works.html')

# @app.route('/thankyou.html')
# def thank_you():
#     return render_template('thankyou.html')


if __name__ == '__main__':
    app.run()