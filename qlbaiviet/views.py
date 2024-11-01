from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import BaiVietForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
  return render(request, 'index.html')

def xembaiviet(request, idbaiviet):
  bai_viet = get_object_or_404(BaiViet, id=idbaiviet)
  return render(request, 'xembaiviet.html', {'baiviet': bai_viet})

def dsbaiviet(request, idchuyenmuc):
  chuyen_muc = get_object_or_404(ChuyenMuc, id=idchuyenmuc)
  bai_viets = BaiVietChuyenMuc.objects.filter(chuyen_muc=chuyen_muc)
  title = f'DANH SÁCH BÀI VIẾT - CHUYÊN MỤC: {chuyen_muc.ten.upper()}'
  return render(request, 'dsbaiviet.html', {'baiviets': bai_viets, 'title': title})

def suabaiviet(request, idbaiviet=None):
  if idbaiviet:
    bai_viet = get_object_or_404(BaiViet, id=idbaiviet)
    title = 'SỬA BÀI VIẾT'
    button = 'Sửa'
  else:
    bai_viet = None
    title = 'TẠO BÀI VIẾT'
    button = 'Tạo'
  form = BaiVietForm(instance=bai_viet)
  if request.POST:
    form = BaiVietForm(request.POST, instance=bai_viet)
    if form.is_valid():
      bai_viet_update = form.save(False)
      if not bai_viet:
        bai_viet_update.nguoi_tao = User.objects.get(username='caotienhai')
      bai_viet_update.save()
      if bai_viet:
        messages.success(request, f'Chỉnh sửa bài viết {bai_viet_update.tieu_de} thành công')
      else:
        messages.success(request, f'Tạo mới bài viết {bai_viet_update.tieu_de} thành công')
      return redirect('xembaiviet', bai_viet_update.id)
  return render(request, 'suabaiviet.html', {'title': title, 'form': form, 'baiviet': bai_viet, 'button': button})