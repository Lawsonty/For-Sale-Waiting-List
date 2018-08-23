import sys
from PyQt5 import QtSql
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                             QHBoxLayout,
                             QPushButton,
                             QAction,  QMainWindow,
                             QListView, QInputDialog, QListWidget,
                             QDialog, QLineEdit)
import backend


class App(QMainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.db = backend.DBM()
        bar = self.menuBar()
        file = bar.addMenu("File")
        quit = QAction("Quit", self)
        file.addAction(quit)
        self.setCentralWidget(MainArea(parent=self))


class MainArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.movies = MovieLayout(parent)
        self.customers = CustomerLayout(self)
        layout.addLayout(self.movies)
        layout.addLayout(self.customers)


class MovieLayout(QVBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.movies = QListView()
        self.addWidget(self.movies)
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('movies.db')
        model = QtSql.QSqlTableModel()
        model.setTable('movies')
        q = QtSql.QSqlQuery('SELECT title FROM movies')
        model.setQuery(q)
        model.select()
        self.movies.setModel(model)

        buttons = QHBoxLayout()
        addButton = QPushButton('+')
        addButton.clicked.connect(self.addMovie)
        buttons.addWidget(QPushButton('-'))
        buttons.addWidget(addButton)
        self.addLayout(buttons)
        self.model = model

    def addMovie(self):
        text, ok = QInputDialog.getText(self.parent, 'Enter New movie',
                                        'Enter a Movie Title')
        if ok:
            self.parent.db.addMovie(text)
            self.model.select()


class CustomerLayout(QVBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.customers = QListWidget()
        self.movieSelected = None
        self.addWidget(self.customers)
        self.parent.movies.movies.clicked.connect(self.test)

        buttons = QHBoxLayout()
        addButton = QPushButton('+')
        delButton = QPushButton('-')
        buttons.addWidget(delButton)
        buttons.addWidget(addButton)
        self.addLayout(buttons)
        addButton.clicked.connect(self.addCustomer)

    def addCustomer(self, customer):
        if self.movieSelected is None:
            return
        d = self.CustomerInput(parent=self.parent.parent)
        d.exec_()
        print(d.getData())
        ok, name, number = d.getData()
        if ok:
            self.parent.parent.db.addCustomer(name, number)
            print(self.movieSelected)
            self.parent.parent.db.addCustomertoMovie(number,
                                                     self.movieSelected)
            self.customers.addItem(name + ' ' + number)
        # self.parent.parent.db.addCustomer

    def test(self, current):
        print(current.data())
        self.movieSelected = current.data()
        self.customers.clear()
        for item in self.parent.parent.db.getMovieList(current.data()):
            print(item)
            self.customers.addItem(str(item[0]))

    class CustomerInput(QDialog):
        def __init__(self, parent=None):
            self.clean = False
            super().__init__(parent)
            layout = QVBoxLayout()
            self.setWindowTitle('Add Customer')
            self.setLayout(layout)
            layout1 = QHBoxLayout()
            layout2 = QHBoxLayout()
            layout3 = QHBoxLayout()
            layout.addLayout(layout1)
            layout.addLayout(layout2)
            layout.addLayout(layout3)
            layout1.addWidget(QLabel('Name'))
            self.nameEdit = QLineEdit()
            layout1.addWidget(self.nameEdit)

            layout2.addWidget(QLabel('Number'))
            self.numberEdit = QLineEdit()
            layout2.addWidget(self.numberEdit)

            layout3.addWidget(QLabel('Name'))
            self.okButton = QPushButton('Ok')
            self.cancelButton = QPushButton('Cancel')
            layout3.addWidget(self.okButton)
            layout3.addWidget(self.cancelButton)
            self.okButton.clicked.connect(self.ok)
            self.cancelButton.clicked.connect(self.cancel)

        def getData(self):
            return self.clean, self.nameEdit.text(), self.numberEdit.text()

        def ok(self):
            self.clean = True
            if self.validate():
                self.close()

        def cancel(self):
            self.clean = False
            self.close()

        def validate(self):
            if not len(self.nameEdit.text().strip()):
                return False
            return True


class CustomerList(QListView):
    def __init__(self, parent=None):
        super().__init__(parent)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
