# RGB-based Action Recognition


## NTURGB+D dataset
The dataset:
- The NTU RGB+D dataset aims to facilitate human activity recognition and pose estimation tasks.
- It contains RGB videos captured using a Kinect v2 sensor from 40 different subjects.
- The dataset covers a wide variety of human actions, including daily and interactive activities so as medical conditions, performed in various indoor and outdoor environments.
- The videos are captured from three camera views, resulting in a total of 56,880 action samples.
- Each video is labeled with a specific action class, representing the activity being performed in the video.

The label format:
- The NTURGB+d dataset uses numerical labels to represent different action classes. The 60 action classes are each assigned a unique numerical value from A1 to A60.
- Each file name is in the format of SsssCcccPpppRrrrAaaa, in which sss is the setup number, ccc is the camera ID, ppp is the performer (subject) ID, rrr is the replication number (1 or 2), and aaa is the action class label.
- For example, if the file name is S001C002P003R002A013, the label are the 3 last digits. Here, it is the action 13 whih corresponds to tearing up paper

Extraction of the dataset:
- dataset.py extracts all the frames from each video. 
- The frames are extracted with the <em>VideoCapture from OpenCV</em>
- dataset.py returns for each video a 6 dimensions array with: the frame index, x, y, R, G and B. 
- The label is separately returned 

## Contribution on RGB based Action Recognition:

MotionBERT : https://motionbert.github.io/

We are using the MotionBERT architecture as a reference. Our contribution is to change the data given to the MotionBERT model to use RGB only videos and not Skeleton-based videos which is actually how MotionBERT works. 

Here is the abstract of the MotionBERT paper to get a rough idea of how it works :

"We present a unified perspective on tackling various
human-centric video tasks by learning human motion representations from large-scale and heterogeneous data resources. Specifically, we propose a pretraining stage in
which a motion encoder is trained to recover the underlying 3D motion from noisy partial 2D observations. The
motion representations acquired in this way incorporate
geometric, kinematic, and physical knowledge about human motion, which can be easily transferred to multiple
downstream tasks. We implement the motion encoder with
a Dual-stream Spatio-temporal Transformer (DSTformer)
neural network. It could capture long-range spatio-temporal
relationships among the skeletal joints comprehensively and
adaptively, exemplified by the lowest 3D pose estimation
error so far when trained from scratch. Furthermore, our
proposed framework achieves state-of-the-art performance
on all three downstream tasks by simply finetuning the pretrained motion encoder with a simple regression head (1-2
layers), which demonstrates the versatility of the learned
motion representations."

## Idea :

To change the input from skeleton based to RGB only, we had the implement the dataloader written in dataset.py as said before. With our new preprocessed data, we have to change the neural network implemented in the previous DSTFormer to make it match the new dimensions of the incomming data.

## Results 
Theoritically, the MotionBert model translated for the NTURGB+D dataset and RGB-based action recognition should work but we never had the opportunity to verify it. Indeed, practically the train.py never compiled correctly and we gave up due to a lack of time. 
