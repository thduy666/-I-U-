# Thuật toán WSPT
def thuat_toan_WSPT(n,pj,wj):
    ThuTu = [i for i in range(1,n+1)]
    List1 = [pj[i]/wj[i] for i in range(n)]
    List2 = ThuTu.copy()
    List1, List2 = zip(*sorted(zip(List1, List2)))  
    ThuTu = List2
    Cj = 0
    Min_C = 0
    for i in ThuTu:
        Cj+= pj[i-1]
        Min_C += Cj*wj[i-1]
    BoSo = ThuTu
    return BoSo,Min_C

# Thuật toán SPT
def thuat_toan_SPT(n,pj):
    ThuTu = [i for i in range(1,n+1)]
    List1 = pj.copy()
    List2 = ThuTu.copy()
    List1, List2 = zip(*sorted(zip(List1, List2)))   
    ThuTu = List2
    Cj = 0
    Min_C = 0
    for i in ThuTu:
        Cj+= pj[i-1]
        Min_C += Cj
    BoSo = ThuTu
    return BoSo,Min_C

# Thuật toán ERD
def thuat_toan_ERD(n,pj,dj):
    ThuTu = [i for i in range(1,n+1)]
    Cj = 0
    ThoiGianKetThuc = []
    ThoiGianTreHan = []
    Min_C = 0
    for i in range(len(pj)):
        Cj += pj[i]
        Delay = Cj -dj[i]
        ThoiGianKetThuc.append(Cj)
        Min_C += Cj
        if Delay <=0:
            ThoiGianTreHan.append(0)
        else:
            ThoiGianTreHan.append(Delay)
    BoSo = ThuTu
    print(ThoiGianKetThuc)
    print(ThoiGianTreHan)
    print("Tổng thời gian các công việc: {}".format(sum(ThoiGianKetThuc)))
    print("Tổng thời gian hoàn thành công việc trung bình {}".format(sum(ThoiGianKetThuc)/len(pj)))
    print("Độ hữu dụng {}% ".format(round(sum(pj)/sum(ThoiGianKetThuc)*100),4))
    print("Số lượng công việc trung bình {} ".format(sum(ThoiGianKetThuc)/sum(pj)))
    print("Độ trễ trung bình {}".format(sum(ThoiGianTreHan)/len(pj)))

    def vetkERD(n,pj,dj):
        Cj = 0
        ThoiGianKetThuc = []
        ThoiGianTreHan = []
        for i in range(n):
            Cj += pj[i]
            Delay = Cj -dj[i]
            ThoiGianKetThuc.append(Cj)
            if Delay <=0:
                ThoiGianTreHan.append(0)
            else:
                ThoiGianTreHan.append(Delay)
        
        g1 = sum(ThoiGianKetThuc)
        g2 = sum(ThoiGianKetThuc)/n
        g3 = round(sum(pj)/sum(ThoiGianKetThuc)*100,2)
        g4 = round(sum(ThoiGianKetThuc)/sum(pj),2)
        g5 = sum(ThoiGianTreHan)/n

        e1.configure(state=NORMAL)
        e1.delete(0, 'end') 
        e1.insert(0, str(g1))
        
        #Final Debt Amount:
        e2.configure(state=NORMAL)
        e2.delete(0, 'end') 
        e2.insert(0, str(g2))
        
        
        e3.configure(state=NORMAL)
        e3.delete(0, 'end') 
        e3.insert(0, str(g3)+"%")
     

        e4.configure(state=NORMAL)
        e4.delete(0, 'end') 
        e4.insert(0, str(g4))
 

        e5.configure(state=NORMAL)
        e5.delete(0, 'end') 
        e5.insert(0, str(g5))

        print("Tổng thời gian các công việc:", g1)
        print("Tổng thời gian hoàn thành công việc trung bình:", g2)
        print("Độ hữu dụng:", g3)
        print("Số lượng công việc trung bình:",g4)
        print("Độ trễ trung bình:", g5)

    master = Tk()
    master.title("FCFS")

    Label(master, text="Bang FCFS").grid(row=0)

    Label(master, text="Tổng thời gian các công việc:").grid(row=1)
    Label(master, text="Tổng thời gian hoàn thành công việc trung bình:").grid(row=2)
    Label(master, text="Độ hữu dụng:").grid(row=3)
    Label(master, text="Số lượng công việc trung bình:").grid(row=4)
    Label(master, text="Độ trễ trung bình:").grid(row=5)

    e1 = Entry(master, state=NORMAL)
    e1.grid(row=1, column=1)
    e2 = Entry(master, state=NORMAL)
    e2.grid(row=2, column=1)
    e3 = Entry(master, state=NORMAL)
    e3.grid(row=3, column=1)
    e4= Entry(master, state=NORMAL)
    e4.grid(row=4, column=1)
    e5 = Entry(master, state=NORMAL)
    e5.grid(row=5, column=1)

    vetkERD(n,pj,dj)
    tieude = "Hàm mục tiêu là: %d"%(Min_C)
    gantt(BoSo,pj,Min_C)

# Thuật toán SPT có thời gian tới hạn
def thuat_toan_SPT_d(n,pj,dj):
    ThuTu = [i for i in range(1,n+1)]
    List1 = pj.copy()
    List2 = ThuTu.copy()
    List1, List2 = zip(*sorted(zip(List1, List2)))   
    ThuTu = List2
    Cj = 0
    ThoiGianKetThuc = []
    ThoiGianTreHan = []
    Min_C = 0
    for i in ThuTu:
        i -=1
        Cj += pj[i]
        Delay = Cj -dj[i]
        ThoiGianKetThuc.append(Cj)
        Min_C += Cj
        if Delay <=0:
            ThoiGianTreHan.append(0)
        else:
            ThoiGianTreHan.append(Delay)
    BoSo = ThuTu

    def vetkSPT_d(ThoiGianKetThuc,ThoiGianTreHan,pj,n):
        
        g1 = sum(ThoiGianKetThuc)
        g2 = sum(ThoiGianKetThuc)/n
        g3 = round(sum(pj)/sum(ThoiGianKetThuc)*100,2)
        g4 = round(sum(ThoiGianKetThuc)/sum(pj),2)
        g5 = sum(ThoiGianTreHan)/n

        e1.configure(state=NORMAL)
        e1.delete(0, 'end') 
        e1.insert(0, str(g1))


        #Final Debt Amount:
        e2.configure(state=NORMAL)
        e2.delete(0, 'end') 
        e2.insert(0, str(g2))
        
        
        e3.configure(state=NORMAL)
        e3.delete(0, 'end') 
        e3.insert(0, str(g3)+"%")
     

        e4.configure(state=NORMAL)
        e4.delete(0, 'end') 
        e4.insert(0, str(g4))
 

        e5.configure(state=NORMAL)
        e5.delete(0, 'end') 
        e5.insert(0, str(g5))

        print(ThoiGianTreHan)
        print("Tổng thời gian các công việc:", g1)
        print("Tổng thời gian hoàn thành công việc trung bình:", g2)
        print("Độ hữu dụng:", g3)
        print("Số lượng công việc trung bình:",g4)
        print("Độ trễ trung bình:", g5)

    master = Tk()
    master.title("SPT_d")

    Label(master, text="Bang SPT").grid(row=0)

    Label(master, text="Tổng thời gian các công việc:").grid(row=1)
    Label(master, text="Tổng thời gian hoàn thành công việc trung bình:").grid(row=2)
    Label(master, text="Độ hữu dụng:").grid(row=3)
    Label(master, text="Số lượng công việc trung bình:").grid(row=4)
    Label(master, text="Độ trễ trung bình:").grid(row=5)

    e1 = Entry(master, state=NORMAL)
    e1.grid(row=1, column=1)
    e2 = Entry(master, state=NORMAL)
    e2.grid(row=2, column=1)
    e3 = Entry(master, state=NORMAL)
    e3.grid(row=3, column=1)
    e4= Entry(master, state=NORMAL)
    e4.grid(row=4, column=1)
    e5 = Entry(master, state=NORMAL)
    e5.grid(row=5, column=1)

    vetkSPT_d(ThoiGianKetThuc,ThoiGianTreHan,pj,n)

    
    tieude = "Hàm mục tiêu là: %d"%(Min_C)
    
    gantt(BoSo,pj,Min_C)

# Thuật toán EDD có thời gian tới hạn
def thuat_toan_EDD(n,pj,dj):
    ThuTu = [i for i in range(1,n+1)]
    List1 = dj.copy()
    List2 = ThuTu.copy()
    List1, List2 = zip(*sorted(zip(List1, List2)))
    ThuTu = List2
    Cj = 0
    ThoiGianKetThuc = []
    ThoiGianTreHan = []
    Min_C = 0
    for i in ThuTu:
        i -=1
        Cj += pj[i]
        Delay = Cj -dj[i]
        ThoiGianKetThuc.append(Cj)
        Min_C += Cj
        if Delay <=0:
            ThoiGianTreHan.append(0)
        else:
            ThoiGianTreHan.append(Delay)
    BoSo = ThuTu

    def vetkEDD(ThoiGianKetThuc,ThoiGianTreHan,pj,n):
        
        g1 = sum(ThoiGianKetThuc)
        g2 = sum(ThoiGianKetThuc)/n
        g3 = round(sum(pj)/sum(ThoiGianKetThuc)*100,2)
        g4 = round(sum(ThoiGianKetThuc)/sum(pj),2)
        g5 = sum(ThoiGianTreHan)/n

        e1.configure(state=NORMAL)
        e1.delete(0, 'end') 
        e1.insert(0, str(g1))


        #Final Debt Amount:
        e2.configure(state=NORMAL)
        e2.delete(0, 'end') 
        e2.insert(0, str(g2))
        
        
        e3.configure(state=NORMAL)
        e3.delete(0, 'end') 
        e3.insert(0, str(g3)+"%")
     

        e4.configure(state=NORMAL)
        e4.delete(0, 'end') 
        e4.insert(0, str(g4))
 

        e5.configure(state=NORMAL)
        e5.delete(0, 'end') 
        e5.insert(0, str(g5))

        print("Tổng thời gian các công việc:", g1)
        print("Tổng thời gian hoàn thành công việc trung bình:", g2)
        print("Độ hữu dụng:", g3)
        print("Số lượng công việc trung bình:",g4)
        print("Độ trễ trung bình:", g5)

    master = Tk()
    master.title("EDD")

    Label(master, text="Bang EDD").grid(row=0)

    Label(master, text="Tổng thời gian các công việc:").grid(row=1)
    Label(master, text="Tổng thời gian hoàn thành công việc trung bình:").grid(row=2)
    Label(master, text="Độ hữu dụng:").grid(row=3)
    Label(master, text="Số lượng công việc trung bình:").grid(row=4)
    Label(master, text="Độ trễ trung bình:").grid(row=5)

    e1 = Entry(master, state=NORMAL)
    e1.grid(row=1, column=1)
    e2 = Entry(master, state=NORMAL)
    e2.grid(row=2, column=1)
    e3 = Entry(master, state=NORMAL)
    e3.grid(row=3, column=1)
    e4= Entry(master, state=NORMAL)
    e4.grid(row=4, column=1)
    e5 = Entry(master, state=NORMAL)
    e5.grid(row=5, column=1)

    vetkEDD(ThoiGianKetThuc,ThoiGianTreHan,pj,n)

    
    tieude = "Hàm mục tiêu là: %d"%(Min_C)
    
    gantt(BoSo,pj,Min_C)

# Thuật toán LPT có thời gian tới hạn
def thuat_toan_LPT(n,pj,dj):
    ThuTu = [i for i in range(1,n+1)]
    List1 = pj.copy()
    List2 = ThuTu.copy()
    List1, List2 = zip(*sorted(zip(List1, List2),reverse=True))   
    
    ThuTu = List2
    Cj = 0
    ThoiGianKetThuc = []
    ThoiGianTreHan = []
    Min_C = 0
    for i in ThuTu:
        i -=1
        Cj += pj[i]
        Delay = Cj -dj[i]
        ThoiGianKetThuc.append(Cj)
        Min_C += Cj
        if Delay <=0:
            ThoiGianTreHan.append(0)
        else:
            ThoiGianTreHan.append(Delay)
    BoSo = ThuTu
    C_max = Cj

    def vetkLPT(ThoiGianKetThuc,ThoiGianTreHan,pj,n):
        
        g1 = sum(ThoiGianKetThuc)
        g2 = sum(ThoiGianKetThuc)/n
        g3 = round(sum(pj)/sum(ThoiGianKetThuc)*100,2)
        g4 = round(sum(ThoiGianKetThuc)/sum(pj),2)
        g5 = sum(ThoiGianTreHan)/n

        e1.configure(state=NORMAL)
        e1.delete(0, 'end') 
        e1.insert(0, str(g1))


        #Final Debt Amount:
        e2.configure(state=NORMAL)
        e2.delete(0, 'end') 
        e2.insert(0, str(g2))
        
        
        e3.configure(state=NORMAL)
        e3.delete(0, 'end') 
        e3.insert(0, str(g3)+"%")
     

        e4.configure(state=NORMAL)
        e4.delete(0, 'end') 
        e4.insert(0, str(g4))
 

        e5.configure(state=NORMAL)
        e5.delete(0, 'end') 
        e5.insert(0, str(g5))

        print(ThoiGianTreHan)
        print("Tổng thời gian các công việc:", g1)
        print("Tổng thời gian hoàn thành công việc trung bình:", g2)
        print("Độ hữu dụng:", g3)
        print("Số lượng công việc trung bình:",g4)
        print("Độ trễ trung bình:", g5)

    master = Tk()
    master.title("LPT")

    Label(master, text="Bang LPT").grid(row=0)

    Label(master, text="Tổng thời gian các công việc:").grid(row=1)
    Label(master, text="Tổng thời gian hoàn thành công việc trung bình:").grid(row=2)
    Label(master, text="Độ hữu dụng:").grid(row=3)
    Label(master, text="Số lượng công việc trung bình:").grid(row=4)
    Label(master, text="Độ trễ trung bình:").grid(row=5)

    e1 = Entry(master, state=NORMAL)
    e1.grid(row=1, column=1)
    e2 = Entry(master, state=NORMAL)
    e2.grid(row=2, column=1)
    e3 = Entry(master, state=NORMAL)
    e3.grid(row=3, column=1)
    e4= Entry(master, state=NORMAL)
    e4.grid(row=4, column=1)
    e5 = Entry(master, state=NORMAL)
    e5.grid(row=5, column=1)

    vetkLPT(ThoiGianKetThuc,ThoiGianTreHan,pj,n)

    
    tieude = "Hàm mục tiêu là: %d"%(C_max)
    
    gantt(BoSo,pj,C_max)
def gantt(BoSo,pj,Min_C):
    import matplotlib.pyplot as plt
    toado = []
    vitri = []
    bat_dau = 0
    for i in BoSo:

        i = i-1

        thoigianthuchien = pj[i]
        ket_thuc = bat_dau +thoigianthuchien
        vitri.append([bat_dau,pj[i]])
        toado.append([bat_dau,ket_thuc])
        bat_dau = ket_thuc

    fig, ax = plt.subplots()

    ax.broken_barh(vitri, (10, 9),
                facecolors=('tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'))
    ax.set_ylim(0, 30)   
    tieude = "Hàm mục tiêu là: %d"%(Min_C)
    ax.set_xlim(0, ket_thuc)
    ax.set_xlabel(tieude)
    ax.set_yticks([10]) 
    ax.set_yticklabels([str(BoSo)])
    ax.grid(True)

    def text_plot(ten,vitri):
        ax.annotate(ten, (0, 0),
                    xytext=(vitri, 13.5),
                    fontsize=16,
                    horizontalalignment='center')
    
    biengia = 0
    for i in BoSo:
        text_plot(i,(toado[biengia][0]+toado[biengia][1])/2)
        biengia +=1
    tieude = "Hàm mục tiêu là: %d"%(Min_C)

    plt.show()
from distutils import filelist
from email.mime import image
import pygame, sys
import matplotlib.pyplot as plt
from pygame.locals import *
import ctypes 
from tkinter import *

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

# ----------------------Setup pygame/window ------------------ #
mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Phần mềm điều độ')
X = 1152
Y = 700
screen = pygame.display.set_mode((X, Y),0,32)
GREY = (120, 120 ,120)
WHITE = (255, 255, 255)
GREEN = (3, 252, 161)
BLUE = (3, 161, 252)
PINK = (255, 112, 181)
BLACK = (0, 0, 0)
BG = (253,243,244)
RED = (255,99,71)

font = pygame.font.SysFont(None, 63)
fontto = pygame.font.Font("F:\ĐIỀU ĐỘ\Raleway-Medium.ttf", 30)
fontnho = pygame.font.Font("F:\ĐIỀU ĐỘ\Raleway-Medium.ttf", 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_image(link,surface,x,y):
    image = pygame.image.load(link)
    surface.blit(image, (x, y))
    click = False

def main_menu():
    while True:
 
        screen.fill(BG)
        draw_text('Màn hình chính:', fontnho, BLACK, screen, 20, 20)
        draw_image('khung.png',screen,307,50)
        draw_image('icon1.png',screen,210,287)
        draw_image('icon1.png',screen,508,287)
        draw_image('icon1.png',screen,806,287)
        draw_image('icon1.png',screen,210,458)
        draw_image('icon1.png',screen,508,458)           
        draw_image('icon1.png',screen,806,458)

        draw_text('LỰA CHỌN LUẬT PHÂN VIỆC', fontto, BLACK, screen, 385, 145)    
        draw_text(("SPT"), fontto, BLACK, screen, 255, 400)
        draw_text(("SPT_d"), fontto, BLACK, screen, 550, 400)
        draw_text(("ERD"), fontto, BLACK, screen, 848, 400)
        draw_text(("WSPT"), fontto, BLACK, screen, 255, 570)
        draw_text(("EDD"), fontto, BLACK, screen, 550, 570)
        draw_text(("LPT"), fontto, BLACK, screen, 848, 570)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                # Nếu click chuột trong khoảng này thì chạy thuật toán SPT
                if (pygame.mouse.get_pos()[0] -256)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -299)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 :
                    draw_image('icon2.png',screen,210,287)

                if (pygame.mouse.get_pos()[0] -546)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -605)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 :   
                    draw_image('icon2.png',screen,508,287)

                if (pygame.mouse.get_pos()[0] -844)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -895)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 :
                    draw_image('icon2.png',screen,806,287)

                if (pygame.mouse.get_pos()[0] -256)**2 + (pygame.mouse.get_pos()[1] -514)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -299)**2 + (pygame.mouse.get_pos()[1] -512)**2 <= (60)**2 :
                    draw_image('icon2.png',screen,210,458)

                if (pygame.mouse.get_pos()[0] -546)**2 + (pygame.mouse.get_pos()[1] -512)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -605)**2 + (pygame.mouse.get_pos()[1] -512)**2 <= (60)**2 :
                    draw_image('icon2.png',screen,508,458)

                if (pygame.mouse.get_pos()[0] -844)**2 + (pygame.mouse.get_pos()[1] -512)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -895)**2 + (pygame.mouse.get_pos()[1] -512)**2 <= (60)**2 :
                    draw_image('icon2.png',screen,806,458)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
            # Nếu click chuột trong khoảng này thì chạy thuật toán SPT
                if (pygame.mouse.get_pos()[0] -256)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -299)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 :
                    game_SPT()

                if (pygame.mouse.get_pos()[0] -546)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -605)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 :   
                    game_SPT_d()

                if (pygame.mouse.get_pos()[0] -844)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -895)**2 + (pygame.mouse.get_pos()[1] -341)**2 <= (60)**2 :
                    game_ERD()

                if (pygame.mouse.get_pos()[0] -256)**2 + (pygame.mouse.get_pos()[1] -514)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -299)**2 + (pygame.mouse.get_pos()[1] -512)**2 <= (60)**2 :
                    game_WSPT()

                if (pygame.mouse.get_pos()[0] -546)**2 + (pygame.mouse.get_pos()[1] -512)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -605)**2 + (pygame.mouse.get_pos()[1] -512)**2 <= (60)**2 :
                    game_EDD()

                if (pygame.mouse.get_pos()[0] -844)**2 + (pygame.mouse.get_pos()[1] -512)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -895)**2 + (pygame.mouse.get_pos()[1] -512)**2 <= (60)**2 :
                    game_LPT()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        click = False
        pygame.display.update()
        mainClock.tick(60)
        


def game_SPT():

    input_box = pygame.Rect(450 ,50, 140, 50)
    input_box2 = pygame.Rect(450, 150, 140, 50)    
    color_inactive = (255,159,156)
    color_active = (255,8,0)
    color = color_inactive
    color2 = color_inactive
    active = False
    active2 = False
    text = ''
    text2 = ''
    done = False
    running = True

    while running:
        screen.fill(BG)
        

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                    #QUAY LẠI MÀN HÌNH CHÍNH
                    if (pygame.mouse.get_pos()[0] -25)**2 + (pygame.mouse.get_pos()[1] -34)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -29)**2 + (pygame.mouse.get_pos()[1] -34)**2 <= (60)**2 :
                        main_menu()
                    if input_box2.collidepoint(event.pos):
                        active2 = not active2
                    else:
                        active2 = False
                    color2 = color_active if active2 else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif event.key == pygame.K_DELETE:
                            text = ''
                        else:
                            text += event.unicode
                    if active2:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            text2 += event.unicode

                    def chaySPT():
                        n = int(text)
                        pj = text2
                        pj = pj.split(' ')
                        pj = [int(i) for i in pj]
                        #Thuật toán xử lý WSPT
                        BoSo, Min_C = thuat_toan_SPT(n,pj)

                        tieude = "Hàm mục tiêu là: %d"%(Min_C)
                        # Hàm hiển thị sơ đồ gantt
                        try:
                            gantt(BoSo,pj,Min_C)
                        except:
                            pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >525 and pygame.mouse.get_pos()[1] >400:
                        if pygame.mouse.get_pos()[0] <625 and pygame.mouse.get_pos()[1] <450:
                            chaySPT()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        chaySPT()
        except:
            Mbox("Ôi không", 'Nhập sai đầu vào rồi', 5)
        screen.fill(BG)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        txt_surface2 = font.render(text2, True, color2)
        width2 = max(400, txt_surface2.get_width()+10)
        input_box2.w = width2
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        pygame.draw.rect(screen, color2, input_box2, 2)

        draw_text('< SPT', fontnho,RED, screen, 25, 10)
        draw_text("Nhập số lượng công việc: ", fontnho, BLACK, screen, 25, 50)
        draw_text("Nhập thời gian hoàn thành từng công việc:", fontnho, BLACK, screen, 25, 150)
        draw_text("(Cách nhau bởi khoảng trắng): ", fontnho, BLACK, screen, 25, 170)

        pygame.draw.rect(screen, PINK, (525,400,100,50))
        draw_text(("GIẢI!"), fontnho, BLACK, screen, 548, 413)
        
        pygame.display.update()
        mainClock.tick(60)
 
def game_WSPT():

    input_box = pygame.Rect(450 ,50, 140, 50)
    input_box2 = pygame.Rect(450, 150, 140, 50)
    input_box3 = pygame.Rect(450, 250, 140, 50)    
    color_inactive = (255,159,156)
    color_active = (255,8,0)
    color = color_inactive
    color2 = color_inactive
    color3 = color_inactive
    active = False
    active2 = False
    active3 = False
    text = ''
    text2 = ''
    text3 = ''
    done = False
    running = True

    while running:
        screen.fill(BG)
        

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                #QUAY LẠI MÀN HÌNH CHÍNH
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (pygame.mouse.get_pos()[0] -25)**2 + (pygame.mouse.get_pos()[1] -34)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -29)**2 + (pygame.mouse.get_pos()[1] -34)**2 <= (60)**2 :
                        main_menu()
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                    if input_box2.collidepoint(event.pos):
                        active2 = not active2
                    else:
                        active2 = False
                    color2 = color_active if active2 else color_inactive
                    if input_box3.collidepoint(event.pos):
                        active3 = not active3
                    else:
                        active3 = False
                    color3 = color_active if active3 else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif event.key == pygame.K_DELETE:
                            text = ''
                        else:
                            text += event.unicode
                    if active2:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            text2 += event.unicode
                    if active3:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text3 = text3[:-1]
                        else:
                            text3 += event.unicode

                    def chayWSPT():
                        n = int(text)

                        pj = text2
                        pj = pj.split(' ')
                        pj = [int(i) for i in pj]
                        wj = text3
                        wj = wj.split(' ')
                        wj = [int(i) for i in wj]
                        #Thuật toán xử lý WSPT
                        BoSo, Min_C = thuat_toan_WSPT(n,pj,wj)

                        tieude = "Hàm mục tiêu là: %d"%(Min_C)
                        # Hàm hiển thị sơ đồ gantt
                        try:
                            gantt(BoSo,pj,Min_C)
                        except:
                            pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >525 and pygame.mouse.get_pos()[1] >400:
                        if pygame.mouse.get_pos()[0] <625 and pygame.mouse.get_pos()[1] <450:
                            chayWSPT()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        chayWSPT()
        except:
            Mbox("Ôi không", 'Nhập sai đầu vào rồi', 5)
        screen.fill(BG)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        txt_surface2 = font.render(text2, True, color2)
        width2 = max(400, txt_surface2.get_width()+10)
        input_box2.w = width2
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        pygame.draw.rect(screen, color2, input_box2, 2)

        txt_surface3 = font.render(text3, True, color3)
        width3 = max(400, txt_surface3.get_width()+10)
        input_box3.w = width3
        screen.blit(txt_surface3, (input_box3.x+5, input_box3.y+5))
        pygame.draw.rect(screen, color3, input_box3, 2)

        # Viết tiêu đề

        draw_text('< WSPT', fontnho,RED, screen, 25, 10)
        draw_text(("Nhập số lượng công việc: "), fontnho, BLACK, screen, 25, 50)
        draw_text(("Nhập thời gian hoàn thành từng công việc:"), fontnho, BLACK, screen, 25, 150)
        draw_text(("(Cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 170)

        draw_text(("Nhập ngày tới hạn từng công việc:"), fontnho, BLACK, screen, 25, 250)
        draw_text(("(Cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 270)

        pygame.draw.rect(screen, PINK, (525,400,100,50))
        draw_text(("GIẢI!"), fontnho, BLACK, screen, 548, 413)


        
        pygame.display.update()
        mainClock.tick(60)

def game_ERD():

    input_box = pygame.Rect(450 ,50, 140, 50)
    input_box2 = pygame.Rect(450, 150, 140, 50)
    input_box3 = pygame.Rect(450, 250, 140, 50)    
    color_inactive = (255,159,156)
    color_active = (255,8,0)
    color = color_inactive
    color2 = color_inactive
    color3 = color_inactive
    active = False
    active2 = False
    active3 = False
    text = ''
    text2 = ''
    text3 = ''
    done = False
    running = True

    while running:
        screen.fill(BG)
        

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                    #QUAY LẠI MÀN HÌNH CHÍNH
                    if (pygame.mouse.get_pos()[0] -25)**2 + (pygame.mouse.get_pos()[1] -34)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -29)**2 + (pygame.mouse.get_pos()[1] -34)**2 <= (60)**2 :
                        main_menu()
                    if input_box2.collidepoint(event.pos):
                        active2 = not active2
                    else:
                        active2 = False
                    color2 = color_active if active2 else color_inactive
                    if input_box3.collidepoint(event.pos):
                        active3 = not active3
                    else:
                        active3 = False
                    color3 = color_active if active3 else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif event.key == pygame.K_DELETE:
                            text = ''
                        else:
                            text += event.unicode
                    if active2:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            text2 += event.unicode
                    if active3:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text3 = text3[:-1]
                        else:
                            text3 += event.unicode

                    def chayERD():
                        n = int(text)

                        pj = text2
                        pj = pj.split(' ')
                        pj = [int(i) for i in pj]
                        dj = text3
                        dj = dj.split(' ')
                        dj = [int(i) for i in dj]
                        #Thuật toán xử lý WSPT
                        thuat_toan_ERD(n,pj,dj)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >525 and pygame.mouse.get_pos()[1] >400:
                        if pygame.mouse.get_pos()[0] <625 and pygame.mouse.get_pos()[1] <450:
                            chayERD()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        chayERD()
        except:
            Mbox("Ôi không", 'Nhập sai đầu vào rồi', 5)
        screen.fill(BG)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        txt_surface2 = font.render(text2, True, color2)
        width2 = max(400, txt_surface2.get_width()+10)
        input_box2.w = width2
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        pygame.draw.rect(screen, color2, input_box2, 2)

        txt_surface3 = font.render(text3, True, color3)
        width3 = max(400, txt_surface3.get_width()+10)
        input_box3.w = width3
        screen.blit(txt_surface3, (input_box3.x+5, input_box3.y+5))
        pygame.draw.rect(screen, color3, input_box3, 2)

        # Viết tiêu đề

        draw_text('< ERD', fontnho,RED, screen, 25, 10)
        draw_text(("Nhập số lượng công việc: "), fontnho, BLACK, screen, 25, 50)
        draw_text(("Nhập thời gian hoàn thành từng công việc:"), fontnho, BLACK, screen, 25, 150)
        draw_text(("(Cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 170)

        draw_text(("Nhập trọng số từng công việc:"), fontnho, BLACK, screen, 25, 250)
        draw_text(("(Cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 270)

        pygame.draw.rect(screen, PINK, (525,400,100,50))
        draw_text(("GIẢI!"), fontnho, BLACK, screen, 548, 413)


        
        pygame.display.update()
        mainClock.tick(60)

def game_SPT_d():
    input_box = pygame.Rect(450 ,50, 140, 50)
    input_box2 = pygame.Rect(450, 150, 140, 50)
    input_box3 = pygame.Rect(450, 250, 140, 50)    
    color_inactive = (255,159,156)
    color_active = (255,8,0)
    color = color_inactive
    color2 = color_inactive
    color3 = color_inactive
    active = False
    active2 = False
    active3 = False
    text = ''
    text2 = ''
    text3 = ''
    done = False
    running = True

    while running:
        screen.fill(BG)
        

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                    #QUAY LẠI MÀN HÌNH CHÍNH
                    if (pygame.mouse.get_pos()[0] -25)**2 + (pygame.mouse.get_pos()[1] -34)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -29)**2 + (pygame.mouse.get_pos()[1] -34)**2 <= (60)**2 :
                        main_menu()
                    if input_box2.collidepoint(event.pos):
                        active2 = not active2
                    else:
                        active2 = False
                    color2 = color_active if active2 else color_inactive
                    if input_box3.collidepoint(event.pos):
                        active3 = not active3
                    else:
                        active3 = False
                    color3 = color_active if active3 else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif event.key == pygame.K_DELETE:
                            text = ''
                        else:
                            text += event.unicode
                    if active2:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            text2 += event.unicode
                    if active3:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text3 = text3[:-1]
                        else:
                            text3 += event.unicode

                    def chaySPT_d():
                        n = int(text)

                        pj = text2
                        pj = pj.split(' ')
                        pj = [int(i) for i in pj]
                        dj = text3
                        dj = dj.split(' ')
                        dj = [int(i) for i in dj]
                        #Thuật toán xử lý WSPT
                        thuat_toan_SPT_d(n,pj,dj)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >525 and pygame.mouse.get_pos()[1] >400:
                        if pygame.mouse.get_pos()[0] <625 and pygame.mouse.get_pos()[1] <450:
                            chaySPT_d()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        chaySPT_d()
        except:
            Mbox("Ôi không", 'Nhập sai đầu vào rồi', 5)
        screen.fill(BG)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        txt_surface2 = font.render(text2, True, color2)
        width2 = max(400, txt_surface2.get_width()+10)
        input_box2.w = width2
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        pygame.draw.rect(screen, color2, input_box2, 2)

        txt_surface3 = font.render(text3, True, color3)
        width3 = max(400, txt_surface3.get_width()+10)
        input_box3.w = width3
        screen.blit(txt_surface3, (input_box3.x+5, input_box3.y+5))
        pygame.draw.rect(screen, color3, input_box3, 2)

      

        draw_text('< SPT_d', fontnho,RED, screen, 25, 10)
        draw_text(("Nhập số lượng công việc: "), fontnho, BLACK, screen, 25, 50)
        draw_text(("Nhập thời gian hoàn thành từng công việc:"), fontnho, BLACK, screen, 25, 150)
        draw_text(("(Cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 170)

        draw_text(("Nhập trọng số từng công việc:"), fontnho, BLACK, screen, 25, 250)
        draw_text(("(Cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 270)

        pygame.draw.rect(screen, PINK, (525,400,100,50))
        draw_text(("GIẢI!"), fontnho, BLACK, screen, 548, 413)

        
        pygame.display.update()
        mainClock.tick(60)

def game_EDD():
    input_box = pygame.Rect(450 ,50, 140, 50)
    input_box2 = pygame.Rect(450, 150, 140, 50)
    input_box3 = pygame.Rect(450, 250, 140, 50)    
    color_inactive = (255,159,156)
    color_active = (255,8,0)
    color = color_inactive
    color2 = color_inactive
    color3 = color_inactive
    active = False
    active2 = False
    active3 = False
    text = ''
    text2 = ''
    text3 = ''
    done = False
    running = True

    while running:
        screen.fill(BG)
        

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                    #QUAY LẠI MÀN HÌNH CHÍNH
                    if (pygame.mouse.get_pos()[0] -25)**2 + (pygame.mouse.get_pos()[1] -34)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -29)**2 + (pygame.mouse.get_pos()[1] -34)**2 <= (60)**2 :
                        main_menu()
                    if input_box2.collidepoint(event.pos):
                        active2 = not active2
                    else:
                        active2 = False
                    color2 = color_active if active2 else color_inactive
                    if input_box3.collidepoint(event.pos):
                        active3 = not active3
                    else:
                        active3 = False
                    color3 = color_active if active3 else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif event.key == pygame.K_DELETE:
                            text = ''
                        else:
                            text += event.unicode
                    if active2:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            text2 += event.unicode
                    if active3:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text3 = text3[:-1]
                        else:
                            text3 += event.unicode

                    def chayEDD():
                        n = int(text)

                        pj = text2
                        pj = pj.split(' ')
                        pj = [int(i) for i in pj]
                        dj = text3
                        dj = dj.split(' ')
                        dj = [int(i) for i in dj]
                        #Thuật toán xử lý WSPT
                        thuat_toan_EDD(n,pj,dj)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >525 and pygame.mouse.get_pos()[1] >400:
                        if pygame.mouse.get_pos()[0] <625 and pygame.mouse.get_pos()[1] <450:
                            chayEDD()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        chayEDD()
        except:
            Mbox("Ôi không", 'Nhập sai đầu vào rồi', 5)
        screen.fill(BG)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        txt_surface2 = font.render(text2, True, color2)
        width2 = max(400, txt_surface2.get_width()+10)
        input_box2.w = width2
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        pygame.draw.rect(screen, color2, input_box2, 2)

        txt_surface3 = font.render(text3, True, color3)
        width3 = max(400, txt_surface3.get_width()+10)
        input_box3.w = width3
        screen.blit(txt_surface3, (input_box3.x+5, input_box3.y+5))
        pygame.draw.rect(screen, color3, input_box3, 2)

        # Viết tiêu đề

        draw_text('< EDD', fontnho,RED, screen, 25, 10)
        draw_text(("Nhập số lượng công việc: "), fontnho, BLACK, screen, 25, 50)
        draw_text(("Nhập thời gian hoàn thành từng công việc:"), fontnho, BLACK, screen, 25, 150)
        draw_text(("(Cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 170)

        draw_text(("Nhập trọng số từng công việc:"), fontnho, BLACK, screen, 25, 250)
        draw_text(("(Cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 270)

        pygame.draw.rect(screen, PINK, (525,400,100,50))
        draw_text(("GIẢI!"), fontnho, BLACK, screen, 548, 413)


        
        pygame.display.update()
        mainClock.tick(60)

def game_LPT():
    input_box = pygame.Rect(450 ,50, 140, 50)
    input_box2 = pygame.Rect(450, 150, 140, 50)
    input_box3 = pygame.Rect(450, 250, 140, 50)    
    color_inactive = (255,159,156)
    color_active = (255,8,0)
    color = color_inactive
    color2 = color_inactive
    color3 = color_inactive
    active = False
    active2 = False
    active3 = False
    text = ''
    text2 = ''
    text3 = ''
    done = False
    running = True

    while running:
        screen.fill(BG)
      

        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                    #QUAY LẠI MÀN HÌNH CHÍNH
                    if (pygame.mouse.get_pos()[0] -25)**2 + (pygame.mouse.get_pos()[1] -34)**2 <= (60)**2 or (pygame.mouse.get_pos()[0] -29)**2 + (pygame.mouse.get_pos()[1] -34)**2 <= (60)**2 :
                        main_menu(), pygame.quit(), sys.exit()
                    if input_box2.collidepoint(event.pos):
                        active2 = not active2
                    else:
                        active2 = False
                    color2 = color_active if active2 else color_inactive
                    if input_box3.collidepoint(event.pos):
                        active3 = not active3
                    else:
                        active3 = False
                    color3 = color_active if active3 else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif event.key == pygame.K_DELETE:
                            text = ''
                        else:
                            text += event.unicode
                    if active2:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            text2 += event.unicode
                    if active3:
                        if event.key == pygame.K_RETURN:
                            pass
                        elif event.key == pygame.K_BACKSPACE:
                            text3 = text3[:-1]
                        else:
                            text3 += event.unicode

                    def chayLPT():
                        n = int(text)

                        pj = text2
                        pj = pj.split(' ')
                        pj = [int(i) for i in pj]
                        dj = text3
                        dj = dj.split(' ')
                        dj = [int(i) for i in dj]
                        #Thuật toán xử lý WSPT
                        thuat_toan_LPT(n,pj,dj)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >525 and pygame.mouse.get_pos()[1] >400:
                        if pygame.mouse.get_pos()[0] <625 and pygame.mouse.get_pos()[1] <450:
                            chayLPT()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        chayLPT()
        except:
            Mbox("Ôi không", 'Nhập sai đầu vào rồi', 5)
        screen.fill(BG)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        txt_surface2 = font.render(text2, True, color2)
        width2 = max(400, txt_surface2.get_width()+10)
        input_box2.w = width2
        screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
        pygame.draw.rect(screen, color2, input_box2, 2)

        txt_surface3 = font.render(text3, True, color3)
        width3 = max(400, txt_surface3.get_width()+10)
        input_box3.w = width3
        screen.blit(txt_surface3, (input_box3.x+5, input_box3.y+5))
        pygame.draw.rect(screen, color3, input_box3, 2)

        # Viết tiêu đề

        draw_text('< LPT', fontnho,RED, screen, 25, 10)
        draw_text(("Nhập số lượng công việc: "), fontnho, BLACK, screen, 25, 50)
        draw_text(("Nhập thời gian hoàn thành từng công việc:"), fontnho, BLACK, screen, 25, 150)
        draw_text(("(Cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 170)

        draw_text(("Nhập trọng số từng công việc:"), fontnho, BLACK, screen, 25, 250)
        draw_text(("(Cách nhau bởi khoảng trắng): "), fontnho, BLACK, screen, 25, 270)

        pygame.draw.rect(screen, PINK, (525,400,100,50))
        draw_text(("GIẢI!"), fontnho, BLACK, screen, 548, 413)

        pygame.display.update()
        mainClock.tick(60)

main_menu()