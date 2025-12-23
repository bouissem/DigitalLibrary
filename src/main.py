from book import Book
from user import User
from library import Library


def main():
    library = Library()

    # إنشاء كتب
    book1 = Book(1, "Python Programming", "Guido van Rossum")
    book2 = Book(2, "Object Oriented Design", "James Gosling")

    # إنشاء مستخدمين
    user1 = User(1, "Ahmed")
    user2 = User(2, "Sara")

    # إضافة الكتب والمستخدمين
    library.add_book(book1)
    library.add_book(book2)

    library.register_user(user1)
    library.register_user(user2)

    # عرض الحالة
    library.display_status()

    # إعارة كتاب
    library.borrow_book(1, 1)

    # عرض الحالة بعد الإعارة
    library.display_status()

    # إرجاع الكتاب
    library.return_book(1)

    # عرض الحالة النهائية
    library.display_status()


if __name__ == "__main__":
    main()
