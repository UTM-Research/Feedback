from matplotlib import pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['Positive', 'Negative', 'Neutral']
students = [23,17,35]
ax.pie(students, labels = langs,autopct='%1.2f%%')
plt.show()
import matplotlib.pyplot as plt
languages = 'Positive', 'Negative', 'Neutral'
popuratity = [22.2, 17.6, 8.8]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
# explode 1st slice
explode = (0.1, 0, 0)
# Plot
plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago", bbox={'facecolor':'0.8', 'pad':5})
plt.show()
import matplotlib.pyplot as plt
def shape(Positive,Negative,Neutral):
    energy=[]
    whole= Positive + (-1)* Negative + Neutral
    energy.append(100 * float(Positive) / float(whole))
    energy.append(100 * float(Negative) / float(whole))
    energy.append(100 * float(Neutral) / float(whole))
    plt.style.use('ggplot')
    x = ['Positive', 'Negative', 'Neutral']
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, energy, color=['green', 'red', 'Gray'])
    plt.xlabel("Sentiment polarity")
    plt.ylabel("Sentiment score (%)")
    plt.title("Students feedback on Module")
    plt.xticks(x_pos, x)
    plt.show()
