import cv2, os, numpy

def dataset(foldername):
    images = []
    sum = [[0 for i in range(256)] for j in range(256)]
    for imgfile in os.listdir(foldername):
            img = cv2.imread(os.path.join(foldername, imgfile), cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img,(256,256))
            images.append(img)
            sum = numpy.add(sum, img)
    sum = numpy.divide(sum, len(images))
    print(sum)
    cv2.imwrite('sum.jpg', sum)
    
dataset("Algeo02-21072/dataset/pins_Ben Affleck")

'''
def dataset(foldername):
    images = []
    sum = [256][0]
    print('hello')
    for folder in os.listdir(foldername):
        for imgfile in os.listdir(foldername+folder):
            print(imgfile)
            img = cv2.imread(os.path.join(foldername+folder, imgfile), cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img,(256,256))
            images.append(img)
    for i in range(len(images)):
        sum += images[i]
    print("selesai")
    mean = sum / len(images)
    print(mean)
    for j in range(len(images)):
        avg = images[i] - mean
    cv2.imshow('avg', avg)
    cv2.waitKey(0)
    
dataset("Algeo02-21072/dataset/")
'''