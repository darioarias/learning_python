# Python dictionaries are sometimes used as records, with the keys used as field names and field values of different types.
# For example, consider a record describing a book in JSON or Python:
data = {
    "isbn": "0134757599",
    "title": "Refactoring, 2e",
    "authors": ["Martin Fowler", "Kent Beck"],
    "pagecount": 478,
}

# attempting to annotate dicts
import json
from typing import List, TypedDict


class BookDict(TypedDict):
    isbn: str
    title: str
    authors: List[str]
    pagecount: int


from typing import TYPE_CHECKING


def demo() -> None:
    book = BookDict(
        isbn="0134757599",
        title="Refactoring, 2e",
        authors=["Martin Fowler", "Kent Beck"],
        pagecount=478,
    )
    authors = book["authors"]
    if TYPE_CHECKING:
        reveal_type(authors)
    authors = "Bob"
    book["weight"] = 4.2
    del book["title"]


AUTHOR_ELEMENT = "<AUTHOR>{}</AUTHOR>"


def to_xml(book: BookDict) -> str:
    elements: List[str] = []
    for key, value in book.items():
        if isinstance(value, list):
            elements.extend(AUTHOR_ELEMENT.format(n) for n in value)

        else:
            tag = key.upper()
            elements.append(f"<{tag}>{value}</{tag}>")
    xml = "\n\t".join(elements)
    return f"<BOOK>\n\t{xml}\n</BOOK>"


def from_json(data: str) -> BookDict:
    whatever = json.loads(data)
    return whatever


print(to_xml(BookDict(**data)))
