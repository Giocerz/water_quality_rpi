class Navigator:
    @staticmethod
    def push(context, view):
        context.addWidget(view)
        context.setCurrentIndex(context.currentIndex() + 1)
    
    @staticmethod
    def pop(context, view):
        context.removeWidget(view)

    @staticmethod
    def pushReplacement(context, view):
        current_widget = context.currentWidget()
        context.addWidget(view)
        context.setCurrentIndex(context.count() - 1)
        context.removeWidget(current_widget) 