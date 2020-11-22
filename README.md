# K-Means
This is an implementation of the well known clusterning algorithm **K-Means** from scratch. The algorithm is implemented in **C++ 17**. A small-scale demo shows how the program operates.

![Demo](https://raw.githubusercontent.com/andreasceid/k-means/master/kmeans.gif?token=AKD4DVB5OIZQUOAJ5WJ4QN27YO4VY)

There are 3 main directories:
* `data`: This is directory is used by the k-means algorithm to output the data computed throughout its execution
* `k-means`: This directory contains all `.h` and `.cpp` files
* `kmeans-visualize`: This directory contains a *Python* script used for visualization while testing the main program
* `png2gif`: This is a complementary script that concats all *PNG*s exported by the Python script to one GIF, like the above, helping with the visualization of the algorithm's progress

The algorithm is not configured for parallelism. This will be done in the future. The algorithm converges in the minute, even with huge dataset ($10000 \cdot 1000$). There are instructions in Greek uploaded (`documentation.pdf`).
