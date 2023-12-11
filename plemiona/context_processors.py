

def unread_notifications_count(request):
    from .models import Notification
    if request.user.is_authenticated:
        notification = Notification.objects.filter(user=request.user, is_read=False)
        print(notification)
        count = Notification.objects.filter(user=request.user, is_read=False).count()
        return {'unread_notifications_count': count}
    else:
        return {}