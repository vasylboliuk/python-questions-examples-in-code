from assertpy import assert_that


class TestComparingDictionaries:

    def test_comparing_dict_list_as_values(self):
        actual = {'a': [1, 2, 3], 'b': [5, 6], "c": "Hello World"}
        expected = {'a': [2, 1, 3], 'b': [5, 6], "c": "Hello World"}

        assert_that(sorted(actual)).extracting('a').is_same_as(sorted(expected.get('a')))
        assert_that(sorted(actual)).extracting('b').is_same_as(sorted(expected.get('b')))
        assert_that(actual).is_equal_to(expected, include="c")






