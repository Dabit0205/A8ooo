from django.db import models
from users.models import User,commonModel

# Create your models here.
class Articles(commonModel):
    class Meta:
        db_table = "Article"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("글제목", max_length=45)
    content = models.TextField("글내용")
    image = models.FileField(
        "이미지", upload_to='', blank=True, null=True) 
    
    def __str__(self):
        return str(self.title)
