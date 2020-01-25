from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Tag
from main.models import Logo

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, pk):
        logo = Logo.objects.latest('pk')
        obj = get_object_or_404(self.model, pk=pk)
        tags = Tag.objects.all()
        return render(request, self.template, context={self.model.__name__.lower():obj,
                                                       'object': obj,
                                                       'tags': tags,
                                                       'logo': logo,
                                                       })
