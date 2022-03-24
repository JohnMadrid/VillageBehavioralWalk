# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as  pd

hit_df = pd.read_csv(f"HitEvents_new_02715e7a-5a68-471b-9e63-f056c5f0df81.csv")
#variables
g_length = 0.260
gaze = hit_df[hit_df["length"] > g_length]
face_cond = gaze["HON"].str.contains("face", regex=False, na=False)
face_fix = gaze[face_cond]
face_size = face_fix.index.size

df = pd.read_csv('Behavior_new_02715e7a-5a68-471b-9e63-f056c5f0df81.csv')

print(df["ETWTime"].describe())



hit_df
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
