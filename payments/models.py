from django.db import models

class Payment(models.Model):
    razorpay_order_id = models.CharField(max_length=100)
    razorpay_payment_id = models.CharField(max_length=100, null=True, blank=True)
    razorpay_signature = models.TextField(null=True, blank=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=50, default="created")  # created, paid, failed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.razorpay_order_id} - {self.status}"
