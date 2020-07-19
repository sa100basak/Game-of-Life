import os
import cv2

def makeclip(fps,n_gen):
    seq = []
    for i in range(n_gen + 1):
        seq.append(cv2.imread(os.getcwd() + '/' + str(i) + '.png'))
    
    #... tuple ...#
    height,width,layers = seq[0].shape
    size = (width,height)
        
    clip = cv2.VideoWriter('movie.avi',cv2.VideoWriter_fourcc(*'DIVX'),fps,size)
    for i in range(len(seq)):
        clip.write(seq[i])
        print('---> RENDERING IN PROGRESS || Generation = ',i)

    clip.release()
    print('FIN')