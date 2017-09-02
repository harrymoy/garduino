void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int tempValue = analogRead(A3);
  int ldrValue = analogRead(A2);
  int soilMoistureValue = analogRead(A0);
  int airQualityValue = analogRead(A4);
  int humidityValue = analogRead(A1);
  float tempVoltage = tempValue * (5000.0 / 1024.0);
  float negTemp = (tempVoltage - 500) / 10;
  int temperature = negTemp * -1;

  float ldrVoltage = ldrValue * 0.0048828125;
  int lux = 500/(10*((5-ldrVoltage)/ldrVoltage));

  String jsonString = "{\"Temperature\":\"";
    jsonString += temperature;
    jsonString +="\",\"Lux\":\"";
    jsonString += lux;
    jsonString +="\",\"Humidity\":\"";
    jsonString += (humidityValue / 10);
    jsonString +="\",\"Air Quality\":\"";
    jsonString += (airQualityValue / 10);
    jsonString +="\",\"Soil Moisture\":\"";
    jsonString += (soilMoistureValue / 10);
    jsonString +="\"}";

    Serial.println(jsonString);
    delay(5000);
}
