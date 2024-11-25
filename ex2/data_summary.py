# %
def DataSummary(self, parameter_list):
    """
    docstring
    """
    def __init__(datafile, metafile):
        """
        Constructor

        """
        if datafile is None or metafile is None:
            raise Exception(ValueError("Data file and meta file must be provided"))
        self.datafile = datafile
        self.metafile = metafile

    def __iter__(self, position):
        """_summary_

        Args:
            position (index or key): _description_

        """
        return

    def sum(self, feature):
        return

    def count(self, feature):
        return

    def mean(self, feature):
        return

    def min(self,feature):
        return

    def max(self,feature):
        return

    def unique(self,feature):
        return

    def mode(self,feature):
        return

    def empty(self,feature):
        return

    def to_csv(self,feature):
        return
    