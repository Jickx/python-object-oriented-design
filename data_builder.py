from datetime import date


# BEGIN (write your solution here)
class Booking:

    def __init__(self):
        self.bookings = []

    def book(self, start, end):
        start_date = self.convert_to_date(start)
        end_date = self.convert_to_date(end)
        if start_date >= end_date:
            return False
        if self.is_available(start_date, end_date):
            self.bookings.append((start_date, end_date))
            print(self.bookings)
            return True
        return False

    def convert_to_date(self, str_date):
        [y, m, d] = str_date.split('-')
        return date(int(y), int(m), int(d))

    def is_available(self, start, end):
        if not self.bookings:
            return True
        for (book_start, book_end) in self.bookings:
            if (start < book_end) and (book_start < end):
                return False
        return True
# END


def test_booking():
    booking = Booking()

    assert not booking.book('2008-11-10', '2008-11-05')
    assert booking.book('2008-11-11', '2008-11-13')
    assert not booking.book('2008-11-12', '2008-11-12')
    assert not booking.book('2008-11-12', '2008-11-14')
    assert booking.book('2008-11-10', '2008-11-11')
    assert not booking.book('2008-11-12', '2008-11-13')
    assert not booking.book('2008-11-13', '2008-11-13')
    assert booking.book('2008-11-13', '2008-11-14')
    assert booking.book('2008-05-08', '2008-05-18')
    assert not booking.book('2008-05-09', '2008-05-10')

test_booking()
