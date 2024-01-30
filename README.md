# Coordinates-Picker-Leaflet-Flask

Coordinates Picker is a web application that allows users to pick coordinates on a map, either by dragging a marker or clicking on the map. The selected latitude and longitude are then displayed in the form.


## Features

- Interactive map with draggable marker
- Ability to update coordinates by dragging the marker or clicking on the map
- Real-time display of latitude and longitude in the form
- User-friendly notifications for form submission and errors

## Technologies Used

- HTML
- CSS (Bootstrap for styling)
- JavaScript (Leaflet library for map functionality)
- Python (Flask framework for backend)

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/OmarKhalil10/Coordinates-Picker-Leaflet-Flask.git
```

### 2. Download virtualenv module
    
```bash
pip install virtualenv
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

```bash
source venv/Scripts/activate
```

### 5. Install the requirements

```bash
pip install -r requirements.txt
```

### 6. Run the flask app

```bash
Flask_APP=app.py 
Flask_ENV=development
FLASK_DEBUG=True
flask run --reload
```

1. Open index.html in a web browser.
2. Start picking coordinates!

when you are done, you can deactivate the virtual environment.

### 7. Deactivate the virtual environment

```bash
deactivate
```

## Usage

* Drag the marker to select a location on the map.
* Alternatively, click on the map to update the marker's position.
* The latitude and longitude values are displayed in the form.
* Click the "Submit Form" button to submit the coordinates.

Project Structure
```
Coordinates-Picker-Leaflet-Flask/
|-- index.html
|-- static/
    |-- css/
    |   |-- style.css
    |   |-- leaflet.css
    |-- js/
    |   |-- leaflet.js
    |   images/
    |   |-- marker-icon.png
    |   |-- ...
|-- templates/
    |-- index.html
|-- README.md
|-- app.py
|-- settings.py
|-- app.yaml
|-- credentials.yaml
|-- requirements.txt
|-- vars.env
|-- venv/
    |-- ...
```

## Code Details

1. Map Initialization

```
// Leaflet map initialization
var map = L.map('map').setView([0, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);
```

2. Marker and Map Interaction

```
// Draggable marker with dragend event
var marker = L.marker([0, 0], { draggable: true }).addTo(map);
marker.on('dragend', function (event) {
    var position = marker.getLatLng();
    document.getElementById('latitude').value = position.lat;
    document.getElementById('longitude').value = position.lng;
});

// Update marker and inputs on map click
map.on('click', function (e) {
    marker.setLatLng(e.latlng);
    document.getElementById('latitude').value = e.latlng.lat;
    document.getElementById('longitude').value = e.latlng.lng;
});
```
3. Notification Handling

```
// Show Bootstrap notification
function showNotification(message, type) {
    var notificationContainer = document.getElementById('notificationContainer');
    var notification = document.createElement('div');
    notification.className = 'alert alert-' + type + ' alert-dismissible fade show';
    notification.role = 'alert';
    notification.innerHTML = message;
    notificationContainer.appendChild(notification);
    setTimeout(function () {
        notificationContainer.removeChild(notification);
    }, 5000);
}
```

## Acknowledgments

1. Leaflet library: https://leafletjs.com/
2. Bootstrap library: https://getbootstrap.com/

## License
This project is licensed under the MIT License - see the LICENSE file for details.