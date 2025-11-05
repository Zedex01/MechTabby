import tensorflow as tf
import numpy as np
import sys, os

def main():
    print("==============================================================================================")
    root = get_root()
    print("Tensorflow Version: ",tf.__version__)
    print("GPUS: ", tf.config.list_physical_devices('GPU'))
    print(root)
    print("==============================================================================================")

    #Lets load the data from the csv
    iris_data = os.path.join(root, "data/dataset/iris.data")
    data = np.genfromtxt(iris_data, delimiter=",", dtype=None, encoding=None, skip_header=1)

    #Extract attributes and classifications
    attr = np.array([row[:-1] for row in data], dtype=float) #First 4 columns as floats
    lbl = np.array([row[-1] for row in data]) #Last column of strings

    #Since tf cannot output strings as result, must map classifications to ints
    species_to_int = {
        "setosa": 0,
        "veriscolor": 1,
        "virginica": 2 
        }

    int_lbl = np.array([species_to_int[s] for s in lbl])
    print("==============================================================================================")
    print(attr)
    print("==============================================================================================")
    print(lbl)
    print("==============================================================================================")
    print(int_lbl)

#Functions & Methods
def get_root():
    return os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    main()