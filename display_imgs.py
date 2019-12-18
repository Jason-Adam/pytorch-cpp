"""Script to generate images from model output"""
import argparse

import matplotlib.pyplot as plt
import torch

PARSER = argparse.ArgumentParser()
PARSER.add_argument("-i", "--sample-file", required=True)
PARSER.add_argument("-o", "--out-file", default="out.png")
PARSER.add_argument("-d", "--dimension", type=int, default=3)
OPTIONS = PARSER.parse_args()
MODULE = torch.jit.load(OPTIONS.sample_file)
IMAGES = list(MODULE.parameters())[0]

for index in range(OPTIONS.dimension * OPTIONS.dimension):
    image = IMAGES[index].detach().cpu().reshape(28, 28).mul(255).to(torch.uint8)
    array = image.numpy()
    axis = plt.subplot(OPTIONS.dimension, OPTIONS.dimension, 1 + index)
    plt.imshow(array, cmap="gray")
    axis.get_xaxis().set_visible(False)
    axis.get_yaxis().set_visible(False)

plt.savefig(OPTIONS.out_file)
print("Saved ", OPTIONS.out_file)
