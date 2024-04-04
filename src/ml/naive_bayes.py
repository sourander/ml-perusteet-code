from collections import defaultdict as dd

# Helper lambda function
argmax = lambda values: values.index(max(values))

class NaiveBayes:
    def __init__(self):
        # Friendly names for the labels
        self.LABELS = (0, 1)
        self.LABEL_NAMES = ("not spam", "spam")

        # Statistics
        self.n = 0                   # N
        self.n_class = {0: 0, 1: 0}  # N(y)
        self.priors = {0: 0, 1: 0}   # P(y)        
        self.word_counts = dd(lambda: dd(int))        # N(x_i | y)
        self.word_likelihoods = dd(lambda: dd(float)) # P(x_i | y)

    @staticmethod
    def preprocess_word(word:str):
        # IMPLEMENT lowercase
        # IMPLEMENT remove non-alphanumeric characters
        return word
    
    @staticmethod
    def count_words(dataset:str, word_preprocessor=None):
        wc = dd(lambda: dd(int))
        for sentence, label in dataset:
            for word in sentence.split():
                if word_preprocessor:
                    word = word_preprocessor(word)
                wc[word][label] += 1
        return wc

    @staticmethod
    def count_sentences_by_y(dataset:tuple[str, int]):
        n_class = {0: 0, 1: 0}
        for _, label in dataset:
            n_class[label] += 1
        return n_class

    @staticmethod
    def validate_dataset(dataset):
        assert isinstance(dataset, list), "Dataset must be a list"
        assert all([isinstance(d, tuple) for d in dataset]), "Each element in the dataset must be a tuple"
        assert all([isinstance(d[0], str) for d in dataset]), "The first element in each tuple must be a string"
        assert all([isinstance(d[1], int) for d in dataset]), "The second element in each tuple must be an integer"

    def fit(self, dataset:tuple[str, int]):
        
        # Validate the dataset
        self.validate_dataset(dataset)

        self.n = len(dataset)
        self.word_counts = NaiveBayes.count_words(dataset, self.preprocess_word)
        self.n_class = NaiveBayes.count_sentences_by_y(dataset)

        # Calculate priors
        for label in self.LABELS:
            self.priors[label] = self.n_class[label] / self.n

        # Calculate word likelihoods
        for word in self.word_counts:
            for label in self.LABELS:
                self.word_likelihoods[word][label] = self.word_counts[word][label] / self.n_class[label]

    def predict(self, evidence:str, verbose=True):
        # Argmax_y P(y) * SUM(P(x_i | y))
        predictions: list[float] = [
            None, # IMPLEMENT the formula here for class 0
            None  # IMPLEMENT the formula here for class 1
        ]
        if verbose:
            print(f"The given evidence is {self.LABEL_NAMES[argmax(predictions)]} ({max(predictions):.2f} > {min(predictions):.2f})")
        
        return self.LABELS[argmax(predictions)]
    
    
if __name__ == "__main__":
    DATASET = [
        ("free viagra now", 1),                 # Spam
        ("viagra for a limited time only", 1),  # Spam
        ("a game of golf tomorrow", 0),
        ("office movie night cancelled", 0),
        ("tldr newsletter", 0),
        ("a cat for sale", 0),
    ]

    # Test it 
    nb = NaiveBayes()
    nb.fit(DATASET)
    print(nb.predict("free viagra movie"))