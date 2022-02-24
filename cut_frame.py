import glob
import os
import cv2
import pandas as pd




video='58106_002918_Sideline.mp4'

labels_path='/home/shigb/nfl/nfl-health-and-safety-helmet-assignment/train_labels.csv'
video_path=f'nfl-health-and-safety-helmet-assignment/train/{video}'


save_dir='cut_image'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

labels=pd.read_csv(labels_path)

cap=cv2.VideoCapture(video_path)
success,image=cap.read()
frame=1
datas=[]
while success:
    video_frame=f"{video.split('.')[0]}_{frame}"

    cv2.imwrite(f'{save_dir}/{video_frame}.jpg',image)

    data=labels[labels.video_frame==video_frame].reset_index(drop=True)
    data['video_frame']=video_frame
    data['label']='Helmet'
    data=data[['video_frame','label','left','width','top','height']]
    datas.append(data)

    success,image=cap.read()
    frame+=1

datas=pd.concat(datas)
datas.to_csv(f'./labels.csv',index=False)




