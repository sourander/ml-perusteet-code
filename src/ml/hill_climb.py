import random

from dataclasses import dataclass

@dataclass
class Solution:
    weights: list[float]
    loss: float
    iterations: int = 0

class HillClimb:
    def __init__(self, max_iterations=10_000, stop_threshold=None):
        self.max_iter = max_iterations      # Maximum number of epochs
        self.dimensions: int = None         # Number of features
        self.max_step_size: float = 0.1     # Maximum size for a step
        self.stop_threshold = (             # Number of iterations without improvement before stopping
            stop_threshold 
            or self.max_iter // 10
        )

        self.best_solution: Solution = None  # Weights for the model

    def _step(self) -> float:
        """Generate a random step in the range [-step_size, step_size]"""
        # IMPLEMENT
        return 0.0

    def _initialize_random_solution(self) -> Solution:
        w = [self._step() for _ in range(self.dimensions)]
        return Solution(weights=w, loss=float("inf"))
    
    def predict(self, X: list[float]) -> float:
        assert self.best_solution, "Model not trained yet"

        predictions = []
        for x in self._add_bias(X):
            predictions.append(self._predict_one(x, self.best_solution.weights))
        return predictions
    
    def _predict_one(self, X: list[float], weights: list[float]) -> float:
        return sum([w * x for x, w in zip(X, weights)])
    
    def _compute_loss(self, X, y, solution: list[float]) -> Solution:
        mse = sum([(self._predict_one(x, solution.weights) - y_) ** 2 for x, y_ in zip(X, y)]) / len(X)
        solution.loss = mse
        return solution
    
    def _offer_new_solution(self, old_solution: Solution, current_iteration:int) -> Solution:

        new_weights = []

        for i, w in enumerate(old_solution.weights):
            new_weights.append(w + self._step())

        return Solution(weights=new_weights, loss=float("inf"), iterations=current_iteration)
    
    def _add_bias(self, X):
        return [[1.0] + list(x) for x in X]

    def fit(self, X: list[list[float]], y: list[float]):
        # Add bias to data
        X = self._add_bias(X)
        self.dimensions = len(X[0])

        best_solution = self._initialize_random_solution()              # Step 1: Initialize random weights
        best_solution = self._compute_loss(X, y, best_solution)         # Step 2: Score the solution
        print(f"Initial solution: {best_solution}")
        
        for i in range(self.max_iter):
            new_solution = self._offer_new_solution(best_solution, i)   # Step 3: In/Decrease one weight
            new_solution = self._compute_loss(X, y, new_solution)       # Step 4: Find the loss (MSE)

            if new_solution.loss < best_solution.loss:                  # Step 5: If new solution is better, keep it
                # IMPLEMENT
                continue

            if i - best_solution.iterations > self.stop_threshold:      # Step 6: Unless stopping criteria met, repeat steps 3-5
                print(
                    f"Stopping early at iteration {i} "
                    f"(No improvement in {self.stop_threshold} iterations)"
                )
                break

        # Save the best solution to the instance variable
        self.best_solution = best_solution


if __name__ == "__main__":

    X = [
        [-0.84, -1.12], 
        [-1.11, -2.36], 
        [-0.96, -0.75], 
        [-1.4, 1.3], 
        [1.86, -0.19], 
        [0.67, 1.59], 
        [-0.22, 1.48], 
        [-0.9, -0.09], 
        [-1.15, 0.77], 
        [-0.51, -0.6]
    ]
    y = [-117.0, -225.09, -92.35, 56.07, 47.31, 149.73, 110.69, -37.88, 23.01, -65.43]

    model = HillClimb()
    model.fit(X, y)
    print(f"Best solution: {model.best_solution}")

    y_hat = model.predict(X)

    for y1, y2 in zip(y, y_hat):
        print(f"Actual: {y1:.2f}, Predicted: {y2:.2f} (Error: {(y1 - y2):.2f})")

    print(f"MSE: {model.best_solution.loss:.2f}")
    print(f"RMSE: {model.best_solution.loss ** 0.5:.2f}")
