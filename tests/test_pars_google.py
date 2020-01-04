from search.google_search import pars_google
from unittest.mock import patch
import validators


@patch('search.google_search.recursion', return_value=["arg1", "arg2"])
def test_go_search_func_with_good_arg(moke_recursion, rand_int):
    pars_google("тест", rand_int)
    rec_arg_1 = moke_recursion.call_args.args[0]
    rec_arg_2 = moke_recursion.call_args.args[1]
    assert moke_recursion.call_count == 7
    assert isinstance(rec_arg_1, str)
    assert isinstance(rec_arg_2, int)
    assert validators.url(rec_arg_1)


@patch('search.google_search.recursion', return_value=["arg1", "arg2"])
def test_go_search_func_with_bad_arg(moke_recursion, rand_int, rand_str):
    pars_google(rand_str, rand_int)
    assert not moke_recursion.called


