import json
from pathlib import Path
from math import log2
from dataclasses import dataclass


@dataclass
class IGScore:
    column_index: int
    column_type: str
    score: float
    split_point: float | None


@dataclass
class Node:
    n_samples: int
    depth: int


@dataclass
class Leaf(Node):
    label: int
    exit_reason: str


@dataclass
class Decision(Node):
    count: int
    ig: IGScore
    left: Node
    right: Node


def entropy(X) -> float:
    H_val = float()
    # IMPLEMENT: Entropy function
    return H_val


def class_probabilities(column_values) -> list[float]:
    # IMPLEMENT: Class probabilities
    #  Returning e.g. [0.5, 0.5] for a binary column with equal number of 0s and 1s
    return [None, None]


def calculate_information_gain(left, right, H_before):

    # Compute the entropy of the two partitions
    H_left = entropy(class_probabilities(left))
    H_right = entropy(class_probabilities(right))

    # Compute the entropy after the split
    n = len(left) + len(right)

    # Weighted by the number of elements in each partition
    q_left = len(left) / n
    q_right = len(right) / n
    H_after = q_left * H_left + q_right * H_right

    # Compute the information gain
    IG = H_before - H_after
    return IG


def find_optimal_split_point(data, i):
    H_before = entropy(class_probabilities([row[-1] for row in data]))
    column_values = sorted([row[i] for row in data])  # Sort the values

    # Init
    best_ig = float("-inf")
    best_split_point = None

    for idx in range(len(column_values) - 1):
        # Try every possible average of two adjacent values
        # As a candidate split point
        split_point = (column_values[idx] + column_values[idx + 1]) / 2
        left = [row[-1] for row in data if row[i] <= split_point]
        right = [row[-1] for row in data if row[i] > split_point]

        # Calculate information gain for this split
        ig = calculate_information_gain(left, right, H_before)

        # Update the best split point if information gain is better
        if ig > best_ig:
            best_ig = ig
            best_split_point = split_point

    return best_split_point


def column_information_gain(data, i) -> tuple[float, None | float]:

    if len(data) == 0:
        raise ValueError("Data must not be empty")

    # Initialize a variable to store the best split value
    best_split_point = 0.5

    # Compute the entropy of the entire dataset
    # This is the entropy before the split
    H_before = entropy(class_probabilities([row[-1] for row in data]))

    # Check that split index column values are binary
    binary_column = all([r[i] in (0, 1) for r in data])

    if binary_column:
        # Partition the data into left and right partitions
        # Based on the binary class label (e.g. there is a shower)
        left = [row[-1] for row in data if not row[i]]
        right = [row[-1] for row in data if row[i]]

    else:
        best_split_point = find_optimal_split_point(data, i)

        # Use the best split point to partition the data
        left = [row[-1] for row in data if row[i] <= best_split_point]
        right = [row[-1] for row in data if row[i] > best_split_point]

    ig = calculate_information_gain(left, right, H_before)
    return IGScore(
        column_index=i,
        column_type="binary" if binary_column else "continuous",
        score=ig,
        split_point=best_split_point,
    )


# Same as a function
def find_max_column_information_gain(data, verbose=False):
    # Find out the best column to split on
    best_ig: IGScore = None

    # We assume that the last column is the class label
    N_FEATURES = len(data[0]) - 1
    
    for i in range(N_FEATURES):
        this_ig: IGScore = column_information_gain(data, i)

        if verbose:
            print(f"[find_max_column_information_gain] IG for column {i}: {this_ig}")

        if best_ig is None or this_ig.score > best_ig.score:
            best_ig = this_ig

    return best_ig


def split_data(data, ig: IGScore):

    # Produce the split based on binary or continuous column
    if ig.column_type == "binary":
        left = [row for row in data if not row[ig.column_index]]
        right = [row for row in data if row[ig.column_index]]
    elif ig.column_type == "continuous":
        left = [row for row in data if row[ig.column_index] <= ig.split_point]
        right = [row for row in data if row[ig.column_index] > ig.split_point]
    else:
        raise ValueError(f"Unknown column type {ig.column_type}")

    return left, right


def build_tree(data, depth=0, **kwargs):

    def majority_class(reason):
        """
        A nested helper function to create a Leaf node
        on early exit with a given reason.
        """
        return Leaf(
            n_samples=len(data),
            depth=depth,
            label=max(set([row[-1] for row in data]), key=[row[-1] for row in data].count),
            exit_reason=None # IMPLEMENT adding the reason
        )

    # Default values
    max_depth = kwargs.get("max_depth", 5)
    min_ig = kwargs.get("min_ig", 0.01)
    min_samples_split = kwargs.get("min_samples_split", 2)
    verbose = kwargs.get("verbose", False)

    if verbose:
        print(
            f"[build_tree] Building a Decision or Leaf at depth {depth} with {len(data)} samples"
        )

    # Stop condition: we have reached a uniform class
    if len(set([row[-1] for row in data])) == 1:
        return majority_class("Uniform class")

    # Early stopping if we reach the maximum depth
    # Predict the most common class
    if depth >= max_depth:
        print(f"[build_tree] Early stopping at depth {depth}")
        return majority_class("Max depth")

    # Stop if the number of samples is below the minimum required to split
    if len(data) < min_samples_split:
        return majority_class("Min samples split")

    # Find out the best column to split on
    ig = find_max_column_information_gain(data, verbose=verbose)

    if ig.score < min_ig:
        return majority_class("Min IG")

    # Split the data based on the best column
    left, right = split_data(data, ig)

    # Create a new node
    node = Decision(
        n_samples=len(data),
        depth=depth,
        count=len(data),
        ig=ig,
        left=build_tree(left, depth + 1, **kwargs),
        right=build_tree(right, depth + 1, **kwargs),
    )

    return node


###################################
# Helper functions - Play around! #
###################################


def visualize_tree(node: Node, indent=0):
    col_names = ["im_well_rested", "dst_has_shower", "required_speed", "go_by_car"]

    if isinstance(node, Leaf):
        print("  " * indent + str(node))
    elif isinstance(node, Decision):
        print(
            "  " * indent + f"Decision ({node.depth}, n={node.n_samples}): "
            f"Split on {col_names[node.ig.column_index]} ({node.ig.split_point})"
        )
        visualize_tree(node.left, indent + 1)
        visualize_tree(node.right, indent + 1)


def predict(node: Node, input_values):
    while True:
        # If we have reached a leaf, return the label
        if isinstance(node, Leaf):
            return node.label
        
        if node.ig.column_type == "binary":
            if input_values[node.ig.column_index] == 0:
                node = node.left
            else:
                node = node.right
        else:
            if input_values[node.ig.column_index] <= node.ig.split_point:
                node = node.left
            else:
                node = node.right




def read_jsonl(file_path: Path):
    # Read
    contents = file_path.read_text(encoding="utf-8")

    # Accumulate
    data = []
    for line in contents.splitlines():
        d = json.loads(line)
        row = (
            d["im_well_rested"],
            d["dst_has_shower"],
            float(d["required_speed"]),
            d["go_by_car"],
        )
        data.append(row)
    return data


######################################################################
# The content below shows an example of how to use the decision tree #
######################################################################

if __name__ == "__main__":

    # Note! Run this file from the root of the project
    data = read_jsonl(Path("data/bike_or_car/16_row_sample.jsonl"))

    # Build the tree
    tree_sample = build_tree(data, max_depth=3, verbose=True)

    # Visualize the tree
    print("\n==== Visualisation begins ====\n")
    visualize_tree(tree_sample)

    # Test the prediction with one sample
    print("\n==== Manual prediction begins ====\n")
    input_values = (0, 1, 10.63)
    print(f"Prediction for {input_values}: {predict(tree_sample, input_values)}")

    # Run against the test data
    print("\n==== Test with larger dataset begins ====\n")
    data_train = read_jsonl(Path("data/bike_or_car/293_train.jsonl"))
    data_test = read_jsonl(Path("data/bike_or_car/100_test.jsonl"))
    tree = build_tree(data, max_depth=3)
    y = [row[-1] for row in data_test]
    y_hat = [predict(build_tree(data), row) for row in data_test]
    false_positives = sum([a == 0 and b == 1 for a, b in zip(y, y_hat)])
    true_positives = sum([a == 1 and b == 1 for a, b in zip(y, y_hat)])
    false_negatives = sum([a == 1 and b == 0 for a, b in zip(y, y_hat)])
    true_negatives = sum([a == 0 and b == 0 for a, b in zip(y, y_hat)])
    print("Confusion matrix:")
    print(f"TP: {true_positives}", f"FP: {false_positives}")
    print(f"FN: {false_negatives}", f"TN: {true_negatives}")
    print(f"Accuracy: {(true_positives + true_negatives) / len(y)}")
