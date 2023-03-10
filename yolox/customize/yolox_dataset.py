import numpy as np
import cv2
import os
from torch.utils.data.dataset import Dataset as torchDataset


class YOLOXDataset(torchDataset):
    def __init__(self, img_root, ann_file):
        self.img_root = img_root
        self.ann_file = ann_file
        self.anns = []
        with open(self.ann_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                ann = line.strip().split(' ')
                img_path = os.path.join(self.img_root, ann[0])
                objects = []
                for obj in ann[1:4]:
                    obj = [float(x) for x in obj.split(',')]
                    objects.append(obj)
                keypoints = []
                for keypnt in ann[5:]:
                    keypnt

                self.anns.append({'img_path': img_path, 'objects': objects})

    def __len__(self):
        return len(self.anns)

    def __getitem__(self, idx):
        ann = self.anns[idx]
        img = cv2.imread(ann['img_path'])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        objects = np.array(ann['objects'], dtype=np.float32)
        return img, objects
