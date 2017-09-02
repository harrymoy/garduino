var express = require('express');
var gardenHandler = require('./bl/gardenHandler.js')

var app = express();


app.get('/soil', function(req, res) {
  gardenHandler.getSoil();
});

app.get('/ph', function(req, res) {
  gardenHandler.getPh();
});

app.get('/temperature', function(req, res) {
  gardenHandler.getTemperature();
});

app.get('/light', function(req, res) {
  gardenHandler.getLight();
});

