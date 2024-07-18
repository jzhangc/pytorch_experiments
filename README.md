## pytorch_experiments
Initial Pytorch experiments

## Set up virtual environment (up: July 18, 2024)

This is repo is to learn and play with Pytorch

NOTE: The following contains steps to install on both PC (mainly Linux), Intel and Apple Silicon Macs.

1. System requirement

    PC (with NVIDIA GPU) and Apple Silicon Macs. For Macs (both Intel and Apple Silicon machines), we will use Pytoch's own `Metal Performance Shaders (MPS)` backend for GPU acceleration. 

2. Install miniforge3 (mini coda with forge channel as default)

   url: <https://github.com/conda-forge/miniforge#miniforge3>

        bash Miniforge3-MacOSX-arm64.sh

   NOTE 1: Although it is possible to use `conda config --add channels conda-forge`  to manually add the `forge` channel to miniconda, it is generally recommended using miniforge version of conda for both Apple and Intel chips.

3. TBC

## Resources

1. Apple Official: <https://developer.apple.com/metal/pytorch/>


## Troubleshooting (up: July 2024)

1. TBC

     `MPS` GitHub issue tracker: <https://github.com/pytorch/pytorch/issues?q=is%3Aissue+is%3Aopen+module%3A+mps>