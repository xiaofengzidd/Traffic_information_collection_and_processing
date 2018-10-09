import matplotlib.pyplot as plt
import datetime
from mpl_toolkits.basemap import Basemap
from matplotlib.ticker import MultipleLocator
from xlrd import open_workbook, xldate_as_tuple
import numpy as np

x_data1,y_data1,z_data1,m_gps,n_gps = [],[],[],[],[]#时间、里程、油量、纬度、经度
s = open_workbook(r'C:\Users\Liu\Desktop\yhjc.xls').sheet_by_name('Sheet1')
for row in range(1,s.nrows):
    values = []
    for col in range(s.ncols):
        values.append(datetime.datetime(*xldate_as_tuple(s.cell(row, col).value, 0))) if s.cell(row,col).ctype == 3 else values.append(s.cell(row,col).value)
    x_data1.append(values[9]),y_data1.append(values[10]),z_data1.append(values[11]), m_gps.append(values[2]), n_gps.append(values[3])
i, i_list, add_num, loss_v, add_v, add_time = 3,[], 0, 0, 0, []
while True:
    if i>=len(z_data1):
        break
    if y_data1[i]-y_data1[i-3]==0 and z_data1[i-3]-z_data1[i]>20:
        print('警告：在%s时间可能有人偷油！！'%x_data1[i])
        i+=3
    if z_data1[i]-z_data1[i-3]>40.0:#每次加油量均大于40
        i_list.append(i-1)#加油时间点的位置
        add_num+=1; add_v+=max(z_data1[i:i+20])-min(z_data1[i-3:i]);add_time.append(str(x_data1[i-1]));
        i += 20#间隔20个油量数，对应时间差不多10分钟，司机不可能每次加完油过10分钟再加一次
    else:
        i+=1#遍历列表，能精确确定加油的时间点
for j in range(1,len(i_list)):
    loss_v+=max(z_data1[i_list[j-1]:i_list[j-1]+20])-min(z_data1[i_list[j]-3:i_list[j]])
sca_listx, sca_listy, sca_listz, mgps_list, ngps_list, add_gps = [], [], [], [], [], []
for q in i_list:
    sca_listx.append(x_data1[q-2]),sca_listy.append(y_data1[q-2]),sca_listz.append(z_data1[q-2]),mgps_list.append(m_gps[q-2]),ngps_list.append(n_gps[q-2])
for e in range(len(mgps_list)):
    add_gps.append((mgps_list[e],ngps_list[e]))
print('加油次数：%d'%add_num,'\n'+'加油量：%.2f'%add_v,'\n'+'耗油量：%.2f'%loss_v,'\n'+'加油时间点：',add_time,'\n'+'加油站GPS坐标：',add_gps)
fig1 = plt.figure(1,figsize=(12,6))
ax1 = plt.subplot(3,1,1)
plt.plot(y_data1,z_data1,'m-',label='油耗/里程关系'),plt.title("营运车辆能耗数据分析"),plt.xlabel("行驶里程/mile"),plt.ylabel("油量/L")
ax2 = plt.subplot(3,1,2)
plt.plot(x_data1,z_data1,'m-',label='油耗/时间关系'),plt.xlabel("时间/s"),plt.ylabel("油量/L")
ax3 = plt.subplot(3,1,3)
plt.plot(x_data1,y_data1,'m-',label='里程/时间关系'),plt.xlabel("时间/s"),plt.ylabel("里程/mile")
plt.rcParams['font.sans-serif']=['SimHei']
fig2, ax4 = plt.subplots(figsize=(12,6))#=============================================================fig2
ax5 = ax4.twinx();ax4.plot(x_data1,z_data1,'m-',label='油耗/时间关系');ax5.plot(x_data1,y_data1,'c-',label='里程/时间关系')
ax4.set_xlabel("时间/s"),ax4.set_ylabel("油耗/L"),ax5.set_ylabel("里程/mile")
plt.rcParams['font.sans-serif']=['SimHei'];plt.title('加油次数：%s  加油量：%.2f  耗油量：%.2f'%(str(add_num),add_v,loss_v))
ax5.scatter(sca_listx,sca_listy,s=20,c='g',marker='o',label='加油点');ax4.scatter(sca_listx,sca_listz,s=20,c='r',marker='s',label='加油点')
for w in sca_listx:
    plt.axvline(w, c='y', linestyle='--')
ax4.xaxis.set_minor_locator(MultipleLocator(0.25));ax4.yaxis.set_minor_locator(MultipleLocator(50))
ax4.grid(which='minor',axis='both',linestyle='-.');fig2.autofmt_xdate(rotation = 45);fig2.legend(loc='upper right')
fig3 = plt.figure(figsize=(10, 10))#===================================================================fig3
m = Basemap(projection='stere', width=1.5E6, height=1.5E6,lat_0=38, lon_0=118, rsphere=6371200.,resolution='l',area_thresh=10000)
m.drawcoastlines();m.drawcountries();m.fillcontinents(color='g',lake_color='b');m.drawmapboundary(fill_color='b');m.readshapefile(r'D:\软件\basemap行政区界线\gadm36_CHN_shp\gadm36_CHN_1','states',drawbounds=True)
parallels, meridians, o = np.arange(0., 90, 2.), np.arange(0., 360., 2.), 1
m.drawparallels(parallels, labels=[1, 0, 0, 0], fontsize=10);m.drawmeridians(meridians, labels=[0, 0, 0, 1], fontsize=10)
for p in range(len(m_gps)//10):
    x,y = m(n_gps[10*p],m_gps[10*p])
    if p ==0:
        plt.plot(x, y, '^y', markersize=10, label='起点')
    elif p ==len(m_gps)//10-1:
        plt.plot(x, y, 'sy', markersize=10,label='终点')
    else:
        plt.plot(x, y, '.r', markersize=1)
for r in add_gps:
    x, y = m(r[1],r[0])# 将经纬度映射为 (x, y) 坐标，用于绘制图像
    if o ==1:
        plt.plot(x, y, 'om', markersize=5, label='加油站(顺序编号)');plt.text(x, y, '%d'%o, color='c', fontsize=12)
    else:
        plt.plot(x, y, 'om', markersize=5);plt.text(x, y, '%d' % o, color='c', fontsize=12)
    o+=1
fig3.legend(loc='upper right');plt.rcParams['font.sans-serif']=['SimHei']
plt.show()