# Simple progress bar for Python

## Dependency
Nothing

## how to run
Clone this repo to your project

## Use the API
````
from progress_bar.progressbar import ProgressBar
data = range(0,10)
pb = ProgressBar(len(data))
for i,x in enumerate(data) :
    pb.update(i)
pb.end()
````
