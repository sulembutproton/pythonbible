import pythonbible as bible


def test_get_references(text_with_reference):
    # Given a text string with at least one scripture reference
    # When parsing that text
    references = bible.get_references(text_with_reference)

    # Then the references are found and returned in a list of normalized reference tuples
    assert len(references) == 2
    assert references[0] == (bible.Book.MATTHEW, 18, 12, 18, 14)
    assert references[1] == (bible.Book.LUKE, 15, 3, 15, 7)


def test_get_references_complex(
    text_with_reference_complex, normalized_references_complex
):
    # Given a text string with multiple complex references
    # When parsing that text
    references = bible.get_references(text_with_reference_complex)

    # Then the references are found and returned in a list of normalized reference tuples
    assert references == normalized_references_complex


def test_normalize_reference(non_normalized_reference):
    # Given a non-normalized reference (just a string)
    # When we normalize that reference
    normalized_references = bible.normalize_reference(non_normalized_reference)

    # Then the reference is returned as a list of tuples with the book enum,
    # start chapter, start verse, end chapter, and end verse
    assert len(normalized_references) == 1
    assert normalized_references[0] == (bible.Book.MATTHEW, 18, 12, 18, 14)


def test_normalize_reference_without_verse_numbers(reference_without_verse_numbers):
    # Given a non-normalized reference that does not contain verse numbers (just book and chapters)
    # When we normalize that reference
    normalized_references = bible.normalize_reference(reference_without_verse_numbers)

    # Then the resulting normalized references contain the proper verse numbers
    assert len(normalized_references) == 1
    assert normalized_references[0] == (bible.Book.EXODUS, 20, 1, 20, 26)


def test_normalize_reference_range_without_verse_numbers(
    reference_range_without_verse_numbers,
):
    # Given a non-normalized reference that does not contain verse numbers (just book and chapters)
    # When we normalize that reference
    normalized_references = bible.normalize_reference(
        reference_range_without_verse_numbers
    )

    # Then the resulting normalized references contain the proper verse numbers
    assert len(normalized_references) == 1
    assert normalized_references[0] == (bible.Book.GENESIS, 1, 1, 4, 26)


def test_get_references_roman_numerals(
    roman_numeral_references, normalized_references_complex
):
    # Given a text string with multiple references with roman numerals
    # When parsing that text
    references = bible.get_references(roman_numeral_references)

    # Then the references are found and returned in a list of normalized reference tuples
    assert references == normalized_references_complex


def test_philemon_vs_philippians():
    """https://github.com/avendesora/python-bible/issues/2"""
    # Given a text string with a reference in the book of Philemon
    text = "Philemon 1:9"

    # When we parse the references from that text
    references = bible.get_references(text)

    # Then the parser does not raise an error and returns the appropriate reference
    assert references == [(bible.Book.PHILEMON, 1, 9, 1, 9)]
