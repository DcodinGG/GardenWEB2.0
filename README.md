
# GardenWEB2.0

**GardenWEB2.0** is a web application developed using Python, Flask, and Chart.js to monitor and visualize soil moisture, temperature, and watering data for plants. The app provides detailed graphs of sensor data and allows users to manage and view plant information efficiently.

## Features

- Real-time monitoring of soil moisture, temperature, and air humidity.
- Interactive data visualizations using Chart.js.
- Plant data management and lookup.
- Responsive design with enhanced user interface using CSS.
- MySQL database connection for data storage.

## Requirements

To run this application, ensure you have the following:

- Python 3.10 or higher
- Flask 2.3.0 or higher
- MySQL Server (can be hosted remotely)
- Chart.js for graph visualizations
- Other dependencies listed in `requirements.txt`

## Installation

Follow these steps to set up and run the project:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/DcodinGG/GardenWEB2.0.git
   cd GardenWEB2.0
   ```

2. **Create and activate a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables** in the `.env` file (create this file if it doesn't exist) for the MySQL database connection:

   ```env
   DB_HOST='your-database-host'
   DB_NAME='your-database-name'
   DB_USER='your-database-user'
   DB_PASSWORD='your-database-password'
   DB_PORT=3306
   ```

5. **Initialize the database**:

   Run the necessary scripts to set up the database and seed initial data:

   ```bash
   python app/database/db_setup.py
   python app/database/seed_data.py
   ```

6. **Run the application**:

   ```bash
   python run.py
   ```

   The app will be available at `http://localhost:5000`.

## Usage

- Access the application at `http://localhost:5000`.
- The home page includes two main sections:
  - Query the `weather` table, which stores sensor readings.
  - A list of plants for managing each plant's information.
- View specific details for each plant, including moisture and watering level graphs, on the `details` page.

## Project Structure

The project structure is as follows:

```
GardenWEB2.0/
│   .env
│   requirements.txt
│   run.py
│
└───app
    │   config.py
    │   forms.py
    │   models.py
    │   routes.py
    │   __init__.py
    │
    ├───database
    │   │   db_setup.py
    │   │   seed_data.py
    │
    ├───static
    │   ├───css
    │   │       style.css
    │   ├───images
    │   └───js
    │           script.js
    │
    ├───templates
    │       index.html
    │       plants.html
    │       plant_detail.html
    │
    └───__pycache__
```

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push your changes to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
