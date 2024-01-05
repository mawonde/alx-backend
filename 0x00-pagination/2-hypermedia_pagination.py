#!/usr/bin/env python3
""" Simplified hypermedia pagination for a baby names database."""

import csv
from math import ceil
from typing import List, Tuple, Dict


class Server:
    """Handles pagination of a baby names dataset."""

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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get hypermedia information for the specified page.

        Args:
            page: Current page number.
            page_size: Total size of each page.

        Returns:
            Dict with hypermedia details:
            - 'page_size': the length of the returned dataset page
            - 'page': the current page number
            - 'data': the dataset page
            - 'next_page': number of the next page, None if no next page
            - 'prev_page': number of the previous page, None if no previous page
            - 'total_pages': the total number of pages in the dataset as an integer
        """
        data = []
        try:
            data = self.get_page(page, page_size)
        except AssertionError:
            return {}

        dataset: List = self.dataset()
        total_pages: int = len(dataset) if dataset else 0
        total_pages = ceil(total_pages / page_size)
        prev_page: int = (page - 1) if (page - 1) >= 1 else None
        next_page: int = (page + 1) if (page + 1) <= total_pages else None

        hypermedia: Dict = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }

        return hypermedia


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
