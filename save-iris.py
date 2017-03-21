from sklearn.datasets import load_iris
import numpy as np
import csv
import argparse


def save_as_csv(file):
    iris = load_iris()
    shape = (iris.data.shape[0], iris.data.shape[1]+1)
    output = np.zeros(shape)
    output[:,:-1] = iris.data
    output[:,-1] = iris.target
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(output)
    print("wrote iris data to:", file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--destination", '-d', default="iris.txt", help="the destination file to save this to")
    args = parser.parse_args()
    save_as_csv(args.destination)
