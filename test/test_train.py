
import pandas as pd
from sklearn.linear_model import LogisticRegression
import os
def test_train_model_file_exists():

    """verifie que fichier  churn_model_clean.pkl est crée apres"""

    assert os.path.exists('data/churn_model_clean.pkl'), ( "le fichier churn_model_clean.pkl n'existe pas apres l'ex")



    


