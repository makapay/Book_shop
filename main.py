from PyQt6 import QtWidgets, QtCore
from Book_shop_main import Ui_Form
import MySQLdb as mbd

conn = mbd.connect('localhost', 'root', '', 'Book_Shop')

def get_genres():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM genre")
    res = cursor.fetchall()
    return res

def get_books_by_genre(id_genre):
    cursor = conn.cursor()
    cursor.execute(f"SELECT id, name, price FROM books WHERE id_genre = {id_genre} AND quantity > 0")
    res = cursor.fetchall()
    return res

class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        res_data = get_genres()
        y = 100
        for id, name in res_data:
            group_box = QtWidgets.QGroupBox(name, self)
            group_box.setGeometry(QtCore.QRect(10, y, 200, 100))
            y += 130
            books_layout = QtWidgets.QVBoxLayout()
            books = get_books_by_genre(id)
            for id, name, price in books:
                check_box = QtWidgets.QCheckBox(f"{name} {price} руб.", self)
                books_layout.addWidget(check_box)
            group_box.setLayout(books_layout)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wind = MainWindow()
    wind.show()
    sys.exit(app.exec())
