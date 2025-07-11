from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.ENDTOENDDSPROJECT.pipelines.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

def get_suggestions(prediction_value, input_data):
    """Generate actionable suggestions based on prediction and input parameters"""
    suggestions = {
        "recommendations": [],
        "actions": [],
        "warnings": []
    }
    
    if prediction_value == 0:  # Low Fertility
        suggestions["recommendations"] = [
            "🔬 Conduct detailed soil testing for micronutrients",
            "🌱 Add organic compost or well-rotted manure",
            "⚗️ Consider soil pH adjustment if needed",
            "💧 Improve irrigation and drainage systems"
        ]
        suggestions["actions"] = [
            "Add 2-3 tons of organic matter per hectare",
            "Apply balanced NPK fertilizer (10-26-26 or similar)",
            "Consider crop rotation with leguminous plants",
            "Implement soil conservation practices"
        ]
        if input_data.ph_level < 6.0:
            suggestions["warnings"].append("⚠️ Soil is too acidic - consider lime application")
        elif input_data.ph_level > 8.0:
            suggestions["warnings"].append("⚠️ Soil is too alkaline - consider sulfur application")
            
    elif prediction_value == 1:  # Medium Fertility
        suggestions["recommendations"] = [
            "📈 Monitor soil regularly to maintain fertility levels",
            "🌿 Apply targeted fertilizers based on crop requirements",
            "🔄 Implement crop rotation to maintain soil health",
            "💚 Continue organic matter addition"
        ]
        suggestions["actions"] = [
            "Apply 1-2 tons of compost per hectare annually",
            "Use precision fertilizer application",
            "Monitor and adjust irrigation schedules",
            "Practice sustainable farming methods"
        ]
        
    else:  # High Fertility (prediction_value == 2)
        suggestions["recommendations"] = [
            "✅ Excellent soil conditions for optimal crop growth",
            "🎯 Focus on crop selection for maximum yield",
            "📊 Monitor nutrient levels to prevent over-fertilization",
            "🌾 Consider high-value or intensive farming"
        ]
        suggestions["actions"] = [
            "Maintain current soil management practices",
            "Select crops with high yield potential",
            "Implement precision agriculture techniques",
            "Regular monitoring to sustain fertility levels"
        ]
    
    # Add specific NPK recommendations
    if input_data.nitrogen_content < 25:
        suggestions["actions"].append("🔶 Increase nitrogen application - current level is low")
    if input_data.phosphorus_content < 15:
        suggestions["actions"].append("🔶 Boost phosphorus levels - consider rock phosphate")
    if input_data.potassium_content < 35:
        suggestions["actions"].append("🔶 Add potassium fertilizer - current level needs improvement")
        
    return suggestions

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            district=request.form.get('district'),
            soil_type=request.form.get('soil_type'),
            ph_level=float(request.form.get('ph_level')),
            organic_matter=float(request.form.get('organic_matter')),
            nitrogen_content=float(request.form.get('nitrogen_content')),
            phosphorus_content=float(request.form.get('phosphorus_content')),
            potassium_content=float(request.form.get('potassium_content'))
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)
        print("After Prediction")
        
        # Convert fertility status to readable format
        fertility_mapping = {0: "Low Fertility", 1: "Medium Fertility", 2: "High Fertility"}
        fertility_status = fertility_mapping.get(results[0], "Unknown")
        
        # Generate suggestions based on prediction
        suggestions = get_suggestions(results[0], data)
        
        # Model information
        model_info = {
            "model_name": "Decision Tree Classifier",
            "confidence": "High",
            "training_data": "800+ soil samples from Rajasthan",
            "accuracy": "95%+"
        }
        
        return render_template('home.html', 
                             results=fertility_status, 
                             suggestions=suggestions, 
                             model_info=model_info,
                             input_data=data)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
