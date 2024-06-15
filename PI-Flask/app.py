from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='energy_saver'
        )
        if connection.is_connected():
            print("Successfully connected to the database")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/tips')
def tips():
    return render_template('tips.html')

@app.route('/profile-settings')
def profile_settings():
    return render_template('profile-settings.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        connection = create_connection()
        cursor = connection.cursor()

        query = "INSERT INTO contact_messages (name, email, message) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, message))
        connection.commit()
        cursor.close()
        connection.close()

        flash('Mensaje enviado exitosamente')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/electrodomesticos', methods=['GET', 'POST'])
def electrodomesticos():
    if request.method == 'POST':
        name = request.form['name']
        brand = request.form['brand']
        model = request.form['model']
        energy_consumption = request.form['energy_consumption']

        connection = create_connection()
        cursor = connection.cursor()

        query = "INSERT INTO appliances (name, brand, model, energy_consumption) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, brand, model, energy_consumption))
        connection.commit()
        cursor.close()
        connection.close()

        flash('Electrodoméstico registrado exitosamente')
        return redirect(url_for('electrodomesticos'))

    return render_template('electrodomesticos.html')

if __name__ == '__main__':
    app.run(debug=True)

