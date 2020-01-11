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
    """Полная проверка программы с корректными входными даными
       без подмены функций с учетом рекурсии,
       в качестве аргумента рекурсии передается
       рандомное целое число от 1 до 10.
    """
    pars_google("тест", rand_int)
    rec_arg_1 = moke_recursion.call_args.args[0]
    rec_arg_2 = moke_recursion.call_args.args[1]
    assert moke_recursion.call_count == 7
    assert isinstance(rec_arg_1, str)
    assert isinstance(rec_arg_2, int)
    assert validators.url(rec_arg_1)


@patch('search.google_search.recursion')
def test_go_search_func_with_bad_arg(moke_recursion, rand_int, rand_str):
    """Проверка запроса в поисковик, при котором будет
       не найдено ни одного результата поиска.
       В качестве искомого слова передается рандомная строка из 30 символов.
    """
    pars_google(rand_str, rand_int)
    assert not moke_recursion.called


rec_arg = b'<div class="g"><a href="https://test.info"></div>'


@patch('search.google_search.recursion')
@patch('search.google_search.request', return_value=BeautifulSoup(rec_arg, "lxml"))
def test_go_search_func_with_moke_rec_and_req(moke_request, moke_recursion, rand_int):
    """Полная проверка программы с корректными входными даными
       с подменой функций recursion и request с учетом рекурсии
    """
    pars_google("тест", rand_int)
    rec_arg_1 = moke_recursion.call_args.args[0]
    moke_request.assert_called_once()
    moke_recursion.assert_called_once()
    assert rec_arg_1 == 'https://test.info'


@patch('search.google_search.request', return_value=BeautifulSoup(b'<a href="https://test.info">', "lxml"))
def test_recursion(moke_requests):
    """Тест функции request с подменой выходных данных
    """
    assert recursion("test.ru", 5) == ['https://test.info']


@patch('search.google_search.pars_google')
@patch('search.google_search.recursion')
def test_main_good_arg(moke_recursion, moke_pars_google):
    """Тест функции main с корректными данными
    """
    main("test", 5)
    assert moke_pars_google.assert_called
    assert moke_recursion.assert_called


def test_main_bad_type_rec():
    """Тест функции main с не верным типом аргумента рекурсии
    """
    with pytest.raises(ValueError):
        main("test", "test")


def test_main_bad_type_url():
    """Тест функции main с не верным типом искомого словом
    """
    with pytest.raises(TypeError):
        main(5, 5)


@patch('search.google_search.pars_google')
def test_main_bad_arg_long_rec(moke_pars_google):
    """Тест функции main с аргументом рекурсии более 10
    """
    with pytest.raises(SystemExit):
        main("test", 30)


@patch('search.google_search.pars_google')
def test_main_bad_arg_long_url(moke_pars_google):
    """Тест функции main с длинной искомого слова более 20 символов
    """
    with pytest.raises(SystemExit):
        main("testsssssssssssssssss", 5)
