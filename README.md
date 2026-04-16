### Hexlet tests and linter status:
[![Actions Status](https://github.com/daniljudo2-pixel/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/daniljudo2-pixel/python-project-49/actions)

## python-project-49
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=daniljudo2-pixel_python-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=daniljudo2-pixel_python-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=daniljudo2-pixel_python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=daniljudo2-pixel_python-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=daniljudo2-pixel_python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=daniljudo2-pixel_python-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=daniljudo2-pixel_python-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=daniljudo2-pixel_python-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=daniljudo2-pixel_python-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=daniljudo2-pixel_python-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=daniljudo2-pixel_python-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=daniljudo2-pixel_python-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=daniljudo2-pixel_python-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=daniljudo2-pixel_python-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=daniljudo2-pixel_python-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=daniljudo2-pixel_python-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=daniljudo2-pixel_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=daniljudo2-pixel_python-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=daniljudo2-pixel_python-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=daniljudo2-pixel_python-project-49)

# 🚀 Brain games (Игры разума)

#### Проект представляет собой пять мини игры для поддержания мозговой активности:

1. «Проверка на чётность»
Суть игры в следующем: пользователю показывается случайное число. 
И ему нужно ответить yes, если число чётное, или no — если нечётное

2. «Калькулятор»
Суть игры в следующем: пользователю показывается случайное математическое выражение, 
например, 35 + 16, которое нужно вычислить и записать правильный ответ.

3. «НОД»
С уть игры в следующем: пользователю показывается два случайных числа, например, 25 50. 
Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.

4. «Арифметическая прогрессия»
Показываем игроку ряд чисел, который образует арифметическую прогрессию, заменив любое из чисел двумя точками. 
Игрок должен определить это число.

5. «Простое ли число?»
Игроку требуется определить, является ли число простым.

#### Минимальные системные требования

Python ≥ 3.12              
`uv`   latest
`make`  любой актуальной версии

#### Установка

Клонируйте репозитори: 
git clone git@github.com:daniljudo2-pixel/python-project-49.git
Установите `uv` (если ещё не установлен): 
https://docs.astral.sh/uv/getting-started/installation/
В корневой папке проекта выполните: 
`uv sync`
Установите `make` (если отсутствует):
**Ubuntu:** `sudo apt install build-essential`
**macOS:** `xcode-select --install`
**Windows:** `choco install make`


#### Запуск игры

Запуск игры осуществялется путем ввода консольных команд в КОРНЕВОЙ папке проекта:
1. make brain-even - «Калькулятор»
2. make brain-calc - «Проверка на чётность»
3. make brain-gcd - «НОД»
4. make brain-progression - «Арифметическая прогрессия»
5. make brain-prime - «Простое ли число?»

#### Возможные ошибки
`make: command not found`- команда для запуска игры введена неверно.
Используйте команды для запуска, описанные в запуске игры.
`brain-calc: command not found `- запуск без 'make'
Используйте команды для запуска, описанные в запуске игры.
`make: *** No rule to make target 'brain-gcd'`- команда запущена не из корневой папки.
Запускайте игры из корневой папки проекта.



#### Геймплей

#### brain-even
[![asciicast](https://asciinema.org/a/QVyUumkUxvewFio0.svg)](https://asciinema.org/a/QVyUumkUxvewFio0)

#### brain-calc
[![asciicast](https://asciinema.org/a/O8vmumJld0LnMRDa.svg)](https://asciinema.org/a/O8vmumJld0LnMRDa)

#### brain-gcd
[![asciicast](https://asciinema.org/a/27K8QhWovB7XBsiO.svg)](https://asciinema.org/a/27K8QhWovB7XBsiO)

#### brain-progression
[![asciicast](https://asciinema.org/a/9MNNPlwHK3RRdJPn.svg)](https://asciinema.org/a/9MNNPlwHK3RRdJPn)

#### brain-prime
[![asciicast](https://asciinema.org/a/cpm6Rfj3AsGPO4yW.svg)](https://asciinema.org/a/cpm6Rfj3AsGPO4yW)