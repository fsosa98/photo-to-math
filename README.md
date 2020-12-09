# Photomath

## Instructions 
Two modes of use:

### 1. Run the program with a trained model
```bash
python src/app.py 2 path_to_trained_model
```
Default:
```bash
python src/app.py 2 trained_model.h5
```

### 2. Run the program with the data set
```bash
python src/app.py 1 path_to_train_data
```

I used [this](https://www.kaggle.com/xainano/handwrittenmathsymbols) data to train model.
Structure of data: <br />
train_data/ <br />
├── 0 <br />
│   └── image1.png <br />
├── 1 <br />
│   └── image100.png <br />
. <br />
. <br />
. <br />
 ── 15 <br />
    └── image1000.png <br />

## Usage
Go to http://127.0.0.1:5000/ <br />
Clik the "Browse..." button and select an image.<br />
After selecting the image clik the "Calculate" button.<br />
The result will be displayed in a new line.
