from kivy.app import App
from kivy.uix.screenmanager import ScreenManager , Screen

class Scr_knowledge(Screen): #หน้าจอที่ 1
    pass

class Scr_bmi(Screen): #หน้าจอที่ 2
    def cal_bmi(self):
    #ค่า bmi= น้ำหนัก กก. / (ส่วนสูง เมตร x ส่วนสูง เมตร)
        weight=float(self.ids.txt_weight.text)
        height=int(self.ids.txt_height.text)
        height= height/100
        bmi = weight/(height*height)
        self.ids.lbl_bmi.text= str(bmi)
        if bmi > 35:
            self.ids.lbl_bmi.color="#FF0000" #แดง
            self.ids.img_bmi.source="pic/5.PNG"
        elif bmi > 30:
            self.ids.lbl_bmi.color="#FF3300"# ส้ม
            self.ids.img_bmi.source="pic/4.PNG"
        elif bmi > 25:
            self.ids.lbl_bmi.color="#FFFF00" #เหลือง
            self.ids.img_bmi.source="pic/3.PNG"
        elif bmi > 18:
            self.ids.lbl_bmi.color="##33FF00" #เขียว
            self.ids.img_bmi.source="pic/2.PNG"
        else: 
            self.ids.lbl_bmi.color="#00FFFF" #ฟ้า
            self.ids.img_bmi.source="pic/1.PNG" 

class UI(ScreenManager): 
    pass

class bmiApp(App):
    def build(self):
        return UI()
     
if __name__=="__main__":
    bmiApp().run()