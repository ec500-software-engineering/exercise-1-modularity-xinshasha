#Copyright @Xinsha Wang
import queue
import Thread_definition
q1 = queue.Queue()
q2 = queue.Queue()
q3 = queue.Queue()
t1 = Thread_definition.inputThread('InputThread',q1,q2)
t2 = Thread_definition.Data_Process('Data',q2,q3)
t3 = Thread_definition.OutThread('Out',q3)
t1.start()
t2.start()
t3.start()
q1.put('bo')
q1.put('bp')
q1.put('pulse')
q1.put('quit')


	



