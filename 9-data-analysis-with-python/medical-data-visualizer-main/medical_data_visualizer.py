import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('9-data-analysis-with-python\\medical-data-visualizer-main\\medical_examination.csv')

# 2
df['bmi'] = df['weight'] / (df['height']/100)**2
df['overweight'] = df['bmi'].apply(lambda bmi: int(bmi > 25))

# 3
df['gluc'] = df['gluc'].apply(lambda x: int(x > 1))
df['cholesterol'] = df['cholesterol'].apply(lambda x: int(x > 1))

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars='cardio', value_vars=('cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'))

    # 6 & 7
    df_cat = df_cat.groupby(['cardio', 'variable'], as_index=False).value_counts()
    df_cat = df_cat.rename(columns={'count':'total'})

    # 8
    fig = sns.catplot(x='variable', y='total', data=df_cat, hue='value', kind='bar', col='cardio').fig

    # 9
    fig.savefig('9-data-analysis-with-python\\medical-data-visualizer-main\\catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    cond1 = df['ap_lo'] <= df['ap_hi']
    cond2 = df['height'] >= df['height'].quantile(0.025)
    cond3 = df['height'] <= df['height'].quantile(0.975)
    cond4 = df['weight'] >= df['weight'].quantile(0.025)
    cond5 = df['weight'] <= df['weight'].quantile(0.975)

    df_heat = df[cond1 & cond2 & cond3 & cond4 & cond5].drop(columns=['bmi'])

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)

    # 14
    fig, ax = plt.subplots(figsize=(11, 9))

    # 15
    corr_vals = np.array(corr).flatten()
    corr_vals = corr_vals[~(corr_vals == 1)]

    sns.heatmap(corr, linewidth=1, annot=True, square=True, mask=mask, fmt='.1f', center=0, vmax=0.3, vmin=np.min(corr_vals), cbar_kws={'shrink':0.5, 'ticks':[-0.08, 0.00, 0.08, 0.16, 0.24]})

    # 16
    fig.savefig('9-data-analysis-with-python\\medical-data-visualizer-main\\heatmap.png')
    return fig