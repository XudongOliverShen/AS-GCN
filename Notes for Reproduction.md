# Notes for Reproducing AS-GCN

Here I wrote down some of the issues/errors you might come across when reproducing AS-GCN and my ways of getting around. see the AS-GCN [Paper](https://arxiv.org/pdf/1904.12659.pdf) as well as their [Github](https://github.com/limaosen0/AS-GCN). Hope it helps.



## Environment

- python=3.6
- CUDA 10 (for NSCC) or 8 (for lab GPU server)
- pytorch & torchvision (corresponding version with CUDA)
- pyyaml, argparse, tqdm(not mentioned but used), h5py (needed for torchlight), matplotlib (not mentioned but used)



## 1. torchlight setup

Their [Github](https://github.com/limaosen0/AS-GCN) gives following command:

```python
cd torchlight, python setup.py, cd..
```

Clearly it should be:

```python
cd torchlight, python setup.py install, cd..
```

refer to the code of [ST-GCN](https://github.com/yysijie/st-gcn).

Besides, the torchlight setup.py from AS-GCN's repo seems not to work properly with python 3.6. I use the torchlight from [ST-GCN](https://github.com/yysijie/st-gcn) instead. And it works well.



## 2. Dataset unzipping

in .data_gen/ntu_gen_preprocess.py, line 143, instead of

```python
gendata(arg.data_path, out_path, arg.ignored_sample_path, benchmark=b, part=sn)
```

it should be

```python
gendata(arg.data_path, out_path, arg.ignored_sample_path, benchmark=b, set_name=sn)
```



## 3. Data preprocessing

instead of

```python
python ./data_gen/ntu_gen_preprocess.py
```

you should

```python
cd datagen, python ntu_gen_preprocess.py, cd ..
```



## 4. Train AIM

When running on servers and using PBS job scheduler, you might wish to add `-koed` to your pbs file, to indicate that you wish to have real-time streaming of your err & out file.

in main.py, comment out line 13, which is following:

```python
processors['demo'] = import_class('processor.demo.Demo')
```

Another obvious typo from their [Github](https://github.com/XudongOliverShen/AS-GCN): when training on cross subject, load configurations from the directory ntu-xsub; when training on cross view, load configurations from the directory nut-xview. 

