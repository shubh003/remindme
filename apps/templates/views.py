from rest_framework.generics import ListAPIView

from .serializers import TemplateSerializer
from .models import Template


# Create your views here.
class TemplateView(ListAPIView):

    serializer_class = TemplateSerializer
    queryset = Template.objects.all()