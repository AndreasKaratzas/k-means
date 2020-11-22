
import pandas
import matplotlib.pyplot as plt


def kerberos():
    cols = ["X", "Y"]
    labels = ["Vec", "Center"]
    colors = ["r"]
    file_dir = '../../Downloads/'
    Vec = pandas.read_csv(file_dir + 'Vec.csv', names=cols, delimiter=None, engine='python')
    Center = pandas.read_csv(file_dir + 'Center.csv', names=cols, delimiter=None, engine='python')

    count = 0

    for df in [Vec, Center]:
        plt.scatter(df["X"], df["Y"], label=labels[count])
        if count >= 1:
            rows = df.shape[0]
            for r in range(rows):
                i, j = df.iloc[r, :]
                c = plt.Circle((i, j), radius=3, color=colors[count - 1], alpha=.2)
                plt.gca().add_artist(c)
        count += 1

    plt.legend(bbox_to_anchor=(1, 1), loc="upper left")
    plt.savefig("kmeans.png")
    plt.show()


if __name__ == '__main__':
    kerberos()
