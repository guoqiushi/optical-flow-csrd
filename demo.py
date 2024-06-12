from torchvision.models.optical_flow import Raft_Small_Weights
from torchvision.utils import flow_to_image
import numpy as np
import torch
import matplotlib.pyplot as plt
import torchvision.transforms.functional as F
import torchvision.transforms as T
from torchvision.models.optical_flow import raft_small
from PIL import Image
import cv2
import os
import glob
from raft import RaftTool
import argparse


device = 'cuda'
model = raft_small(weights=Raft_Small_Weights.DEFAULT, progress=False).to(device)
model = model.eval()

raft = RaftTool()


def gen_gif(frame_folder,start,end,out_path=''):
    frames = []
    img_type = os.listdir(frame_folder)[0].split('.')[-1]
    print(img_type)
    img_list = sorted(glob.glob('{}/*.{}'.format(frame_folder,img_type)))
    for i in range(start,end):
        out = raft.infer(img_list[i],img_list[i+1])
        frames.append(out)
        frames[0].save('{}/{}_animation.gif'.format(out_path,out_path), save_all=True, append_images=frames[1:], loop=0, duration=200)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('frame_folder',type=str,help='folder path of frames')
    parser.add_argument('start',type=int,help='start frame')
    parser.add_argument('end',type=int,help='end frame')
    parser.add_argument('out_path',type=str)

    args = parser.parse_args()

    frame_folder = args.frame_folder
    start = args.start
    end = args.end
    out_path = args.out_path

    gen_gif(frame_folder,start,end,out_path)


