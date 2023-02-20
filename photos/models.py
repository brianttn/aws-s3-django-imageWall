from django.db import models
from django.utils import timezone

# = = = = = = = = = = = =   Create models   = = = = = = = = = = = =
class Photo(models.Model):
    '''
    使用者將圖片上傳後，會將圖片存放在 => 「檔案：models.py」中「method：ImageField()」的「參數：upload_to」所指定的「Model：欄位(ImageField)」中。
    '''
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    # Write the current time in the local time zone when adding an image to the database
    upload_date = models.DateField(default=timezone.now)