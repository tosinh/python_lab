from HinhChuNhat import HinhChuNhat

class HinhVuong(HinhChuNhat):
    def __init__(self):
        super().__init__(canh)
    
    def Xuat(self):
        print(f"Hình vuông có cạnh {self.canh}")