# todo_app

## System design

One of the main considerations from the outset of the project was the ownership of tkinters root. The MainController class
will handle the root and utility classes will be implemented to keep additional view items modular, such as a "message box".

The MVC pattern was adopted to avoid passing root around, as early designs where getting unnecessarily complex.

We are passing dependencies explicitly, such as the controller into the view to avoid components creating their own dependencies.
