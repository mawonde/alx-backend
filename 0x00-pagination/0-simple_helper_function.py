#!/usr/bin/env python3
"""Module with a simple helper function for pagination"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of the start and end index of the page"""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
