# Garduino

The Garduino is an Arduino based system that has two components. The first is writing the data gathered from the sensors to a database. The second is the Node based component that makes the database accessible via a REST-based API.

### Why?

The original vision behind the Garduino was to allow hobbyist gardeners learn more about their garden without having to fork out on expensive equipment. The code is open-source so that you can add more components to your Arduino and tweak the code accordingly.

### How Does It Work?

garduino.ino takes data gathered from the sensors (you will need to tweak the pin number depending on your configuration) and writes the data in JSON format into the Serial port. As data is being written you will need writeToDb.py running to write data into the database, this reads from the Serial port, parses the JSON data and then writes it into an SQLite database. SQLite is used because it is lightweight and easy to understand.
Once the data is written to the database, the data is made available via a REST-based API. The API can be interfaced with to create a front-end component that visualises your garden data.
