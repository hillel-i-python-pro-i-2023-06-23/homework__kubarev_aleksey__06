import pandas as pd


def average():
    url = 'https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt'
    df = pd.io.parsers.read_csv(url)
    height = df[['Height(Inches)']].mean()
    weight = df[['Weight(Pounds)']].mean()

    height_cm = round(height*2.54, 2)
    weight_kg = round(weight*0.45359237, 2)

    print('Height', height_cm.values[0])
    print('Weight', weight_kg.values[0])