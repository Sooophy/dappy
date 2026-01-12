# Overview
This README is intended for setting up tsne analysis following the DANNCE prediction.
Please refer to the [DANNCE prediction protocol](https://github.com/Sooophy/dannce/tree/stroke_analysis/trace_protocol) for precious steps.

## Install your environment
Please install your environment following the README [here](https://github.com/Sooophy/neuroposelib/blob/stroke_analysis_sophie/README.md) written by Josh.

## Folder structure and files
Now you already have a folder structure like this for the DANNCE prediction.
```
seguralab
    |
    netid_folder (your folder under the lab space, e.g.: nvp17)
        |
        experiment1 (contains all the videos for the series of the experiment)
            |
            20240612_c1_m1 (YYYYMMDD_cX_mX)
            20240612_c1_m1_cylinder (YYYYMMDD_cX_mX_cylinder)
            20240612_c1_m2
            ...
        |
        experiment2
        |
        experiment3
```

Now create a new folder under your netid_folder, you can call it stroke_exp here.
Organize your folder to the following structure:

```
seguralab
    |
    netid_folder (your folder under the lab space, e.g.: nvp17)
        |
        stroke_exp
            |
            configs
                |
                stroke_exp.yaml
            data
                |
                metadata.csv
            stroke_exp.py
            stroke_exp.sh
            preprocess_for_tsne.py
```

We have provided an example metadata.csv for your reference.
Note that the videoID need to be unique for each row. You can leave the ClusterDirectory blank or simply not have this column if you follow the same naming rules. We will fill with the preprocessed data path later. Check `preprocess_for_tsne.py` comments for more information.

## Data Processing
First activate your environment, run:

 `conda activate neuroposelib`

For data preprocessing, run:

`python preprocess_for_tsne.py`. 

Remember to modify the path in the script.
Check your metadata, ensure you have the ClusterDirectory correct after running the script.

Then run:

`sh stroke_exp.sh`

This will request memory You can check stroke_exp.out for the running result.
