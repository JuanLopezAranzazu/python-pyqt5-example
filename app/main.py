from PyQt5.QtWidgets import *
import database

# utils

STATES: list[str] = ["completed", "active", "inactive"]

database.init()

def create_note_ui():
  try:
    item = list_states.currentItem()
    print(item.text())
    
    if len(title.text()) == 0 or not item:
      message = QMessageBox()
      message.setWindowTitle("Error")
      message.setText("Invalid entry data")
      message.exec_()
      return 
    
    database.create_note(title=title.text(), state=item.text())
    
    title.setText(None)
  
  except Exception as error:
    print("Error code:", error)
  
def get_notes_ui():
  try:
    notes = database.get_notes()
    
    while result_layout.count() > 0:
      item = result_layout.takeAt(0)
      widget = item.widget()
      widget.deleteLater()

    for note in notes:
      note_label = f"Title: {note[1]}, state: {note[2]}"
      result_layout.addWidget(QLabel(note_label))
  
  except Exception as error:
    print("Error code:", error)

def get_notes_by_state_ui():
  try:
    item = list_states2.currentItem()
    print(item.text())
    
    if not item:
      message = QMessageBox()
      message.setWindowTitle("Error")
      message.setText("Invalid entry data")
      message.exec_()
      return 
    
    notes = database.get_notes_by_state(state=item.text())
    
    while result_layout.count() > 0:
      item = result_layout.takeAt(0)
      widget = item.widget()
      widget.deleteLater()
      
    for note in notes:
      note_label = f"Title: {note[1]}, state: {note[2]}"
      result_layout.addWidget(QLabel(note_label))

  except Exception as error:
    print("Error code:", error)

# ui

def main():
  app = QApplication([])
  window = QWidget()
  window.setGeometry(100, 100, 500, 600)
  window.setWindowTitle("MY APPLICATION EXAMPLE PYQT")

  layout = QVBoxLayout()
  
  tabs = QTabWidget()
  tabs.addTab(create_tab1(), "Tab1")
  tabs.addTab(create_tab2(), "Tab2")
  
  layout.addWidget(tabs)
  
  window.setLayout(layout)
  window.show()
  app.exec_()
  
  
def create_tab1():
  tab1 = QWidget()
  
  layout = QVBoxLayout()
  
  form_layout = QFormLayout()
  
  global title
  title = QLineEdit()
  title_label = QLabel("Title:")
  submit_btn = QPushButton("Create note")
  submit_btn.clicked.connect(create_note_ui)
  
  global list_states
  list_states = QListWidget()
  
  for i in range(0, len(STATES)):
    list_states.insertItem(i, STATES[i])

  list_states.setCurrentRow(0)
  
  form_layout.addRow(title_label, title)
  form_layout.addRow(list_states)
  form_layout.addRow(submit_btn)
   
  layout.addLayout(form_layout)

  tab1.setLayout(layout)
  return tab1

def create_tab2():
  tab2 = QWidget()
  layout = QVBoxLayout()
  
  form_layout = QFormLayout()
  submit_btn = QPushButton("Get notes")
  submit_btn.clicked.connect(get_notes_ui)
  query_btn = QPushButton("Get notes by state")
  query_btn.clicked.connect(get_notes_by_state_ui)
  
  global list_states2
  list_states2 = QListWidget()
  
  for i in range(0, len(STATES)):
    list_states2.insertItem(i, STATES[i])

  list_states2.setCurrentRow(0)  

  form_layout.addRow(list_states2)
  form_layout.addRow(query_btn)
  form_layout.addRow(submit_btn)
  
  global result_layout
  result_layout = QVBoxLayout()
  
  notes = database.get_notes()
  for note in notes:
    note_label = f"Title: {note[1]}, state: {note[2]}"
    result_layout.addWidget(QLabel(note_label))
  
  layout.addLayout(form_layout)
  layout.addLayout(result_layout)
  
  tab2.setLayout(layout)
  return tab2

if __name__ == "__main__":
  main()
  

