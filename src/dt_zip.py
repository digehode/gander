from  DType import *



pk= DType("PKZip")
t= DTest("magic word", requirements=[("bytes",(0,4))],priority=10,fn=lambda x: x.hbit(0)=="50" and x.hbit(1)=="4b" and x.hbit(2)=="03" and x.hbit(3)=="04")
pk.addTest(t)
