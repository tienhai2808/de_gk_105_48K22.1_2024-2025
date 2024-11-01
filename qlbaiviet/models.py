from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChuyenMuc(models.Model):
  ten = models.CharField(max_length=200)
  
  
class BaiViet(models.Model):
  tieu_de = models.CharField(max_length=250)
  noi_dung = models.TextField(blank=True, null=True)
  ngay_tao = models.DateField()
  nguoi_tao = models.ForeignKey(User, on_delete=models.CASCADE)
  chuyen_muc = models.ManyToManyField(ChuyenMuc, through='BaiVietChuyenMuc')
  

class BaiVietChuyenMuc(models.Model):
  bai_viet = models.ForeignKey(BaiViet, on_delete=models.CASCADE)
  chuyen_muc = models.ForeignKey(ChuyenMuc, on_delete=models.CASCADE)
  thu_tu = models.IntegerField()
  