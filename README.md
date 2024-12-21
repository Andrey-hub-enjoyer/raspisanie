В коде используются следующие паттерны проектирования:
Наблюдатель (Observer):
ScheduleNotifier — наблюдаемый объект, уведомляет подписчиков (Student) о событиях через метод notify_observers.

Фабрика (Factory):
Factory предоставляет методы для создания объектов Student и Teacher, упрощая их создание.

Шаблонный метод (Template Method):
Базовый класс Observer задает структуру метода update, реализуемого в подклассах (Student).

Полиморфизм:
Разные реализации методов в классах Student и Teacher, унаследованных от Person.

![Иллюстрация к проекту](https://github.com/Andrey-hub-enjoyer/raspisanie/blob/main/uml.png)
