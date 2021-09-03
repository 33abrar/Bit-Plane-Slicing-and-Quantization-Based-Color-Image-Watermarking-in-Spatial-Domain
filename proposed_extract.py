import PIL.Image as pimg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np, copy, os
import arnold, yCbCr, single_channel, benchmark
from pytictoc import TicToc

#Gauss_0.001p0.5
#S&P_2%
#BLF_n=10&D0=100
#median_filter_3x3
#JPEG_50

#avionw
#baboonw
#lenaw
#peppersw
#sailboatw
def myFunc(e):
    return e[0]

def extract(Media_dir, img_path):
    t = TicToc() #create instance of class

    t.tic() #Start timer
    
    h=mpimg.imread(img_path);

    M=512;N=32;m=4;kT=1;

    h=yCbCr.rgb2ycbcr(h);
    Yh=h[:,:,0];Cbh=h[:,:,1];Crh=h[:,:,2];

    kb=33;kT=1;
    bit_seq=single_channel.single_channel_extract(np.double(Yh.copy()),N,m,kb,kT);

    xRw=bit_seq[0:N*N*4];xGw=bit_seq[N*N*4:2*N*N*4];xBw=bit_seq[2*N*N*4:3*N*N*4];
    z_pad=np.zeros((N*N,4),np.uint8);
    xRw=xRw.reshape((N*N,4));xRw=np.concatenate((xRw,z_pad),axis=1);xRw=np.packbits(xRw,axis=1);xRw=xRw.reshape((N,N))+8;
    xGw=xGw.reshape((N*N,4));xGw=np.concatenate((xGw,z_pad),axis=1);xGw=np.packbits(xGw,axis=1);xGw=xGw.reshape((N,N))+8;
    xBw=xBw.reshape((N*N,4));xBw=np.concatenate((xBw,z_pad),axis=1);xBw=np.packbits(xBw,axis=1);xBw=xBw.reshape((N,N))+8;

    iterR=13;iterG=23;iterB=33;
    xRw=arnold.iarnold(xRw,iterR);xGw=arnold.iarnold(xGw,iterG);xBw=arnold.iarnold(xBw,iterB);

    xw=np.dstack((xRw,xGw,xBw));
    xw[xw>255]=255;xw[xw<0]=0;
    t.toc() #Time elapsed since t.tic()
    
    files = os.listdir(Media_dir)

    lst=[]
    for index, file in enumerate(files):
        w=pimg.open(os.path.join(Media_dir, file));
        w=w.resize((N,N),0);w=copy.deepcopy(np.asarray(w));w=w[:,:,0:3];#plt.imshow(w/255);plt.show();
        
        ben = benchmark.NC(w/255,xw/255);        
        
        lst.append([ben, file])

        plt.figure(figsize=(3,3));
        plt.subplot(1,2,1);plt.imshow(w),plt.title("Logo");
        plt.subplot(1,2,2);plt.imshow(xw/255),plt.title("Extracted");
        plt.show()        

    lst.sort(key=myFunc)
    lst.reverse()
    print(lst)
    if (lst[0][0]>=.9):
       return lst
    return None

    #plt.imshow(xw/255);plt.show();
    #plt.imsave('D:/Computer/MIST/Level-04/Thesis/Code/paper/Attack/mf_lena.bmp',(xw/255));

