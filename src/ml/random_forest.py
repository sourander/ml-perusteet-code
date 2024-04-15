import random
import ml.decision_tree as dt


def sample_with_replacement(data):
    """Alias:
    Bagging with bootstrap
    """
    # IMPLEMENT
    return data


def sample_without_replacement(data, n):
    """Alias:
    Bagging with a random subset
    """
    # IMPLEMENT
    return data


class RandomForest:
    def __init__(self, num_trees, verbose=False):
        self.num_trees = num_trees
        self.trees = []
        self.verbose = verbose

    def train(self, data: list[tuple], replacement=True):

        subsets = []
        if replacement:
            subsets = [sample_with_replacement(data) for _ in range(self.num_trees)]
        else:
            sample_size = len(data) // self.num_trees
            subsets = [
                sample_without_replacement(data, sample_size)
                for _ in range(self.num_trees)
            ]

        for subset in subsets:

            if self.verbose:
                percentage = sum([x[-1] for x in subset]) / len(subset) * 100
                print(
                    f"Building tree with {percentage:.1f} % positive samples (n rows {len(subset)})."
                )

            tree = dt.build_tree(subset)
            self.trees.append(tree)

    def predict(self, sample):
        labels = [dt.predict(tree, sample) for tree in self.trees]

        # Print the labels of the trees
        if self.verbose:
            for i, label in enumerate(labels):
                print(f"Tree {i}: {label}")

        return max(set(labels), key=labels.count)