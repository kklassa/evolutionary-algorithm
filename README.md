# evolutionary-algorithm

### evolutionary algorithm implementation in python

***evolutionary.py*** contains the algoritm implementation in three versions:
  - **evolutionary returns** only the best fitness found and the individual for which it is reached
  - **evolutionary_for_plots** returns an array containing points representing individuals with best fitness values in each iteration
  - **evolutionary_plot_all** returns an array of all fitness values that were reached by the algorythm paired with the corresponding iterations

***simulation.py*** has access to all files essential for solving minimization problems with the evolutionary algorithm as well as visualising the results in various ways

***test_evolutionary.py*** contains simple unit tests for the algorithm

***time_evolutionary.py*** contains a functions which can be used to measure the egzecution time of the algorithm

**utils** module contains filies with simple utility functions used throughout the project
