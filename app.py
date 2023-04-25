import mysql.connector
from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='FD3npAChvj#',
        database='com4003'
    )


@app.route('/cool_form', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted
        field1 = request.form['field1']
        field2 = request.form['field2']
        
        # Insert data into the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO your_table_name (field1, field2) VALUES (%s, %s)", (field1, field2))
        conn.commit()
        cursor.close()
        conn.close()

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('cool_form.html')

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)











