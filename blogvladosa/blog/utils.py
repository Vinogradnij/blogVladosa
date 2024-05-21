from . import models


class DataMixin:
    paginate_by = 6

    def get_mixin_context(self, context, **kwargs):
        context['categories'] = models.Category.objects.all()
        context.update(kwargs)
        return context
