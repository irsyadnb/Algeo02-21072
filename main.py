import cv2, os, numpy

#kalo nemu ds_store gjls
#find . -name ".DS_Store" -delete

ctr = 0
for folder in os.listdir("Algeo02-21072/setdata/"):
    for imgfile in os.listdir("Algeo02-21072/setdata/"+folder):
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
    return a #ngehasilin matrix isi normalized vectors (A)

#average(setdata("Algeo02-21072/testdata/"))

def bigA(vectorM):
    biga = vectorM[0]
    for i in range(1,len(vectorM)):
        biga = numpy.hstack((biga, vectorM[i]))
    return biga

#bigA(average(setdata("Algeo02-21072/testdata/")))

def cofmatrix(normalvector):
    normal = normalvector
    transpose = numpy.transpose(normal)
    cof = numpy.matmul(transpose, normal)
    return cof

def cofmatrixbig(normalvector):
    normal = normalvector
    transpose = numpy.transpose(normal)
    cof = numpy.matmul(normal, transpose)
    return cof #eigen vectors versi gede

#cofmatrix(bigA(setdata("Algeo02-21072/testdata/")))

#cofmatrix(average(setdata("Algeo02-21072/testdata/")))

def eigenK(cofm, bigA):
    ui = []

    for i in range(len(cofm)):
        ui.append(numpy.matmul(bigA, cofm[:,i]))

    for j in range(len(cofm)):
        filename = "eigen%d.jpg"%j
        cv2.imwrite(filename, numpy.reshape(numpy.matmul(bigA, cofm[:,j]),(256,256)))
#eigenK(cofmatrix(bigA(setdata("Algeo02-21072/setdata/"))), bigA(average(setdata("Algeo02-21072/setdata/"))))