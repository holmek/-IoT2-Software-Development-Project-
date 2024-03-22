from flask import Flask, render_template
import asyncio
import sqlite3
from datetime import datetime
import paho.mqtt.subscribe as subscribe

app = Flask(__name__)

async def mqtt_subscriber():
    conn = sqlite3.connect('mqtt/sensor_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_data (
                        timestamp NUMERIC,
                        temperature INTEGER,
                        humidity INTEGER,
                        air_quality INTEGER,
                        percentage INTEGER,
                        orientation INTEGER,
                        detection INTEGER
                    )''')
    conn.commit()

    while True:
        sensor_data_message = subscribe.simple("sg5-2a", hostname="mqtt.eclipseprojects.io")
        sensor_data_contents = sensor_data_message.payload.decode('utf-8').split(',')
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('INSERT INTO sensor_data VALUES (?, ?, ?, ?, ?, ?, ?)', (current_time,) + tuple(sensor_data_contents))
        conn.commit()

@app.route('/')
def index():
    conn = sqlite3.connect('mqtt/sensor_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, temperature, humidity, air_quality, orientation, percentage FROM sensor_data ORDER BY timestamp DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    return render_template('index.html', timestamp=row[0], temperature=row[1], humidity=row[2], air_quality=row[3], orientation=row[4], percentage=row[5])

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(mqtt_subscriber())
    app.run(debug=True)
