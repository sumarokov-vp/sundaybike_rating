from typing import Collection, Iterable, Iterator, Sequence, Set, Tuple

def sort_as_subsets(tuples: Collection[Tuple[_T, _T]], allitems: Collection[_T]) -> Iterator[Sequence[_T]]: ...
def sort(tuples: Collection[Tuple[_T, _T]], allitems: Collection[_T], deterministic_order: bool = ...) -> Iterator[_T]: ...
def find_cycles(tuples: Iterable[Tuple[_T, _T]], allitems: Iterable[_T]) -> Set[_T]: ...
