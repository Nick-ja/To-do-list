from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

from PyQt5.QtWidgets import QMessageBox

# Create a database or connect to one
conn = sqlite3.connect('mylist.db')
# Create a cursor
c = conn.cursor()

# Create a Table
c.execute(""" CREATE TABLE if not exists todo_list(
    list_item text)
    """)

# Commit the changes
conn.commit()

# Close our connection
conn.close()


class Ui_Title(object):
    def setupUi(self, Title):
        Title.setObjectName("Title")
        Title.resize(613, 737)
        self.centralwidget = QtWidgets.QWidget(Title)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 591, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_push_button = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked=lambda: self.add())
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.add_push_button.setFont(font)
        self.add_push_button.setObjectName("add_push_button")
        self.horizontalLayout.addWidget(self.add_push_button)
        self.delete_push_button = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked=lambda: self.delete())
        font = QtGui.QFont()
        font.setPointSize(11)
        self.delete_push_button.setFont(font)
        self.delete_push_button.setObjectName("delete_push_button")
        self.horizontalLayout.addWidget(self.delete_push_button)
        self.clear_push_button = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked=lambda: self.clear())
        font = QtGui.QFont()
        font.setPointSize(11)
        self.clear_push_button.setFont(font)
        self.clear_push_button.setObjectName("clear_push_button")
        self.horizontalLayout.addWidget(self.clear_push_button)
        self.savedb_push_button = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked=lambda: self.save())
        font = QtGui.QFont()
        font.setPointSize(11)
        self.savedb_push_button.setFont(font)
        self.savedb_push_button.setObjectName("savedb_push_button")
        self.horizontalLayout.addWidget(self.savedb_push_button)
        self.add_item_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.add_item_lineEdit.setGeometry(QtCore.QRect(10, 10, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add_item_lineEdit.setFont(font)
        self.add_item_lineEdit.setText("")
        self.add_item_lineEdit.setObjectName("add_item_lineEdit")
        self.mylist_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.mylist_listWidget.setGeometry(QtCore.QRect(10, 110, 591, 531))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.mylist_listWidget.setFont(font)
        self.mylist_listWidget.setObjectName("mylist_listWidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 650, 591, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.move_up_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2, clicked=lambda: self.move_up())
        font = QtGui.QFont()
        font.setPointSize(11)
        self.move_up_pushButton.setFont(font)
        self.move_up_pushButton.setObjectName("move_up_pushButton")
        self.horizontalLayout_2.addWidget(self.move_up_pushButton)
        self.move_down_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2, clicked=lambda: self.move_down())
        font = QtGui.QFont()
        font.setPointSize(11)
        self.move_down_pushButton.setFont(font)
        self.move_down_pushButton.setObjectName("move_down_pushButton")
        self.horizontalLayout_2.addWidget(self.move_down_pushButton)
        Title.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Title)
        self.statusbar.setObjectName("statusbar")
        Title.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(Title)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 21))
        self.menubar.setObjectName("menubar")
        Title.setMenuBar(self.menubar)
        self.actionClose = QtWidgets.QAction(Title)
        self.actionClose.setObjectName("actionClose")

        self.retranslateUi(Title)
        QtCore.QMetaObject.connectSlotsByName(Title)
        # Grab all the items from the database
        self.grab_all()

    # Grab items from the database (function)
    def grab_all(self):
        # Create a database or connect to one
        conn = sqlite3.connect('mylist.db')
        # Create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()

        # Commit the changes
        conn.commit()

        # Close our connection
        conn.close()

        # Loop thru records an add to screen
        for record in records:
            self.mylist_listWidget.addItem(str(record[0]))

    # Add item to list
    def add(self):
        # Grab the item from the list box
        item = self.add_item_lineEdit.text()

        # Add item to list
        self.mylist_listWidget.addItem(item)

        # Clear the item box
        self.add_item_lineEdit.setText("")

    # Delete item from the list
    def delete(self):
        # Grab the selected row or current row
        clicked = self.mylist_listWidget.currentRow()

        # Delete selected row
        self.mylist_listWidget.takeItem(clicked)

    # Clear the list
    def clear(self):
        self.mylist_listWidget.clear()

    def move_up(self):
        index = self.mylist_listWidget.currentRow()
        if index >= 1:
            item = self.mylist_listWidget.takeItem(index)
            self.mylist_listWidget.insertItem(index-1,item)
            self.mylist_listWidget.setCurrentItem(item)

    def move_down(self):
        index = self.mylist_listWidget.currentRow()
        if index < self.mylist_listWidget.count()-1:
            item = self.mylist_listWidget.takeItem(index)
            self.mylist_listWidget.insertItem(index + 1, item)
            self.mylist_listWidget.setCurrentItem(item)

    # Save item to the list
    def save(self):
        # Create a database or connect to one
        conn = sqlite3.connect('mylist.db')
        # Create a cursor
        c = conn.cursor()

        # Delete everything in the database table
        c.execute('DELETE FROM todo_list;', )

        # Create blank list to hold toto items
        items = []
        # Loop through the listWidget and pull out each item
        for index in range(self.mylist_listWidget.count()):
            items.append(self.mylist_listWidget.item(index))
        # Reformat object into text
        for item in items:
            # print(item.text())
            # Add stuff to the table
            c.execute("INSERT INTO todo_list VALUES (:item)",
                      {
                          'item': item.text(),
                      })

        # Commit the changes
        conn.commit()

        # Close our connection
        conn.close()

        # Pop up box
        msg = QMessageBox()
        msg.setWindowTitle("Saved to Database!")
        msg.setText("Your Todo list has been saved!")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def retranslateUi(self, Title):
        _translate = QtCore.QCoreApplication.translate
        Title.setWindowTitle(_translate("Title", "To Do List"))
        self.add_push_button.setText(_translate("Title", "Add Item To List"))
        self.delete_push_button.setText(_translate("Title", "Delete Item From List"))
        self.clear_push_button.setText(_translate("Title", "Clear list"))
        self.savedb_push_button.setText(_translate("Title", "Save To Database"))
        self.move_up_pushButton.setText(_translate("Title", "↑ Move Item Up ↑"))
        self.move_down_pushButton.setText(_translate("Title", "↓ Move Item Down ↓"))
        self.actionClose.setText(_translate("Title", "Close"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Title = QtWidgets.QMainWindow()
    ui = Ui_Title()
    ui.setupUi(Title)
    Title.show()
    sys.exit(app.exec_())
