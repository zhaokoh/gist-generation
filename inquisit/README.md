# Gist generation experiment using Inquisit 5

This is the main directory that contains all the necessary Inquisit files to run the gist generation experiment.

## Inquisit Overview

The experiments built using Inquisit is declarative - i.e. no programming code required. Inquisit has a number of pre-defined items/objects to be used in an experiment, such as picture, text, trial, block. Inquisit also has many input objects that accepts user inputs, such as textbox, radio buttons. Here is a good overview with many examples: https://www.millisecond.com/support/docs/v5/html/viewer.htm#introduction.htm.

## Justification of using Inquisit for this project

* Inquisit was chosen because Monash has license to it and can host Inquisit Web experiments.
* Inquisit timing accuracy is independently tested and verified: https://www.millisecond.com/products/inquisit5/timing.aspx, saving us to measure the timing accuracy if we choose another framework such as jspsych. 
* Integrates well with MTurk via survey link and approved by Amazon as a MTurk external platform.

## Pre-requisites

### Software

* Inquisit Lab 5 installed on your machine (I am using version 5.0.14.0 on Mac OS) - there is another way to access Inquisit using [Monash vLab](https://www.monash.edu/research-portal/vlab/applications/inquisit/inquisit-lab) but could be slower and exchange files between the virtual machine and local could be cumbersome. [Monash Research Portal](https://www.monash.edu/research-portal/vlab/applications/inquisit) also contains information about Inquisit installation.

* Get a licence for Inquisit Lab - once installed, follow the instructions to get a registration key.

* Apparently there are limited licence in Monash for Inquisit Web, so we may have to share the same account. Please let me know if you need to access Inqusit Web and I can share the login details with you.
  
## Steps to run the experiment using Inquisit Lab (local - not integrated with MTurk)

* Clone this repository to your local machine.
* Open ```gist.iqx``` file with Inquisit Lab. This is the main definition file. I created this script by using one of the examples that others have created (in the tutorial) and modified from there.
* There are several wrapper scripts (such as ```gist_imgset_1.iqx```) that wrap around ```gist.iqx```. The purpose is to define different image stimuli and the main core logic is still reusable.
* Open ```gist_imgset_1.iqx``` and update the item ```pictures``` to contain only a handful of images (for demo purposes).
* click the "Run" button at the top and the experiment should run on your local machine if everything is setup correctly - and images are found.
* The experiment will prompt you for a subject id and group id - just keep the default values.
* If you want to abandon the experiment half way, press "Command+Control+Q" on Mac.


## Steps to run the experiment in Inquisit Web

Once you are happy with your experiment locally, then it is time to open to the world. To host your experiment on millisecond:

* Login to millisecond server using Monash login.
* Click My Account -> Web Scripts
* Register your new script using the "Register New Script". There are many options to setup your experiment but this won't be covered here.
* After successfully registered the web script, you will get a launch page URL and you can send this link to the participants or anyone you want to test.

## References

* https://www.millisecond.com/support/docs/v5/html/viewer.htm#introduction.htm
