from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # first image
        img=Image.open("C:/face recognition attendence system/images/3025CDA7-1DB4-4909-AEBF-E13BC58EA9D8.jpeg")
        img=img.resize((800,200), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        # second image
        img1=Image.open("C:/face recognition attendence system/images/stock-photo-group-of-beautiful-students-studying-in-the-classroom-interior-415138456.jpg")
        img1=img1.resize((800,200), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        # bg image
        img3=Image.open("C:/face recognition attendence system/images/hand-touching-ui-unlocking-face-260nw-1390273304.webp")
        img3=img3.resize((1530,710), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDENCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student Attendence Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open("C:/face recognition attendence system/images/26.jpg")
        img_left=img_left.resize((700,130), Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        #label and entry
        # attendenceid
        Attendence_label=Label(left_inside_frame,text="AttendenceId:",font=("times new roman",13,"bold"),bg="white")
        Attendence_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        AttendenceID_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
        AttendenceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Name
        rollLabel=Label(left_inside_frame,text="Roll:",bg="white",font="comicsansns 11 bold")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,pady=8)

        # date
        nameLabel=Label(left_inside_frame,text="Name:",bg="white",font="comicsansns 11 bold")
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1,pady=8)

        # Department
        depLabel=Label(left_inside_frame,text="Department:",bg="white",font="comicsansns 11 bold")
        depLabel.grid(row=1,column=2)

        atten_Department=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_Department.grid(row=1,column=3,pady=8)

        # time
        timeLabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)

        # date
        dateLabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=8)

        # attendence
        AttendenceLabel=Label(left_inside_frame,text="Attendence status:",bg="white",font="comicsansns 11 bold")
        AttendenceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("status","present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        save_btn=Button(btn_frame,text="Import csv",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export csv",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        # Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=445)

        # =====Scrollbar table=============
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.atttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.atttendenceReportTable.xview)
        scroll_y.config(command=self.atttendenceReportTable.yview)

        self.atttendenceReportTable.heading("id",text="Attendence ID")
        self.atttendenceReportTable.heading("roll",text="Roll")
        self.atttendenceReportTable.heading("name",text="Name")
        self.atttendenceReportTable.heading("department",text="department")
        self.atttendenceReportTable.heading("time",text="Time")
        self.atttendenceReportTable.heading("date",text="Date")
        self.atttendenceReportTable.heading("attendence",text="Attendence")
        
        self.atttendenceReportTable["show"]="headings"

        self.atttendenceReportTable.column("id",width=100)
        self.atttendenceReportTable.column("roll",width=100)
        self.atttendenceReportTable.column("name",width=100)
        self.atttendenceReportTable.column("department",width=100)
        self.atttendenceReportTable.column("time",width=100)
        self.atttendenceReportTable.column("date",width=100)
        self.atttendenceReportTable.column("attendence",width=100)

        self.atttendenceReportTable.pack(fill=BOTH,expand=1)






if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()