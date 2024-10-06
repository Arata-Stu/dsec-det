from pathlib import Path
import numpy as np
import cv2
import argparse
import yaml  # 追加
from dsec_det.dataset import DSECDet


if __name__ == '__main__':
    parser = argparse.ArgumentParser("""Visualize an example.""")
    parser.add_argument("--dsec_merged", type=Path, required=True)
    parser.add_argument("--split_config", type=Path, required=False, help="Path to YAML config file.")
    parser.add_argument("--mode", type=str, required=True, choices=["train", "val", "test"], help="Mode to run: train, val or test")  # modeを追加
    args = parser.parse_args()


    
    with open(args.split_config, "r") as f:
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
    dataset = DSECDet(args.dsec_merged, split_config=chosen_split, sync="back", debug=True)
    dataset.print_summary()
