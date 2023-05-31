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

## Results 
Theoritically, the MotionBert model translated for the NTURGB+D dataset and RGB-based action recognition should work but we never had the opportunity to verify it. Indeed, practically the train.py never compiled correctly and we gave up due to a lack of time. 
