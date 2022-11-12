import cv2, os, numpy

#kalo nemu ds_store gjls
#find . -name ".DS_Store" -delete

ctr = 0
for folder in os.listdir("Algeo02-21072/testdata/"):
    for imgfile in os.listdir("Algeo02-21072/testdata/"+folder):
        ctr+=1

def setdata(foldername):
    images = []
    for folder in os.listdir(foldername):
        for imgfile in os.listdir(foldername+folder):
            img = cv2.imread(os.path.join(foldername+folder, imgfile), cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img,(256,256))
            images.append(img.reshape(-1,1)) 
            #vector face dibuat dari 256x256 jadi 65536 x M 
            #dimasukan ke face vector space (images)
    return images
#setdata("Algeo02-21072/testdata/")  

def average(arr):
    sum = [[0 for i in range(1)] for j in range(256*256)]
    a = []
    for i in range(ctr):
        sum = numpy.array(numpy.add(sum, arr[i]))
    mean = numpy.array(numpy.divide(sum, ctr))

    for j in range(ctr): #matrix a diisi normalized vector (tiap vector face - mean)
        a.append(numpy.array(numpy.subtract(arr[j], mean)))
    #hasil matrix a -> N^2 x M

    #buat hasilin average face
    box = int(numpy.sqrt(mean.shape[0]))
    cv2.imwrite("kelaji.jpg", numpy.reshape(mean,(box,box)))

    biga = a[0]
    for i in range(1,len(a)):
        biga = numpy.hstack((biga, a[i]))

    return biga #ngehasilin matrix isi normalized vectors (A)

#average(setdata("Algeo02-21072/testdata/"))

def cofmatrix(normalvector):
    normal = normalvector
    transpose = numpy.transpose(normal)
    cof = numpy.matmul(transpose, normal)
    return cof #eigen vectors

def cofmatrixbig(normalvector):
    normal = normalvector
    transpose = numpy.transpose(normal)
    cof = numpy.matmul(normal, transpose)
    return cof #eigen vectors versi gede

#cofmatrix(average(setdata("Algeo02-21072/testdata/")))