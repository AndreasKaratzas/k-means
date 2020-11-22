
import os
import pandas
import matplotlib.pyplot as plt


def kerberos():
    cols = ["X", "Y"]
    labels = ["Vec", "Center"]
    items = [f for f in os.listdir(os.getcwd() + "\\") if os.path.isfile(os.path.join(os.getcwd() + "\\", f))]
    old_centers = list(filter(lambda k: "old_Center" in k, items))
    new_centers = list(filter(lambda k: "new_Center" in k, items))
    vec = list(filter(lambda k: "Vec" in k, items))
    colors = ["r"]
    file_dir = os.getcwd() + "\\"

    count = 0
    filecount = 0
    
    # old_center output
    Vec = pandas.read_csv(file_dir + vec[0], names=cols, delimiter=None, engine='python')
    Center = pandas.read_csv(file_dir + old_centers[0], names=cols, delimiter=None, engine='python')
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
    plt.savefig("kmeans" + str(filecount) + ".png")
    plt.show()

    # new_center output
    for file in new_centers:
        count = 0
        Vec = pandas.read_csv(file_dir + vec[0], names=cols, delimiter=None, engine='python')
        Center = pandas.read_csv(file_dir + file, names=cols, delimiter=None, engine='python')
        for df in [Vec, Center]:
            plt.scatter(df["X"], df["Y"], label=labels[count])
            if count >= 1:
                rows = df.shape[0]
                for r in range(rows):
                    i, j = df.iloc[r, :]
                    c = plt.Circle((i, j), radius=3, color=colors[count - 1], alpha=.2)
                    plt.gca().add_artist(c)
            count += 1
        filecount += 1
        plt.legend(bbox_to_anchor=(1, 1), loc="upper left")
        plt.savefig("kmeans" + str(filecount) + ".png")
        plt.show()


if __name__ == '__main__':
    kerberos()
