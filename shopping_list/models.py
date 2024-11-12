from django.db import models
from simple_history.models import HistoricalRecords
from base.models import BaseModel
from users.models import User

# Create your models here.

class Shopping(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_shoppings")
    name = models.CharField(max_length=255)
    shared_with = models.ManyToManyField(User, related_name="shared_shoppings", blank=True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
    class Meta:
        
        verbose_name = 'Lista de compra'
        verbose_name_plural = 'Listas de compras'
    
    def __str__(self):
        return self.name
