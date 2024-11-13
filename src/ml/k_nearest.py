from collections import defaultdict
from dataclasses import dataclass

from ml.utils.math import euclidean_distance # IMPLEMENT

@dataclass
class Point:
    features: tuple[float|int]
    label: str|None

@dataclass
class Neighbor:
    distance: float
    label: str|int

class kNN:
    def __init__(self, k):
        self.k = k
        self.points = []

    def fit(self, data: list):
        """A method for fitting a dataset where the last column is the label"""
        self.points = [
            # IMPLEMENT
            # Point(features=???, label=???) for point in data
        ]
    
    @staticmethod
    def majority_vote(neighbors:list[Neighbor]):
        votes = defaultdict(int)
        # IMPLEMENT
        return max(votes, key=votes.get)
    
    def predict(self, features: list[float|int]):
        """A method for predicting a label for given of features"""
        neighbors: list[Neighbor] = []
        for point in self.points:
            distance = euclidean_distance(point.features, features)
            neighbors.append(Neighbor(distance, point.label))
        neighbors = sorted(neighbors, key=lambda x: x.distance)
        k_nearest = neighbors[:self.k]
        return self.majority_vote(k_nearest)


if __name__ == "__main__":
    data = [
        (1, 2, 3, "cat"),
        (4, 5, 6, "cat"),
        (7, 8, 9, "dog"),
        (10, 11, 12, "dog"),
    ]

    model = kNN(k=3)
    model.fit(data)
    observation = (1, 2, 4)
    prediction = model.predict(observation)
    print(f"The observartion ({observation}) is predicted to be a {prediction}.")
    assert prediction == "cat"