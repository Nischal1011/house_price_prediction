import joblib
import os
import json
import numpy as np
import pandas as pd

def model_fn(model_dir: str):
    """
    Deserialize fitted model
    """
    model_artifcat = joblib.load(os.path.join(model_dir, "xg_boost_model.joblib"))
    return model_artifcat


def input_fn(request_body, content_type = 'application/json'):
    """
    Input has to be in JSON format
    """
    try:
        request_body = json.loads(request_body)
        inpVar = request_body['Input']
        input_df = pd.DataFrame(inpVar)
        return input_df
    except Exception as e:
        print(e)



def predict_fn(input_data, model):
    y_pred_test_xgb = model.predict(input_data)
    predicted_sale_price = np.expm1(y_pred_test_xgb)
    return predicted_sale_price



def output_fn(predicted_sale_price):
    return predicted_sale_price['Body'].read().decode('utf-8')



  