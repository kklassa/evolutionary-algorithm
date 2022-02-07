# evolutionary-algorithm

### evolutionary algorithm implementation in python

***evolutionary.py*** contains the algoritm implementation in three versions:
  - **evolutionary returns** only the best fitness found and the individual for which it is reached
  - **evolutionary_for_plots** returns an array containing points representing individuals with best fitness values in each iteration
  - **evolutionary_plot_all** returns an array of all fitness values that were reached by the algorythm paired with the corresponding iterations

***simulation.py*** has access to all files essential for solving minimization problems with the evolutionary algorithm as well as visualising the results in various ways

***test_evolutionary.py*** contains simple unit tests for the algorithm

***time_evolutionary.py*** contains a functions which can be used to measure the execution time of the algorithm

**utils** module contains filies with simple utility functions used throughout the project


### 3D best individual per iteration graph
generated using **evolutionary_for_plots**

![best](https://user-images.githubusercontent.com/74139325/152820125-72e65312-a18c-4900-ba95-34c3eba6aa0b.png)


### 2D fitness per iteration graph
generated using **evolutionary_plot_all**

![fitness](https://user-images.githubusercontent.com/74139325/152820095-81703d3e-1f01-4bbc-9567-6eab235b7ec2.png)
