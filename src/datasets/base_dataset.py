from abc import ABC, abstractmethod
from pathlib import Path

from torch.utils.data import DataLoader
from torch.utils.data import Dataset, DataLoader, random_split


# from datasets import load_dataset


class BaseDataset(ABC):
    base_data_dir = Path('./data')

    @abstractmethod
    def get_dataset(self, split: str) -> Dataset:
        """Return the DataLoader for the dataset.

        Returns:
            DataLoader: The DataLoader instance for the data.
        """
        pass

    @property
    @abstractmethod
    def vocab_size(self):
        pass

    def get_train_dataset(self) -> Dataset:
        return self.get_dataset("train")

    def get_test_dataset(self) -> Dataset:
        return self.get_dataset("test")

    def get_val_dataset(self) -> Dataset:
        return self.get_dataset("validation")
