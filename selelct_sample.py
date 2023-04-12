# -*- coding: utf-8 -*- 
# @Time : 2023/4/11 14:14 
# @Author : DirtyBoy 
# @File : selelct_sample.py
import random
import pandas as pd

def txt_to_list(txt_path):
    f = open(txt_path, "r")
    return f.read().splitlines()


def save_to_vocab(goal, file_path):
    f = open(file_path, "w")
    for line in goal:
        f.write(line + '\n')
    f.close()


if __name__ == '__main__':
    data  = pd.read_csv('D:\Pycharm\Project\Android_malware_detector_set\APIGraph\Dataset\\androzoo_csv\\2021_Benign.csv')
    list1 = data['sha256'].tolist()
    if len(list1)>=2100:
        list1 = random.sample(list1,2100)
    save_to_vocab(list1,'D:\Pycharm\Project\Android_malware_detector_set\APIGraph\Dataset\download_dataset_sha256\\2021_benign.txt')



