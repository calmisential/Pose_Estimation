import os
import collections


class OpenPoseCfg:
    # 模型保存
    load_weights_before_training = False
    load_weights_from_epoch = 0
    save_frequency = 5
    save_model_dir = "save/"


    # 测试图片路径
    test_image_dir = "test_pictures/"
    test_images_during_training = False

    # 输入图片大小 : (H, W, C)
    input_size = (368, 368, 3)

    # 训练超参数
    batch_size = 2
    epochs = 100

    # COCO数据集
    coco_root = "./datasets/COCO/2017/"
    coco_images = coco_root + "train2017/"
    coco_labels = coco_root + "annotations/"
    train_anns = coco_labels + "person_keypoints_train2017.json"
    tfrecords_root = "./openpose/data/tfrecords/"
    train_tfrecords = tfrecords_root + "train"
    images_per_tfrecord = 1000

    # keypoints
    dataset_num_keypoints = 17
    KEYPOINTS_DEF = {
        'nose': {"idx": 0, "name": 'nose', "side": "C", "ds_idxs": 0, "mirror_name": None},
        'sternum': {"idx": 1, "name": 'sternum', "side": "C", "ds_idxs": (5, 6), "mirror_name": None},
        'Rshoulder': {"idx": 2, "name": 'Rshoulder', "side": "R", "ds_idxs": 6, "mirror_name": 'Lshoulder'},
        'Relbow': {"idx": 3, "name": 'Relbow', "side": "R", "ds_idxs": 8, "mirror_name": 'Lelbow'},
        'Rwrist': {"idx": 4, "name": 'Rwrist', "side": "R", "ds_idxs": 10, "mirror_name": 'Lwrist'},
        'Rhip': {"idx": 5, "name": 'Rhip', "side": "R", "ds_idxs": 12, "mirror_name": 'Lhip'},
        'Rknee': {"idx": 6, "name": 'Rknee', "side": "R", "ds_idxs": 14, "mirror_name": 'Lknee'},
        'Rankle': {"idx": 7, "name": 'Rankle', "side": "R", "ds_idxs": 16, "mirror_name": 'Lankle'},
        'Reye': {"idx": 8, "name": 'Reye', "side": "R", "ds_idxs": 2, "mirror_name": 'Leye'},
        'Rear': {"idx": 9, "name": 'Rear', "side": "R", "ds_idxs": 4, "mirror_name": 'Lear'},
        'Lshoulder': {"idx": 10, "name": 'Lshoulder', "side": "L", "ds_idxs": 5, "mirror_name": 'Rshoulder'},
        'Lelbow': {"idx": 11, "name": 'Lelbow', "side": "L", "ds_idxs": 7, "mirror_name": 'Relbow'},
        'Lwrist': {"idx": 12, "name": 'Lwrist', "side": "L", "ds_idxs": 9, "mirror_name": 'Rwrist'},
        'Lhip': {"idx": 13, "name": 'Lhip', "side": "L", "ds_idxs": 11, "mirror_name": 'Rhip'},
        'Lknee': {"idx": 14, "name": 'Lknee', "side": "L", "ds_idxs": 13, "mirror_name": 'Rknee'},
        'Lankle': {"idx": 15, "name": 'Lankle', "side": "L", "ds_idxs": 15, "mirror_name": 'Rankle'},
        'Leye': {"idx": 16, "name": 'Leye', "side": "L", "ds_idxs": 1, "mirror_name": 'Reye'},
        'Lear': {"idx": 17, "name": 'Lear', "side": "L", "ds_idxs": 3, "mirror_name": 'Rear'}
    }

    KEYPOINTS_DEF = collections.OrderedDict(sorted(KEYPOINTS_DEF.items(), key=lambda t: t[1]["idx"]))
    KEYPOINTS_SIDES = {"C": (0, 1), "R": (2, 9), "L": (10, 17)}

    JOINTS_DEF = {
        "neck": {"idx": 0, "kpts": ('nose', 'sternum'), "side": "C", "name": "neck", "other_side_idx": None},
        "Rshoulder": {"idx": 1, "kpts": ('sternum', 'Rshoulder'), "side": "R", "name": "Rshoulder",
                      "other_side_idx": "Lshoulder"},
        "RupperArm": {"idx": 2, "kpts": ('Rshoulder', 'Relbow'), "side": "R", "name": "RupperArm",
                      "other_side_idx": "LupperArm"},
        "Rlowerarm": {"idx": 3, "kpts": ('Relbow', 'Rwrist'), "side": "R", "name": "Rlowerarm",
                      "other_side_idx": "Llowerarm"},
        "Rbodyside": {"idx": 4, "kpts": ('sternum', 'Rhip'), "side": "R", "name": "Rbodyside",
                      "other_side_idx": "Lbodyside"},
        "Rupperleg": {"idx": 5, "kpts": ('Rhip', 'Rknee'), "side": "R", "name": "Rupperleg",
                      "other_side_idx": "Lupperleg"},
        "Rlowerleg": {"idx": 6, "kpts": ('Rknee', 'Rankle'), "side": "R", "name": "Rlowerleg",
                      "other_side_idx": "Llowerleg"},
        "Rchick": {"idx": 7, "kpts": ('nose', 'Reye'), "side": "R", "name": "Rchick", "other_side_idx": "Lchick"},
        "Rtemple": {"idx": 8, "kpts": ('Reye', 'Rear'), "side": "R", "name": "Rtemple", "other_side_idx": "Ltemple"},
        "Lshoulder": {"idx": 9, "kpts": ('sternum', 'Lshoulder'), "side": "L", "name": "Lshoulder",
                      "other_side_idx": "Rshoulder"},
        "LupperArm": {"idx": 10, "kpts": ('Lshoulder', 'Lelbow'), "side": "L", "name": "LupperArm",
                      "other_side_idx": "RupperArm"},
        "Llowerarm": {"idx": 11, "kpts": ('Lelbow', 'Lwrist'), "side": "L", "name": "Llowerarm",
                      "other_side_idx": "Rlowerarm"},
        "Lbodyside": {"idx": 12, "kpts": ('sternum', 'Lhip'), "side": "L", "name": "Lbodyside",
                      "other_side_idx": "Rbodyside"},
        "Lupperleg": {"idx": 13, "kpts": ('Lhip', 'Lknee'), "side": "L", "name": "Lupperleg",
                      "other_side_idx": "Rupperleg"},
        "Llowerleg": {"idx": 14, "kpts": ('Lknee', 'Lankle'), "side": "L", "name": "Llowerleg",
                      "other_side_idx": "Rlowerleg"},
        "Lchick": {"idx": 15, "kpts": ('nose', 'Leye'), "side": "L", "name": "Lchick", "other_side_idx": "Rchick"},
        "Ltemple": {"idx": 16, "kpts": ('Leye', 'Lear'), "side": "L", "name": "Ltemple", "other_side_idx": "Rtemple"}
    }
    JOINTS_DEF = collections.OrderedDict(sorted(JOINTS_DEF.items(), key=lambda t: t[1]["idx"]))
    JOINTS_SIDES = {"C": (0, 0), "R": (1, 8), "L": (9, 16)}


    # 网络结构参数
    batch_norm_on = False
    dropout_rate = 0
    paf_num_filters = len(JOINTS_DEF) * 2
    heatmap_num_filters = len(KEYPOINTS_DEF)
    model_output_size = (46, 46)

    # this is the gaussian spot sie that will be drawn on the training labels
    KPT_HEATMAP_GAUSSIAN_SIGMA_SQ = 0.008  # used for the size of the gaussian spot for each keypoint
    # for lower resolution, a value too low (~0.005) here will make the vectors too sparse
    PAF_GAUSSIAN_SIGMA_SQ = 0.0015  # similar to joint width, but works on gaussian width, tradeoff between model certainty and number of persons that can be discriminated in a frame

    # 数据增强
    image_aug_on = True
    contrast_range = 0.5
    brightness_range = 0.2
    hue_range = 0.1
    saturation_range = 0.2
    mirror_aug_on = True

    KEYPOINTS_HEATMAP_THRESHOLD = 0.5
    JOINT_ALIGNMENT_THRESHOLD = 0.5




algorithms = {
    0: OpenPoseCfg
}


def get_cfg():
    return algorithms[0]