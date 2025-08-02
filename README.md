# Incident-Ticket-Classification-
This project implements an automated classification system for customer service incident tickets to optimize IT service management workflows. It is designed to reduce manual workload by automatically assigning incident reports to the appropriate expertise domains
## Features
- Preprocesses messages (supports French and English)
- Classifies messages using a pre-trained deep learning model
- Simple and user-friendly Flask web interface
- Tokenization and text cleaning included

---

## Technologies
- Python 3.10
- Flask
- TensorFlow / Keras
- Pandas, Numpy

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/customer-service-classifier.git
    cd customer-service-classifier
    ```

2. Create and activate a virtual environment:
    - Windows CMD:
      ```bash
      py -3.10 -m venv venv
      venv\Scripts\activate
      ```
    - PowerShell:
      ```powershell
      py -3.10 -m venv venv
      venv\Scripts\Activate.ps1
      ```
    - Linux/Mac:
      ```bash
      python3.10 -m venv venv
      source venv/bin/activate
      ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

1. Run the Flask app:
    ```bash
    python app.py
    ```

2. Open your browser and go to:
    ```
    http://localhost:5000
    ```

3. Submit a customer message on the form and get the classification result.

---
## Contact

For questions or suggestions, feel free to reach out via my GitHub profile:  
[https://github.com/maziz933]
