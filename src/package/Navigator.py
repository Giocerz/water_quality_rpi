class Navigator:
    @staticmethod
    def push(context, view):
        """
        Agrega una nueva vista (widget) a la pila de navegación y la muestra.

        :param context: El QStackedWidget que actúa como contenedor de las vistas.
        :param view: El widget (vista) que se desea agregar y mostrar.
        """
        context.addWidget(view)
        context.setCurrentIndex(context.currentIndex() + 1)

    @staticmethod
    def pop(context, view):
        """
        Elimina una vista (widget) de la pila de navegación y la destruye.

        :param context: El QStackedWidget que actúa como contenedor de las vistas.
        :param view: El widget (vista) que se desea eliminar.
        """
        context.removeWidget(view)
        view.deleteLater()  # Libera los recursos de la vista eliminada

    @staticmethod
    def pushReplacement(context, view):
        """
        Reemplaza la vista actual con una nueva vista.

        :param context: El QStackedWidget que actúa como contenedor de las vistas.
        :param view: El widget (vista) que reemplazará a la vista actual.
        """
        current_widget = context.currentWidget()
        context.addWidget(view)
        context.setCurrentIndex(context.count() - 1)
        context.removeWidget(current_widget)
        current_widget.deleteLater()  # Libera los recursos de la vista eliminada