#!/usr/bin/env python3
""" Simple pagination for a database of popular baby names."""

import csv
from typing import List, Tuple


class Server:
    """Handles pagination of baby names database."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Returns the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a specific page from the baby names dataset.

        Args:
            page: Current page number.
            page_size: Total size of each page.

        Returns:
            List of baby names for the specified page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        range_start, range_end = index_range(page, page_size)
        pagination = self.dataset()

        return pagination[range_start:range_end]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a given page and page size.

    Args:
        page: Current page number.
        page_size: Total size of each page.

    Returns:
        Tuple containing start and end index for the specified page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
