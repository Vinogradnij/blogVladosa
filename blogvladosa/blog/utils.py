from . import models


class DataMixin:
    def get_mixin_context(self, context, **kwargs):
        context['categories'] = models.Category.objects.all()
        context.update(kwargs)
        return context
