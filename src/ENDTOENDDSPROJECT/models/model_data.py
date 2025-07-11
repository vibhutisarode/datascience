import pickle
import base64

def get_model_and_preprocessor():
    # Load the model and preprocessor from artifacts
    try:
        with open('artifacts/model.pkl', 'rb') as f:
            model_bytes = f.read()
        with open('artifacts/preprocessor.pkl', 'rb') as f:
            preprocessor_bytes = f.read()
            
        # Convert to base64 strings
        model_b64 = base64.b64encode(model_bytes).decode('utf-8')
        preprocessor_b64 = base64.b64encode(preprocessor_bytes).decode('utf-8')
        
        return model_b64, preprocessor_b64
    except Exception as e:
        print(f"Error loading model files: {e}")
        return None, None

def load_model_from_b64(model_b64, preprocessor_b64):
    try:
        # Decode base64 strings back to bytes
        model_bytes = base64.b64decode(model_b64)
        preprocessor_bytes = base64.b64decode(preprocessor_b64)
        
        # Load the model and preprocessor
        model = pickle.loads(model_bytes)
        preprocessor = pickle.loads(preprocessor_bytes)
        
        return model, preprocessor
    except Exception as e:
        print(f"Error loading model from base64: {e}")
        return None, None
