import matplotlib.pyplot as plt, copy
def arnold( inn, iterr ):    
    if (inn.ndim != 2):
        error('Oly two dimensions allowed');
        
    (m, n) = inn.shape;
    if (m != n):
        error('Arnold Transform is defined only for squares. Please complete empty rows or columns to make the square.');
    
    out=copy.deepcopy(inn);
    #print(type(out))
    for c in range (1,iterr):
        for i in range (0,n):
            for j in range (0,n):
                i_1=((i*1+j*1)%m);
                j_1=((i*1+j*2)%m);                   
                out[i_1, j_1] = inn[i, j];                  
    return out;


def iarnold( inn, iterr ):   
    if (inn.ndim != 2):
        error('Oly two dimensions allowed');
        
    (m, n) = inn.shape;
    if (m != n):
        error('Arnold Transform is defined only for squares. Please complete empty rows or columns to make the square.');
    
    out=copy.deepcopy(inn);
    #print(type(out))
    for c in range (1,iterr):
        for i in range (0,n):
            for j in range (0,n):
                i_1=((i*2+j*(-1))%m);
                j_1=((i*(-1)+j*1)%m);                   
                out[i_1, j_1] = inn[i, j];                  
    return out;
