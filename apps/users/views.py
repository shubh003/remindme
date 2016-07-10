from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from .serializers import UserSerializer
from .models import User

# Create your views here.

class UserView(APIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request):
        params = request.GET
        email = params.get('email')
        mobile_no = params.get('mobile_no')

        result = self.queryset.get(email=email, mobile_no=mobile_no)
        serializer = self.serializer_class(result)

        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=HTTP_201_CREATED)