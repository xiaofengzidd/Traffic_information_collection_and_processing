import matplotlib.pyplot as plt
import datetime
from xlrd import open_workbook, xldate_as_tuple

x_data1,y_data1,z_data1,m_gps,n_gps = [],[],[],[],[]
s = open_workbook(r'C:\Users\Liu\Desktop\yhjc.xls').sheet_by_name('Sheet1')
rown = 101
plt.figure(1,figsize=(10,6))
plt.ion()
try:
    while True:
        plt.clf()
        if (s.nrows+101-rown)//100==0:
            while True:
                s = open_workbook(r'C:\Users\Liu\Desktop\yhjc.xls').sheet_by_name('Sheet1')
                if (s.nrows + 101 - rown) // 100 == 0:
                    plt.cla()
                    print('等待数据更新中。。。')
                    plt.rcParams['font.sans-serif'] = ['SimHei']
                    ax1 = plt.subplot(3, 1, 1)  # 使用子图
                    plt.xlim(y_data1[0], y_data1[rown - 102], 6)
                    plt.plot(y_data1, z_data1, 'r', label='油耗/里程关系'), plt.title("营运车辆能耗数据分析(等待数据更新中...)"+'\n'+'加油次数：%s  加油量：%.2f  耗油量：%.2f'%(str(add_num),add_v,loss_v)+'\n'+'加油时间点：%s'%str(add_time[-1])+'\n'+'加油站GPS坐标：%s'%str(add_gps[-1])), plt.xlabel("行驶里程/mile"), plt.ylabel("油量/L")
                    ax2 = plt.subplot(3, 1, 2)
                    plt.xlim(x_data1[0], x_data1[rown - 102], 6)
                    plt.plot(x_data1, z_data1, 'g', label='油耗/时间关系'), plt.xlabel("时间/s"), plt.ylabel("油量/L")
                    ax3 = plt.subplot(3, 1, 3)
                    plt.xlim(x_data1[0], x_data1[rown - 102], 6)
                    plt.plot(x_data1, y_data1, 'b', label='里程/时间关系'), plt.xlabel("时间/s"), plt.ylabel("里程/mile")
                    plt.pause(2)
                else:
                    break
        for row in range(rown-100,rown):
            values = []
            for col in range(s.ncols):
                values.append(datetime.datetime(*xldate_as_tuple(s.cell(row, col).value, 0))) if s.cell(row,col).ctype == 3 else values.append(s.cell(row,col).value)
            x_data1.append(values[9]),y_data1.append(values[10]), z_data1.append(values[11]), m_gps.append(values[2]), n_gps.append(values[3])
        i, i_list, add_num, loss_v, add_v, add_time, mgps_list, ngps_list, add_gps = 3, [], 0, 0, 0, [], [], [], []
        while True:
            if i>=len(z_data1):
                break
            if z_data1[i]-z_data1[i-3]>40.0:#每次加油量均大于40
                i_list.append(i-1)#加油时间点的位置
                add_num+=1; add_v+=max(z_data1[i:i+20])-min(z_data1[i-3:i]);add_time.append(str(x_data1[i-1]));
                i += 20#间隔20个油量数，对应时间差不多10分钟，司机不可能每次加完油过10分钟再加一次
            else:
                i+=1#遍历列表，能精确确定加油的时间点
        for j in range(1,len(i_list)):
            loss_v+=max(z_data1[i_list[j-1]:i_list[j-1]+20])-min(z_data1[i_list[j]-3:i_list[j]])
        for q in i_list:
            mgps_list.append(m_gps[q - 2]), ngps_list.append(n_gps[q - 2])
        for e in range(len(mgps_list)):
            add_gps.append((mgps_list[e],ngps_list[e]))
        print('加油次数：%d'%add_num,'\n'+'加油量：%.2f'%add_v,'\n'+'耗油量：%.2f'%loss_v,'\n'+'加油时间点：',add_time,'\n'+'加油站GPS坐标：',add_gps)

        plt.cla()
        plt.rcParams['font.sans-serif'] = ['SimHei']
        ax1 = plt.subplot(3, 1, 1)  # 使用子图
        plt.xlim(y_data1[0], y_data1[rown - 2], 6)
        plt.plot(y_data1, z_data1, 'r', label='油耗/里程关系'), plt.title("营运车辆能耗数据分析"+'\n'+'加油次数：%s  加油量：%.2f  耗油量：%.2f'%(str(add_num),add_v,loss_v)+'\n'+'加油时间点：%s'%str(add_time[-1])+'\n'+'加油站GPS坐标：%s'%str(add_gps[-1])), plt.xlabel("行驶里程/mile"), plt.ylabel("油量/L")
        ax2 = plt.subplot(3,1,2)
        plt.xlim(x_data1[0], x_data1[rown - 2], 6)
        plt.plot(x_data1, z_data1, 'g', label='油耗/时间关系'), plt.xlabel("时间/s"), plt.ylabel("油量/L")
        ax3 = plt.subplot(3,1,3)
        plt.xlim(x_data1[0], x_data1[rown - 2], 6)
        plt.plot(x_data1, y_data1, 'b', label='里程/时间关系'), plt.xlabel("时间/s"), plt.ylabel("里程/mile")
        plt.pause(0.033)
        rown += 100
except:
    print('Error!!')