import sys
from PyQt5 import QtCore, QtSql, Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                             QTabWidget, QHBoxLayout, QTableWidget,
                             QPushButton, QTableWidgetItem, QAbstractItemView,
                             QTableView, QAction, qApp, QMenu, QMainWindow,
                             QListView, QInputDialog, QListWidget, QListWidgetItem)
from PyQt5.QtGui import QIcon, QPixmap
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
        self.addWidget(self.customers)
        # self.model = QtSql.QSqlRelationalTableModel()
        # self.model.setTable('list')
        # self.model.setRelation(1, QtSql.QSqlRelation('movies', 'id', 'title'))
        # self.model.setRelation(2, QtSql.QSqlRelation('customers', 'phone', 'name'))
        # self.model.removeColumns(0, 2)
        # self.model.removeColumns(0, 1)
        # customers.setModel(self.model)
        # self.parent.movies.movies.itemClicked.connect(self.model.select)
        self.parent.movies.movies.clicked.connect(self.test)

    def test(self, current):
        print(current.data())
        # q = QtSql.QSqlQuery('''
        #         SELECT list.CustomerID
        #         FROM customers
        #         INNER JOIN list on list.CustomerID = customer.phone
        #         INNER JOIN movies on movies.id = list.MovieID
        #         ORDER BY list.Time
        #         ''')
        # q = QtSql.QSqlQuery('SELECT customers.phone')
        # self.model.setQuery(q)
        self.customers.clear()
        for item in self.parent.parent.db.getMovieList(current.data()):
            print(item)
            self.customers.addItem(str(item[0]))
        # self.model.select()


class CustomerList(QListView):
    def __init__(self, parent=None):
        super().__init__(parent)

    # @override
    # def currentChanged(self, current, previous):
    #     super.currentChanged(current, previous)
    #     print('changed')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
