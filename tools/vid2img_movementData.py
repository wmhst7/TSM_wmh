import os

TRAIN_ROOT = '/data1/movementData/train/'         
VAL_ROOT = '/data1/movementData/val/'
FRAME_ROOT = '/data1/movementData/frames'  


def extract(video_root, prefix, video, typee):
    vname = os.path.join(video_root, prefix)
    vname = os.path.join(vname, video)
    fdir = prefix + "-" + video.split(".")[0]
    cmd = 'ffmpeg -loglevel quiet -i \"{}\" -threads 1 -vf scale=-1:480 -q:v 0 \"{}/{}/{}/%06d.jpg\"'.format(vname, FRAME_ROOT, typee, fdir)
    
    if os.path.exists("{}/{}/{}".format(FRAME_ROOT, typee, fdir)):
        return
    os.makedirs("{}/{}/{}".format(FRAME_ROOT, typee, fdir))
    print(prefix)
    os.system(cmd)


def main(video_root, typee):
    for item in os.listdir(video_root):
        path = os.path.join(video_root, item)
        if not os.path.isdir(path):
            continue
        for video in os.listdir(path):
            extract(video_root, item, video, typee)


if __name__ == "__main__":
    main(TRAIN_ROOT, "train")
    main(VAL_ROOT, "val")