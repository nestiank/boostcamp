import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transform

import numpy as np
import selectivesearch as ss

class SelectiveSearch(nn.Module):
    def __init__(self):
        super().__init__()

        # Parameters not to be trained
        self.initial = True
        self.resize = transform.Resize([227, 227])
        self.labeled_images = []
        self.image_regions = []
        self.predictions = []

        # Parameters to be trained
        self.alexnet = []

    def forward(self, images):
        '''
        Input: images
        Returns:
            labeled_images: extended image([R, G, B, label])
            predictions:
                i: image index
                j: label index (when the length of square['labels'] is 1, it is the label index)
                predictions[i][j]: class prediction
        '''
        if self.initial:
            self.initial = False
            for i, image in enumerate(images):
                # Prepare AlexNet
                self.alexnet.append([])

                # Selective search
                labeled_image, regions = ss.selective_search(image, scale=500, sigma=0.8, min_size=10)
                self.labeled_images.append(labeled_image)
                self.image_regions.append(regions)

                # Making class predictions
                self.predictions.append([])
                for j, square in enumerate(regions):
                    if len(square['labels'] == 1):
                        # Prepare AlexNet
                        alexnet = models.alexnet(pretrained=True, num_classes=20)
                        self.alexnet[i].append(alexnet)

                        # Crop image
                        left, top, width, height = square['rect']
                        cropped_image = transform.functional.crop(image, top=top, left=left, height=height, width=width)
                        cropped_image = self.resize(cropped_image)

                        # Train AlexNet
                        class_pred = np.argmax(self.alexnet[i][j](cropped_image))
                        self.predictions[i].append(class_pred)
        else:
            for i, image in enumerate(images):
                for j, square in enumerate(self.image_regions[i]):
                    if len(square['labels'] == 1):
                        # Crop image
                        left, top, width, height = square['rect']
                        cropped_image = transform.functional.crop(image, top=top, left=left, height=height, width=width)
                        cropped_image = self.resize(cropped_image)

                        # Train AlexNet
                        self.predictions[i][j] = np.argmax(self.alexnet[i][j](cropped_image))

        return self.labeled_images, self.predictions

class RCNN(nn.module):
    def __init__(self):
        super().__init__()

        self.ss = SelectiveSearch()

    def forward(self, images):
        labeled_images, predictions = self.ss(images)

        # Train only AlexNets
        for param in self.ss.parameters():
            param.requires_grad = False
        for alexnet in self.ss.alexnet.flatten():
            for param in alexnet.parameters():
                param.requires_grad = True

        return (labeled_images, predictions)

class NotImplementedLoss(nn.modules.loss._Loss):
    def __init__(self):
        super().__init__()

    def forward(self, input, target):
        raise NotImplementedError
