import sys, os, sqlite3, random
from PyQt5 import QtGui

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


class Database:
    def __init__(self):
        self.db = sqlite3.connect("rsrc/db/data.db")
        self.curs = self.db.cursor()
        self.req_q = RequestQueue()

    def updateRsrc(self, init=None):
        if init:
            self.fontDB = QtGui.QFontDatabase()
            self.fontDB.addApplicationFont("rsrc/font/Better Grade/Better Grade.ttf")
            self.fontDB.addApplicationFont("rsrc/font/Freight/Freight Big Black SC.otf")
            self.fontDB.addApplicationFont("rsrc/font/Palatino/Palatino.ttf")
            self.fontDB.addApplicationFont(
                "rsrc/font/Product Sans/Product Sans Regular.ttf"
            )
            self.fontDB.addApplicationFont(
                "rsrc/font/Helvetica Neue/Helvetica Neue LT 93 Black Extended Oblique.ttf"
            )
            self.fontDB.addApplicationFont(
                "rsrc/font/Helvetica Neue/Helvetica Neue LT 87 Heavy Condensed Oblique.ttf"
            )
            self.fontDB.addApplicationFont(
                "rsrc/font/Helvetica Neue/Helvetica Neue LT 65 Medium.ttf"
            )
            self.fontDB.addApplicationFont(
                "rsrc/font/Helvetica Neue/Helvetica Neue LT 63 Medium Extended Oblique.ttf"
            )
            self.fontDB.addApplicationFont(
                "rsrc/font/Helvetica Neue/Helvetica Neue LT 63 Medium Extended.ttf"
            )
            self.fontDB.addApplicationFont(
                "rsrc/font/Helvetica Neue/Helvetica Neue LT 53 Extended.ttf"
            )
            self.fontDB.addApplicationFont(
                "rsrc/font/Helvetica Neue/Helvetica Neue LT 55 Roman.ttf"
            )
            self.fontDB.addApplicationFont(
                "rsrc/font/Helvetica Neue/Helvetica Neue LT 47 Light Condensed.ttf"
            )
            self.fontDB.addApplicationFont(
                "rsrc/font/Helvetica Neue/Helvetica Neue LT 23 Ultra Light Extended Oblique.ttf"
            )
            self.book_img = []
            self.curs.execute("SELECT * FROM books")
            books_db = self.curs.fetchall()
            for i in books_db:
                self.book_img.append(QtGui.QPixmap(i[2]))
            self.star = QtGui.QPixmap("rsrc/img/star.png")
            self.star_latter = QtGui.QPixmap("rsrc/img/star_latter.png")
            self.star_off = QtGui.QPixmap("rsrc/img/star_off.png")
            self.star_off_latter = QtGui.QPixmap("rsrc/img/star_off_latter.png")

        self.user_img = []
        self.user_img_pixmap = []
        self.curs.execute("SELECT * FROM users")
        users_db = self.curs.fetchall()
        default_prof = QtGui.QPixmap("rsrc/db/userimg/dafault-pic.png")
        for i in users_db:
            self.user_img.append([i[0], i[6]])
            if i[6] == "rsrc/db/userimg/dafault-pic.png":
                self.user_img_pixmap.append(default_prof)
            else:
                self.user_img_pixmap.append(QtGui.QPixmap(i[6]))

    def updateDatabase(self, reviews=False, users=False, books=False, cur_user=False):
        if reviews:
            self.curs.execute("SELECT * FROM comments")
            comments_db = self.curs.fetchall()
            comment_db = [i for i in range(len(comments_db))]
            self.comments_ll = CommentLinkedList()
            for i in range(len(comments_db)):
                comment_db[i] = CommentNode(
                    comments_db[i][0],
                    comments_db[i][1],
                    comments_db[i][2],
                    comments_db[i][3],
                    comments_db[i][4],
                )
                self.comments_ll.append(comment_db[i])

            self.curs.execute("SELECT * FROM ratings")
            ratings_db = self.curs.fetchall()
            rating_db = [i for i in range(len(ratings_db))]
            self.ratings_ll = RatingLinkedList()
            for i in range(len(ratings_db)):
                rating_db[i] = RatingNode(
                    ratings_db[i][0],
                    ratings_db[i][1],
                    ratings_db[i][2],
                    ratings_db[i][3],
                )
                self.ratings_ll.append(rating_db[i])

        if users:
            self.updateRsrc()
            self.curs.execute("SELECT * FROM users")
            users_db = self.curs.fetchall()
            user_db = [i for i in range(len(users_db))]
            self.users_ll = UserLinkedList()
            for i in range(len(users_db)):
                user_db[i] = UserNode(
                    users_db[i][0],
                    users_db[i][1],
                    users_db[i][2],
                    users_db[i][3],
                    users_db[i][4],
                    users_db[i][5],
                    self.user_img_pixmap[i],
                    users_db[i][7],
                )
                self.users_ll.append(user_db[i])

        if books:
            self.curs.execute("SELECT * FROM books")
            books_db = self.curs.fetchall()
            book_db = [i for i in range(len(books_db))]
            self.books_ll = BookLinkedList()
            for i in range(len(books_db)):
                book_db[i] = BookNode(
                    books_db[i][0],
                    books_db[i][1],
                    self.book_img[i],
                    books_db[i][3],
                    books_db[i][4],
                    books_db[i][5],
                    books_db[i][6],
                    books_db[i][7],
                )
                self.books_ll.append(book_db[i])
            self.books_ll.sort(0)

            self.fictions_ll = BookLinkedList()
            for i in self.books_ll:
                if i[6] == "fiction":
                    self.fictions_ll.append(i)

            self.thrillers_ll = BookLinkedList()
            for i in self.books_ll:
                if i[6] == "thriller":
                    self.thrillers_ll.append(i)

            self.fantasies_ll = BookLinkedList()
            for i in self.books_ll:
                if i[6] == "fantasy":
                    self.fantasies_ll.append(i)

            self.romances_ll = BookLinkedList()
            for i in self.books_ll:
                if i[6] == "romance":
                    self.romances_ll.append(i)

            self.biographies_ll = BookLinkedList()
            for i in self.books_ll:
                if i[6] == "biography":
                    self.biographies_ll.append(i)

            self.comedies_ll = BookLinkedList()
            for i in self.books_ll:
                if i[6] == "comedy":
                    self.comedies_ll.append(i)

            self.horrors_ll = BookLinkedList()
            for i in self.books_ll:
                if i[6] == "horror":
                    self.horrors_ll.append(i)

            self.poetries_ll = BookLinkedList()
            for i in self.books_ll:
                if i[6] == "poetry":
                    self.poetries_ll.append(i)

        if cur_user:
            self.curs.execute("SELECT * FROM current_user")
            try:
                cur_users_db = self.curs.fetchone()
                self.cur_user = CurUser(cur_users_db[0], cur_users_db[1])
            except:
                self.cur_user = CurUser(None, None)

    def exit(self, justReq=None):
        if not justReq:
            print("\nExitting the program...")
        print()
        for i in range(len(self.req_q)):
            req = self.req_q.dequeue()
            print(str(i + 1) + ".) Push " + str(req) + " to the database.")
            self.curs.execute(
                "INSERT INTO requests (title, author) VALUES (?,?)", [req[0], req[1]]
            )
            self.db.commit()
        print()
        if not justReq:
            self.db.close()


class CurUser:
    def __init__(self, id, rmb):
        self.id = id
        self.rmb = rmb if rmb else None

    def __getitem__(self, index):
        self.items = [self.id, self.rmb]
        return self.items[index]

    def __str__(self):
        return "[" + ", ".join([str(self.id), str(self.rmb)]) + "]"


class UserNode:
    def __init__(
        self,
        id,
        f_name,
        l_name,
        username,
        password,
        email=None,
        img=None,
        cur_read=None,
    ):
        self.next = None
        self.prev = None
        self.id = id
        self.f_name = f_name
        self.l_name = l_name
        self.username = username
        self.password = password
        self.email = email if email else None
        self.img = img if img else ":/Image/db/userimg/dafault-pic.png"
        self.cur_read = cur_read if cur_read else None

    def __getitem__(self, index):
        self.items = [
            self.id,
            self.f_name,
            self.l_name,
            self.username,
            self.password,
            self.email,
            self.img,
            self.cur_read,
        ]
        return self.items[index]

    def __str__(self):
        return (
            "["
            + ", ".join(
                [
                    str(self.id),
                    str(self.f_name),
                    str(self.l_name),
                    str(self.username),
                    str(self.password),
                    str(self.email),
                    str(self.img),
                    str(self.cur_read),
                ]
            )
            + "]"
        )


class UserLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def __str__(self):
        cur = self.head
        l = []
        while cur:
            l.append(str(cur))
            cur = cur.next
        if l == []:
            return "[]"
        else:
            return "[" + ", ".join(l) + "]"

    def __getitem__(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def append(self, node):
        new_node = UserNode(
            node[0], node[1], node[2], node[3], node[4], node[5], node[6], node[7]
        )
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, node):
        new_node = UserNode(
            node[0], node[1], node[2], node[3], node[4], node[5], node[6], node[7]
        )
        if not self.head:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert(self, node, index):
        new_node = UserNode(
            node[0], node[1], node[2], node[3], node[4], node[5], node[6], node[7]
        )
        if index == 0:
            self.prepend(node)
        elif index == len(self):
            self.append(node)
        elif index > len(self):
            print("Index out of range.")
        else:
            cur = self[index]
            prv = cur.prev
            prv.next = new_node
            cur.prev = new_node
            new_node.next = cur
            new_node.prev = prv

    def pop(self, index=None):
        if index:
            return self.remove(self[index])
        elif index == 0:
            return self.remove(self[0])
        elif not index:
            return self.remove(self[len(self)])

    def remove(self, node):
        new_node = UserNode(
            node[0], node[1], node[2], node[3], node[4], node[5], node[6], node[7]
        )
        cur = self.head
        while cur:
            if cur == new_node:
                if cur == self.head:
                    if not cur.next:
                        cur = None
                        self.head = None
                        return new_node
                    else:
                        nxt = cur.next
                        cur.next = None
                        nxt.prev = None
                        cur = None
                        self.head = nxt
                        return new_node
                else:
                    if not cur.next:
                        prv = cur.prev
                        prv.next = None
                        cur.prev = None
                        cur = None
                        return new_node
                    else:
                        nxt = cur.next
                        prv = cur.prev
                        prv.next = nxt
                        nxt.prev = prv
                        cur.prev = None
                        cur.next = None
                        cur = None
                        return new_node
            cur = cur.next


class BookNode:
    def __init__(
        self, id, title, img, author, pages, synop=None, genre=None, rating=None
    ):
        self.next = None
        self.prev = None
        self.id = id
        self.title = title
        self.img = img
        self.author = author
        self.pages = pages
        self.synop = synop if synop else "< No Synopsis >"
        self.genre = genre if genre else None
        self.rating = rating if rating else 0

    def __getitem__(self, index):
        self.items = [
            self.id,
            self.title,
            self.img,
            self.author,
            self.pages,
            self.synop,
            self.genre,
            self.rating,
        ]
        return self.items[index]

    def __str__(self):
        return (
            "["
            + ", ".join(
                [
                    str(self.id),
                    str(self.title),
                    str(self.img),
                    str(self.author),
                    str(self.pages),
                    str(self.synop),
                    str(self.genre),
                    str(self.rating),
                ]
            )
            + "]"
        )


class BookLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def __str__(self):
        cur = self.head
        l = []
        while cur:
            l.append(str(cur))
            cur = cur.next
        if l == []:
            return "[]"
        else:
            return "[" + ", ".join(l) + "]"

    def __getitem__(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def append(self, node):
        new_node = BookNode(
            node[0], node[1], node[2], node[3], node[4], node[5], node[6], node[7]
        )
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, node):
        new_node = BookNode(
            node[0], node[1], node[2], node[3], node[4], node[5], node[6], node[7]
        )
        if not self.head:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert(self, node, index):
        new_node = BookNode(
            node[0], node[1], node[2], node[3], node[4], node[5], node[6], node[7]
        )
        if index == 0:
            self.prepend(node)
        elif index == len(self):
            self.append(node)
        elif index > len(self):
            print("Index out of range.")
        else:
            cur = self[index]
            prv = cur.prev
            prv.next = new_node
            cur.prev = new_node
            new_node.next = cur
            new_node.prev = prv

    def pop(self, index=None):
        if index:
            return self.remove(self[index])
        elif index == 0:
            return self.remove(self[0])
        elif not index:
            return self.remove(self[len(self)])

    def remove(self, node):
        new_node = BookNode(
            node[0], node[1], node[2], node[3], node[4], node[5], node[6], node[7]
        )
        cur = self.head
        while cur:
            if cur == new_node:
                if cur == self.head:
                    if not cur.next:
                        cur = None
                        self.head = None
                        return new_node
                    else:
                        nxt = cur.next
                        cur.next = None
                        nxt.prev = None
                        cur = None
                        self.head = nxt
                        return new_node
                else:
                    if not cur.next:
                        prv = cur.prev
                        prv.next = None
                        cur.prev = None
                        cur = None
                        return new_node
                    else:
                        nxt = cur.next
                        prv = cur.prev
                        prv.next = nxt
                        nxt.prev = prv
                        cur.prev = None
                        cur.next = None
                        cur = None
                        return new_node
            cur = cur.next

    def swap(self, x, y):
        if x == y:
            return

        cur_x = self.head
        prev_x = None
        cur_y = self.head
        prev_y = None
        while cur_x and cur_x != x:
            prev_x = cur_x
            cur_x = cur_x.next
        while cur_y and cur_y != y:
            prev_y = cur_y
            cur_y = cur_y.next

        if not cur_x or not cur_y:
            return
        if prev_x:
            prev_x.next = cur_y
        else:
            self.head = cur_y
        if prev_y:
            prev_y.next = cur_x
        else:
            self.head = cur_x
        cur_x.next, cur_y.next = cur_y.next, cur_x.next

    def merge(self, first, second):
        if first is None:
            return second
        if second is None:
            return first
        if self.sort_type == 2:
            if first.rating > second.rating:
                first.next = self.merge(first.next, second)
                first.next.prev = first
                first.prev = None
                self.head = first
                return first
            elif first.rating < second.rating:
                second.next = self.merge(first, second.next)
                second.next.prev = second
                second.prev = None
                return second
            elif first.rating == second.rating:
                equal = True
                if len(second.title) <= len(first.title):
                    for i in range(len(second.title)):
                        if ord(second.title[i]) < ord(first.title[i]):
                            equal = False
                            second.next = self.merge(first, second.next)
                            second.next.prev = second
                            second.prev = None
                            return second
                        elif ord(second.title[i]) > ord(first.title[i]):
                            equal = "more than"
                            first.next = self.merge(first.next, second)
                            first.next.prev = first
                            first.prev = None
                            self.head = first
                            return first

                    if equal == True:
                        second.next = self.merge(first, second.next)
                        second.next.prev = second
                        second.prev = None
                        return second
                else:
                    for i in range(len(first.title)):
                        if ord(first.title[i]) > ord(second.title[i]):
                            second.next = self.merge(first, second.next)
                            second.next.prev = second
                            second.prev = None
                            return second
                        elif ord(first.title[i]) < ord(second.title[i]):
                            first.next = self.merge(first.next, second)
                            first.next.prev = first
                            first.prev = None
                            self.head = first
                            return first

                    if equal == True:
                        first.next = self.merge(first.next, second)
                        first.next.prev = first
                        first.prev = None
                        self.head = first
                        return first

        elif self.sort_type == 3:
            if first.rating < second.rating:
                first.next = self.merge(first.next, second)
                first.next.prev = first
                first.prev = None
                self.head = first
                return first
            elif first.rating > second.rating:
                second.next = self.merge(first, second.next)
                second.next.prev = second
                second.prev = None
                return second
            elif first.rating == second.rating:
                equal = True
                if len(second.title) <= len(first.title):
                    for i in range(len(second.title)):
                        if ord(second.title[i]) < ord(first.title[i]):
                            equal = False
                            second.next = self.merge(first, second.next)
                            second.next.prev = second
                            second.prev = None
                            return second
                        elif ord(second.title[i]) > ord(first.title[i]):
                            equal = "more than"
                            first.next = self.merge(first.next, second)
                            first.next.prev = first
                            first.prev = None
                            self.head = first
                            return first

                    if equal == True:
                        second.next = self.merge(first, second.next)
                        second.next.prev = second
                        second.prev = None
                        return second
                else:
                    for i in range(len(first.title)):
                        if ord(first.title[i]) > ord(second.title[i]):
                            second.next = self.merge(first, second.next)
                            second.next.prev = second
                            second.prev = None
                            return second
                        elif ord(first.title[i]) < ord(second.title[i]):
                            first.next = self.merge(first.next, second)
                            first.next.prev = first
                            first.prev = None
                            self.head = first
                            return first

                    if equal == True:
                        first.next = self.merge(first.next, second)
                        first.next.prev = first
                        first.prev = None
                        self.head = first
                        return first

    def split(self, tempHead):
        fast = slow = tempHead
        while True:
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        return temp

    def mergeSort(self, tempHead):
        if tempHead is None:
            return tempHead
        if tempHead.next is None:
            return tempHead
        second = self.split(tempHead)
        tempHead = self.mergeSort(tempHead)
        second = self.mergeSort(second)
        return self.merge(tempHead, second)

    def sort(self, type):
        self.sort_type = type
        if self.sort_type == 0:
            for i in range(1, len(self), 1):
                for j in range(i, -1, -1):
                    if j != 0:
                        equal = True
                        bNode = self[j].title.upper()
                        fNode = self[j - 1].title.upper()
                        if len(bNode) <= len(fNode):
                            for k in range(len(bNode)):
                                if ord(bNode[k]) < ord(fNode[k]):
                                    self.swap(self[j - 1], self[j])
                                    equal = False
                                    break
                                elif ord(bNode[k]) > ord(fNode[k]):
                                    equal = "more than"
                                    break
                            if equal == "more than":
                                break
                            elif equal == True:
                                self.swap(self[j - 1], self[j])
                        else:
                            for k in range(len(fNode)):
                                if ord(bNode[k]) < ord(fNode[k]):
                                    self.swap(self[j - 1], self[j])
                                    equal = False
                                    break
                                elif ord(bNode[k]) > ord(fNode[k]):
                                    equal = "more than"
                                    break
                            if equal == "more than":
                                break
                            elif equal == True:
                                break
        elif self.sort_type == 1:
            for i in range(1, len(self), 1):
                for j in range(i, -1, -1):
                    if j != 0:
                        equal = True
                        bNode = self[j].title.upper()
                        fNode = self[j - 1].title.upper()
                        if len(bNode) <= len(fNode):
                            for k in range(len(bNode)):
                                if ord(bNode[k]) > ord(fNode[k]):
                                    self.swap(self[j - 1], self[j])
                                    equal = False
                                    break
                                elif ord(bNode[k]) < ord(fNode[k]):
                                    equal = "less than"
                                    break
                            if equal == "less than":
                                break
                            elif equal == True:
                                self.swap(self[j - 1], self[j])
                        else:
                            for k in range(len(fNode)):
                                if ord(bNode[k]) > ord(fNode[k]):
                                    self.swap(self[j - 1], self[j])
                                    equal = False
                                    break
                                elif ord(bNode[k]) < ord(fNode[k]):
                                    equal = "less than"
                                    break
                            if equal == "less than":
                                break
                            elif equal == True:
                                break
        elif self.sort_type == 2:
            self.head = self.mergeSort(self.head)
        elif self.sort_type == 3:
            self.head = self.mergeSort(self.head)
        return self

    def search(self, key):
        if not key:
            return
        key = key.upper()
        isKeyAWord = True if len(key.split()) == 1 else False
        res = BookLinkedList()
        cur = self.head
        added = False
        while cur:
            word = cur.title.upper() + " " + cur.author.upper()
            words = word.split()
            if isKeyAWord:
                for w in words:
                    if w.startswith(key) and not added:
                        res.append(cur)
                        added = True
            else:
                if key in word and not added:
                    res.append(cur)
                    added = True
            cur = cur.next
            added = False
        if not cur:
            return res

    def recommended(self):
        return self[random.randrange(len(self))]

    def binarySearch(self, ll, l, r, title, author):
        if l > r:
            return False
        mid = (l + r) // 2
        if ll[mid].title.upper() == title and ll[mid].author.upper() == author:
            return True
        elif ll[mid].title.upper() > title and ll[mid].author.upper() > author:
            return self.binarySearch(ll, l, mid - 1, title, author)
        else:
            return self.binarySearch(ll, mid + 1, r, title, author)

    def existed(self, title, author):
        title = title.upper()
        author = author.upper()
        self.sort(0)
        return self.binarySearch(self, 0, len(self) - 1, title, author)


class CommentNode:
    def __init__(self, id, user_id, book_id, comment, date_created):
        self.next = None
        self.prev = None
        self.id = id
        self.user_id = user_id
        self.book_id = book_id
        self.comment = comment
        self.date_created = date_created

    def __getitem__(self, index):
        self.items = [
            self.id,
            self.user_id,
            self.book_id,
            self.comment,
            self.date_created,
        ]
        return self.items[index]

    def __str__(self):
        return (
            "["
            + ", ".join(
                [
                    str(self.id),
                    str(self.user_id),
                    str(self.book_id),
                    str(self.comment),
                    str(self.date_created),
                ]
            )
            + "]"
        )


class CommentLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def __str__(self):
        cur = self.head
        l = []
        while cur:
            l.append(str(cur))
            cur = cur.next
        if l == []:
            return "[]"
        else:
            return "[" + ", ".join(l) + "]"

    def __getitem__(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def append(self, node):
        new_node = CommentNode(node[0], node[1], node[2], node[3], node[4])
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, node):
        new_node = CommentNode(node[0], node[1], node[2], node[3], node[4])
        if not self.head:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert(self, node, index):
        new_node = CommentNode(node[0], node[1], node[2], node[3], node[4])
        if index == 0:
            self.prepend(node)
        elif index == len(self):
            self.append(node)
        elif index > len(self):
            print("Index out of range.")
        else:
            cur = self[index]
            prv = cur.prev
            prv.next = new_node
            cur.prev = new_node
            new_node.next = cur
            new_node.prev = prv

    def pop(self, index=None):
        if index:
            return self.remove(self[index])
        elif index == 0:
            return self.remove(self[0])
        elif not index:
            return self.remove(self[len(self)])

    def remove(self, node):
        new_node = CommentNode(node[0], node[1], node[2], node[3], node[4])
        cur = self.head
        while cur:
            if cur == new_node:
                if cur == self.head:
                    if not cur.next:
                        cur = None
                        self.head = None
                        return new_node
                    else:
                        nxt = cur.next
                        cur.next = None
                        nxt.prev = None
                        cur = None
                        self.head = nxt
                        return new_node
                else:
                    if not cur.next:
                        prv = cur.prev
                        prv.next = None
                        cur.prev = None
                        cur = None
                        return new_node
                    else:
                        nxt = cur.next
                        prv = cur.prev
                        prv.next = nxt
                        nxt.prev = prv
                        cur.prev = None
                        cur.next = None
                        cur = None
                        return new_node
            cur = cur.next


class RatingNode:
    def __init__(self, id, user_id, book_id, rating):
        self.next = None
        self.prev = None
        self.id = id
        self.user_id = user_id
        self.book_id = book_id
        self.rating = rating

    def __getitem__(self, index):
        self.items = [self.id, self.user_id, self.book_id, self.rating]
        return self.items[index]

    def __str__(self):
        return (
            "["
            + ", ".join(
                [str(self.id), str(self.user_id), str(self.book_id), str(self.rating)]
            )
            + "]"
        )


class RatingLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def __str__(self):
        cur = self.head
        l = []
        while cur:
            l.append(str(cur))
            cur = cur.next
        if l == []:
            return "[]"
        else:
            return "[" + ", ".join(l) + "]"

    def __getitem__(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def append(self, node):
        new_node = RatingNode(node[0], node[1], node[2], node[3])
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, node):
        new_node = RatingNode(node[0], node[1], node[2], node[3])
        if not self.head:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert(self, node, index):
        new_node = RatingNode(node[0], node[1], node[2], node[3])
        if index == 0:
            self.prepend(node)
        elif index == len(self):
            self.append(node)
        elif index > len(self):
            print("Index out of range.")
        else:
            cur = self[index]
            prv = cur.prev
            prv.next = new_node
            cur.prev = new_node
            new_node.next = cur
            new_node.prev = prv

    def pop(self, index=None):
        if index:
            return self.remove(self[index])
        elif index == 0:
            return self.remove(self[0])
        elif not index:
            return self.remove(self[len(self)])

    def remove(self, node):
        new_node = RatingNode(node[0], node[1], node[2], node[3])
        cur = self.head
        while cur:
            if cur == new_node:
                if cur == self.head:
                    if not cur.next:
                        cur = None
                        self.head = None
                        return new_node
                    else:
                        nxt = cur.next
                        cur.next = None
                        nxt.prev = None
                        cur = None
                        self.head = nxt
                        return new_node
                else:
                    if not cur.next:
                        prv = cur.prev
                        prv.next = None
                        cur.prev = None
                        cur = None
                        return new_node
                    else:
                        nxt = cur.next
                        prv = cur.prev
                        prv.next = nxt
                        nxt.prev = prv
                        cur.prev = None
                        cur.next = None
                        cur = None
                        return new_node
            cur = cur.next


class RequestNode:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __getitem__(self, index):
        self.items = [self.title, self.author]
        return self.items[index]

    def __len__(self):
        return 1

    def __str__(self):
        return "[" + ", ".join([str(self.title), str(self.author)]) + "]"


class RequestQueue:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __str__(self):
        l = []
        for i in self.items:
            l.append(str(i))
        return "[" + ", ".join(l) + "]"

    def enqueue(self, node):
        self.items.append(node)

    def dequeue(self):
        return self.items.pop(0)


database = Database()
