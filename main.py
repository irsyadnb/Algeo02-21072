import cv2, os, numpy

#kalo nemu ds_store gjls
#find . -name ".DS_Store" -delete
#Algeo02-21072/setdata/

path = "Algeo02-21072/setdata/"
ctr = 0
for folder in os.listdir(path):
    for imgfile in os.listdir(path+folder):
        ctr+=1

def setdata(foldername):
    images = []
    for folder in os.listdir(foldername):
        for imgfile in os.listdir(foldername+folder):
            img = cv2.imread(os.path.join(foldername+folder, imgfile), cv2.IMREAD_GRAYSCALE)
            img = img/255
            img = cv2.resize(img,(256,256))
            images.append(img.reshape(-1,1)) 
            #vector face dibuat dari 256x256 jadi 65536 x M 
            #dimasukan ke face vector space (images)
    return images

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
    result = cv2.normalize(numpy.reshape(mean, (256,256)), dst=None, alpha=0, beta=255,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imwrite("kelaji.jpg", result)
    return a #ngehasilin matrix isi normalized vectors (A)

def bigA(vectorM):
    biga = vectorM[0]
    for i in range(1,len(vectorM)):
        biga = numpy.hstack((biga, vectorM[i]))
    return biga

def cofmatrix(normalvector): #versi kecil
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
    print ('A = ')
    print (A)
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

def eigen_qr_simple(A):
    #Ak = numpy.copy(A)
    QQ = numpy.eye(A.shape[0])
    for k in range(500):
        Q, R = gramschmidt(A)
        A = R @ Q
        QQ = QQ @ Q
        
    return numpy.diag(A), QQ

def eigenface(matrix):
    ui = []
    avg = bigA(average(matrix))
    eigval, eigvec = eigen_qr_simple(cofmatrix(bigA(average(matrix)))) 

    #eigenfaces
    for i in range(ctr):   
        ui.append(avg @ eigvec[:, i])

    #BUAT PRINT EIGENFACES
    '''
    for i in range(ctr):
        outfile = '%s.jpg' % ("eigen"+ str(i))
        result = cv2.normalize(numpy.reshape(ui[i][:], (256,256)), dst=None, alpha=0, beta=255,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        cv2.imwrite(outfile, result)
    '''
    sum = [[0 for i in range(1)] for j in range(256*256)]
    for i in range(ctr):
        sum = numpy.array(numpy.add(sum, matrix[i]))
    mean = numpy.array(numpy.divide(sum, ctr))    

    weight = ui @ avg
    
    return ui, mean, weight
#eigenface(setdata(path))

def eucdistance(m1,m2):
    selisih = m1 - m2
    eucDist = numpy.sqrt(numpy.dot(selisih.T,selisih))
    return eucDist
#ui, mean, weight = eigenface(setdata(path))