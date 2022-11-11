import cv2, os, numpy
#kalo nemu ds_store gjls
#find . -name ".DS_Store" -delete
ctr = 0
for folder in os.listdir("Algeo02-21072/setdata/"):
    for imgfile in os.listdir("Algeo02-21072/setdata/"+folder):
        ctr+=1

def setdata(foldername):
    images = []
    print(numpy.shape(images))

    for folder in os.listdir(foldername):
        for imgfile in os.listdir(foldername+folder):
            img = cv2.imread(os.path.join(foldername+folder, imgfile), cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img,(256,256))
            images.append(img.reshape(-1,1))

    return images

#setdata("Algeo02-21072/dataset/")  

def average(arr):
    sum = [[0 for i in range(1)] for j in range(256*256)]
    for i in range(ctr):
        sum = numpy.array(numpy.add(sum, arr[i]))
    mean = numpy.array(numpy.divide(sum, ctr))
    box = int(numpy.sqrt(mean.shape[0]))
    cv2.imwrite("WOIPRINTWOI.jpg", numpy.reshape(mean,(box,box)))
    return mean

#average(setdata("Algeo02-21072/dataset/"))

def cofmatrix(apakek):
    normal = apakek
    transpose = numpy.transpose(apakek)
    cof = numpy.multiply(normal, transpose)
    print(numpy.shape(numpy.array(cof)))
    return cof

cofmatrix(average(setdata("Algeo02-21072/setdata/")))


#nyimpen
'''
def dataset(foldername):
    images = []
    
    sum = [[0 for i in range(256)] for j in range(256)]
    for folder in os.listdir(foldername):
        for imgfile in os.listdir(foldername+folder):
            img = cv2.imread(os.path.join(foldername+folder, imgfile), cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img,(256,256))
            images.append(img)
            sum = numpy.add(sum, img)
    mean = numpy.array(numpy.divide(sum, len(images)))
    image = numpy.array(images)
    cv2.imwrite('avg.jpg', mean)

    a = []

    for i in range(len(images)):
        a.append(numpy.array(numpy.subtract(image[i], mean)))
    
    return(numpy.array(a))
    
#dataset("Algeo02-21072/setdata/")

def cofmatrix(a):
    normal = a
    transpose = numpy.transpose(a)
    print("normal :")
    print(numpy.array(normal).shape)
    print("transpose:")
    print(numpy.array(transpose).shape)

#cofmatrix(dataset("Algeo02-21072/dataset/"))
'''