# a-plot-a-day
Here I will create plots analysing some interesting datasets. The goal is to showcase interesting plots that are related to events that happen on the news.




# Usage


Make sure first that you are on a virtual environment
```
sudo apt install python3.12-venv 
python3 -m venv myenv
source myenv/bin/activate
pip install numpy
pip install .
```

To install the required packages
```
pip install -r requirements.txt
```

Then you can create the plot of the day with
```
python3 YYYYMMDD/poltter.py
```

Or see the data learning process with
```
jupyter-notebook YYYYMMDD/data_experimentation.ipynb
```
