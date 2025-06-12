# Aircraft Fuel Consumption Prediction Model

This project provides a web application to predict the fuel consumption of an aircraft based on various input parameters using a machine learning model.

## Features

- Predicts aircraft fuel consumption based on:
  - Flight Distance (km)
  - Number of Passengers
  - Flight Duration (hours)
  - Aircraft Type (Type 1, Type 2, Type 3)
- User-friendly web interface built with Streamlit

## Getting Started

### Prerequisites

- Python 3.7+
- The required Python packages (see [requirements.txt](Aircraft_Fuel_Consumption_prediction_Model-Sample/requirements.txt))
- The trained model file: `aircraft.pkl`

### Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/yourusername/Aircraft_Fuel_Consumption_prediction_Model-Sample.git
    cd Aircraft_Fuel_Consumption_prediction_Model-Sample
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure `aircraft.pkl` is present in the project directory.

### Running the App

Start the Streamlit app with:
```sh
streamlit run app.py
```

The app will open in your browser. Enter the required parameters and click "Predict" to see the predicted fuel consumption.

## Project Structure

- [`app.py`](Aircraft_Fuel_Consumption_prediction_Model-Sample/app.py): Streamlit web application source code
- [`aircraft.pkl`](Aircraft_Fuel_Consumption_prediction_Model-Sample/aircraft.pkl): Trained machine learning model
- [`requirements.txt`](Aircraft_Fuel_Consumption_prediction_Model-Sample/requirements.txt): List of required Python packages

## License

This project is licensed under the MIT License.

## Acknowledgements

- Built with [Streamlit](https://streamlit.io/)
- Machine learning powered by [scikit-learn](https://scikit-learn.org/)
