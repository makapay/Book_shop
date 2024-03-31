from PyQt6 import QtWidgets
from ShopMain import Ui_MainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QByteArray
import MySQLdb as mdb
##from PIL import Image

conn = mdb.connect('localhost', 'root', 'root', 'clothes_Shop')
def get_data():
    cursor = conn.cursor()
    cursor.execute("CALL `HP1`(g)")
    res = cursor.fetchall()
    return  res

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self). __init__(parent)
        self.setupUi(self)