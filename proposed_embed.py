import PIL.Image as pimg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np, copy
import arnold, yCbCr, single_channel, benchmark  #from .model.proposed_embed
import skimage.metrics as ssim
from pytictoc import TicToc

#D:/Computer/MIST/Level-04/Thesis/Code/DATASET/CVG-UGR/c512_001/avion.ppm
#D:/Computer/MIST/Level-04/Thesis/Code/DATASET/CVG-UGR/c512_001/baboon.ppm
#D:/Computer/MIST/Level-04/Thesis/Code/DATASET/CVG-UGR/c512_003/lena.ppm
#D:/Computer/MIST/Level-04/Thesis/Code/DATASET/CVG-UGR/c512_004/peppers.ppm
#D:/Computer/MIST/Level-04/Thesis/Code/DATASET/CVG-UGR/c512_005/sailboat.ppm

def embed(path1, path2):

    t = TicToc() #create instance of class

    t.tic() #Start timer
    h=pimg.open(path1);
    w=pimg.open(path2);

    M=512;N=32;m=4;kT=1;
    h=h.resize((M,M),0);w=w.resize((N,N),0);

    #converting PIL.Image to ndarray. So that we can divided this into channel
    #matplotlib.pyplot using ndarray to hold image

    h=copy.deepcopy(np.asarray(h,np.float));w=copy.deepcopy(np.asarray(w));
    h=yCbCr.rgb2ycbcr(h);
    Yh=h[:,:,0];Cbh=h[:,:,1];Crh=h[:,:,2];Rw=w[:,:,0];Gw=w[:,:,1];Bw=w[:,:,2];

    iterR=13;iterG=23;iterB=33;
    Rw=arnold.arnold(Rw,iterR);Gw=arnold.arnold(Gw,iterG);Bw=arnold.arnold(Bw,iterB);

    Rw=Rw.reshape((N*N,1));Rw=np.unpackbits(Rw,axis=1);Rw=Rw[:,0:4];Rw=Rw.reshape((N*N*4));
    Gw=Gw.reshape((N*N,1));Gw=np.unpackbits(Gw,axis=1);Gw=Gw[:,0:4];Gw=Gw.reshape((N*N*4));
    Bw=Bw.reshape((N*N,1));Bw=np.unpackbits(Bw,axis=1);Bw=Bw[:,0:4];Bw=Bw.reshape((N*N*4));
    bit_seq=np.concatenate([Rw,Gw,Bw]);

    kb=33;kT=1;
    eYh=single_channel.single_channel_embed(np.double(Yh.copy()),bit_seq,m,kb,kT);
    #print(Yh.dtype);print(eYh.dtype);
    eh=(np.dstack((eYh,Cbh,Crh)));eh=yCbCr.ycbcr2rgb(eh);eh[eh>255]=255;eh[eh<0]=0;

    t.toc() #Time elapsed since t.tic()

    h=yCbCr.ycbcr2rgb(h);

    print('PSNR =',benchmark.PSNR(h/255,eh/255));
    print('SSIM =',ssim.structural_similarity(h/255,eh/255,multichannel=True));

    plt.figure(1);
    plt.subplot(1,2,1);plt.imshow(h/255);plt.title("Host");
    plt.subplot(1,2,2);plt.imshow(eh/255);plt.title("Watermarked");
    plt.show();
    #plt.imsave('D:/Computer/MIST/Level-04/Thesis/Code/methods/Python/proposed_method/iMAGE/Watermarked/baboon.ppm',(eh/255));
    return eh;
    #plt.imsave('D:/Computer/MIST/Level-04/Thesis/Code/methods/python/proposed_method/watermarked_image/sailboatw.jpg',(eh/255));

    #plt.imshow(Gw);plt.show()
    #plt.imshow(Bw);plt.show()


    #plt.imshow(Rh);plt.show()
    #plt.imshow(Gh);plt.show()
    #plt.imshow(Bh);plt.show()

    #print(type(h))
    #print((h.dtype))
    #print(h.shape)
    #print(h.size)
    #plt.imshow(h)
    #plt.show()


