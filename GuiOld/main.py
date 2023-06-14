from SSIS_GUI import Ui_SSIS
from PyQt6.QtCore import Qt, QSortFilterProxyModel
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QDialog, QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem,QIntValidator
import mySQLconnection as mysql



def show_error_message(message):
    error_box = QMessageBox()
    error_box.setIcon(QMessageBox.Icon.Critical)
    error_box.setWindowTitle("Error")
    error_box.setText("An error occurred.")
    error_box.setInformativeText(message)
    error_box.exec()

class studentIdPopUp(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("StudentID Window")
        student_id_label = QLabel("Student ID:")
        self.student_id_line_edit = QLineEdit()
        self.student_id_line_edit.setValidator(QIntValidator())
        self.student_id_line_edit.setPlaceholderText("XXXX-XXXX (input No. Only)")
        self.student_id_line_edit.textEdited.connect(self.add_dash)
        self.student_id_line_edit.setMaxLength(9)


        self.confirm_button = QtWidgets.QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        # Create a layout for the input window
        layout = QVBoxLayout()
        self.setLayout(layout)
    
        # Add the labels, line edits, and combo boxes to the layout

        layout.addWidget(student_id_label)
        layout.addWidget(self.student_id_line_edit)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)
        
    def add_dash(self, text):
        # Remove any existing dashes from the text
        text = text.replace("-", "")
        # Insert a dash after the 5th character
        if len(text) >= 5:
            text = text[:4] + "-" + text[4:]
            print(len(text))

        # Set the updated text in the line edit
        self.student_id_line_edit.setText(text)

    def return_info(self):
        
        if len(self.student_id_line_edit.text()) >= 1:
            return self.student_id_line_edit.text()
        else:
            show_error_message("BLANK FIELD, TRY AGAIN")
            return 0

class studentNamePopUp(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Name Window")

        # Create labels
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()
        self.name_line_edit.setMaxLength(80)

        self.confirm_button = QtWidgets.QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        # Create a layout for the input window
        layout = QVBoxLayout()
        self.setLayout(layout)
    
        # Add the labels, line edits, and combo boxes to the layout

        layout.addWidget(name_label)
        layout.addWidget(self.name_line_edit)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)

    def return_info(self):      
        if len(self.name_line_edit.text()) >= 1:
            return self.name_line_edit.text()
        else:
            show_error_message("BLANK FIELD, TRY AGAIN")
            return 0

class studentGenderPopUp(QDialog):
    

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gender Window")
        gender_label = QLabel("Gender:")
        self.gender_combo_box = QComboBox()
        self.gender_combo_box.addItems(["M", "F", "O"])
        self.confirm_button = QtWidgets.QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)
        # Create a layout for the input window
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(gender_label)
        layout.addWidget(self.gender_combo_box)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)

    def return_info(self):
        
        return self.gender_combo_box.currentText()

class studentYearPopUp(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Year Window")
        year_level_label = QLabel("Year Level:")

        # Create combo boxes
        self.year_level_combo_box = QComboBox()
        self.year_level_combo_box.addItems(["1", "2", "3", "4"])

        self.confirm_button = QtWidgets.QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        # Create a layout for the input window
        layout = QVBoxLayout()
        self.setLayout(layout)
    
        # Add the labels, line edits, and combo boxes to the layout

        layout.addWidget(year_level_label)
        layout.addWidget(self.year_level_combo_box)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)
        

    def return_info(self):
        return self.year_level_combo_box.currentText()
    
class studentCoursePopUp(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Course Window")

        course_label = QLabel("Course Code:")

        self.course_combo_box = QComboBox()

        self.confirm_button = QtWidgets.QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(course_label)
        layout.addWidget(self.course_combo_box)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)
        

    def return_info(self):
        return self.course_combo_box.currentText()

class studentAddWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ADD Window")

        # Create labels
        name_label = QLabel("Name:")
        student_id_label = QLabel("Student ID:")
        year_level_label = QLabel("Year Level:")
        course_label = QLabel("Course Code:")
        gender_label = QLabel("Gender:")

        # Create line edits
        self.name_line_edit = QLineEdit()
        self.student_id_line_edit = QLineEdit()
        self.student_id_line_edit.setValidator(QIntValidator())
        self.student_id_line_edit.setPlaceholderText("XXXX-XXXX (input No. Only)")
        self.student_id_line_edit.textEdited.connect(self.add_dash)
        self.name_line_edit.setMaxLength(80)
        self.student_id_line_edit.setMaxLength(9)
        

        # Create combo boxes
        self.year_level_combo_box = QComboBox()
        self.year_level_combo_box.addItems(["1", "2", "3", "4"])
        self.course_combo_box = QComboBox()
        self.gender_combo_box = QComboBox()
        self.gender_combo_box.addItems(["M", "F", "O"])

        self.confirm_button = QtWidgets.QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        # Create a layout for the input window
        layout = QVBoxLayout()
        self.setLayout(layout)
    
        # Add the labels, line edits, and combo boxes to the layout

        layout.addWidget(student_id_label)
        layout.addWidget(self.student_id_line_edit)
        layout.addWidget(name_label)
        layout.addWidget(self.name_line_edit)
        layout.addWidget(gender_label)
        layout.addWidget(self.gender_combo_box)
        layout.addWidget(year_level_label)
        layout.addWidget(self.year_level_combo_box)
        layout.addWidget(course_label)
        layout.addWidget(self.course_combo_box)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)
        
    
    def add_dash(self, text):
        # Remove any existing dashes from the text
        text = text.replace("-", "")
        # Insert a dash after the 5th character
        if len(text) >= 5:
            text = text[:4] + "-" + text[4:]
            print(len(text))

        # Set the updated text in the line edit
        self.student_id_line_edit.setText(text)



    def return_info(self):
        list = [self.student_id_line_edit.text(), self.name_line_edit.text(), self.gender_combo_box.currentText(), int(self.year_level_combo_box.currentText()), self.course_combo_box.currentText()]
        if len(list[4]) < 1:
            show_error_message("NO COURSES AVAILABLE, PLEASE ADD A COURSE")
            return 0
        
        if len(list[0]) >= 1 and len(list[1]) >= 1:
            return list
        else:
            show_error_message("BLANK FIELDS, TRY AGAIN")
            return 0

class courseCodePopUp(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Course Code Window")

        self.courseCodeLabel = QLabel("Course Code:")

        self.courseCodeLine = QLineEdit()
        self.courseCodeLine.setMaxLength(10)
        
        self.confirm_button = QtWidgets.QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.courseCodeLabel)
        layout.addWidget(self.courseCodeLine)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)
    
    def return_info(self):
        if self.courseCodeLine.text():
            return self.courseCodeLine.text()
        else:
            show_error_message("BLANK FIELDS, TRY AGAIN")
            return 0
        
class courseLinePopUp(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Course Window")

        self.courseLabel = QLabel("Course:")

        self.courseLine = QLineEdit()
        self.courseLine.setMaxLength(80)
        
        self.confirm_button = QtWidgets.QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.courseLabel)
        layout.addWidget(self.courseLine)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)
    
    def return_info(self):
        if self.courseLine.text():
            return self.courseLine.text()
        else:
            show_error_message("BLANK FIELDS, TRY AGAIN")
            return 0
        
class courseAddWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ADD Window")

        # Create labels
        self.courseCodeLabel = QLabel("Course Code:")
        self.courseLabel = QLabel("Course:")

        # Create line edits
        self.courseCodeLine = QLineEdit()
        self.courseLine = QLineEdit()
        self.courseCodeLine.setMaxLength(10)
        self.courseLine.setMaxLength(80)
        
        self.confirm_button = QtWidgets.QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        # Create a layout for the input window
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Add the labels, line edits, and combo boxes to the layout
        layout.addWidget(self.courseCodeLabel)
        layout.addWidget(self.courseCodeLine)
        layout.addWidget(self.courseLabel)
        layout.addWidget(self.courseLine)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)
    
    def return_info(self):
        list = [self.courseCodeLine.text(), self.courseLine.text()]
        if len(list[0]) >= 1 and len(list[1]) >= 1:
            return list
        else:
            show_error_message("BLANK FIELDS, TRY AGAIN")
            return 0



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
        self.addButtonStudent.clicked.connect(self.addStudentPopUp)
        self.addButtonCourse.clicked.connect(self.addCoursePopUp)
        self.studentTable.selectionModel().selectionChanged.connect(self.cellSelectedStudent)
        self.courseTable.selectionModel().selectionChanged.connect(self.cellSelectedCourse)
        self.studentTable.doubleClicked.connect(self.handleDataChangedStudent)
        self.courseTable.doubleClicked.connect(self.handleDataChangedCourse)
        #self.modelStudent.dataChanged.connect(self.handleDataChangedStudent)
        #self.modelCourse.dataChanged.connect(self.handleDataChangedCourse)
        self.studentTable.pressed.connect(self.cellSelectedStudent)
        self.courseTable.clicked.connect(self.cellSelectedCourse)
        self.deleteButtonStudent.clicked.connect(self.deleteRowStudent)
        self.deleteButtonCourse.clicked.connect(self.deleteRowCourse)
        
        self.updateTable(0)
        self.updateTable(1)
        #super().__init__(SSIS)

    def duplicateChecker(self, stringVal, value):
        list = [item[0] for item in mysql.queryTable(value)]
        print("HEY")
        for row in list:
            print(row)
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
        print("COLUMN IS:", column, "PK IS:", self.studentPK[0])

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
        print("EDITED")
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
                print("Course")
                inputWindow = courseLinePopUp()
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
                mysql.editTable(columnName, [data, self.coursePK[0]], 1)
                self.updateTable(0)
                self.updateTable(1)
                return
           
        self.modelCourse.setData(model_index, data, Qt.ItemDataRole.EditRole)
        print("EDITED")
        mysql.editTable(columnName, [data, self.coursePK[0]], 1)


    def cellSelectedStudent(self, selected):
        selected_indexes = self.studentTable.selectedIndexes()
        first_column_data = []

        for index in selected_indexes:
            row = index.row()
            item = self.studentTable.model().index(row, 0).data()  # Retrieve data from the first column
            if item not in first_column_data:
                first_column_data.append(item)
       

        self.studentPK = first_column_data
        print(self.studentPK)

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
        for item in self.studentPK:
            print(item)
            mysql.deleteTableRow(item, 0)
            self.updateTable(0)

    def deleteRowCourse(self):
        for item in self.coursePK:
            print(item)
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
        for row in rows:
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
