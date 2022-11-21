import cv2, os, numpy
# import matplotlib.pyplot as plt
import os


#kalo nemu ds_store gjls
#find . -name ".DS_Store" -delete
#Algeo02-21072/setdata/

# path = ".\\sample\\"
# ctr = 0
# for folder in os.listdir(path):
#     for imgfile in os.listdir(path+folder):
#         ctr+=1

def setdata(foldername):
    images = []
    for folder in os.listdir(foldername):
        for imgfile in os.listdir(foldername +"/" + folder):
            img = cv2.imread(os.path.join(foldername + "/"+ folder, imgfile), cv2.IMREAD_GRAYSCALE)
            img = img/255
            img = cv2.resize(img,(256,256))
            images.append(img.reshape(-1,1)) 
            #vector face dibuat dari 256x256 jadi 65536 x M 
            #dimasukan ke face vector space (images)
    return images    

def average(arr,ctr): #V
    sum = [[0 for i in range(1)] for j in range(256*256)]
    a = []
    for i in range(ctr):
        sum = numpy.array(numpy.add(sum, arr[i]))
    mean = numpy.array(numpy.divide(sum, ctr))
    '''
    result = cv2.normalize(numpy.reshape(mean, (256,256)), dst=None, alpha=0, beta=255,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imwrite("kelaji.jpg", result)
    '''

    for j in range(ctr): #matrix a diisi normalized vector (tiap vector face - mean)
        a.append(numpy.array(numpy.subtract(arr[j], mean)))
    #hasil matrix a -> N^2 x M

    #buat hasilin average face
    
    return a #ngehasilin matrix isi normalized vectors (A)

def bigA(vectorM): #V
    biga = vectorM[0]
    for i in range(1,len(vectorM)):
        biga = numpy.hstack((biga, vectorM[i]))
    return biga

def cofmatrix(normalvector): #V
    normal = normalvector
    transpose = numpy.transpose(normal)
    #cof = numpy.matmul(transpose, normal)
    cof = transpose @ normal
    return cof

def gramschmidt(A):
    R = numpy.zeros((A.shape[1], A.shape[1]))
    Q = numpy.zeros(A.shape)
    for k in range(0, A.shape[1]):
        R[k, k] = numpy.sqrt(numpy.dot(A[:, k], A[:, k]))
        Q[:, k] = A[:, k]/R[k, k]
        for j in range(k+1, A.shape[1]):
            R[k, j] = numpy.dot(Q[:, k], A[:, j])
            A[:, j] = A[:, j] - R[k, j]*Q[:, k]
    return Q, R

def qrdecomp(A):
    Q, R = gramschmidt(A)
    ''' buat cek matrix di file
    matq = numpy.matrix(Q)
    with open('Q.txt','wb') as f:
        for line in matq:
            numpy.savetxt(f, line, fmt='%.2f')
    matr = numpy.matrix(R)
    with open('R.txt','wb') as f:
        for line in matr:
            numpy.savetxt(f, line, fmt='%.2f')

        buat cek hasil qr decomposition 
    print ('Q = ')
    rint (Q)
    print ('R = ')
    print (R)
    print ('Q^T*Q = ')
    print (numpy.dot(Q.transpose(), Q))
    print ('Q*R =')
    print (numpy.dot(Q, R))
    '''
    return Q,R

def eigen_qr_practical(A):
    Ak = numpy.copy(A)
    n = Ak.shape[0]
    QQ = numpy.eye(n)
    for k in range(500):

        s = Ak.item(n-1, n-1)
        smult = s * numpy.eye(n)

        Q, R = numpy.linalg.qr(numpy.subtract(Ak, smult))

        Ak = numpy.add(R @ Q, smult)
        QQ = QQ @ Q
    return numpy.diag(Ak), QQ

def eigen_qr_simple(A):
    #Ak = numpy.copy(A)
    QQ = numpy.eye(A.shape[0])
    for k in range(500):
        Q, R = numpy.linalg.qr(A)
        A = R @ Q
        QQ = QQ @ Q
        
    return numpy.diag(A), QQ

def eigenface(matrix,ctr):
    w=[0 for i in range(ctr)]
    ui = []
    avg = bigA(average(matrix,ctr)) #V
    eigval, eigvec = eigen_qr_practical(cofmatrix(bigA(average(matrix,ctr)))) #V

    #eigenfaces
    for i in range(ctr):   
        ui.append((avg @ eigvec[:, i])/numpy.linalg.norm(avg @ eigvec[:,i]))

    #BUAT PRINT EIGENFACES
    '''
    for i in range(ctr):
        outfile = '%s.jpg' % ("eigens"+ str(i))
        result = cv2.normalize(numpy.reshape(ui[i][:], (256,256)), dst=None, alpha=0, beta=255,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        cv2.imwrite(outfile, result)
    '''
    sum = [[0 for i in range(1)] for j in range(256*256)]
    for i in range(ctr):
        sum = numpy.array(numpy.add(sum, matrix[i]))
    mean = numpy.array(numpy.divide(sum, ctr))   
    
    w = ui @ avg

    return ui, mean, numpy.array(w), avg

def eucdistance(m1,m2):
    selisih = m1 - m2
    eucDist = numpy.linalg.norm(selisih)
    return eucDist

def mainprog(imginput,path):
    ctr = 0
    for folder in os.listdir(path):
        for imgfile in os.listdir(path+"/"+folder):
            ctr+=1
    
    ui, mean, w, avg = eigenface(setdata(path),ctr)

    #NYOCOKIN
    images = []
    print(imginput)
    img = cv2.imread(rf'{imginput}', cv2.IMREAD_GRAYSCALE)
    print(imginput)
    img = img / 255
    img = cv2.resize(img, (256, 256))
    images.append(img.reshape(-1,1)) 
    testimage = bigA(images)
    result = cv2.normalize(numpy.reshape(testimage, (256,256)), dst=None, alpha=0, beta=255,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # cv2.imwrite("yangdiTest.jpg", result)

    normalize = testimage - mean

    testWeigth = ui @ normalize

    euc = []

    for i in range(ctr):
        euc.append(eucdistance(testWeigth[:,0], w[:,i]))


    for i in range(ctr):
        if euc[i] == numpy.amin(euc):
            break

    # print("YANG DICARI GAMBAR KE ",i)
    x = setdata(path)

    result = cv2.normalize(numpy.reshape(bigA(x)[:,i], (256,256)), dst=None, alpha=0, beta=255,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imwrite("identified.jpg", result)
    imgresult=os.path.abspath("identified.jpg")
    return imgresult
# print(numpy.amin(euc))
# imginput=r"C:\Users\ASUS\Documents\TBAlgeo2\Algeo02-21072\ironman.jpg"
# x=mainprog(imginput)
# print(x)