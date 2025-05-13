from django.urls import path

from notification.views import user_notifications, mark_as_read

app_name = 'notification'

urlpatterns = [
    path('', user_notifications, name='user_notifications'),
    path('read/<int:notification_id>/', mark_as_read, name='mark_as_read'),
]