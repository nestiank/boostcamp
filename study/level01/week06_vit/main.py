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
from torch.utils.data import DataLoader

import os
import shutil
import time
import pickle

from model import ViT

def get_time() -> str:
    return time.strftime('%c', time.localtime(time.time()))

def clear_pycache(root: str = './') -> None:
    if os.path.exists(os.path.join(root, '__pycache__')):
        shutil.rmtree(os.path.join(root, '__pycache__'))

def clear_log_folders(root: str = './') -> None:
    if os.path.exists(os.path.join(root, 'checkpoints')):
        shutil.rmtree(os.path.join(root, 'checkpoints'))
    if os.path.exists(os.path.join(root, 'history')):
        shutil.rmtree(os.path.join(root, 'history'))
    if os.path.exists(os.path.join(root, 'results')):
        shutil.rmtree(os.path.join(root, 'results'))

# For updating learning rate
def update_learning_rate(optimizer, lr: float) -> None:
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr

def train_and_eval(done_epochs: int, train_epochs: int, clear_log: bool = False) -> None:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    if clear_log:
        clear_log_folders()

    ######## Preparing Dataset ########
    print(f"Dataset | Data preparation start @ {get_time()}", flush=True)

    timestamp = get_time().replace(':', '')
    location = {
        'base_path': './dataset',
        'checkpoints_path': os.path.join('./checkpoints', timestamp),
        'history_path': os.path.join('./history', timestamp),
        'results_path': os.path.join('./results', timestamp)
    }
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

    train_loader = DataLoader(
        dataset=dataset_train,
        batch_size=batch_size,
        shuffle=True
    )
    test_loader = DataLoader(
        dataset=dataset_test,
        batch_size=batch_size,
        shuffle=False,
        drop_last=False
    )

    train_batches = len(train_loader)
    test_batches = len(test_loader)

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
        checkpoint = torch.load(f"./checkpoints/epoch{done_epochs}.pt", map_location=device)
        model.load_state_dict(checkpoint['model'])
        optimizer.load_state_dict(checkpoint['optimizer'])
        with open(f"./history/epoch{done_epochs}.pickle", 'rb') as fr:
            history = pickle.load(fr)
    else:
        history = {'train_loss': [], 'train_acc': []}

    ######## Train ########
    print('Train | Training start @ {}'.format(get_time()), flush=True)

    for epoch in range(done_epochs, done_epochs + train_epochs):
        if (epoch + 1) % (printing_ratio * train_epochs) == 0:
            print('Train | Epoch {:02d} start @ {}'.format(epoch + 1, get_time()), flush=True)

        model.train()
        train_loss = 0
        total = 0
        correct = 0

        for batch_index, (images, labels) in enumerate(train_loader):
            print('Train | Epoch {:02d} | Batch {} / {} start'.format(epoch + 1, batch_index + 1, train_batches), flush=True)

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
            prediction = torch.argmax(outputs, dim=1)
            total += labels.size(0)
            correct += (prediction == labels).sum().item()

        train_acc = 100 * correct / total

        if (epoch + 1) > plot_bound:
            history['train_loss'].append(train_loss)
            history['train_acc'].append(train_acc)

        print('Train | Loss: {:.4f} | Accuracy: {:.4f}%'.format(train_loss, train_acc), flush=True)

        # Save checkpoint
        checkpoint = {'model': model.state_dict(), 'optimizer': optimizer.state_dict()}
        torch.save(checkpoint, os.path.join(location['checkpoints_path'], f"epoch{epoch + 1}.pt"))

        # Decay learning rate
        if (epoch + 1) % (lr_update_ratio * train_epochs) == 0:
            learning_rate /= 10
            update_learning_rate(optimizer, learning_rate)

        ######## Saving History ########
        with open(os.path.join(location['history_path'], f"epoch{epoch + 1}.pickle"), 'wb') as fw:
            pickle.dump(history, fw)

    print(f"Train | Finished training @ {get_time()}", flush=True)

    ######## Test ########
    print(f"Test | Evaluation start @ {get_time()}", flush=True)

    model.eval()
    with torch.no_grad():
        total = 0
        correct = 0

        for batch_index, (images, labels) in enumerate(test_loader):
            print('Test | Batch {} / {} start'.format(batch_index + 1, test_batches), flush=True)

            images = images.to(device)
            labels = labels.to(device)

            # Forward pass
            outputs = model(images)
            loss = criterion(outputs, labels)

            # Test accuracy
            prediction = torch.argmax(outputs, dim=1)
            total += labels.size(0)
            correct += (prediction == labels).sum().item()

        test_acc = 100 * correct / total

    print('Test | Accuracy: {:.4f}%'.format(test_acc))
    print(f"Test | Finished evaluation @ {get_time()}", flush=True)

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
    plt.savefig(os.path.join(location['results_path'], 'result.png'), dpi=1000)

    print(f"Code execution done @ {get_time()}", flush=True)

if __name__ == '__main__':
    # Last checkpoint's training position
    done_epochs = 0

    # How much epochs to train now
    train_epochs = 10

    train_and_eval(done_epochs, train_epochs, clear_log=False)
