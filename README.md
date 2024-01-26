# Оцінка ефективності жадібного алгоритму та алгоритму динамічного програмування

## Вступ
Цей проект включає реалізацію та порівняльний аналіз двох алгоритмів: жадібного алгоритму та алгоритму динамічного програмування. Обидва алгоритми розроблено для вирішення задачі визначення оптимального способу видачі решти з заданих номіналів монет.

## Опис алгоритмів
- `find_coins_greedy`: Жадібний алгоритм, що вибирає найбільші доступні номінали монет для складання заданої суми.
- `find_min_coins`: Алгоритм динамічного програмування, який знаходить мінімальну кількість монет, необхідних для формування заданої суми.

## Порівняльний аналіз
Виконано порівняння часу виконання обох алгоритмів за допомогою модуля `timeit` у Python. Тестування проводилося на прикладі суми в 1000 одиниць.

- Час виконання жадібного алгоритму: `{greedy_time}` секунд
- Час виконання алгоритму динамічного програмування: `{dp_time}` секунд

## Висновки
Порівняльний аналіз показав, що для великих сум алгоритм динамічного програмування може бути ефективнішим за жадібний алгоритм. Це пов’язано з тим, що динамічне програмування забезпечує оптимальне вирішення завдання з мінімізації кількості монет, в той час як жадібний алгоритм працює швидше, але може не завжди знаходити оптимальний результат.