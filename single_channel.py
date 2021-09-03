import numpy as np, random, math
def single_channel_embed(h, wm, m, kb, kT):    
    (M, M)=h.shape;(N,)=wm.shape;
    np.random.seed(kb);bk=np.random.permutation(int((M*M)/(m*m)));
    random.seed(kT);T=55+80*np.random.rand(N);
    for w in range (0,N):
        # find DCC 
        i=math.floor(bk[w]/(M/m))*4;        
        j=int((bk[w]%(M/m))*4);
        temp = h[i:i+m,j:j+m];
        DCC=np.sum(temp);OC=DCC;    
        # Cl & ch boundary
        #print(bk[w],wm[w],i,j);
        if (wm[w]==1):
            Cl=math.floor(DCC/T[w])*T[w] +0.25*T[w];     
            Ch=(math.floor(DCC/T[w])+1)*T[w]+0.25*T[w];        
        elif (wm[w]==0):
            Cl=(math.floor(DCC/T[w])-1)*T[w] +0.75*T[w];
            Ch=math.floor(DCC/T[w])*T[w]+0.75*T[w];    
        # find OC         
        if (abs(Cl-DCC)<=abs(Ch-DCC)):
            OC=Cl;
        else:
            OC=Ch;            
        #print(h[i:i+m,j:j+m].shape);
        h[i:i+m,j:j+m]=h[i:i+m,j:j+m]+((OC-DCC)/(m*m));
        #print(h[i:i+m,j:j+m]);
    return h;


def single_channel_extract(h, N, m, kb, kT):    
    (M, M)=h.shape;xwm=np.zeros((N*N*3*4),np.uint8);
    np.random.seed(kb);bk=np.random.permutation(int((M*M)/(m*m)));
    random.seed(kT);T=55+80*np.random.rand((N*N*3*4));
    
    for w in range (0,N*N*3*4):
        # find DCC 
        i=math.floor(bk[w]/(M/m))*4;        
        j=int((bk[w]%(M/m))*4);
        temp = h[i:i+m,j:j+m];
        DCC=np.sum(temp);          
        if ((round(DCC)%T[w])<0.5*T[w]):
            xwm[w]=1;
        else :
            xwm[w]=0;
        #print(h[i:i+m,j:j+m].shape);
        #h[i:i+m,j:j+m]=h[i:i+m,j:j+m]+((OC-DCC)/(m*m));
        #print(h[i:i+m,j:j+m]);
    return xwm;             
