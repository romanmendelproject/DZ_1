# Программа-поисковик
Программа парсит первую страницу результатов поиска google.com.<br/>
Входные данные:<br/>
Первый аргумент - искомое слово<br/>
Второй аргумент - глубина рекурсии вложенных ссылок<br/>
Если второй аргумент не указан, тогда рекурсия отключена<br/>
Результат поиска записывается в файл result.txt<br/>
Пример запуска:
- без рекурсии
go_search.py Россия
- с учетом рекурсии
go_search.py Россия 5<br/>
Результат:<br/>
<br/>
ОПИСАНИЕ:<br/>
Авиакомпания "Россия"https://www.rossiya-airlines.comСохраненная копияАвиакомпания ГТК <br/>"Россия" - Российские авиалинии: бронирование и продажа билетов на самолет, расписание <br/>рейсов, информация о ценах на ...<br/>
ОСНОВНАЯ ССЫЛКА:<br/>
https://www.rossiya-airlines.com/<br/>
РЕКУРСИВНЫЕ ССЫЛКИ:<br/>
https://www.youtube.com/c/авиакомпанияроссия<br/>
https://www.instagram.com/rossiya_airlines/?from=main_page_header<br/>
https://wci.rossiya-airlines.com/?lang=ru<br/>
https://wci.rossiya-airlines.com/?lang=ru<br/>
https://wtrweb.worldtracer.aero/filedsp/fv.htm<br/>
<br/>
Тестирование проекта:
<pre>
pytest -v
==================================================== test session starts =====================================================
platform win32 -- Python 3.8.0, pytest-5.3.2, py-1.8.1, pluggy-0.13.1 -- c:\users\дом\appdata\local\programs\python\python38-32\python.exe
cachedir: .pytest_cache
rootdir: C:\web_python
collected 9 items                                                                                                             
DZ_1/tests/test_pars_google.py::test_go_search_func_with_good_arg PASSED [ 11%]
DZ_1/tests/test_pars_google.py::test_go_search_func_with_bad_arg PASSED [ 22%]
DZ_1/tests/test_pars_google.py::test_go_search_func_with_moke_rec_and_req PASSED [ 33%]
DZ_1/tests/test_pars_google.py::test_recursion PASSED [ 44%]
DZ_1/tests/test_pars_google.py::test_main_good_arg PASSED [ 55%]
DZ_1/tests/test_pars_google.py::test_main_bad_type_rec PASSED [ 66%]
DZ_1/tests/test_pars_google.py::test_main_bad_type_url PASSED [ 77%]
DZ_1/tests/test_pars_google.py::test_main_bad_arg_long_rec PASSED [ 88%]
DZ_1/tests/test_pars_google.py::test_main_bad_arg_long_url PASSED [100%]
</pre>


