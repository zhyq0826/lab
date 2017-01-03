from nose.plugins.attrib import attr
from nose.tools import (
    assert_false,
    assert_true,
    assert_raises,
    assert_equal,
    assert_equals,
    assert_not_equal,
    assert_almost_equal,
    assert_not_almost_equal,
    assert_sequence_equal,
    assert_list_equal,
    assert_tuple_equal,
    assert_set_equal,
    assert_in,
    assert_not_in,
    assert_is,
    assert_is_not,
    assert_dict_equal,
    assert_dict_contains_subset,
    assert_items_equal,
    assert_multi_line_equal,
    assert_less,
    assert_less_equal,
    assert_greater,
    assert_greater_equal,
    assert_is_none,
    assert_is_not_none,
    assert_is_instance,
    assert_not_is_instance,
    assert_raises_regexp,
    assert_regexp_matches,
    assert_not_regexp_matches,
)


from unittest import TestCase


@attr(tag='a')
def test_function_a():
    assert_equals(1, 1)


@attr(tag='b')
def test_function_b():
    with assert_raises(ValueError):
        raise TypeError('hello')


@attr(tags=['b'])
def test_function_c():
    with assert_raises(ValueError):
        raise TypeError('hello')


