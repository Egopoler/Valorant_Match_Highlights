import torch
import torch_directml
def get_device():
    """
    Returns the device to be used for computations.

    Returns:
        str: The device to be used for computations. Possible values are "mps", "cuda", or "cpu".
    """
    if torch.backends.mps.is_available():
        return "mps"
    elif torch.cuda.is_available():
        return "cuda"
    return "cpu"

print(get_device())