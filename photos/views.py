from django.shortcuts import render, redirect
from .models import Photo
from .forms import UploadModelForm

# = = = = = = = = = = = =   Create views here   = = = = = = = = = = = =
def index(request):
    photos = Photo.objects.all()    # 查詢所有資料
    form = UploadModelForm()        # 建立：上傳圖片的表單物件

    if request.method == "POST":
        # - - -   利用「儲存於request.POST的提交數據」，覆蓋「原來request.FILES裡的資料」   - - -
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/photos')

    context = {'photos': photos, 'form': form}              # 將「表單物件」傳送至template進行顯示
    return render(request, 'photos/index.html', context)    # 將「儲存的圖片」顯示在「首頁」