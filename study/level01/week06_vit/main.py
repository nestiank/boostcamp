#
# ViT Implementation
#
# Paper citation
#
# An Image is Worth 16x16 Words:
# Transformers for Image Recognition at Scale
# 2020, Alexey Dosovitskiy et al.
# https://arxiv.org/pdf/2010.11929.pdf
#

import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

import os
import time
import pickle

import pandas as pd

from model import ViT

# For updating learning rate
def update_learning_rate(optimizer, lr):
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr

def train_and_eval(done_epochs, train_epochs):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    ######## Preparing Dataset ########
    print('Dataset: preparation start @ {}'.format(time.strftime('%c', time.localtime(time.time()))))

    timestamp = time.strftime('%c', time.localtime(time.time())).replace(':', '')
    location = {
        'base_path': './dataset',
        'checkpoints_path': './checkpoints/' + timestamp,
        'results_path': './results/' + timestamp,
        'history_path': './history/' + timestamp
    }
    if not os.path.isdir(location['checkpoints_path']):
        os.makedirs(location['checkpoints_path'])
        os.makedirs(location['results_path'])
        os.makedirs(location['history_path'])

    transform_train = transforms.Compose([
        transforms.Resize([224, 224]),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    transform_test = transforms.Compose([
        transforms.Resize([224, 224]),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    dataset_train = torchvision.datasets.ImageNet(
        root=location['base_path'],
        split='train',
        transform=transform_train
    )
    dataset_test = torchvision.datasets.ImageNet(
        root=location['base_path'],
        split='val',
        transform=transform_test
    )

    batch_size = 256
    train_loader = torch.utils.data.DataLoader(
        dataset=dataset_train,
        batch_size=batch_size,
        shuffle=True
    )
    test_loader = torch.utils.data.DataLoader(
        dataset=dataset_test,
        batch_size=batch_size,
        shuffle=False
    )

    ######## Model & Hyperparameters ########
    model = ViT().to(device)

    learning_rate = 0.1
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(
        model.parameters(),
        lr=learning_rate,
        weight_decay=0.0001,
        momentum=0.9
    )

    plot_bound = 0
    lr_update_ratio = 0.5
    printing_ratio = 0.1

    ######## Loading Model ########
    if done_epochs > 0:
        checkpoint = torch.load('./checkpoints/epoch' + str(done_epochs) + '.pt', map_location=device)
        model.load_state_dict(checkpoint['model'])
        optimizer.load_state_dict(checkpoint['optimizer'])
        with open('./history/epoch' + str(done_epochs) + '.pickle', 'rb') as fr:
            history = pickle.load(fr)
    else:
        history = {'train_loss': [], 'train_acc': []}

    ######## Train ########
    for epoch in range(done_epochs, done_epochs + train_epochs):
        if (epoch + 1) % (printing_ratio * train_epochs) == 0:
            print('Train: Epoch {:02d} start @ {}'.format(epoch + 1, time.strftime('%c', time.localtime(time.time()))))

        model.train()
        train_loss = 0
        total = 0
        correct = 0

        for batch_index, (images, labels) in enumerate(train_loader):
            if (batch_index + 1) % (printing_ratio * batch_size) == 0:
                print('Batch {} / {}'.format(batch_index + 1, batch_size))

            images = images.to(device)
            labels = labels.to(device)

            # Forward pass
            outputs = model(images)
            loss = criterion(outputs, labels)

            # Backward pass and optimization
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # Train loss
            train_loss += loss.item()

            # Train accuracy
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        train_acc = 100 * correct / total

        if (epoch + 1) > plot_bound:
            history['train_loss'].append(train_loss)
            history['train_acc'].append(train_acc)

        if (epoch + 1) % (printing_ratio * train_epochs) == 0:
            print('Train: Epoch [{:02d}/{:02d}], Loss: {:.4f}'.format(epoch + 1, done_epochs + train_epochs, train_loss))
            print('Train accuracy: {:.4f}%'.format(train_acc))

        # Decay learning rate
        if (epoch + 1) % (lr_update_ratio * train_epochs) == 0:
            learning_rate /= 10
            update_learning_rate(optimizer, learning_rate)

        # Save checkpoint
        if (epoch + 1) % (printing_ratio * train_epochs) == 0:
            checkpoint = {'model': model.state_dict(), 'optimizer': optimizer.state_dict()}
            torch.save(checkpoint, location['checkpoints_path'] + '/epoch' + str(epoch + 1) + '.pt')

        ######## Saving History ########
        if (epoch + 1) % (printing_ratio * train_epochs) == 0:
            with open(location['history_path'] + '/epoch' + str(epoch + 1) + '.pickle', 'wb') as fw:
                pickle.dump(history, fw)

    print('Finished training @ {}'.format(time.strftime('%c', time.localtime(time.time()))))

    ######## Test ########
    print('Test: evaluation start @ {}'.format(time.strftime('%c', time.localtime(time.time()))))

    model.eval()

    with torch.no_grad():
        test_loss = 0
        total = 0
        correct = 0

        for batch_index, (images, labels) in enumerate(test_loader):
            images = images.to(device)
            labels = labels.to(device)

            # Forward pass
            outputs = model(images)
            loss = criterion(outputs, labels)

            # Test loss
            test_loss += loss.item()

            # Test accuracy
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        test_acc = 100 * correct / total

        print('Test loss: {:.4f}'.format(test_loss))
        print('Test accuracy: {:.4f}%'.format(test_acc))

    ######## Learning Statistics ########
    if train_epochs == 0:
        epoch = done_epochs - 1

    plt.subplot(2, 1, 1)
    plt.plot(range(plot_bound + 1, epoch + 2), history['train_loss'], label='Train', color='red', linestyle='dashed')

    plt.title('Loss history')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(range(plot_bound + 1, epoch + 2), history['train_acc'], label='Train', color='red', linestyle='dashed')

    plt.title('Accuracy history')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.tight_layout()
    plt.savefig(location['results_path'] + '/result' + time.strftime('_%Y%m%d_%H%M%S', time.localtime(time.time())) + '.png')

if __name__ == '__main__':
    # Last checkpoint's training position
    done_epochs = 0

    # How much epochs to train now
    train_epochs = 10

    train_and_eval(done_epochs, train_epochs)
