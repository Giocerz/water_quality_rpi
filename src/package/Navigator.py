class Navigator:
    @staticmethod
    def push(context, view):
        context.addWidget(view)
        context.setCurrentIndex(context.currentIndex() + 1)
    
    @staticmethod
    def pop(context, view):
        context.removeWidget(view)