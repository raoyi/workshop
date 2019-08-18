串口通信是指外设和计算机间，通过数据信号线 、地线、控制线等，按位进行传输数据的一种通讯方式。这种通信方式使用的数据线少，在远距离通信中可以节约通信成本，但其传输速度比并行传输低。串口是计算机上一种非常通用的设备通信协议。pyserial模块封装了python对串口的访问，为多平台的使用提供了统一的接口。

 **安装：**

```
pip install pyserial
```

**测试：**

两个CH340 （TTL转串口模块）接入到PC串口上，通过Python进行数据交互：



 简单串口程序实现：

复制代码
 1 import serial #导入模块
 2 try:
 3   #端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
 4   portx="COM3"
 5   #波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
 6   bps=115200
 7   #超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
 8   timex=5
 9   # 打开串口，并得到串口对象
10   ser=serial.Serial(portx,bps,timeout=timex)
11 
12   # 写数据
13   result=ser.write("我是东小东".encode("gbk"))
14   print("写总字节数:",result)
15 
16   ser.close()#关闭串口
17 
18 except Exception as e:
19     print("---异常---：",e)
复制代码
 获取可用串口列表：

复制代码
 1 import serial #导入模块
 2 
 3 import serial.tools.list_ports
 4 port_list = list(serial.tools.list_ports.comports())
 5 print(port_list)
 6 if len(port_list) == 0:
 7    print('无可用串口')
 8 else:
 9     for i in range(0,len(port_list)):
10         print(port_list[i])
复制代码
十六进制处理：

复制代码
 1 import serial #导入模块
 2 try:
 3   portx="COM3"
 4   bps=115200
 5   #超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
 6   timex=None
 7   ser=serial.Serial(portx,bps,timeout=timex)
 8   print("串口详情参数：", ser)
 9 
10   #十六进制的发送
11   result=ser.write(chr(0x06).encode("utf-8"))#写数据
12   print("写总字节数:",result)
13 
14   #十六进制的读取
15   print(ser.read().hex())#读一个字节
16 
17   print("---------------")
18   ser.close()#关闭串口
19 
20 except Exception as e:
21     print("---异常---：",e)
复制代码
 其他细节补充：

复制代码
 1 import serial #导入模块
 2 try:
 3 
 4   #端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
 5   portx="COM3"
 6   #波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
 7   bps=115200
 8   #超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
 9   timex=5
10   # 打开串口，并得到串口对象
11   ser=serial.Serial(portx,bps,timeout=timex)
12   print("串口详情参数：", ser)
13 
14 
15 
16   print(ser.port)#获取到当前打开的串口名
17   print(ser.baudrate)#获取波特率
18 
19   result=ser.write("我是东小东".encode("gbk"))#写数据
20   print("写总字节数:",result)
21 
22 
23   #print(ser.read())#读一个字节
24   # print(ser.read(10).decode("gbk"))#读十个字节
25   #print(ser.readline().decode("gbk"))#读一行
26   #print(ser.readlines())#读取多行，返回列表，必须匹配超时（timeout)使用
27   #print(ser.in_waiting)#获取输入缓冲区的剩余字节数
28   #print(ser.out_waiting)#获取输出缓冲区的字节数
29 
30   #循环接收数据，此为死循环，可用线程实现
31   while True:
32          if ser.in_waiting:
33              str=ser.read(ser.in_waiting ).decode("gbk")
34              if(str=="exit"):#退出标志
35                  break
36              else:
37                print("收到数据：",str)
38 
39   print("---------------")
40   ser.close()#关闭串口
41 
42 
43 except Exception as e:
44     print("---异常---：",e)
复制代码
部分封装：

其中读数据的封装方法并不是很好用，使用的话又得循环接收，这样反而更加复杂了

复制代码
 1 import serial #导入模块
 2 import threading
 3 STRGLO="" #读取的数据
 4 BOOL=True  #读取标志位
 5 
 6 #读数代码本体实现
 7 def ReadData(ser):
 8     global STRGLO,BOOL
 9     # 循环接收数据，此为死循环，可用线程实现
10     while BOOL:
11         if ser.in_waiting:
12             STRGLO = ser.read(ser.in_waiting).decode("gbk")
13             print(STRGLO)
14 
15 
16 #打开串口
17 # 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
18 # 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
19 # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
20 def DOpenPort(portx,bps,timeout):
21     ret=False
22     try:
23         # 打开串口，并得到串口对象
24         ser = serial.Serial(portx, bps, timeout=timeout)
25         #判断是否打开成功
26         if(ser.is_open):
27            ret=True
28            threading.Thread(target=ReadData, args=(ser,)).start()
29     except Exception as e:
30         print("---异常---：", e)
31     return ser,ret
32 
33 
34 
35 #关闭串口
36 def DColsePort(ser):
37     global BOOL
38     BOOL=False
39     ser.close()
40 
41 
42 
43 #写数据
44 def DWritePort(ser,text):
45     result = ser.write(text.encode("gbk"))  # 写数据
46     return result
47 
48 
49 
50 
51 #读数据
52 def DReadPort():
53     global STRGLO
54     str=STRGLO
55     STRGLO=""#清空当次读取
56     return str
57 
58 
59 
60 if __name__=="__main__":
61     ser,ret=DOpenPort("COM6",115200,None)
62     if(ret==True):#判断串口是否成功打开
63          count=DWritePort(ser,"我是东小东，哈哈")
64          print("写入字节数：",count)
65          #DReadPort() #读串口数据
66          #DColsePort(ser)  #关闭串口
