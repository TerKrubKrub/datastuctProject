import sys, os, datetime
from PyQt5 import QtWidgets, QtCore, QtGui, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import app, db
import rsrc.rsrc
import rsrc.style.book as style

LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo


class Book(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/book.ui", self)
        global bookApp
        bookApp = self
        self.setStyleSheet(style.default)
        self.book_id = None
        self.rating = 0.00
        self.btn05.toggled.connect(lambda: self.updateStar(float(self.btn05.text())))
        self.star05.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
        self.star05.setScaledContents(True)
        self.btn1.toggled.connect(lambda: self.updateStar(float(self.btn1.text())))
        self.star1.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
        self.star1.setScaledContents(True)
        self.btn15.toggled.connect(lambda: self.updateStar(float(self.btn15.text())))
        self.star15.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
        self.star15.setScaledContents(True)
        self.btn2.toggled.connect(lambda: self.updateStar(float(self.btn2.text())))
        self.star2.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
        self.star2.setScaledContents(True)
        self.btn25.toggled.connect(lambda: self.updateStar(float(self.btn25.text())))
        self.star25.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
        self.star25.setScaledContents(True)
        self.btn3.toggled.connect(lambda: self.updateStar(float(self.btn3.text())))
        self.star3.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
        self.star3.setScaledContents(True)
        self.btn35.toggled.connect(lambda: self.updateStar(float(self.btn35.text())))
        self.star35.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
        self.star35.setScaledContents(True)
        self.btn4.toggled.connect(lambda: self.updateStar(float(self.btn4.text())))
        self.star4.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
        self.star4.setScaledContents(True)
        self.btn45.toggled.connect(lambda: self.updateStar(float(self.btn45.text())))
        self.star45.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
        self.star45.setScaledContents(True)
        self.btn5.toggled.connect(lambda: self.updateStar(float(self.btn5.text())))
        self.star5.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
        self.star5.setScaledContents(True)
        self.user_img.setScaledContents(True)
        self.user_frame.setScaledContents(True)
        self.submit_btn.clicked.connect(self.submitComment)
        QtWidgets.QScroller.grabGesture(
            self.scrollArea, QtWidgets.QScroller.LeftMouseButtonGesture
        )
        self.user_frame.setPixmap(QtGui.QPixmap("rsrc/img/frame.png"))
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowIcon(QtGui.QIcon("rsrc/img/logo.png"))

    def resetId(self):
        self.updateStar(0)
        self.comment.clear()
        self.currentRating.setAutoExclusive(False)
        self.currentRating.setChecked(False)
        self.currentRating.setAutoExclusive(True)

    def setId(self, id):
        self.book_id = id
        self.currentRating = self.btn05
        self.scrollArea.verticalScrollBar().setValue(0)
        self.resetId()
        self.book_title.setText(
            [i[1] for i in db.database.books_ll if i[0] == self.book_id][0]
        )
        self.book_author.setText(
            [i[3] for i in db.database.books_ll if i[0] == self.book_id][0]
        )
        self.book_rating.setText(
            "⭐ {0:.2f}".format(
                ([float(i[7]) for i in db.database.books_ll if i[0] == self.book_id][0])
            )
        )
        self.book_img.setPixmap(
            QtGui.QPixmap(
                [i[2] for i in db.database.books_ll if i[0] == self.book_id][0]
            )
        )
        self.book_img.setScaledContents(True)
        self.book_synop.setText(
            [i[5] for i in db.database.books_ll if i[0] == self.book_id][0].replace(
                "\n", "\n\n"
            )
        )
        self.user_img.setPixmap(
            QtGui.QPixmap([i[6] for i in db.database.users_ll if i[0] == app.id][0])
        )
        try:
            self.past_rating = [
                x[3]
                for x in db.database.ratings_ll
                if x[1] == self.book_id and x[2] == app.id
            ][0]
        except:
            self.past_rating = 0
        self.updateStar(self.past_rating)
        self.updateComment()

    def updateStar(self, id):
        self.rating = id
        if self.rating == 0:
            self.star05.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star1.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star15.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star2.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star25.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star3.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star35.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star4.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star45.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star5.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
        elif self.rating == 0.5:
            self.currentRating = self.btn05
            self.star05.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star1.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star15.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star2.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star25.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star3.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star35.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star4.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star45.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star5.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
        elif self.rating == 1:
            self.currentRating = self.btn1
            self.star05.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star1.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star15.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star2.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star25.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star3.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star35.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star4.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star45.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star5.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
        elif self.rating == 1.5:
            self.currentRating = self.btn15
            self.star05.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star1.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star15.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star2.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star25.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star3.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star35.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star4.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star45.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star5.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
        elif self.rating == 2:
            self.currentRating = self.btn2
            self.star05.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star1.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star15.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star2.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star25.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star3.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star35.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star4.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star45.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star5.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
        elif self.rating == 2.5:
            self.currentRating = self.btn25
            self.star05.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star1.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star15.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star2.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star25.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star3.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star35.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star4.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star45.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star5.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
        elif self.rating == 3:
            self.currentRating = self.btn2
            self.star05.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star1.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star15.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star2.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star25.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star3.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star35.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star4.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star45.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star5.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
        elif self.rating == 3.5:
            self.currentRating = self.btn35
            self.star05.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star1.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star15.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star2.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star25.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star3.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star35.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star4.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
            self.star45.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star5.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
        elif self.rating == 4:
            self.currentRating = self.btn4
            self.star05.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star1.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star15.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star2.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star25.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star3.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star35.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star4.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star45.setPixmap(QtGui.QPixmap("rsrc/img/star_off.png"))
            self.star5.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
        elif self.rating == 4.5:
            self.currentRating = self.btn45
            self.star05.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star1.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star15.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star2.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star25.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star3.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star35.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star4.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star45.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star5.setPixmap(QtGui.QPixmap("rsrc/img/star_off_latter.png"))
        elif self.rating == 5:
            self.currentRating = self.btn5
            self.star05.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star1.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star15.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star2.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star25.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star3.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star35.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star4.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))
            self.star45.setPixmap(QtGui.QPixmap("rsrc/img/star.png"))
            self.star5.setPixmap(QtGui.QPixmap("rsrc/img/star_latter.png"))

    def clearLayout(self, layout):
        self.comment_id = []
        self.rev_comment = []
        self.rev_rating = []
        self.rev_date = []
        self.rev_fname = []
        self.rev_lname = []
        self.rev_username = []
        self.rev_userimg = []
        self.pos = []
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    self.clearLayout(child.layout())

    def updateComment(self):
        self.clearLayout(self.comment_section)
        self.comment_id = [
            i[0] for i in db.database.comments_ll if i[1] == self.book_id
        ]
        rev_book_id = []
        rev_user_id = []
        if self.comment_id:
            self.pos = [i for i in range(len(self.comment_id))]
            for i in self.comment_id:
                rev_book_id.append(
                    [x[1] for x in db.database.comments_ll if x[0] == i][0]
                )
                rev_user_id.append(
                    [x[2] for x in db.database.comments_ll if x[0] == i][0]
                )
                self.rev_comment.append(
                    [x[3] for x in db.database.comments_ll if x[0] == i][0]
                )
                self.rev_date.append(
                    [x[4] for x in db.database.comments_ll if x[0] == i][0]
                )
            for i in rev_user_id:
                self.rev_fname.append(
                    [x[1] for x in db.database.users_ll if x[0] == i][0]
                )
                self.rev_lname.append(
                    [x[2] for x in db.database.users_ll if x[0] == i][0]
                )
                self.rev_username.append(
                    [x[3] for x in db.database.users_ll if x[0] == i][0]
                )
                self.rev_userimg.append(
                    [x[6] for x in db.database.users_ll if x[0] == i][0]
                )
            for i, j in zip(rev_book_id, rev_user_id):
                try:
                    self.rev_rating.append(
                        [
                            float(x[3])
                            for x in db.database.ratings_ll
                            if x[1] == i and x[2] == j
                        ][0]
                    )
                except:
                    self.rev_rating.append(None)

            for pos, id, comment, rating, date, fname, lname, username, userimg in zip(
                self.pos,
                self.comment_id,
                self.rev_comment,
                self.rev_rating,
                self.rev_date,
                self.rev_fname,
                self.rev_lname,
                self.rev_username,
                self.rev_userimg,
            ):
                user_container = QtWidgets.QHBoxLayout()
                user_container.setSpacing(10)
                user_frame = QtWidgets.QFrame()
                user_frame.setSizePolicy(
                    QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
                    )
                )
                user_frame.setMinimumSize(QtCore.QSize(50, 50))
                user_frame.setMaximumSize(QtCore.QSize(50, 50))
                user_img = QtWidgets.QLabel(user_frame)
                user_img.setSizePolicy(
                    QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
                )
                user_img.setMaximumSize(50, 50)
                user_img.setPixmap(QtGui.QPixmap(userimg))
                user_img.setGeometry(QtCore.QRect(0, 0, 50, 50))
                user_img.setScaledContents(True)
                frame = QtWidgets.QLabel(user_frame)
                frame.setSizePolicy(
                    QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
                )
                frame.setMaximumSize(50, 50)
                if app.dark:
                    frame.setPixmap(QtGui.QPixmap("rsrc/img/frame_dark.png"))
                else:
                    frame.setPixmap(QtGui.QPixmap("rsrc/img/frame.png"))
                frame.setGeometry(QtCore.QRect(0, 0, 50, 50))
                frame.setScaledContents(True)
                user_container.addWidget(user_frame)
                user_name = QtWidgets.QLabel(self.review_section)
                if (
                    fname + " " + lname
                    == [i[1] for i in db.database.users_ll if i[0] == app.id][0]
                    + " "
                    + [i[2] for i in db.database.users_ll if i[0] == app.id][0]
                ):
                    user_name.setText("You")
                else:
                    user_name.setText(fname + " " + lname)
                user_name.setFont(QtGui.QFont("Product Sans", 12))
                user_name.setSizePolicy(
                    QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
                )
                user_container.addWidget(user_name)
                user_username = QtWidgets.QLabel(self.review_section)
                user_username.setText("@" + username)
                user_username.setFont(QtGui.QFont("Product Sans", 12))
                user_username.setStyleSheet("color: grey;")
                user_container.addWidget(user_username)
                if rating:
                    user_rating = QtWidgets.QLabel(self.review_section)
                    user_rating.setText("⭐ {0:.1f}".format(rating))
                    user_rating.setFont(QtGui.QFont("Product Sans", 12))
                    user_container.addWidget(user_rating)
                spacerItem = QtWidgets.QSpacerItem(
                    5,
                    5,
                    QtWidgets.QSizePolicy.Expanding,
                    QtWidgets.QSizePolicy.Minimum,
                )
                user_container.addItem(spacerItem)
                if (
                    fname + " " + lname
                    == [i[1] for i in db.database.users_ll if i[0] == app.id][0]
                    + " "
                    + [i[2] for i in db.database.users_ll if i[0] == app.id][0]
                ):
                    del_comment = QtWidgets.QPushButton("-", self.review_section)
                    del_comment.setFont(QtGui.QFont("Helvetica Neue LT", 6))
                    del_comment.setSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
                    )
                    del_comment.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    del_comment.setMinimumSize(14, 14)
                    del_comment.setIconSize(del_comment.minimumSize())
                    del_comment.setStyleSheet("border-radius: 7px; ")
                    del_comment.clicked.connect(lambda x, id=id: self.delComment(id))
                    user_container.addWidget(del_comment)
                comment_label = QtWidgets.QLabel(self.review_section)
                comment_label.setText(comment)
                comment_label.setFont(QtGui.QFont("Product Sans", 12))
                comment_label.setStyleSheet(
                    """
                    background-color: rgb(255, 231, 203);
                    border-radius: 15px;
                    margin-left: 60px;
                    padding: 10px 15px;
                    color: black;
                """
                )
                comment_label.setSizePolicy(
                    QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
                    )
                )
                comment_label.setMaximumHeight(100)
                comment_label.setAlignment(QtCore.Qt.AlignTop)
                comment_label.setWordWrap(True)
                comment_date = QtWidgets.QLabel(self.review_section)
                comment_date.setText(date)
                comment_date.setFont(QtGui.QFont("Product Sans", 10))
                comment_date.setStyleSheet("margin-left: 60px;")
                comment_date.setWordWrap(True)
                comment_container = QtWidgets.QVBoxLayout()
                comment_container.setSpacing(5)
                comment_container.addLayout(user_container, 0)
                comment_container.addWidget(comment_label, 1)
                comment_container.addWidget(comment_date, 2)
                self.comment_section.addLayout(comment_container, pos)

    def submitComment(self):
        date_created = datetime.datetime.now(LOCAL_TIMEZONE).strftime(
            "%a, %d %b %Y at %I:%M %p"
        )
        posted = False
        if self.comment.toPlainText():
            db.database.curs.execute(
                "INSERT INTO Comments (book_id, user_id, comment, date_created) VALUES (?,?,?,?)",
                [
                    self.book_id,
                    app.id,
                    self.comment.toPlainText(),
                    date_created,
                ],
            )
            db.database.db.commit()
            db.database.updateDatabase(True, False, False, False)
            self.comment.clear()
            posted = True

        if self.rating != self.past_rating:
            try:
                past_rating = [
                    x[3]
                    for x in db.database.ratings_ll
                    if x[1] == self.book_id and x[2] == app.id
                ][0]
            except:
                past_rating = None
            if not past_rating:
                db.database.curs.execute(
                    "INSERT INTO ratings (book_id, user_id, rating) VALUES (?,?,?)",
                    [self.book_id, app.id, self.rating],
                )
            else:
                db.database.curs.execute(
                    "UPDATE ratings SET rating="
                    + str(self.rating)
                    + " WHERE book_id="
                    + str(self.book_id)
                    + " and user_id="
                    + str(app.id)
                )
            db.database.db.commit()
            db.database.updateDatabase(True, False, True, False)
            self.book_rating.setText("⭐ {0:.2f}".format(self.rating))
            posted = True

        if posted:
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setWindowTitle("Comment posted!")
            self.msg.setText("Your review is posted to the book.")
            self.msg.exec_()
            posted = False

        self.updateComment()

    def delComment(self, comment_id):
        self.msg.setIcon(QtWidgets.QMessageBox.Question)
        self.msg.setWindowTitle("Confirm deletion.")
        self.msg.setText("Are you sure to delete this comment?")
        self.msg.setStandardButtons(
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel
        )
        self.msg.buttonClicked.connect(lambda x, id=comment_id: self.delete(x, id))
        self.msg.exec_()

    def delete(self, signal, comment_id):
        if signal.text() == "&Yes":
            db.database.curs.execute("DELETE FROM comments WHERE id=" + str(comment_id))
            db.database.db.commit()
            db.database.updateDatabase(True, False, False, False)
            self.updateComment()
