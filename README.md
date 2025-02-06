# praktyka2025
Принцип роботи програмного застосунку за темою "Введення та оброблення переліку книг у бібліотеці"
Користувач надсилає HTTP-запити (GET, POST, DELETE) до API.
Обробники маршрутів (@app.get, @app.post, @app.delete) виконують відповідні операції з базою даних через SQLAlchemy.
Всі зміни або дані повертаються як JSON-відповідь.
FastAPI автоматично перевіряє вхідні дані за допомогою Pydantic і повертає повідомлення про помилки у разі невідповідностей.
Приклад внесення книжки до бази даних: https://github.com/AndriyRakoyid/praktyka2025/blob/main/picture.png
Приклад отримання даних про книгу за id номером: https://github.com/AndriyRakoyid/praktyka2025/blob/main/picture%201.png
