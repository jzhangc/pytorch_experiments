"""
This is the playground for pytorch on both the NVIDIA and Apple platforms

"""

# ------ imports ------
import torch

# ------ test and verification
# -- base torch --
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
