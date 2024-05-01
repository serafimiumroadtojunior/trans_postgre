import sys
from connect import Connect
from googletrans import Translator
from PySide6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QMessageBox
from uimain_ui import Ui_MainWindow
from PySide6.QtSql import QSqlTableModel
import pyttsx3


class TranslatorApp(QMainWindow):
    def __init__(self):
        super(TranslatorApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.voice = pyttsx3.init()
        self.translator = Translator()
        self.conn = Connect()

        self.ui.TRANSLATE_BUTTON.clicked.connect(self.translate_text)
        self.ui.VOICE_BUTTON1.clicked.connect(self.speak_text_source)
        self.ui.COPY_BUTTON1.clicked.connect(self.copy_text_source)
        self.ui.VOICE_BUTTON2.clicked.connect(self.speak_text_target)
        self.ui.COPY_BUTTON2.clicked.connect(self.copy_text_target)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('info_res')
        self.model.select()
        self.ui.POSTGRE_SQL.setModel(self.model)

    def copy_text_source(self):
        text_to_copy = self.ui.USER_TEXT.toPlainText()
        QApplication.clipboard().setText(text_to_copy)

    def copy_text_target(self):
        text_to_copy = self.ui.TRANSLATE_TEXT.toPlainText()
        QApplication.clipboard().setText(text_to_copy)

    def speak_text_source(self):
        language = self.ui.comboBox.currentText()
        text = self.ui.USER_TEXT.toPlainText().strip()
        self.speak_text(text, language)

    def speak_text_target(self):
        language = self.ui.comboBox_2.currentText()
        text = self.ui.TRANSLATE_TEXT.toPlainText().strip()
        self.speak_text(text, language)


    def translate_text(self):
            for language, suffix in self.ui.languages.items():
                if self.ui.comboBox_2.currentText() == language:
                    text = self.ui.USER_TEXT.toPlainText()
                    translation = self.translator.translate(text, dest=suffix)
                    self.ui.TRANSLATE_TEXT.clear()
                    self.ui.TRANSLATE_TEXT.insertPlainText(translation.text)
                    self.translated_text = self.ui.TRANSLATE_TEXT.toPlainText()

                    self.view_data()
                    self.inserts(text, self.translated_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TranslatorApp()
    window.show()
    sys.exit(app.exec())