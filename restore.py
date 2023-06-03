import numpy as np
import os
from skimage.io import imsave
from basicsr.utils import imwrite
from gfpgan import GFPGANer

def img_repair(infile, outfile):
    upscale = 2
    version = 1.2
    bg_tile = 400
    weights = 0.5

    aligned = False
    only_center_face = False

    arch = 'clean'
    channel_multiplier = 2
    model_path = "c:/Users/Gowtham Ramesh/Desktop/FullStackWebDevelopment/scripts/PythonGUI_ImageViewer_Editor/GFPGAN/experiments/pretrained_models/GFPGANCleanv1-NoCE-C2.pth"
    
    bg_upsampler = None

    restorer = GFPGANer(
        model_path=model_path,
        upscale=upscale,
        arch=arch,
        channel_multiplier=channel_multiplier,
        bg_upsampler=bg_upsampler)

    cropped_faces, restored_faces, restored_img = restorer.enhance(
            infile,
            has_aligned=aligned,
            only_center_face=only_center_face,
            paste_back=True,
            weight=weights)

    out = os.path.join(outfile, 'restored.png')
    imsave(out, restored_img)
