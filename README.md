# bfss
Building Footprint Segmentation from Satellite images

- [Project Structure](#project-structure)
- [Project Setup](#project-setup)
- [Project description](#proj-des)
- [To-Do](#to-do)

<a name="project-structure"></a>
## 1. Project Structure

```
bfss
  ├── train.py
  ├── config.py
  ├── src  
  |   ├── training/
  |   ├── evaluation/
  |   ├── networks/   
  |   └── utils/
  ├── data
  |   ├── datasets/AerialImageDataset/
  |   └── test/
```

_Data_: <br>
the `data` folder is not a part of this git project as it was heavy. The same can be downloaded from below link:

```sh
https://project.inria.fr/aerialimagelabeling/
```

<a name="project-setup"></a>
## 2. Project Setup
To setup the virtual environment for this project do the following steps:

Step 1: ```cd bfss``` #Enter the project folder! <br />
Step 2: ```conda env create -f envs/bfss.yml``` #create the virutal environment from the yml file provided. <br />
Step 3: ```conda activate bfss``` #activate the virtual env.

<a name="proj-des"></a>
## 3. Project description
The training script is `train.py` <br>
The entire training configuration including the dataset path, hyper-parameters and other arguments are specified in `config.py`, which you can modify and experiment with.

<a name="to-do"></a>
## 4. To-Do

- [ ] Data download and EDA.
- [x] Basic framework for evaluating existing models
- [x] Complete framework with mulitple models tested
- [ ] Pre and Post Processing techniques (on-going)
- [x] Transfer Learning framework
- [ ] Model training (On-Going)
