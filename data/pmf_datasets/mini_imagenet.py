import numpy as np
import torchvision.transforms as transforms

def dataset_setting(nSupport, img_size=80):
    """
    Return dataset setting

    :param int nSupport: number of support examples
    """
    mean = [x/255.0 for x in [120.39586422,  115.59361427, 104.54012653]]
    std = [x/255.0 for x in [70.68188272,  68.27635443,  72.54505529]]
    normalize = transforms.Normalize(mean=mean, std=std)
    trainTransform = transforms.Compose([#transforms.RandomCrop(img_size, padding=8),
                                         transforms.RandomResizedCrop((img_size, img_size), scale=(0.05, 1.0)),
                                         transforms.ColorJitter(brightness=0.4, contrast=0.4, saturation=0.4),
                                         transforms.RandomHorizontalFlip(),
                                         #lambda x: np.asarray(x),
                                         transforms.ToTensor(),
                                         normalize
                                        ])

    valTransform = transforms.Compose([#transforms.CenterCrop(80),
                                       transforms.Resize((img_size, img_size)),
                                       #lambda x: np.asarray(x),
                                       transforms.ToTensor(),
                                       normalize])

    inputW, inputH, nbCls = img_size, img_size, 64

    trainDir = '/Users/DAHS/Desktop/대학원 course/고급메타러닝/StyleAdv-CDFSL/data/filelists/Mini-ImageNet/train/'
    #trainDir = '/share/test/lovelyqian/CROSS-DOMAIN-FSL-DATASETS/miniImagenet/source/mini_imagenet_full_size/train/'
    valDir = '/Users/DAHS/Desktop/대학원 course/고급메타러닝/StyleAdv-CDFSL/data/filelists/Mini-ImageNet/val/'
    #valDir = '/share/test/lovelyqian/CROSS-DOMAIN-FSL-DATASETS/miniImagenet/source/mini_imagenet_full_size/val/'
    testDir = '/Users/DAHS/Desktop/대학원 course/고급메타러닝/StyleAdv-CDFSL/data/filelists/Mini-ImageNet/test/'
    #testDir = '/share/test/lovelyqian/CROSS-DOMAIN-FSL-DATASETS/miniImagenet/source/mini_imagenet_full_size/test/'
    episodeJson = '/Users/DAHS/Desktop/대학원 course/고급메타러닝/StyleAdv-CDFSL/data/filelists/Mini-ImageNet/val1000Episode_5_way_1_shot.json' if nSupport == 1 \
            else '/Users/DAHS/Desktop/대학원 course/고급메타러닝/StyleAdv-CDFSL/data/filelists/Mini-ImageNet/val1000Episode_5_way_5_shot.json'

    return trainTransform, valTransform, inputW, inputH, trainDir, valDir, testDir, episodeJson, nbCls
