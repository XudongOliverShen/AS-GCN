import numpy as np
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='check the output of data preprocessing.')
    parser.add_argument('--data_path', default='./AS-GCN/AS-GCN/data/nturgb_d/xsub/train_data_joint_pad.npy')

    arg = parser.parse_args()

    fp = np.load(arg.data_path)

    fp = fp