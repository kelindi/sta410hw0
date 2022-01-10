# UofT STA410/2102 Statistical Computation

Return to STA410 Programming Portfolio Parent Repository [here](https://github.com/pointOfive/STA410_HW/blob/master/README.md#uoft-sta4102102-statistical-computation).

## Submitting Programming Portfolio Assignment 0
Submit `.ipynb` file to [MarkUs](https://markus-ds.teach.cs.toronto.edu/) before the end of the calendar day (EoD) on the due date.

## Programming Portfolio Assignment 0

[Programming Portfolio Assignment 0](sta410hw0.ipynb)  introduces Python through the following foundational computational and statistical computation problems:

1. Bit string representation of integer value numbers
2. Pseudorandom integer generation with modulus
3. Floating-point error accumulation reduction
4. High precision single pass variance calculations

### Accessing Programming Portfolio Assignment 0
UofT students may access this the collection of programming problems with the [UofT JupyterHub](https://jupyter.utoronto.ca) via

> https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https://github.com/pointOfive/sta410hw0&branch=master

Some notes to faciltate getting started in this environment are available on the UofT JupyterHub [support page](https://act.utoronto.ca/jupyterhub-support/).
If for some reason JupyterHub is not loading the repository, you can delete and reload repositories (after downloading and saving what you need).  

> From JupyterHub, open a new terminal with `New` > `Terminal` and then use `yes y | rm -r <path to directory to delete>` to a delete the repository directory.

Alternatively, the programming problems may also be accessed without UofT authentication using 
[Google Colab](https://colab.research.google.com) via

> https://colab.research.google.com/github/pointOfive/sta410hw0/blob/master/sta410hw0.ipynb

***If you're working in some other environment, 
the versioning there must support [notebook format 4.5](https://github.com/jupyterlab/jupyterlab/issues/9729), e.g.,
[jupyterlab](https://jupyter.org/install) version
[3.0.13 or greater](https://github.com/jupyterlab/jupyterlab/releases/tag/v3.0.13);
otherwise, your notebook cell-ids will not be supported and you will not get any credit for your submitted work.***

> You may check if cell ids are present or changing at each save with `! grep '"id":' <path/to/notebook>.ipynb`
