# Different Design patterns in Software Architecture Implementation using Python

Certainly! Here's a list of various design patterns used in software development:

### Creational Design Patterns:
1. **Singleton Pattern:** Ensures a class has only one instance and provides a global point of access to it. Here is an example of a Ticket Dispensing Machine designed with a Singleton Design Pattern.

![Screenshot 2023-12-20 at 9 39 42 PM](https://github.com/manojbusam/DesignPatterns/assets/44409170/f4e9f89d-6dfd-468d-b137-cdca8ba0e018)

2. **Factory Method Pattern:** Defines an interface for creating an object but lets subclasses decide which class to instantiate. Here is an example of ICeCream Vending MAchine built using the Factory Method Design Pattern.

![Screenshot 2023-12-20 at 10 21 49 PM](https://github.com/manojbusam/DesignPatterns/assets/44409170/818cd720-817c-4883-aa24-98f0cacb1a97)

3. **Abstract Factory Pattern:** Provides an interface to create families of related or dependent objects without specifying their concrete classes.
4. **Builder Pattern:** Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
5. **Prototype Pattern:** Creates new objects by copying an existing object, known as the prototype, through cloning.

### Structural Design Patterns:
1. **Adapter Pattern:** Allows incompatible interfaces to work together by wrapping an interface around an existing class.
2. **Bridge Pattern:** Decouples an abstraction from its implementation so that the two can vary independently.
3. **Composite Pattern:** Composes objects into tree structures to represent part-whole hierarchies.
4. **Decorator Pattern:** Attaches additional responsibilities to objects dynamically, providing a flexible alternative to subclassing for extending functionality.
5. **Facade Pattern:** Provides a unified interface to a set of interfaces in a subsystem, simplifying its usage.

### Behavioral Design Patterns:
1. **Observer Pattern:** Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
2. **Strategy Pattern:** Defines a family of algorithms, encapsulates each one, and makes them interchangeable. Clients can switch algorithms at runtime.
3. **Command Pattern:** Encapsulates a request as an object, thereby allowing parameterization of clients with queues, requests, and operations.
4. **Chain of Responsibility Pattern:** Passes a request along a chain of handlers, each of which decides whether to process the request or pass it to the next handler in the chain.
5. **Template Method Pattern:** Defines the skeleton of an algorithm in a method, deferring some steps to subclasses.

### Other Patterns:
1. **MVC (Model-View-Controller) Pattern:** Separates an application into three interconnected components to separate internal representations of information from the ways that information is presented to and accepted from the user.
2. **DAO (Data Access Object) Pattern:** Provides an abstract interface to some type of database or other persistence mechanism, separating the application's business logic from the data access logic.

These design patterns provide established solutions to common problems encountered in software development, aiding in creating more maintainable, scalable, and flexible software systems.
