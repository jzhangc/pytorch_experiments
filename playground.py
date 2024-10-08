"""
This is the playground for pytorch on both the NVIDIA and Apple platforms.

Resource:
https://www.learnpytorch.io/pytorch_cheatsheet/#device-agnostic-code-using-pytorch-on-cpu-gpu-or-mps
https://pytorch.org/get-started/locally/
https://mobiarch.wordpress.com/2024/03/18/install-pytorch-in-apple-silicon/

"""

# ------ imports ------
import torch

# ------ test and verification
# -- base torch --
print(f"PyTorch version: {torch.__version__}")

x = torch.rand(5, 3)
print(x)


# -- GPU --
if torch.cuda.is_available():
    device = "cuda"  # NVIDIA GPU
elif torch.backends.mps.is_available():
    device = "mps"  # Apple GPU
else:
    device = "cpu"  # Defaults to CPU if NVIDIA GPU/Apple GPU aren't available

print(f"Using device: {device}")
