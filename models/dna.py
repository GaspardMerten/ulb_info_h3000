from typing import Tuple

__all__ = ("DNA", "DNAFragment")
# Tuple of size 19 + 1 (0) + 2 (groups)
DNA = Tuple[
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
]
DNAFragment = Tuple[int, ...]
