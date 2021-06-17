# Conectando Sheets ao Colab

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import auth
auth.authenticate_user()

import gspread
from oauth2client.client import GoogleCredentials

gc = gspread.authorize(GoogleCredentials.get_application_default())

# Importando o arquivo desejado do Sheets

worksheet = gc.open('File')
page1 = worksheet.sheet1

dados_df = pd.DataFrame(page1.get_all_records())
display(dados_df)
