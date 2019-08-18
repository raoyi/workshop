串口通信是指外设和计算机间，通过数据信号线 、地线、控制线等，按位进行传输数据的一种通讯方式。这种通信方式使用的数据线少，在远距离通信中可以节约通信成本，但其传输速度比并行传输低。串口是计算机上一种非常通用的设备通信协议。pyserial模块封装了python对串口的访问，为多平台的使用提供了统一的接口。

 **安装：**

```
pip install pyserial
```

**测试：**

两个CH340（TTL转串口模块）接入到PC串口上，通过Python进行数据交互：

**简单串口程序实现：**

```python
import serial #导入模块
try:
  #端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
  portx="COM3"
  #波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
  bps=115200
  #超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
  timex=5
  # 打开串口，并得到串口对象
  ser=serial.Serial(portx,bps,timeout=timex)

  # 写数据
  result=ser.write("我是东小东".encode("gbk"))
  print("写总字节数:",result)

  ser.close()#关闭串口

except Exception as e:
    print("---异常---：",e)
```

**获取可用串口列表：**

```python
import serial #导入模块

import serial.tools.list_ports
port_list = list(serial.tools.list_ports.comports())
print(port_list)
if len(port_list) == 0:
   print('无可用串口')
else:
    for i in range(0,len(port_list)):
        print(port_list[i])
```

**十六进制处理：**

```python
import serial #导入模块
try:
  portx="COM3"
  bps=115200
  #超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
  timex=None
  ser=serial.Serial(portx,bps,timeout=timex)
  print("串口详情参数：", ser)

  #十六进制的发送
  result=ser.write(chr(0x06).encode("utf-8"))#写数据
  print("写总字节数:",result)

  #十六进制的读取
  print(ser.read().hex())#读一个字节

  print("---------------")
  ser.close()#关闭串口

except Exception as e:
    print("---异常---：",e)
```

**其他细节补充：**

```python
import serial #导入模块
try:

  #端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
  portx="COM3"
  #波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
  bps=115200
  #超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
  timex=5
  # 打开串口，并得到串口对象
  ser=serial.Serial(portx,bps,timeout=timex)
  print("串口详情参数：", ser)

  print(ser.port)#获取到当前打开的串口名
  print(ser.baudrate)#获取波特率

  result=ser.write("我是东小东".encode("gbk"))#写数据
  print("写总字节数:",result)

  #print(ser.read())#读一个字节
  # print(ser.read(10).decode("gbk"))#读十个字节
  #print(ser.readline().decode("gbk"))#读一行
  #print(ser.readlines())#读取多行，返回列表，必须匹配超时（timeout)使用
  #print(ser.in_waiting)#获取输入缓冲区的剩余字节数
  #print(ser.out_waiting)#获取输出缓冲区的字节数

  #循环接收数据，此为死循环，可用线程实现
  while True:
         if ser.in_waiting:
             str=ser.read(ser.in_waiting ).decode("gbk")
             if(str=="exit"):#退出标志
                 break
             else:
               print("收到数据：",str)

  print("---------------")
  ser.close()#关闭串口

except Exception as e:
    print("---异常---：",e)
```

**部分封装：**

其中读数据的封装方法并不是很好用，使用的话又得循环接收，这样反而更加复杂了

```python
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
```
