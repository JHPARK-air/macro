from tkinter import *

root = Tk()
root.title("나도 GUI")


btn1= Button(root, text="버튼1")
btn1.pack()


btn2 = Button(root, padx=5, pady=10, text="버튼2") #버튼의 크기
btn2.pack()
#글자수에 따라 유동적이다

btn3 = Button(root, width=10, height=3, text="버튼3")
btn3.pack()
#글자수가 늘어나도 고정임

btn4 = Button(root, fg="red", bg="yellow")
btn4.pack()

# photo = PhotoImage(file=경로)
# btn5 = Button(root, image=photo)
# btn5.pack()

def btncmd():
    print("매수주문이 체결되었습니다.")
btn6 = Button(root, text="동작하는 버튼", command=btncmd)
btn6.pack()
root.mainloop()

