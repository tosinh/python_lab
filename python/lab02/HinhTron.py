from HinhHoc import HinhHoc

class HinhTron(HinhHoc):
    def __init__(self):
        super().__init__(canh)

    def TinhDienTich(self):
        return 3.14 * (self.canh ** 2)

    def Xuat(self):
        return f"Hình tròn có bán kính {self.canh} có diện tích là : {self.TinhDienTich}"

    @property
    def banKinh(self):
        return self.canh

    