

import tkinter.ttk as ttk
from tkinter import *
import tkinter.messagebox as msgbox
import pyautogui

root = Tk()
root.title("StockMarket")

w=300
h=450

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x") #가로로 쭉 벌어진다



#1층
first_floor=Frame(root, relief="groove", borderwidth="3")
first_floor.pack(fill="x")


#1층_종목명 콤보
opt_width = ["삼성전자", "NAVER", "SK하이닉스", "녹십자홀딩스"]
cmb_width = ttk.Combobox(first_floor, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left")

#1층_검색버튼
image=PhotoImage(file="C:\\Users\\papas\\Desktop\\StockMarket\\search.png")
btn_search=Button(first_floor, image=image, width=15, height=15)
btn_search.pack(side="left")

#1층_현재가
lbl_width = Label(first_floor, text="85000", fg="red", width=8)
lbl_width.pack(side="left")


#2층
second_floor = Frame(root, relief="groove", borderwidth="3")
second_floor.pack(fill="x")

#2층_미체결 거래량
sell_amount = Frame(second_floor)
sell_amount.pack(side="left")

lbl_unsell_1=Label(sell_amount, text="400", width=10)
lbl_unsell_1.pack()
lbl_unsell_2=Label(sell_amount, text="1245", width=10)
lbl_unsell_2.pack()
lbl_unsell_3=Label(sell_amount, text="3462", width=10)
lbl_unsell_3.pack()
lbl_unsell_4=Label(sell_amount, text="1242", width=10)
lbl_unsell_4.pack()
lbl_unsell_5=Label(sell_amount, text="1353", width=10)
lbl_unsell_5.pack()
lbl_unsell_6=Label(sell_amount, text="21313", width=10)
lbl_unsell_6.pack()

#2층_호가창
sell_price = Frame(second_floor)
sell_price.pack(side="left")


for i in range(0,6):
    lbl_sell_price_i=Button(sell_price, text=84500-500*i, fg="blue", width=10)
    lbl_sell_price_i.pack()

#2층_정보
stock_info = Frame(second_floor)
stock_info.pack(side="left")

lbl_sotck_info_1=Label(stock_info, text="예상가격", width=15)
lbl_sotck_info_1.pack()
lbl_sotck_info_2=Label(stock_info, text="예상체결량",  width=10)
lbl_sotck_info_2.pack()
lbl_sotck_info_3=Label(stock_info, text="전일거래량" ,width=10)
lbl_sotck_info_3.pack()
lbl_sotck_info_4=Label(stock_info, text="거래량" , width=10)
lbl_sotck_info_4.pack()
lbl_sotck_info_5=Label(stock_info, text="기준가" , width=10)
lbl_sotck_info_5.pack()
lbl_sotck_info_6=Label(stock_info, text="시가"  ,width=10)
lbl_sotck_info_6.pack()

#3층
third_floor = Frame(root, relief="groove", borderwidth="3")
third_floor.pack(fill="x")

#3층_정보
stock_today_info = Frame(third_floor)
stock_today_info.pack(side="left")

lbl_sotck_info_1=Label(stock_info, text="예상가격", width=15)
lbl_sotck_info_1.pack()
lbl_sotck_info_2=Label(stock_today_info, text="예상체결량",  width=10)
lbl_sotck_info_2.pack()
lbl_sotck_info_3=Label(stock_today_info, text="전일거래량" ,width=10)
lbl_sotck_info_3.pack()
lbl_sotck_info_4=Label(stock_today_info, text="거래량" , width=10)
lbl_sotck_info_4.pack()
lbl_sotck_info_5=Label(stock_today_info, text="기준가" , width=10)
lbl_sotck_info_5.pack()
lbl_sotck_info_6=Label(stock_today_info, text="시가"  ,width=10)
lbl_sotck_info_6.pack()

#3층_호가창
buy_price = Frame(third_floor)
buy_price.pack(side="left")


for i in range(0,6):
    lbl_buy_price_i=Button(buy_price, text=84500-500*i, fg="red", width=10)
    lbl_buy_price_i.pack()


#3층_미체결 거래창
buy_amount = Frame(third_floor)
buy_amount.pack(side="left")

lbl_unsell_1=Label(buy_amount, text="12454", width=10)
lbl_unsell_1.pack()
lbl_unsell_2=Label(buy_amount, text="12445", width=10)
lbl_unsell_2.pack()
lbl_unsell_3=Label(buy_amount, text="34162", width=10)
lbl_unsell_3.pack()
lbl_unsell_4=Label(buy_amount, text="1242", width=10)
lbl_unsell_4.pack()
lbl_unsell_5=Label(buy_amount, text="1353", width=10)
lbl_unsell_5.pack()
lbl_unsell_6=Label(buy_amount, text="21313", width=10)
lbl_unsell_6.pack()

#4층
fourth_floor = Frame(root, relief="groove", borderwidth="3")
fourth_floor.pack(fill="x")

#4층_주문내역 entry

order_stock_lbl = Label(fourth_floor, text="가격")
order_stock_lbl.grid(row=0, column=0)
order_stock = Entry(fourth_floor, width=20)
order_stock.grid(row=0, column=1)

amount_stock_lbl = Label(fourth_floor, text="수량")
amount_stock_lbl.grid(row=1, column=0)
amount_stock = Entry(fourth_floor, width=20)
amount_stock.grid(row=1, column=1)

def buy():
    msgbox.showinfo("매수주문","매수주문이 체결되었습니다. 체결가 : ??, 체결량 : ??")

def sell():
    msgbox.showinfo("매도주문","매도주문이 체결되었습니다. 체결가 : ??, 체결량 : ??")
stock_buy=Button(fourth_floor, text="매수", fg="red", width=5, height=3, command=buy)
stock_buy.grid(row=0, column=2, rowspan=2)

stock_sell=Button(fourth_floor, text="매도", fg="blue", width=5 , height=3, command=sell)
stock_sell.grid(row=0, column=3, rowspan=2)



#4층 button
root.resizable(False, False) #윈도우 크기 고정
#991, 713
pyautogui.moveTo(1000,731,2)
root.mainloop()
pyautogui.click()

#추가할 것
# 1층에서 정보 넣기
# 전체적인 줄간격 맞추기
# 콤보박스에서 선택하고 검색 누르면 다른 종목으로 바꾸기
# 버튼 누르면 매수, 매도주문 할 수 있게 하기 Command
# 3층에서 거래량표로 바꾸기
# 거래량 표 예쁘게 바꾸기
# 반복문으로 어떻게 처리하는지 알기
#
