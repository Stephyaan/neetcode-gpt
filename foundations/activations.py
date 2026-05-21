#Qn: https://neetcode.io/problems/sigmoid-and-relu/question
#my answer(simple logic code)
import numpy as np
from numpy.typing import NDArray
class Solution:   
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
    
        res=np.round(1 / (1 + np.exp(-z)), 5)
        return res

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        result=[]
        for x in z:
            result.append(float(max(0,x)))
        return result
#original code:using numpy library completely
import numpy as np
from numpy.typing import NDArray
class Solution:
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        return np.round(1 / (1 + np.exp(-z)), 5)

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        return np.maximum(0, z)
