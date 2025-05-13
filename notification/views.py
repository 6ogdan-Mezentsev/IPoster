from django.shortcuts import render, redirect, get_object_or_404

from notification.models import Notification


def user_notifications(request):
    notification_list = Notification.objects.filter(recipient=request.user)
    return render(request, 'notification/notification_list.html', {'notification_list': notification_list})


def mark_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, recipient=request.user)
    if not notification.is_read:
        notification.is_read = True
        notification.save()
    else:
        notification.is_read = False
        notification.save()
    previous_page = request.META.get('HTTP_REFERER', '/')
    return redirect(previous_page)
