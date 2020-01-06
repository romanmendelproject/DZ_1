from search.google_search import pars_google
from search.google_search import recursion
from unittest.mock import patch
from go_search import main
import validators
import sys
import pytest
from bs4 import BeautifulSoup


@patch('search.google_search.recursion')
def test_go_search_func_with_good_arg(moke_recursion, rand_int):
    pars_google("тест", rand_int)
    rec_arg_1 = moke_recursion.call_args.args[0]
    rec_arg_2 = moke_recursion.call_args.args[1]
    assert moke_recursion.call_count == 7
    assert isinstance(rec_arg_1, str)
    assert isinstance(rec_arg_2, int)
    assert validators.url(rec_arg_1)


@patch('search.google_search.recursion')
def test_go_search_func_with_bad_arg(moke_recursion, rand_int, rand_str):
    pars_google(rand_str, rand_int)
    assert not moke_recursion.called


rec_arg = b'<div class="g"><a href="https://test.info"></div>'


@patch('search.google_search.recursion')
@patch('search.google_search.request', return_value=BeautifulSoup(rec_arg, "lxml"))
def test_go_search_func_with_moke_rec_and_req(moke_request, moke_recursion, rand_int):
    pars_google("тест", rand_int)
    rec_arg_1 = moke_recursion.call_args.args[0]
    moke_request.assert_called_once()
    moke_recursion.assert_called_once()
    assert rec_arg_1 == 'https://test.info'


@patch('search.google_search.request', return_value=BeautifulSoup(b'<a href="https://test.info">', "lxml"))
def test_recursion(moke_requests):
    assert recursion("test.ru", 5) == ['https://test.info']


@patch('search.google_search.pars_google')
@patch('search.google_search.recursion')
def test_main_good_arg(moke_recursion, moke_pars_google):
    url = "test"
    rec = 5
    main(url, rec)
    assert moke_pars_google.assert_called
    assert moke_recursion.assert_called


def test_main_bad_type_rec():
    url = "test"
    rec = "test"
    with pytest.raises(ValueError):
        main(url, rec)


def test_main_bad_type_url():
    url = 5
    rec = 5
    with pytest.raises(TypeError):
        main(url, rec)


@patch('search.google_search.pars_google')
def test_main_bad_arg_long_rec(moke_pars_google):
    url = "test"
    rec = 30
    with pytest.raises(SystemExit):
        main(url, rec)


@patch('search.google_search.pars_google')
def test_main_bad_arg_long_url(moke_pars_google):
    url = "testsssssssssssssssss"
    rec = 5
    with pytest.raises(SystemExit):
        main(url, rec)
