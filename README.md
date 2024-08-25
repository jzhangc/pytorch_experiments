## pytorch_experiments
Initial `Pytorch` experiments

## Set up virtual environment (up: July 18, 2024)

This is repo is to learn and play with `Pytorch`

NOTE: The following contains steps to install on both PC (mainly Linux), Intel and Apple Silicon Macs. This text has yet to include instructions to set up CUDA for NVIDIA GPUs. 

1. System requirement

    PC (with NVIDIA GPU) and Apple Silicon Macs. For Macs (both Intel and Apple Silicon machines), we will use Pytoch's own `Metal Performance Shaders (MPS)` backend for GPU acceleration. 

    `Pytorch` version >= `2.3`

    `Python` version >= `3.7`


2. Install miniforge3 (mini coda with forge channel as default)

   url: <https://github.com/conda-forge/miniforge#miniforge3>

        bash Miniforge3-MacOSX-arm64.sh

   NOTE 1: Although it is possible to use `conda config --add channels conda-forge`  to manually add the `forge` channel to miniconda, it is generally recommended using miniforge version of conda for both Apple and Intel chips.

3. Set up environment (will install all the essential libraries)


     Apple
     
          conda create -f ./inst/environment_apple.yml --prefix ./conda_env_apple

     Linux NVIDIA

          conda create -f ./inst/environment_linux_nivida.yml --prefix ./conda_env_nivida_ln


4. Install Pytorch

          pip3 install torch torchvision torchtext

## Resources

1. Apple Official: <https://developer.apple.com/metal/pytorch/>


## Troubleshooting (up: July 2024)

1. TBC

     `MPS` GitHub issue tracker: <https://github.com/pytorch/pytorch/issues?q=is%3Aissue+is%3Aopen+module%3A+mps>