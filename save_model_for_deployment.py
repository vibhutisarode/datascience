"""
Run this script once before deployment to embed your model in the code.
"""
import os
from src.ENDTOENDDSPROJECT.models.model_data import get_model_and_preprocessor

def main():
    # Get base64 encoded model and preprocessor
    model_b64, preprocessor_b64 = get_model_and_preprocessor()
    
    if model_b64 is None or preprocessor_b64 is None:
        print("Error: Could not load model files")
        return
        
    # Create the embedded model file
    code = f'''# This file is auto-generated. Do not edit manually.
MODEL_B64 = "{model_b64}"
PREPROCESSOR_B64 = "{preprocessor_b64}"
'''
    
    # Save to a Python file
    output_path = os.path.join('src', 'ENDTOENDDSPROJECT', 'models', 'embedded_model.py')
    with open(output_path, 'w') as f:
        f.write(code)
    
    print(f"Successfully embedded model in {output_path}")

if __name__ == "__main__":
    main()
