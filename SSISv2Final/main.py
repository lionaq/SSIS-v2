from SSIS_GUI import Ui_SSIS, studentIdPopUp, studentNamePopUp, studentGenderPopUp, studentYearPopUp, studentAddWindow, studentCoursePopUp, courseCodePopUp, courseLinePopUp, courseAddWindow, show_error_message, deletePopUp
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QSortFilterProxyModel
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import mySQLconnection as mysql

class function(Ui_SSIS):
    def __init__(self, SSIS):
        self.studentPK = []
        self.coursePK = []
        self.modelStudent = QStandardItemModel()
        self.modelCourse = QStandardItemModel()
        Ui_SSIS.setupUi(self, SSIS)
        self.searchLineInit()
        self.studentTable.setModel(self.filterStudent)
        self.courseTable.setModel(self.filterCourse)
        self.studentIdRadio.toggled.connect(lambda a :self.filterStudent.setFilterKeyColumn(0) )
        self.studentNameRadio.toggled.connect(lambda a : self.filterStudent.setFilterKeyColumn(1))
        self.studentGenderRadio.toggled.connect(lambda a : self.filterStudent.setFilterKeyColumn(2))
        self.studentYearLevelRadio.toggled.connect(lambda a : self.filterStudent.setFilterKeyColumn(3))
        self.studentCourseCodeRadio.toggled.connect(lambda a : self.filterStudent.setFilterKeyColumn(4))
        self.courseCourseCodeRadio.toggled.connect(lambda a : self.filterCourse.setFilterKeyColumn(0))
        self.courseCourseRadio.toggled.connect(lambda a : self.filterCourse.setFilterKeyColumn(1))
        self.addButtonStudent.clicked.connect(self.addStudentPopUp)
        self.addButtonCourse.clicked.connect(self.addCoursePopUp)
        self.studentTable.selectionModel().selectionChanged.connect(self.cellSelectedStudent)
        self.courseTable.selectionModel().selectionChanged.connect(self.cellSelectedCourse)
        self.studentTable.doubleClicked.connect(self.handleDataChangedStudent)
        self.courseTable.doubleClicked.connect(self.handleDataChangedCourse)
        self.studentTable.pressed.connect(self.cellSelectedStudent)
        self.courseTable.clicked.connect(self.cellSelectedCourse)
        self.deleteButtonStudent.clicked.connect(self.deleteRowStudent)
        self.deleteButtonCourse.clicked.connect(self.deleteRowCourse)   
        self.updateTable(0)
        self.updateTable(1)

    def duplicateChecker(self, stringVal, value):
        list = [item[0] for item in mysql.queryTable(value)]
        for row in list:
            #print(row)
            if row == stringVal:
                show_error_message("STUDENT ID ALREADY EXISTS")
                return True
            
        return False
        
    def handleDataChangedStudent(self, index):
        column = index.column()
        model_index = self.modelStudent.index(index.row(), column)
        columnName = self.modelStudent.horizontalHeaderItem(column).text()
        inputWindow = None
        data = 0
       #print("COLUMN IS:", column, "PK IS:", self.studentPK[0])

        match column:
            case 0:
                inputWindow = studentIdPopUp()
            case 1:
                inputWindow = studentNamePopUp()
            case 2:
                inputWindow = studentGenderPopUp()
            case 3:
                inputWindow = studentYearPopUp()
            case 4:
                inputWindow = studentCoursePopUp() 
                items = [item[0] for item in mysql.queryTable(1)]
                for item in items:
                    inputWindow.course_combo_box.addItem(item)
            case _:
                return
            
        if inputWindow.exec() == 1:
            data = inputWindow.return_info()

        if data == 0:
            return
        
        if column == 0:
           if self.duplicateChecker(data, 0) == True:
                return
           else:
                mysql.editTable(columnName, [data, self.studentPK[0]], 0)
                self.updateTable(0)
                return
    
        self.modelStudent.setData(model_index, data, Qt.ItemDataRole.EditRole)
        #print("EDITED")
        mysql.editTable(columnName, [data, self.studentPK[0]], 0)
        
    def handleDataChangedCourse(self, index):
        # Retrieve the edited data and its row and column index
        column = index.column()
        model_index = self.modelCourse.index(index.row(), column)
        columnName = self.modelCourse.horizontalHeaderItem(column).text()
        inputWindow = None
        data = 0
        match column:
            case 0:
                inputWindow = courseCodePopUp()
            case 1:
                inputWindow = courseLinePopUp()
            case _:
                return
        
        if inputWindow.exec() == 1:
            data = inputWindow.return_info()

        if data == 0:
            return
        
        if column == 0:
           if self.duplicateChecker(data, 1) == True:
                return
           else:
                mysql.editTable(columnName, [data, self.coursePK[0]], 1)
                self.updateTable(0)
                self.updateTable(1)
                return
           
        self.modelCourse.setData(model_index, data, Qt.ItemDataRole.EditRole)
        #print("EDITED")
        mysql.editTable(columnName, [data, self.coursePK[0]], 1)

    def cellSelectedStudent(self):
        selected_indexes = self.studentTable.selectedIndexes()
        first_column_data = []

        for index in selected_indexes:
            row = index.row()
            item = self.studentTable.model().index(row, 0).data()  # Retrieve data from the first column
            if item not in first_column_data:
                first_column_data.append(item)
       

        self.studentPK = first_column_data
        #print(self.studentPK)

    def cellSelectedCourse(self):
        selected_indexes = self.courseTable.selectedIndexes()
       # print(selected_indexes[0])
        first_column_data = []

        for index in selected_indexes:
            row = index.row()
            item = self.courseTable.model().index(row, 0).data()  # Retrieve data from the first column
            if item not in first_column_data:
                first_column_data.append(item)

        self.coursePK = first_column_data
        #print(self.coursePK)

    def deleteRowStudent(self):
        popUp = deletePopUp()
        if popUp.exec() == 1:
            for item in self.studentPK:
                #print(item)
                mysql.deleteTableRow(item, 0)
                self.updateTable(0)

    def deleteRowCourse(self):
        popUp = deletePopUp()
        if popUp.exec() == 1:
            for item in self.coursePK:
                #print(item)
                mysql.deleteTableRow(item, 1)
                self.updateTable(0)
                self.updateTable(1)

    def searchLineInit(self):
        self.filterStudent = QSortFilterProxyModel()
        self.filterCourse = QSortFilterProxyModel()

        self.filterStudent.setSourceModel(self.modelStudent)
        self.filterStudent.setFilterKeyColumn(0)
        self.filterStudent.setSourceModel(self.modelStudent)
        self.studentLineEdit.textChanged.connect(self.filterStudent.setFilterRegularExpression)

        self.filterCourse.setSourceModel(self.modelCourse)
        self.filterCourse.setFilterKeyColumn(0)
        self.filterCourse.setSourceModel(self.modelCourse)
        self.courseLineEdit.textChanged.connect(self.filterCourse.setFilterRegularExpression)

    def addStudentPopUp(self):
        inputwindowStudent = studentAddWindow() 
        items = [item[0] for item in mysql.queryTable(1)]
        for item in items:
            inputwindowStudent.course_combo_box.addItem(item)

        if inputwindowStudent.exec() == 1:
            data = inputwindowStudent.return_info()
            if data == 0:
                return
        
            if self.duplicateChecker(data[0],0) != True and data != 0:
                mysql.insertTable(data, 0)
                self.updateTable(0)

    def addCoursePopUp(self):
        inputwindowCourse = courseAddWindow()

        if inputwindowCourse.exec() == 1:
            data = inputwindowCourse.return_info()
            if data == 0:
                return
            
            #print(data)
            if self.duplicateChecker(data[0], 1) != True and data != 0:
                mysql.insertTable(data, 1)
                self.updateTable(1)
                
    def updateTable(self, choice):
        if choice == 0:
                self.modelStudent.clear()
                self.displayStudentTable(mysql.queryTable(0))
                self.studentTable.setModel(self.filterStudent)
        elif choice == 1:
                self.modelCourse.clear()
                self.displayCourseTable(mysql.queryTable(1))
                self.courseTable.setModel(self.filterCourse)
        else:
                print("No choice selected")

    def displayStudentTable(self, rows):
        # Set the column headers
        headers = ["StudentID", "Name", "Gender", "YearLevel", "CourseCode"]
        self.modelStudent.setHorizontalHeaderLabels(headers)
        self.studentTable.setColumnWidth(1,324)
        for row in rows:
            print(row)
            item_row = []
            for value in row:
                item = QStandardItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                item_row.append(item)
            self.modelStudent.appendRow(item_row)
        return self.modelStudent
    
    def displayCourseTable(self, rows):
        # Set the column headers
        headers = ["CourseCode", "Course"]
        self.modelCourse.setHorizontalHeaderLabels(headers)
        self.courseTable.setColumnWidth(1,624)
        for row in rows:
            item_row = []
            for value in row:
                item = QStandardItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                #print(value)
                item_row.append(item)
            self.modelCourse.appendRow(item_row)
        return self.modelCourse
      
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SSIS = QtWidgets.QMainWindow()
    ui = function(SSIS)
    app.aboutToQuit.connect(mysql.closeConnection)
    SSIS.show()

    sys.exit(app.exec())
