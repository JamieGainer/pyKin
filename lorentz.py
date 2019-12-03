from __future__ import annotations

import sys
sys.path.append('/Users/jgainer/PMC/Physics/Utilities/einstein_tensor/einstein_tensor')
import einstein_tensor as et

class FrameTensor(et.Tensor):

    def __init__(self, value, indices, frame):
        self.tensor = et.Tensor(value, indices)
        self.frame = frame

    def __eq__(self, other) -> bool:
        try:
            return (self.tensor == other.tensor) and (self.frame == other.frame)
        except:
            return False

    def __add__(self, other):
        try:
            if self.frame != other.frame:
                raise ValueError('Cannot add tensors from different frames')
        except AttributeError:
            raise ValueError("Cannot add a tensor with a frame to a different kind of object.")
        try:
            tensor_sum = self.tensor + other.tensor
            return FrameTensor(tensor_sum.value, tensor_sum.indices, self.frame)
        except AttributeError:
            raise ValueError("Cannot add a tensor to a non-tensor object.")


class FourVector(et.Tensor):


    def __add__(self, other: FourVector) -> FourVector:
        if self.indices != other.indices:
            raise ValueError("Tensors have different indices so cannot be added.")

        return FourVector(self.value + other.value, self.indices, self.frame)