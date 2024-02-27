from math import pi,sin,cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task

#this is where you display thingsd
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        #from panda3d doccumentation
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25,0.25,0.25)
        self.scene.setPos(-8,42,0)

        #this part is for the camera
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi/180.0)
        self.camera.setPos(20*sin(angleRadians),-20*cos(angleRadians),3)
        self.camera.setHpr(angleDegrees,0,0)
        return Task.cont

app = MyApp()
app.run()