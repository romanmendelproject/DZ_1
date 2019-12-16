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
