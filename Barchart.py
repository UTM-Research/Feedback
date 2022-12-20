import matplotlib.pyplot as plt
def shape(Positive,Negative):
    energy=[]
    whole= Positive + (-1)* Negative
    energy.append(100 * float(Positive) / float(whole))
    energy.append(100 * float(Negative) / float(whole))
    plt.style.use('ggplot')
    x = ['Positive', 'Negative']
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, energy, color=['green', 'red'])
    plt.xlabel("Sentiment polarity")
    plt.ylabel("Sentiment score (%)")
    plt.title("Students feedback on Module 3")
    plt.xticks(x_pos, x)
    plt.show()



