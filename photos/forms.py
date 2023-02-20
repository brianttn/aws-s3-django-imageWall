from django import forms
from .models import Photo

# = = = = = =   建立可供使用者「上傳圖片」的表單   = = = = = =
class UploadModelForm(forms.ModelForm):
    class Meta:
        model = Photo           # 設定：表單要綁定的modelConstructor名稱
        fields = ('image',)     # 顯示：資料模型(Model)中的「field：image」
        # 使用Django ModelForm提供的「屬性：widgets」來客製化表單的顯示外觀
        widgets = {
            # 套用Bootstrap「檔案輸入表單」的CSS class
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }