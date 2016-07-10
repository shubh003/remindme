from rest_framework import serializers

from .models import Reminder, AlertMethod

class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = ('id', 'user', 'alert_at', 'message', 'method')

class AlertSerializer(serializers.ModelSerializer):

    #name = serializers.CharField(max_length=8)

    class Meta:
        model = AlertMethod
        fields = ('id', 'type')

    """
    def get_name(self, obj):
        for tp, name in AlertMethod.TYPE_CHOICES:
            if tp == obj.type:
                return name
    """