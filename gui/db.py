import sys, os, sqlite3
from PyQt5 import QtGui

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


class Database:
    def __init__(self):
        self.db = sqlite3.connect("rsrc/db/data.db")
        self.curs = self.db.cursor()
        self.updateDatabase(True, True, True, True)
        # self.rank = Rank()

    def initFont(self):
        self.fontDB = QtGui.QFontDatabase()
        self.fontDB.addApplicationFont(":/Font/font/Better Grade/Better Grade.ttf")
        self.fontDB.addApplicationFont(
            ":/Font/font/Product Sans/Product Sans Regular.ttf"
        )
        self.fontDB.addApplicationFont(
            ":/Font/font/Helvetica Neue/Helvetica Neue LT 93 Black Extended Oblique.ttf"
        )
        self.fontDB.addApplicationFont(
            ":/Font/font/Helvetica Neue/Helvetica Neue LT 87 Heavy Condensed Oblique.ttf"
        )
        self.fontDB.addApplicationFont(
            ":/Font/font/Helvetica Neue/Helvetica Neue LT 63 Medium Extended Oblique.ttf"
        )
        self.fontDB.addApplicationFont(
            ":/Font/font/Helvetica Neue/Helvetica Neue LT 63 Medium Extended.ttf"
        )
        self.fontDB.addApplicationFont(
            ":/Font/font/Helvetica Neue/Helvetica Neue LT 53 Extended.ttf"
        )
        self.fontDB.addApplicationFont(
            ":/Font/font/Helvetica Neue/Helvetica Neue LT 55 Roman.ttf"
        )
        self.fontDB.addApplicationFont(
            ":/Font/font/Helvetica Neue/Helvetica Neue LT 47 Light Condensed.ttf"
        )
        self.fontDB.addApplicationFont(
            ":/Font/font/Helvetica Neue/Helvetica Neue LT 23 Ultra Light Extended Oblique.ttf"
        )

    def updateDatabase(self, users=False, books=False, cur_user=False, reviews=False):
        if users:
            self.curs.execute("SELECT * FROM users")
            users_db = self.curs.fetchall()
            user_db = [i for i in range(len(users_db))]
            self.users_ll = UserLinkedList()
            for i in range(len(users_db)):
                user_db[i] = UserNode(
                    users_db[i][0],
                    users_db[i][3],
                    users_db[i][2],
                    users_db[i][3],
                    users_db[i][4],
                    users_db[i][5],
                    users_db[i][6],
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
                    books_db[i][2],
                    books_db[i][3],
                    books_db[i][4],
                    books_db[i][5],
                    books_db[i][6],
                    books_db[i][7],
                )
                self.books_ll.append(book_db[i])
            self.books_ll.sort(0)

            self.fiction_ll = BookLinkedList()
            for i in self.books_ll:
                if i[6] == "fiction":
                    self.fiction_ll.append(i)

            self.thriller_ll = BookLinkedList()
            for i in self.books_ll:
                if i[6] == "thriller":
                    self.thriller_ll.append(i)

            self.fantasy_ll = BookLinkedList()
            for i in self.books_ll:
                if i[6] == "fantasy":
                    self.fantasy_ll.append(i)

            self.romance_ll = BookLinkedList()
            for i in self.books_ll:
                if i[6] == "romance":
                    self.romance_ll.append(i)

            self.biography_ll = BookLinkedList()
            for i in self.books_ll:
                if i[6] == "biography":
                    self.biography_ll.append(i)

            self.comedy_ll = BookLinkedList()
            for i in self.books_ll:
                if i[6] == "comedy":
                    self.comedy_ll.append(i)

            self.horror_ll = BookLinkedList()
            for i in self.books_ll:
                if i[6] == "horror":
                    self.horror_ll.append(i)

            self.poetry_ll = BookLinkedList()
            for i in self.books_ll:
                if i[6] == "poetry":
                    self.poetry_ll.append(i)

        if cur_user:
            self.curs.execute("SELECT * FROM current_user")
            try:
                cur_users_db = self.curs.fetchone()
                self.cur_user = CurUser(cur_users_db[0], cur_users_db[1])
            except:
                self.cur_user = CurUser(None, None)

        if reviews:
            self.curs.execute("SELECT * FROM reviews")
            revs_db = self.curs.fetchall()
            rev_db = [i for i in range(len(revs_db))]
            self.revs_ll = ReviewLinkedList()
            for i in range(len(revs_db)):
                rev_db[i] = ReviewNode(
                    revs_db[i][0],
                    revs_db[i][1],
                    revs_db[i][2],
                    revs_db[i][5],
                    revs_db[i][3],
                    revs_db[i][4],
                )
                self.revs_ll.append(rev_db[i])

            self.revs_user = {}
            self.revs_book = {}
            for i in self.revs_ll:
                try:
                    self.revs_book[i[1]].append(i[0])
                    self.revs_user[i[2]].append(i[0])
                except:
                    self.revs_book[i[1]] = [i[0]]
                    self.revs_user[i[2]] = [i[0]]


class Rank:
    def __init__(self, genre=None, rank=None):
        self.genre = genre
        self.rank = rank


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
    def __init__(self, id, f_name, l_name, username, password, email=None, img=None):
        self.next = None
        self.prev = None
        self.id = id
        self.f_name = f_name
        self.l_name = l_name
        self.username = username
        self.password = password
        self.email = email if email else None
        self.img = img if img else ":/Image/db/userimg/dafault-pic.png"

    def __getitem__(self, index):
        self.items = [
            self.id,
            self.f_name,
            self.l_name,
            self.username,
            self.password,
            self.email,
            self.img,
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
            node[0], node[1], node[2], node[3], node[4], node[5], node[6]
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
            node[0], node[1], node[2], node[3], node[4], node[5], node[6]
        )
        if not self.head:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert(self, node, index):
        new_node = UserNode(
            node[0], node[1], node[2], node[3], node[4], node[5], node[6]
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
            node[0], node[1], node[2], node[3], node[4], node[5], node[6]
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
                    # str(self.synop),
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

    def sort(self, type):
        if type == 0:
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
        elif type == 1:
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
        elif type == 3:
            pass
        elif type == 4:
            pass
        return self

    def search(self, key):
        if not key:
            return
        key = key.upper()
        res = BookLinkedList()
        cur = self.head
        added = False
        while cur:
            title = cur.title.split()
            for t in title:
                if t.upper().startswith(key):
                    res.append(cur)
                    added = True
            author = cur.author.split()
            for a in author:
                if a.upper().startswith(key) and not added:
                    res.append(cur)
            cur = cur.next
            added = False
        if not cur:
            return res


class ReviewNode:
    def __init__(self, id, user_id, book_id, date_created, rating=None, comment=None):
        self.next = None
        self.prev = None
        self.id = id
        self.user_id = user_id
        self.book_id = book_id
        self.date_created = date_created
        self.rating = rating if rating else None
        self.comment = comment if comment else None

    def __getitem__(self, index):
        self.items = [
            self.id,
            self.user_id,
            self.book_id,
            self.date_created,
            self.rating,
            self.comment,
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
                    str(self.date_created),
                    str(self.rating),
                    str(self.comment),
                ]
            )
            + "]"
        )


class ReviewLinkedList:
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
        new_node = ReviewNode(node[0], node[1], node[2], node[3], node[4], node[5])
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
        new_node = ReviewNode(node[0], node[1], node[2], node[3], node[4], node[5])
        if not self.head:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert(self, node, index):
        new_node = ReviewNode(node[0], node[1], node[2], node[3], node[4], node[5])
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
        new_node = ReviewNode(node[0], node[1], node[2], node[3], node[4], node[5])
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
    def __init__(self, user_id, title, author):
        self.user_id = user_id
        self.title = title
        self.author = author

    def __getitem__(self, index):
        self.items = [self.user_id, self.title, self.author]
        return self.items[index]

    def __len__(self):
        return 1

    def __str__(self):
        return (
            "["
            + ", ".join([str(self.user_id), str(self.title), str(self.author)])
            + "]"
        )


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


def exit():
    for i in req_q:
        database.curs.execute(
            "INSERT INTO requests (user_id, title, author) VALUES (?,?,?)",
            [i[0], i[1], i[2]],
        )
        database.db.commit()
    database.db.close()


database = Database()
req_q = RequestQueue()
