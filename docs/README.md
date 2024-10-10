# geometric_lib functions documentation
- --
## circle.py
### area(r)
- Находит площать круга.

        Параметры:
            r (float): Радиус круга.

        Возвращаемое значение:
            area (float): Площадь круга.
        
        Пример вызова:
            circle_area = area(2) #12.566370614359172

### perimeter(r)
- Находит периметр окружности.

        Параметры:
            r (float): Радиус окружности.

        Возвращаемое значение:
            perimeter (float): Периметр окружности.
        
        Пример вызова:
            circle_perimeter = perimeter(3) #18.84955592153876
- --
## rectangle.py
### area(a, b)
- Находит площадь прямоугольника.

            Параметры:
                a (float): Первая сторона прямоугольника.
                b (float): Вторая сторона прямоугольника.

            Возвращаемое значение:
                area (float): Площадь прямоугольника.
            
            Пример вызова:
                rectangle_area = area(2, 3) #6

### perimeter(a, b)
- Находит периметр прямоугольника.

            Параметры:
                a (float): Первая сторона прямоугольника.
                b (float): Вторая сторона прямоугольника.

            Возвращаемое значение:
                perimeter (float): Периметр прямоугольника.
            
            Пример вызова:
                rectangle_perimeter = perieter(2, 3) #12
- --
## triangle.py
### area(a, h)
- Находит площадь треугольника.

            Параметры:
                a (float): Сторона треугольника, к которой преведена высота.
                h (float): Высота треугольника.

            Возвращаемое значение:
                area (float): Площадь треугольника.
            
            Пример вызова:
                triangle_area = area(2, 5) #5
    

### perimeter(a, b, c)
- Находит периметр треугольника.

            Параметры:
               a (float): Первая сторона треугольника.
               b (float): Вторая сторона треугольника.
               c (float): Третья сторона треугольника.

            Возвращаемое значение:
               perimeter (float): Периметр треугольника.

            Пример вызова:
                triangle_perimeter = area(2, 3, 4) #9
- --
## square.py
### area(a)
- Находит площадь квадрата.

            Параметры:
                a (float): Сторона квадрата.

            Возвращаемое значение:
                area (float): Площадь квадрата.

            Пример вызова:
                square_area = area(5) #25

### perimeter(r)
- Находит периметр квадрата.

            Параметры:
                a (float): Сторона квадрата.

            Возвращаемое значение:
                perimeter (float): Периметр квадрата.

            Пример вызова:
                square_perimeter = area(3) #12
- --
## commits hash codes
### commit 5fd6cef19b648b4b0040abb29fbeb41fe660df37
- all code restored after git branch remove.
- made documentations for functions in *.py files.
### commit 65ceaa9296a7f966ab632273ffe8cb7a4bf5972a
- made README.md documentation for *.py geometric lib files in docs directory.
- --
## general solution description
- Переделал все файлы после удаления ветки в первой лабораторной.
- Добавил документацию внутрь кода при помощи комментирования.
- На основе комментариев из кода создал README.md файл с повторной документацией всех функций из файлов.
- Визуально разделил функции по файлам при помощи линий.