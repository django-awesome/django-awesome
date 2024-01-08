from unittest import TestCase

from ...checks import check_model
from ..models import Entry


class AutocompleteSearchFieldsChecksTests(TestCase):
    @staticmethod
    def test_sample_model_has_search_field_success():
        # Not strictly necessary as the check will run as part of the above
        assert check_model(Entry) == []

    @staticmethod
    def test_sample_model_has_search_field_failed():
        def broken():
            return ("tytle__icontains",)

        orig = Entry.__dict__["autocomplete_search_fields"]
        try:
            Entry.autocomplete_search_fields = broken
            errors = check_model(Entry)
            assert len(errors) == 1
            assert (
                errors[0].msg == "Model grappelli_test.entry returned bad entries for "
                "autocomplete_search_fields: tytle__icontains"
            )
        finally:
            Entry.autocomplete_search_fields = orig
