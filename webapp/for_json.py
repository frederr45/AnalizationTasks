import pandas as pd


def predicts(json_, model_columns, classifier):
    query_ = pd.get_dummies(pd.DataFrame(json_, index=[0]))
    query = query_.reindex(columns=model_columns, fill_value=1)
    prediction = (classifier.predict(query))
    return {
        "POLICY_ID": str(*query["POLICY_ID"]),
        "POLICY_IS_RENEWED": int(*prediction)
        }
