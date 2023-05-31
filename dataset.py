import os
import cv2
import torch
from torch.utils.data import Dataset, DataLoader

class NTURGBD_Dataset(Dataset):
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.file_list = os.listdir(data_dir)

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        video_file = self.file_list[idx]
        video_path = os.path.join(self.data_dir, video_file)
        frames = self.load_video_frames(video_path)

        # Extract height, width, and separate R, G, B values
        height, width, _ = frames[0].shape
        r_values = [frame[:, :, 0] for frame in frames]
        g_values = [frame[:, :, 1] for frame in frames]
        b_values = [frame[:, :, 2] for frame in frames]

        # Extract the label from the video filename
        label = video_file[16:20]

        return frames, height, width, r_values, g_values, b_values, label

    def load_video_frames(self, video_path):
        frames = []
        cap = cv2.VideoCapture(video_path)

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)

        cap.release()
        return frames

# Example usage
data_dir = 'DATASET//wow'
dataset = NTURGBD_Dataset(data_dir)
dataloader = DataLoader(dataset, batch_size=1, shuffle=True)

print(dataset.__len__())

for frames, height, width, r_values, g_values, b_values, label in dataloader:
    print("Frames:", frames)
    print("Height:", height)
    print("Width:", width)
    #print("R Values:", r_values)
    #print("G Values:", g_values)
    #print("B Values:", b_values)
    print("Label:", label)
    break  # Print only the first batch
