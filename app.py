import numpy as np #linear algebra
import pandas as pd # data processing, CSV file 1/0 (e.g. pd.read_csv)
import streamlit as st
import atplotlib.pyplot as plt

# pip install streamlit panda numpy matplotlib seaborn
from skylearn.metrics.paiware import cosine_similarity
from skylearn.features.extraction.text import countvectorizer

#link do local dos dados
# https://www.kaggle.com/datasets/suraj520/music-dataset-song-information-and-lyrics?resource=download