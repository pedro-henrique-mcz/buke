import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
)

from src.data.dao.db import get_db
from src.utils import utils
from src.data.dao.person_dao_postgress import PersonDAO
from src.service.person_service import PersonService



db_param = 'json/db.json'
param = utils.load_json(db_param)

db = get_db(param)
person_dao = PersonDAO(db)
person_service = PersonService(person_dao=person_dao)
name = person_service.set_yesterday()
name = person_service.set_today()[1]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel(name)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )

        self.setCentralWidget(label)



app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()









