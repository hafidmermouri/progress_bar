# Simple progress bar for Python

## Dependency
Nothing

## how to run
Clone this repo to your project

## Use the API
````
from progress_bar.progressbar import ProgressBar
data = [1,2,3,4,5,6,7,8,9,10]
pb = ProgressBar(len(data))
for i,x in enumerate(data) :
    pb.update(i)
pb.end()
````