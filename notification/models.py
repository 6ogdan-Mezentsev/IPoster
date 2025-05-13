from django.db import models
from users.models import CustomUser


class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_notifications')
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender_notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Уведомление от {self.sender.username} для {self.recipient.username}: {self.message}"
