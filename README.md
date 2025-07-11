# Soil Fertility Prediction Web Application

## 🌱 Overview
This is an end-to-end machine learning web application that predicts soil fertility based on various soil parameters. The application uses a trained Decision Tree model to classify soil fertility into three categories: Low, Medium, and High fertility.

## 🚀 Features
- **Beautiful Web Interface**: Modern, responsive UI for easy data input
- **Real-time Predictions**: Instant fertility predictions based on soil parameters
- **Multiple Input Parameters**: Supports District, Soil Type, pH Level, Organic Matter %, and NPK content
- **Deployment Ready**: Easy to deploy on cloud platforms

## 📋 Input Parameters
1. **District**: Geographic location (Rajasthan districts)
2. **Soil Type**: Type of soil (Alkaline, Clay, Loamy, etc.)
3. **pH Level**: Soil acidity/alkalinity (0-14 scale)
4. **Organic Matter (%)**: Percentage of organic content
5. **Nitrogen Content (kg/ha)**: Nitrogen levels in soil
6. **Phosphorus Content (kg/ha)**: Phosphorus levels in soil
7. **Potassium Content (kg/ha)**: Potassium levels in soil

## 🎯 Output
The model predicts one of three fertility categories:
- **High Fertility**: Optimal conditions for crop growth
- **Medium Fertility**: Moderate fertility, may need some improvements
- **Low Fertility**: Poor conditions, requires significant soil treatment

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7+
- pip package manager

### Quick Start
1. **Clone/Download the project**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```bash
   python application.py
   ```
4. **Open your browser** and go to: `http://localhost:5000`

### Testing the Prediction
Run the test script to verify everything works:
```bash
python test_prediction.py
```

## 🌐 Usage
1. Open the web application in your browser
2. Click "Start Soil Analysis"
3. Fill in all the soil parameters
4. Click "Analyze Soil Fertility"
5. View your prediction result!

## 📊 Model Information
- **Algorithm**: Decision Tree Regressor
- **Accuracy**: ~95% on test data
- **Training Data**: Soil samples from Rajasthan districts
- **Features**: 7 input parameters (geographic + chemical)

## 🔧 Technical Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **ML Framework**: Scikit-learn
- **Model Tracking**: MLflow with DagsHub
- **Data Processing**: Pandas, NumPy

## 📁 Project Structure
```
├── application.py              # Flask web application
├── app.py                     # Model training pipeline
├── test_prediction.py         # Test script
├── requirements.txt           # Dependencies
├── artifacts/                 # Trained models and data
│   ├── model.pkl             # Trained ML model
│   └── preprocessor.pkl      # Data preprocessor
├── src/ENDTOENDDSPROJECT/    # Source code
│   ├── components/           # ML pipeline components
│   ├── pipelines/           # Training and prediction pipelines
│   └── utils.py             # Utility functions
└── templates/               # HTML templates
    ├── index.html          # Home page
    └── home.html           # Prediction form
```

## 🚀 Deployment Options

### Local Development
```bash
python application.py
```
Access at: `http://localhost:5000`

### Cloud Deployment
The application is ready for deployment on:
- **Heroku**: Add `Procfile` with `web: python application.py`
- **AWS EC2**: Use the application.py as entry point
- **Google Cloud Platform**: Deploy using App Engine
- **Azure**: Use Azure Web Apps

## 📈 Model Performance
- **Training Accuracy**: 95%+
- **Cross-validation Score**: Robust performance across different data splits
- **Feature Importance**: pH Level and NPK content are key predictors

## 🔍 Sample Prediction
**Input:**
- District: Jaipur, Soil Type: Clay, pH: 7.5, Organic Matter: 2.0%
- Nitrogen: 30.0 kg/ha, Phosphorus: 20.0 kg/ha, Potassium: 40.0 kg/ha

**Output:** Medium Fertility

## 🙏 MLflow Tracking
```python
import dagshub
dagshub.init(repo_owner='vibhutisarode', repo_name='datascience', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
```

---

**Happy Farming! 🌾**