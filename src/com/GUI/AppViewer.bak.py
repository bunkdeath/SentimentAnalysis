#import sys
#from PySide.QtCore import *
#from PySide.QtGui import *
#from PySide import QtDeclarative
#import sys
#
#app = QApplication(sys.argv)
#
#view = QtDeclarative.QDeclarativeView()
#view.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)
#view.setSource('focus.qml')
#view.show()
#sys.exit(app.exec_())



from PySide import QtDeclarative
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtGui import QApplication

from PySide import QtCore
from PySide import QtDeclarative

# Create Qt application and the QDeclarative view
app = QApplication(sys.argv)
view = QtDeclarative.QDeclarativeView()
#view = QDeclarativeView()
# Create an URL to the QML file
url = QUrl('focus.qml')
# Set the QML file and show
view.setSource(url)
view.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)
view.show()
# Enter Qt main loop
sys.exit(app.exec_())