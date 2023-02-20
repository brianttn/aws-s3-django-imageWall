from django.contrib import admin
from .models import Photo

# = = = = = =   建立繼承自「類別：ModelAdmin」的「類別：PhotoAdmin」   = = = = = =
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'upload_date')       # 顯示：id、image、upload_date欄位
    list_filter = ('id', 'upload_date')                 # 使用id、upload_date欄位進行過濾
    search_fields = ('id',)                             # 使用id欄位進行搜尋
    ordering = ('upload_date',)                         # Ascending order
    # ordering = ('-upload_date',)                      # Descending order

# 註冊「modelConstructor：Photo」至Administration(管理員後台)
admin.site.register(Photo, PhotoAdmin)