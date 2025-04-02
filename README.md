# Stock Forecasting with Streamlit

This project demonstrates how to forecast stock prices using machine learning and deploy the model as an interactive web application using Streamlit.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Overview

Stock forecasting involves predicting future stock prices based on historical data and various market indicators. This project utilizes machine learning techniques to forecast stock prices and Streamlit to create an interactive web application for real-time predictions.

## Project Structure

The repository contains the following files:

- `app.py`: The main Python script that loads stock data, trains a forecasting model, and sets up the Streamlit web application.
- `requirements.txt`: A text file listing the Python packages required to run the project.

## Setup Instructions

To set up and run the project locally, follow these steps:

1. **Clone the Repository**: Use the following command to clone the repository to your local machine:

   ```bash
   git clone https://github.com/dattatejaofficial/Stock-Forecasting-using-Streamlit.git
   ```

2. **Navigate to the Project Directory**: Move into the project directory:

   ```bash
   cd Stock-Forecasting-using-Streamlit
   ```

3. **Create a Virtual Environment** (optional but recommended): Set up a virtual environment to manage project dependencies:

   ```bash
   python3 -m venv env
   ```

   Activate the virtual environment:

   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install Dependencies**: Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the Streamlit web application:

1. **Ensure the Virtual Environment is Activated**: Make sure your virtual environment is active (refer to the setup instructions above).

2. **Run the Streamlit App**: Execute the following command:

   ```bash
   streamlit run app.py
   ```

3. **Access the Web Application**: After running the command, Streamlit will provide a local URL (typically `http://localhost:8501`) in the terminal. Open this URL in your web browser to interact with the stock forecasting application.

## Dependencies

The project requires the following Python packages:

- `streamlit`
- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `yfinance`

These dependencies are listed in the `requirements.txt` file. To install them, run:

```bash
pip install -r requirements.txt
```
