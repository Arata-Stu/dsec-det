from pathlib import Path
import numpy as np
import cv2
import argparse
import yaml  # 追加
from dsec_det.dataset import DsecDetDataset


if __name__ == '__main__':
    parser = argparse.ArgumentParser("""Visualize an example.""")
    parser.add_argument("--mode", type=str, required=True, choices=["train", "val", "test"], help="Mode to run: train, val or test")  # modeを追加
    args = parser.parse_args()

    root_dir = Path('/mnt/data_ssd/DSEC/')

    yaml_path = './../config/train_val_test_split.yaml'
    with open(yaml_path, "r") as f:
        config = yaml.safe_load(f)
            
    # modeに基づいて条件分岐
    if args.mode == "train":
        chosen_split = config["train"]
    elif args.mode == "val":
        chosen_split = config["val"]
    elif args.mode == "test":
        chosen_split = config["test"]
    else:
        raise ValueError("Invalid mode. Choose from 'train', 'val', or 'test'.")

    # DSECDetクラスにmodeに基づいたsplitを設定してインスタンスを作成
    dataset = DsecDetDataset(root_dir, split_config=chosen_split, img_size=(480, 640), sync="back", transform=None, use_imgs=True, use_events=True)
    print(len(dataset))
    
