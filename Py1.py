from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
import requests

class SummerThemeApp(QWidget):
    def __init__(self):
        super().__init__()

        # 설정
        self.setWindowTitle("Checking URL")
        self.setGeometry(600, 400, 900, 600)  # 창의 너비와 높이 조정

        # 레이아웃
        layout = QVBoxLayout()

        # 제목 레이블
        self.title = QLabel()
        self.title.setText("Check Your URL")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setTextFormat(Qt.RichText)
        self.title.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.title.setStyleSheet("font-size: 45px; font-weight: bold; color: rgb(0, 0, 0);")  # 제목 스타일
        layout.addWidget(self.title)

        # URL 입력 필드
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL here...")
        layout.addWidget(self.url_input)

        # 확인 버튼
        self.check_button = QPushButton("Check URL")
        self.check_button.clicked.connect(self.check_url)
        layout.addWidget(self.check_button)

        # 결과 레이블
        self.result = QLabel("")
        self.result.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result)

        # 스타일 적용
        self.setLayout(layout)
        self.apply_styles()

    def apply_styles(self):
        # 여름 색상 테마
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))  # 흰색 배경
        palette.setColor(QPalette.Button, QColor(70, 130, 180))  # 버튼 색상
        palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))  # 버튼 텍스트 색상
        palette.setColor(QPalette.Text, QColor(0, 0, 0))  # 텍스트 색상
        self.setPalette(palette)

        # 버튼 스타일
        self.check_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(70, 130, 180);
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgb(100, 149, 237);
            }
            QPushButton:pressed {
                background-color: rgb(65, 105, 225);
            }
        """)

        # URL 입력 필드 스타일
        self.url_input.setStyleSheet("""
            QLineEdit {
                background-color: rgb(240, 240, 240);  # 밝은 회색 배경
                color: rgb(0, 0, 0);  # 검정색 텍스트
                border: 1px solid rgb(200, 200, 200);  # 연한 회색 테두리
                border-radius: 5px;  # 둥근 모서리
                padding: 5px;  # 패딩
            }
            QLineEdit:focus {
                border: 1px solid rgb(70, 130, 180);  # 포커스 시 파란색 테두리
            }
        """)

        # 결과 레이블 스타일
        self.result.setStyleSheet("""
            QLabel {
                color: rgb(0, 128, 0);  # 결과 텍스트 색상
                font-size: 30px;  # 글자 크기
            }
        """)

    def check_url(self):
        url = self.url_input.text()
        if not url:
            self.show_message("Input Error", "Please enter a URL.")
            return

        try:
            # Flask 서버에 POST 요청
            response = requests.post("http://localhost:5000/predict", json={"url": url})
            if response.status_code == 200:
                prediction = response.json().get('prediction', [None])[0]  # 'prediction' 리스트에서 첫 번째 요소 가져오기
                if prediction == 0:
                    self.show_message("Result", "입력하신 URL은 악성입니다.")
                elif prediction == 1:
                    self.show_message("Result", "입력하신 URL은 정상입니다.")
                else:
                    self.show_message("Result", "Unknown result from server.")
            else:
                self.show_message("Error", "Error: Server issue")
        except requests.RequestException as e:
            self.show_message("Error", f"Error: {e}")

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(f"<p style='font-size: 30px;'>{message}</p>")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setButtonText(QMessageBox.Ok, "OK")
        msg_box.setStyleSheet("""
            QMessageBox {
                width: 400px;
                height: 300px;
            }
            QPushButton {
                font-size: 18px;
            }
        """)
        msg_box.exec()

# 애플리케이션 실행
if __name__ == "__main__":
    app = QApplication([])
    window = SummerThemeApp()
    window.show()
    app.exec()
