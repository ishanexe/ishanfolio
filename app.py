from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('reviews.html')

@app.route('/submit_review', methods=['POST'])
def submit_review():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        review = request.form['review']

        # Here you can save the review to a file or a database

        return 'Review submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
