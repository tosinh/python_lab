from HinhHoc import HinhHoc

class HinhChuNhat(HinhHoc):
    def __init__(self, rong: float):
        super().__init__(canh)
        self._rong = rong

    def TinhDienTich(self):
        return self.canh * self.rong
    
    def Xuat(self):
        print(f"Hình chữ nhật có chiều dài {self.canh} và chiều rộng {self.rong} có diện tích là {TinhDienTich}")

    @property
    def chieuDai(self):
        return self.canh
    def chieuRong(self):
        return self.rong