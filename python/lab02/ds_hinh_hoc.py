from HinhHoc import HinhHoc
from HinhTron import HinhTron
from HinhChuNhat import HinhChuNhat
from HinhVuong import HinhVuong
from LoaiHinh import LoaiHinh


class DanhSachHinhHoc:
    def __init__(self):
        self.danh_sach_hinh_hoc = []

    def themHinh(self, hinh: HinhHoc):
        self.danh_sach_hinh_hoc.append(hinh)

    def xuat(self):
        for hinh in self.danh_sach_hinh_hoc:
            hinh.xuat()
        
    def timHinhCoDienTichLonNhat(self):
        dienTichLonNhat = 0
        hinhLonNhat = None
        for hinh in self.danh_sach_hinh_hoc:
            dien_tich = hinh.TinhDienTich()
            if dien_tich > dienTichLonNhat:
                dienTichLonNhat = dien_tich
                hinhLonNhat = hinh
        return hinhLonNhat

    def TimHinhCoDienTichNhoNhat(self):
        dienTichNhoNhat = 0
        hinhNhoNhat = None
        for hinh in self.danh_sach_hinh_hoc:
            dien_tich = hinh.TinhDienTich()
            if dien_tich < dienTichNhoNhat:
                dienTichNhoNhat = dien_tich
                hinhNhoNhat = hinh
        return hinhNhoNhat

    def TimHinhTronNhoNhat(self , lh : LoaiHinh):
        hinhtronnhonhat = None
        for hinh in self.danhsach:
        if hinh.loaihinh == lh:
            if hinhtronnhonhat is None or hinh.r < hinhtronnhonhat.r:
            hinhtronnhonhat = hinh
        return hinhtronnhonhat

    def SapGiamTheoDienTich(self):
        self.danh_sach_hinh_hoc.sort(key=lambda hinh: hinh.dientich, reverse=True)

    def DemSoLuongHinh(self, lh : LoaiHinh):
        count = 0
        for hinh in self.danh_sach_hinh_hoc:
        if hinh.lh == lh:
            count += 1
        return count

    def TinhTongDienTich(self):
        tong_dien_tich = 0
        for hinh in self.danh_sach_hinh_hoc:
            tong_dien_tich += hinh.TinhDienTich()
        return tong_dien_tich