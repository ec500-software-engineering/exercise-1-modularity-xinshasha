import Input_Module_lkn
import storage
import Alert_module
import AiModule
import threading
import time
class inputThread(threading.Thread):
    def __init__(self,tName,Inqueue,Outqueue):
        threading.Thread.__init__(self)
        self.name = tName
        self.Inqueue=Inqueue
        self.Outqueue=Outqueue
        self.bo = []
        self.bp = []
        self.pul= []
        self.thread_stop = False
    def run(self):
      while self.thread_stop is False:
        try:
          path = self.Inqueue.get()
          if path == 'quit':
            self.thread_stop = True
            self.Outqueue.put('quit')
            break
          elif path == 'bo':
            self.bo=Input_Module_lkn.read_data('./'+path+'.txt')
            self.Outqueue.put(['bo',self.bo])
          elif path == 'bp':
            self.bp=Input_Module_lkn.read_data('./'+path+'.txt')
            self.Outqueue.put(['bp',self.bp])
          elif path == 'pulse':
            self.pul=Input_Module_lkn.read_data('./'+path+'.txt')
            self.Outqueue.put(['pul',self.pul])
          else:
            print("Wrong Input")
        except BaseException:
          pass


class Data_Process(threading.Thread):
  """docstring for Data_Process"""
  def __init__(self,tName,Inqueue,Outqueue):
    threading.Thread.__init__(self)
    self.Inqueue = Inqueue
    self.Outqueue = Outqueue
    self.thread_stop = False

  def run(self):
    bo_f = 0
    bp_f = 0
    pul_f = 0
    bp = []
    bo = []
    pul = []
    while self.thread_stop is False:
      try:
        data = self.Inqueue.get()
        if data == 'quit':
          self.Outqueue.put('quit')
          self.thread_stop = True
          break
        if data[0] == 'bo':
          if bo_f == 0:
            bo_f = 1
            bo = data[1]   
        if data[0] == 'bp':
          if bp_f == 0:
            bp_f = 1
            bp = data[1]
        if data[0] == 'pul':
          if pul_f == 0:
            pul_f = 1
            pul = data[1]

        if bp_f == 1 and bo_f == 1 and pul_f == 1:   
          bo_f = bp_f = pul_f = 0
          data = []
          for i in range(len(bo)):
            t=storage.storage(bo[i],bp[i],pul[i])
            data.append(t)

          alert_sys = Alert_module.Alert()
          for i in data:
            alert_sys.get_bo_data(i.read('bo'))
            alert_sys.get_bp_data(i.read('bp'))
            alert_sys.get_pul_data(i.read('pul'))
          self.Outqueue.put(['Alert',alert_sys.Alert_Output()])

          ai = AiModule.AiModule()
          ai.input_check(bo,bp,pul)
          pbo,pbp,ppul=ai.predict()
          self.Outqueue.put(['AI',(pbo,pbp,ppul)])
        else:
          print("Wating For Complete.")
          time.sleep(1)
      except BaseException:
        print("Waiting for input")
        time.sleep(3)

class OutThread(threading.Thread):
  """docstring for Data_Process"""
  def __init__(self,tName,Inqueue):
    threading.Thread.__init__(self)
    self.Inqueue = Inqueue
    self.thread_stop = False
  def run(self):
    while self.thread_stop is False:
      try:
        d = self.Inqueue.get()
        if d == 'quit':
          self.thread_stop = True
          break
        elif d[0] == 'AI':
          print('predicted blood oxygen is: ' + str(d[1][0]))
          print('predicted blood pressure is: ' + str(d[1][1]))
          print('predicted pulse is: ' + str(d[1][2]))
        elif d[0] == 'Alert':
          alert_number = d[1]
          if alert_number == 0:
            print("OK")
          elif alert_number == 1:
            print("BO Alert!")
          elif alert_number == 2:
            print("BP Alert!")
          elif alert_number == 3:
            print("PUL Alert!")

      except BaseException:
        time.sleep(1)
