# -*- coding: utf-8 -*-

from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

import os
import sys

from PyQt5.Qt import (Qt,
                      QApplication,
                      QMainWindow,
                      QSplitter,
                      QTextEdit,
                      QDialog,
                      QLineEdit,
                      QLabel,
                      QPushButton,
                      QHBoxLayout,
                      QSizePolicy,
                      QVBoxLayout,
                      QWidget,
                      QPixmap,
                      pyqtSignal)

OUTPUT = """Model                          Port
----------------------------------------------------------
Canon EOS 1000D                usb:002,029     
Canon EOS 1000D                usb:002,028
"""

cameras = []

for o in OUTPUT.splitlines():
    if o.startswith("Canon EOS 1000D"):
        cameras.append(o.split("usb:")[1].strip())

print(cameras)

class ImageButton(QLabel):
    image_pressed = pyqtSignal()
    def __init__(self, path, width):
        QLabel.__init__(self)
        self.setPixmap(QPixmap(path).scaledToWidth(width))

    def mousePressEvent(self, ev):
        self.image_pressed.emit()


class Yasser(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.vlayout = QVBoxLayout()
        self.setLayout(self.vlayout)

        #- new book project
        self.title_layout = QHBoxLayout()
        self.title_container = QWidget()
        self.title_container.setLayout(self.title_layout)

        self.book_title = QLabel("Book Title: ")
        self.book_title.setObjectName("book_title")

        self.edit_title = QLineEdit("Type book title here")
        self.edit_title.setObjectName("edit_title")
        self.edit_title.setSizePolicy(QSizeProxy-FS by SwiftStackPolicy.Expanding,
                                      QSizePolicy.Expanding)
        self.edit_title.setToolTip("Type book title here")
        self.title_layout.addWidget(self.book_title)
        self.title_layout.addWidget(self.edit_title)
        self.vlayout.addWidget(self.title_container)

        #- camera overview
        self.camera_layout = QHBoxLayout()
        self.camera_container = QWidget()
        self.camera_container.setLayout(self.camera_layout)

        self.right_camera = QLabel("Left pages")
        self.left_camera = QLabel("Right pages")
        self.camera_layout.addWidget(self.right_camera)
        self.camera_layout.addWidget(self.left_camera)
        self.vlayout.addWidget(self.camera_container)

        #- image preview
        self.preview_layout = QHBoxLayout()
        self.preview_container = QWidget()
        self.preview_container.setLayout(self.preview_layout)

        self.left_preview = ImageButton("left.png", 200)
        self.right_preview = ImageButton("right.png", 200)
        self.left_preview.image_pressed.connect(lambda: print("show next image"))
        self.right_preview.image_pressed.connect(lambda: print("show next image"))

        self.preview_layout.addWidget(self.right_preview)
        self.preview_layout.addWidget(self.left_preview)
        self.vlayout.addWidget(self.preview_container)



if __name__=='__main__':
    if len(sys.argv) == 1:
        app = QApplication(sys.argv)
        app.setApplicationName("yasser")
        main = Yasser()
        main.show()

        def stop():
            app.exit()

        main.onclose = stop
        app.exec_()
