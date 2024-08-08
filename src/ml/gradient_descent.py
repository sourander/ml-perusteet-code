import random

from dataclasses import dataclass, field
from ml.vector import Vector
from copy import deepcopy


@dataclass
class TrainingStep:
    i: int
    loss: float


@dataclass
class TrainingHistory:
    steps: list[TrainingStep] = field(default_factory=list)


class GradientDescent:
    def __init__(self, learning_rate: float = 0.01, max_iterations: int = 1000):
        self.learning_rate = learning_rate
        self.epochs = max_iterations

        self.X = None
        self.y = None
        self.w = None
        self.m = None

        self.history = TrainingHistory()

    def _add_bias(self, X):
        return [Vector(1.0).concat(x) for x in X]

    def compute_slope_using_delta(self, delta=0.0000001):
        """This is not used, but here for reference."""
        slopes = {}

        for i in range(len(self.w)):
            w_delta = deepcopy(self.w)
            w_delta[i] += delta

            delta_loss = self.loss(self.X, w_delta)
            actual_loss = self.loss(self.X, self.w)

            slope = (delta_loss - actual_loss) / delta
            slopes[i] = round(slope, 2)
        return slopes

    def _partial_derivative(self, x: Vector, feature_index, observation_index):
        return 2 * x[feature_index] * (self.w @ x - self.y[observation_index])

    def _predict_one(self, x, w) -> float:
        return sum([w * x for x, w in zip(x, w)])

    def predict(self, X, w) -> float:

        predictions = []
        for x in self.X:
            predictions.append(self._predict_one(x, w))
        return Vector(*predictions)

    def loss(self, X, w) -> float:
        return sum((self.y - self.predict(X, w)) ** 2) / self.m

    def gradient(self) -> Vector:
        # Accumulator
        partials = [0] * len(self.w)

        for obs_i, x in enumerate(self.X):
            for feature_i, w in enumerate(self.w):
                partials[feature_i] += self._partial_derivative(x, feature_i, obs_i)

        return Vector(*partials) / self.m

    def training_step(self, i):
        gradient = self.gradient()
        step = self.learning_rate * Vector(*gradient)
        # IMPLEMENT
        self.history.steps.append(TrainingStep(i=i, loss=self.loss(self.X, self.w)))

    def fit(self, X: list[Vector], y: Vector):
        self.X = self._add_bias(X)
        self.y = y
        self.m = len(self.X[0])
        self.w = Vector(*[random.uniform(-1, 1) for _ in range(self.m)])

        for i in range(self.epochs):
            self.training_step(i)


if __name__ == "__main__":
    model = GradientDescent()

    # These values are from the lesson Mkdocs material
    X = [Vector(x) for x in range(8)]
    y = Vector(*[1.52, 1.24, 1.03, 0.83, 0.49, 0.24, 0.08, -0.21])

    model.fit(X, y)

    assert 1.51 < model.w[0] < 1.52
    assert -0.24 > model.w[1] > -0.25
