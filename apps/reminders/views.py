from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from .serializers import ReminderSerializer, AlertSerializer
from .models import Reminder, AlertMethod

from apps.users.models import User

# Create your views here.

class AlertView(ListAPIView):

    serializer_class = AlertSerializer
    queryset = AlertMethod.objects.all()

    def get(self, request, *args, **kwargs):
        print ('here')
        try:
            response = super(AlertView, self).get(request, *args, **kwargs)
        except Exception as ex:
            print (ex)
        print (response)
        return response


    """
    def get(self, request):
        res_list = []

        for each in AlertMethod.objects.all():

            serializer = self.serializer_class(data=each)

            try:
                if serializer.is_valid():
                    res_list.append(serializer.data)
                else:
                    print (serializer.error)
            except Exception as ex:
                print (ex)

        print (res_list)
        result = {
            "results": res_list
        }
        return Response(result)
    """


class ReminderView(APIView):

    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()

    def get_user(self, **kwargs):
        email = kwargs.get('email')
        mobile_no = kwargs.get('mobile_no')

        user_count = User.objects.filter(email=email, mobile_no=mobile_no).count()
        if user_count:
            return User.objects.get(email=email, mobile_no=mobile_no)
        else:
            new_user = User.object.create(**self.kwargs)
            new_user.save()
            return new_user

    def get(self, request):
        user = self.get_user(**request.GET)
        result = Reminder.objects.get(user=user)

        serializer = self.serializer_class(result, many=True)

        return Response(serializer.data)

    def post(self, request):
        user = self.get_user(**request.data)

        request.data.update({'user': user.pk})

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=HTTP_201_CREATED)

    def delete(self, request):
        user = self.get_user(**request.data)

        request.data.update({'user': user.pk})

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.delete()
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        return Response(serializer.data)