# %
import csv
import json
import os


class DataSummary:
    """
    A class to summarize data from a JSON file and its corresponding metadata CSV file.
    """

    data = []
    names = {}

    def __init__(self, datafile: str = None, metafile: str = None):
        """
        Constructor to initialize the DataSummary object.

        Parameters:
        datafile (str): Path to the JSON data file.
        metafile (str): Path to the CSV metadata file.

        Raises:
        ValueError: If datafile or metafile is not provided.
        FileNotFoundError: If datafile or metafile does not exist.
        """
        if datafile is None or metafile is None:
            raise ValueError("Data file and meta file must be provided")
        if not os.path.exists(datafile):
            raise FileNotFoundError("Data file does not exist")
        if not os.path.exists(metafile):
            raise FileNotFoundError("Meta file does not exist")
        self.datafile = datafile
        self.metafile = metafile
        with open(metafile) as file:
            csv_file = csv.reader(file)
            keys = next(csv_file)
            types = next(csv_file)
            self.names = dict(zip(keys, types))
        with open(datafile) as file:
            self.json_file = json.load(file)
            self.data = self.json_file["data"]
        for row in self.data:
            keys_to_remove = [key for key in row if key not in self.names]
            for key in keys_to_remove:
                row.pop(key)
            for key in self.names:
                if key not in row:
                    row[key] = None

    def __getitem__(self, key):
        """
        Get item by index or feature name.

        Parameters:
        key (int or str): Index or feature name.

        Returns:
        dict or list: Data row or list of feature values.

        Raises:
        IndexError: If index is out of range.
        KeyError: If feature name is not found.
        TypeError: If key is not int or str.
        """
        if isinstance(key, int):
            if key < 0 or key >= len(self.data):
                raise IndexError("Index out of range")
            return self.data[key].copy()
        if isinstance(key, str):
            self._is_feature(key)
            return [row[key] for row in self.data if key in row]
        else:
            raise TypeError("Invalid argument type.")

    def sum(self, feature):
        """
        Calculate the sum of a numerical feature.

        Parameters:
        feature (str): Feature name.

        Returns:
        float: Sum of the feature values.

        Raises:
        ValueError: If feature is categorical.
        """
        self._number_feature_check(feature)
        return sum(float(row[feature]) for row in self.data if row[feature] is not None)

    def count(self, feature):
        """
        Count the number of non-None values for a feature.

        Parameters:
        feature (str): Feature name.

        Returns:
        int: Count of non-None values.
        """
        self._is_feature(feature)
        return sum(1 for row in self.data if row[feature] is not None)

    def mean(self, feature):
        """
        Calculate the mean of a numerical feature.

        Parameters:
        feature (str): Feature name.

        Returns:
        float: Mean of the feature values.

        Raises:
        ValueError: If feature is categorical.
        """
        self._number_feature_check(feature)
        return self.sum(feature) / self.count(feature)

    def min(self, feature):
        """
        Calculate the minimum value of a numerical feature.

        Parameters:
        feature (str): Feature name.

        Returns:
        float: Minimum value of the feature.

        Raises:
        ValueError: If feature is categorical.
        """
        self._number_feature_check(feature)
        return min(float(row[feature]) for row in self.data if row[feature] is not None)

    def max(self, feature):
        """
        Calculate the maximum value of a numerical feature.

        Parameters:
        feature (str): Feature name.

        Returns:
        float: Maximum value of the feature.

        Raises:
        ValueError: If feature is categorical.
        """
        self._number_feature_check(feature)
        return max(float(row[feature]) for row in self.data if row[feature] is not None)

    def unique(self, feature):
        """
        Get the unique values of a feature.
        Unique are values that appear only once in the data.

        Parameters:
        feature (str): Feature name.

        Returns:
        list: List of unique values.
        """
        self._is_feature(feature)
        uni = self._sorted_counter(feature)
        uni = sorted([key for key in uni if uni[key] == 1])
        return uni

    def mode(self, feature):
        """
        Get the mode(s) of a feature.

        Parameters:
        feature (str): Feature name.

        Returns:
        list: List of the 10 most common values.
        """
        self._is_feature(feature)
        counter = self._sorted_counter(feature)
        return list(counter.keys())[:10]

    def empty(self, feature):
        """
        Count the number of empty values for a feature.

        Parameters:
        feature (str): Feature name.

        Returns:
        int: Count of empty values.
        """
        self._is_feature(feature)
        return sum(row[feature] is None for row in self.data)

    def to_csv(self, filename, delimiter=","):
        """
        Export the data to a CSV file.

        Parameters:
        filename (str): Path to the output CSV file.
        delimiter (str): Delimiter for the CSV file.
        """
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file, delimiter=delimiter)
            writer.writerow(self.names.keys())
            for row in self.data:
                writer.writerow([row[key] for key in self.names.keys()])

    def _sorted_counter(self, feature):
        """
        Get a sorted counter of feature values.

        Parameters:
        feature (str): Feature name.

        Returns:
        dict: Counter of feature values.
        """
        counter = {}
        for row in self.data:
            if row[feature] is not None:
                if row[feature] in counter:
                    counter[row[feature]] += 1
                else:
                    counter[row[feature]] = 1
        return dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))

    def _number_feature_check(self, feature):
        """
        Check if a feature is numerical.

        Parameters:
        feature (str): Feature name.

        Raises:
        KeyError: If feature is not found.
        ValueError: If feature is categorical.
        """
        self._is_feature(feature)
        if self.names[feature] == "string":
            raise ValueError(f"Cannot calculate for categorical feature '{feature}'")
        return True

    def _is_feature(self, feature):
        """
        Check if a feature is in the data or throw an error if it is not.

        Parameters:
        feature (str): Feature name.

        Raises:
        KeyError: If feature is not found.
        """
        if feature not in self.names.keys():
            raise KeyError(f"Feature '{feature}' not found in data")
