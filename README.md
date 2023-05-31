# Group8_RGB-based_Action_Recognition

## NTURGB+d Dataset:
- The NTURGB+d dataset is an extension of the NTU RGB+D dataset, which aims to facilitate human activity recognition and pose estimation tasks.
- It contains RGB and depth videos captured using a Kinect v2 sensor from 40 different subjects.
- The dataset covers a wide variety of human actions, including both daily and interactive activities, performed in various indoor and outdoor environments.
- The videos are captured from three camera views, resulting in a total of 80,000 action samples.
- Each video is labeled with a specific action class, representing the activity being performed in the video.

### Label Format:
- The NTURGB+d dataset uses numerical labels to represent different action classes.
- The dataset consists of 60 action classes, each assigned a unique numerical value.
- For example, if there are 60 action classes, the labels could range from 1 to 60, with each number corresponding to a specific action category.

### Acquiring the NTURGB+d Dataset:
- The NTURGB+d dataset is publicly available for research purposes.
- To acquire the dataset, you can visit the official website of the NTU RGB+D dataset (http://rose1.ntu.edu.sg/Datasets/actionRecognition.asp).
- On the website, you will find information about the dataset, including instructions on how to request access.
- Typically, you may need to register, agree to the dataset's terms of use, and provide details about your research project before gaining access to the dataset.
- The dataset is often provided as a set of downloadable files, including RGB and depth video clips, along with corresponding label files.

It's important to note that the availability and access procedure for the NTURGB+d dataset may have changed since my last knowledge update in September 2021. Therefore, I recommend visiting the official website mentioned above or conducting a search for the most up-to-date information on acquiring the NTURGB+d dataset.

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


