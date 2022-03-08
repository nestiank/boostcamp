import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms

from typing import Tuple

import numpy as np
import selectivesearch as ss

class SelectiveSearch(nn.Module):
    def __init__(self) -> None:
        super().__init__()

        self.resize = transforms.Resize([227, 227])

    def init_params(self, images: torch.Tensor) -> None:
        # Parameters to be trained
        self.alexnet = []

        # Parameters not to be trained
        self.labeled_images = []
        self.image_regions = []
        self.predictions = []

        for i, image in enumerate(images):
            # Prepare AlexNet
            self.alexnet.append([])

            # Selective search
            labeled_image, regions = ss.selective_search(image, scale=500, sigma=0.8, min_size=10)
            self.labeled_images.append(labeled_image)
            self.image_regions.append(regions)
            self.predictions.append([])

            for _, square in enumerate(regions):
                if len(square['labels'] == 1):
                    # Prepare AlexNet
                    alexnet = models.alexnet(pretrained=True, num_classes=20)
                    self.alexnet[i].append(alexnet)

                    # Prepare making predictions
                    self.predictions[i].append(0)

    def forward(self, images: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        '''
        Input: images
        Returns:
            labeled_images: extended image([R, G, B, label])
            predictions:
                i: image index
                j: label index (when the length of square['labels'] is 1, it is the label index)
                predictions[i][j]: class prediction
        '''
        for i, image in enumerate(images):
            for j, square in enumerate(self.image_regions[i]):
                if len(square['labels'] == 1):
                    # Crop image
                    left, top, width, height = square['rect']
                    cropped_image = transforms.functional.crop(image, top=top, left=left, height=height, width=width)
                    cropped_image = self.resize(cropped_image)

                    # Train AlexNet
                    self.predictions[i][j] = np.argmax(self.alexnet[i][j](cropped_image))

        return (self.labeled_images, self.predictions)

class RCNN(nn.Module):
    def __init__(self) -> None:
        super().__init__()

        self.ss = SelectiveSearch()

    def init_params(self, images: torch.Tensor) -> None:
        self.ss.init_params(images)

        # Train only AlexNets
        for param in self.ss.parameters():
            param.requires_grad = False
        for alexnet in np.array(self.ss.alexnet).flatten():
            for param in alexnet.parameters():
                param.requires_grad = True

    def forward(self, images: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        return self.ss(images)

class NotImplementedLoss(nn.modules.loss._Loss):
    def __init__(self) -> None:
        super().__init__()

    def forward(self, input: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError
