# optical-flow-csrd

## Introduction
This repository is about detecting intrusion in railway
scenario. Raft is used as our optical-flow model due to its
performance. 


<div align=center>
<img src="imgs/md_1.png" alt="示例图片" width="500" height="300">
</div>

The proposed approach can detect not only pedestrians, but also
moving objects.

<div align=center>
<img src="imgs/md_3.png" alt="示例图片" width="500" height="150">
</div>

## Usage

## Methods
The input consists of two consecutive frames from a video,
annotated as $I_{t_{1}}$ and $I_{t_{2}}$. where the time interval
is around 200ms. Label the intrusion area in advance, and a pre-define
a threshold $\Eta$. Feeding the pair frames $I_{t_{i}}$ and $I_{t_{i+1}}$
to the model and calculate the total detected pixels inside the Intrusion area,
once the value is over the $\Eta$, report it.

