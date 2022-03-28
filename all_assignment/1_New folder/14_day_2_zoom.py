import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
titanic = sns.load_dataset("titanic")
print(titanic)
p1 = sns.countplot(x='who', data=titanic, hue= 'alone')
p1.set_title("Plot for Counting")
plt.show()