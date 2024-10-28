from flask import render_template
from app import app, get_db_connection

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Get weather data
    cursor.execute("SELECT * FROM weather ORDER BY date")
    weather_data = cursor.fetchall()

    # Get plant data
    cursor.execute("SELECT * FROM plants")
    plants = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('index.html', weather_data=weather_data, plants=plants)

@app.route('/moisture_watering/<int:plant_id>')
def moisture_watering(plant_id):
    connection = get_db_connection()
    
    # Get moisture data
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM moistures WHERE plant_id = %s ORDER BY date", (plant_id,))
    moistures_data = cursor.fetchall()

    # Get watering data
    cursor.execute("SELECT * FROM watering WHERE plant_id = %s ORDER BY date", (plant_id,))
    watering_data = cursor.fetchall()

    # Get the plant name
    cursor.execute("SELECT name FROM plants WHERE plant_id = %s", (plant_id,))
    plant_name = cursor.fetchone()
    cursor.close()
    connection.close()

    # Check if the plant name was found
    if plant_name and 'name' in plant_name:
        plant_name = plant_name['name']
    else:
        plant_name = "Unknown Plant"

    # Calculate the max value for the slider
    max_slider_value = max(0, len(moistures_data) - 72)

    return render_template('moisture_watering.html', 
                        moistures_data=moistures_data, 
                        watering_data=watering_data, 
                        plant_name=plant_name,
                        max_slider_value=max_slider_value)
