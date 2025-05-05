from tkinter import *
from tkinter import filedialog,messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,inch
from PyPDF2 import PdfReader,PdfWriter
import re

root=Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
label=Label(root,text="Bill Management",font=("Gabriola",40,"bold"),bg="black",fg="white",width=100).pack()

#Functions
def Reset():
    print(e1)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    text_area.delete("1.0",END)

def Submit():
    b=0
    total=0
    
    text_area.insert(END,'\t** Welcome Customer **\n')
    text_area.insert(END,f'\nBill Number: {b}\n')
    text_area.insert(END,'\n=============================================')
    text_area.insert(END,'\nPRODUCT\t\tQUANTITY\t\tPRICE')
    text_area.insert(END,'\n=============================================')
    if e1.get()!=0 and e1.get()!='':
        s=int(e1.get())
        p1=s*5
        total=total+p1
        text_area.insert(END,f'\nScale\t\t{e1.get()}\t\t{p1}')
    if e2.get()!=0 and e2.get()!='':
        s1=int(e2.get())
        p2=s1*5
        total=total+p2
        text_area.insert(END,f'\nPencil\t\t{e2.get()}\t\t{p2}')
    if e3.get()!=0 and e3.get()!='':
        s2=int(e3.get())
        p3=s2*10
        total=total+p3
        text_area.insert(END,f'\nMech_Pencil\t\t{e3.get()}\t\t{p3}')
    if e4.get()!=0 and e4.get()!='':
        s3=int(e4.get())
        p4=s3*50
        total=total+p4
        text_area.insert(END,f'\nNoteBook_R\t\t{e4.get()}\t\t{p4}')
    if e5.get()!=0 and e5.get()!='':
        s4=int(e5.get())
        p5=s4*50
        total=total+p5
        text_area.insert(END,f'\nNoteBook_UR\t\t{e5.get()}\t\t{p5}')
    if e6.get()!=0 and e6.get()!='':
        s5=int(e6.get())
        p6=s5*150
        total=total+p6
        text_area.insert(END,f'\nBooks\t\t{e6.get()}\t\t{p6}')
    if e7.get()!=0 and e7.get()!='':
        s6=int(e7.get())
        p7=s6*30
        total=total+p7
        text_area.insert(END,f'\nPen\t\t{e7.get()}\t\t{p7}')
    if e8.get()!=0 and e8.get()!='':
        s7=int(e8.get())
        p8=s7*70
        total=total+p8
        text_area.insert(END,f'\nE_DrawKit\t\t{e8.get()}\t\t{p8}')    
    text_area.insert(END,'\n=============================================')
    text_area.insert(END,f'\n\tTotal Price:\t\t{total}')
    text_area.insert(END,'\n=============================================')
    text_area.insert(END,"\nThank You For Visting,Come Again")

def save():
    file_path = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[("PDF files", "*.pdf")])
    
    if file_path:
        text = text_area.get("1.0", "end-1c")
        lines = [line.strip() for line in text.split("\n") if line.strip()]  

        
        template_path = "bill_temp.pdf"
        output_path = file_path  

        reader = PdfReader(template_path)
        writer = PdfWriter()

       
        overlay_pdf = canvas.Canvas("temp_overlay.pdf", pagesize=letter)
        overlay_pdf.setFont("Courier", 12)

       
        y_position = 9 * inch  

        
        for line in lines:
            if "=" in line:  
                overlay_pdf.drawCentredString(4 * inch, y_position, line) 
            else:
                items = re.split(r'\s+', line)  

                if len(items) == 3:  
                    product = items[0]
                    quantity = items[1]
                    price = items[2]

                    overlay_pdf.drawString(1 * inch, y_position, product.ljust(20))   
                    overlay_pdf.drawString(3.5 * inch, y_position, quantity.center(5))  
                    overlay_pdf.drawString(5.5 * inch, y_position, price.rjust(10))    

            y_position -= 0.3 * inch 
        overlay_pdf.save()  

       
        with open("temp_overlay.pdf", "rb") as text_file:
            text_pdf = PdfReader(text_file)
            for page in range(len(reader.pages)):
                page_obj = reader.pages[page]
                if page == 0:
                    page_obj.merge_page(text_pdf.pages[0])
                writer.add_page(page_obj)

       
        with open(output_path, "wb") as output_file:
            writer.write(output_file)

        messagebox.showinfo("Success", "PDF saved successfully!")

    

#Frame1
frame1=Frame(root,bg="lightgreen",height=900,width=400,relief=RAISED,pady=5).place(x=10,y=110)

label=Label(frame1,text="List of Items",font=("Lucida Calligraphy",15,"bold"),fg="Black",bg="lightgreen").place(x=100,y=130)

scale=Label(frame1,text="Scale.....Rs.5/Piece",font=("Lucida Calligraphy",15,"bold"),fg="Black",bg="lightgreen").place(x=50,y=180)
pencil=Label(frame1,text="Pencil.....Rs.5/Piece",font=("Lucida Calligraphy",15,"bold"),fg="Black",bg="lightgreen").place(x=50,y=230)
mech_p=Label(frame1,text="Mech Pencil(0.7)....Rs.10/Piece",font=("Lucida Calligraphy",15,"bold"),fg="Black",bg="lightgreen").place(x=50,y=280)
notebooks_r=Label(frame1,text="NoteBook_R....Rs.50/Piece",font=("Lucida Calligraphy",15,"bold"),fg="Black",bg="lightgreen").place(x=50,y=330)
notebooks_ur=Label(frame1,text="NoteBook_UR....Rs.50/Piece",font=("Lucida Calligraphy",15,"bold"),fg="Black",bg="lightgreen").place(x=50,y=380)
books=Label(frame1,text="Book....Rs.150/Piece",font=("Lucida Calligraphy",15,"bold"),fg="Black",bg="lightgreen").place(x=50,y=430)
pen=Label(frame1,text="Pen....Rs.30/Piece",font=("Lucida Calligraphy",15,"bold"),fg="Black",bg="lightgreen").place(x=50,y=480)
e_draw=Label(frame1,text="E_DrawKit....Rs.70/Piece",font=("Lucida Calligraphy",15,"bold"),fg="Black",bg="lightgreen").place(x=50,y=530)


#Frame2
frame2=Frame(root,bg="lightblue",height=900,width=500,relief=RAISED,padx=5).place(x=420,y=110)
label2=Label(frame2,text="Quantity",font=("Aria",15,"bold"),fg="Black",bg="lightblue").place(x=500,y=130)

#sideLabels
lbl_s=Label(frame2,text="Scale",font=("Aria",15,"bold"),fg="Black",bg="lightblue").place(x=450,y=180)
lbl_p=Label(frame2,text="Pencil",font=("Aria",15,"bold"),fg="Black",bg="lightblue").place(x=450,y=230)
lbl_mp=Label(frame2,text="Mech Pencil",font=("Aria",15,"bold"),fg="Black",bg="lightblue").place(x=450,y=280)
lbl_nr=Label(frame2,text="NoteBook_R",font=("Aria",15,"bold"),fg="Black",bg="lightblue").place(x=450,y=330)
lbl_nr=Label(frame2,text="NoteBook_UR",font=("Aria",15,"bold"),fg="Black",bg="lightblue").place(x=450,y=380)
lbl_nr=Label(frame2,text="Books",font=("Aria",15,"bold"),fg="Black",bg="lightblue").place(x=450,y=430)
lbl_nr=Label(frame2,text="Pen",font=("Aria",15,"bold"),fg="Black",bg="lightblue").place(x=450,y=480)
lbl_nr=Label(frame2,text="E_DrawKit",font=("Aria",15,"bold"),fg="Black",bg="lightblue").place(x=450,y=530)

#variables

a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
e=StringVar()
f=StringVar()
g=StringVar()
h=StringVar()

#sideentry
e1=Entry(frame2,bd=6)
e1.place(x=600,y=180)
e2=Entry(frame2,bd=6)
e2.place(x=600,y=230)
e3=Entry(frame2,bd=6)
e3.place(x=600,y=280)
e4=Entry(frame2,bd=6)
e4.place(x=600,y=330)
e5=Entry(frame2,bd=6)
e5.place(x=600,y=380)
e6=Entry(frame2,bd=6)
e6.place(x=600,y=430)
e7=Entry(frame2,bd=6)
e7.place(x=600,y=480)
e8=Entry(frame2,bd=6)
e8.place(x=600,y=530)

#Buttons
reset=Button(frame2,text="Reset",font=("Bold",15),bg="blue",fg="black",padx=10,command=Reset).place(x=450,y=580)
submit=Button(frame2,text="Submit",font=("Bold",15),bg="blue",fg="black",padx=10,command=Submit).place(x=600,y=580)

#Frame3
frame3=Frame(root,bg="white",height=900,width=425,relief=RAISED,bd=5).place(x=930,y=110)

label3=Label(frame3,text="Bill",bg="white",font=("Bold",20,"bold"),relief=RAISED,bd=3,width=20).place(x=950,y=130)
text_area=Text(frame3,width=45,height=30,bd=3,bg="white")
text_area.place(x=950,y=180)


button=Button(frame3,text="Save As Pdf",font=("Bold",15),bg="blue",fg="black",padx=10,command=save).place(x=1050,y=600)

bill=Text(frame3,bd=4)

root.mainloop()
