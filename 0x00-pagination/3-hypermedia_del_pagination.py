#!/usr/bin/env python3
"""
Simple and robust hypermedia pagination with deletion resilience
"""

import csv
from typing import List, Dict


class Server:
    """Handles pagination of a baby names database."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Returns the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Returns the dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get hypermedia information for the specified index.

        Args:
            index: Starting index.
            page_size: Total size of each page.

        Returns:
            Dict with hypermedia details:
            - 'index': the current starting index
            - 'next_index': the starting index for the next page
            - 'page_size': the length of the returned dataset page
            - 'data': the dataset page
        """
        result_dataset = []
        index_data = self.indexed_dataset()
        keys_list = list(index_data.keys())
        assert index + page_size < len(keys_list)
        assert index < len(keys_list)

        if index not in index_data:
            start_index = keys_list[index]
        else:
            start_index = index

        for i in range(start_index, start_index + page_size):
            if i not in index_data:
                result_dataset.append(index_data[keys_list[i]])
            else:
                result_dataset.append(index_data[i])

        next_index: int = index + page_size

        if index in keys_list:
            next_index
        else:
            next_index = keys_list[next_index]

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(result_dataset),
            "data": result_dataset,
        }
