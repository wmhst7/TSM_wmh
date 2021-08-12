import os, json

TRAIN_ROOT = '/data1/movementData/train/'         
VAL_ROOT = '/data1/movementData/val/'
LABEL_PATH = '/data1/movementData/v1_full_trailer.json'
TRAIN_OUT = '/data1/movementData/labels/train_videofolder.txt'
VAL_OUT = '/data1/movementData/labels/val_videofolder.txt'


def get_label(dd, item, video):
    # print(item, video)
    video = video.split(".")[0][-4:]
    label = dd.get(item).get(video).get("movement").get("value")
    return label


def get_label_train(video_root):
    label_dict = None
    output = []
    with open(LABEL_PATH, "r") as f:
        label_dict = json.loads(f.read())
    for item in os.listdir(video_root):
        path = os.path.join(video_root, item)
        if not os.path.isdir(path):
            continue
        for video in os.listdir(path):
            fdir = item + "-" + video.split(".")[0]
            curFolder = "train/" + fdir
            curIDX = get_label(label_dict, item, video)
            dir_files = os.listdir(os.path.join('/data1/movementData/frames/', curFolder))
            ss = '%s %d %d' % (curFolder, len(dir_files), curIDX)
            output.append(ss)
            # print(ss)
            # exit()
    with open(TRAIN_OUT, 'w') as f:
        f.write('\n'.join(output))


def get_label_val(video_root):
    label_dict = None
    output = []
    with open(LABEL_PATH, "r") as f:
        label_dict = json.loads(f.read())
    for item in os.listdir(video_root):
        path = os.path.join(video_root, item)
        if not os.path.isdir(path):
            continue
        for video in os.listdir(path):
            fdir = item + "-" + video.split(".")[0]
            # watch out prefix 
            curFolder = "val/" + fdir
            curIDX = get_label(label_dict, item, video)
            dir_files = os.listdir(os.path.join('/data1/movementData/frames/', curFolder))
            output.append('%s %d %d' % (curFolder, len(dir_files), curIDX))
    with open(VAL_OUT, 'w') as f:
        f.write('\n'.join(output))


if __name__ == "__main__":
    get_label_train(TRAIN_ROOT)
    get_label_val(VAL_ROOT)