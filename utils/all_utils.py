import matplotlib.pyplot as plt
import numpy as np
import joblib  # FOR SAVING MY MODEL AS A BINARY FILE
from matplotlib.colors import ListedColormap
import os

plt.style.use("fivethirtyeight")

def prepare_data(df):
  X = df.drop("y", axis=1)

  y = df["y"]

  return X, y