#Link for qn. and explaination: https://neetcode.io/problems/gradient-descent/question
class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        minimizer=init

        for _ in range(iterations):
            derivative=2*minimizer  # Derivative:f'(x) = 2x
            minimizer=minimizer-learning_rate*derivative # Update rule:x=x-learning_rate*f'(x)

        # Round final answer to 5 decimal places
        return round(minimizer,5)
