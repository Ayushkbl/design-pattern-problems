from datetime import datetime, timedelta

from movie_ticket.location.cinema import Cinema
from movie_ticket.location.layout import Layout
from movie_ticket.location.room import Room
from movie_ticket.movie_booking_system import MovieBookingSystem
from movie_ticket.rate.normal_rate import NormalRate
from movie_ticket.showing.movie import Movie
from movie_ticket.showing.screening import Screening

class TestMovieBookingSystem:

    def test_browse_and_buy(self):
        print("\n=== Testing Movie Booking System: Browse and Buy Flow ===")
        booking_system = MovieBookingSystem()
        print("\n--- Creating Room and Setting Up Seat Pricing ---")
        # create a room with a layout of 10x10 seats with a normal rate of $10.00
        room = Room("1", Layout(10, 10))
        for i in range(10):
            for j in range(10):
                seat = room.layout.get_seats_by_position(i, j)
                if seat:
                    seat.pricing_strategy = NormalRate(10.00)

        print("✓ Created room '1' with 10x10 seats, each seat priced at $10.00")

        print("\n--- Adding Cinema to Booking System ---")
        # create a cinema with the room
        booking_system.add_cinema(Cinema("Test Cinema", "Test Location"))
        print("✓ Added cinema: 'Test Cinema' at 'Test Location'")

        print("\n--- Creating Movie and Screening ---")
        # create a test movie with a test screening in the room
        length = 180
        movie = Movie("Test Movie", "Test Description", length)
        screening = Screening(movie, room, datetime.now(), datetime.now()+timedelta(minutes=length))
        print("✓ Created movie: 'Test Movie' (180 min)")
        print("✓ Created screening for 'Test Movie' in room '1'")

        print("\n--- Adding Movie and Screening to Booking System ---")
        # add the movie and screening to the booking system
        booking_system.add_movie(movie)
        booking_system.add_screening(movie, screening)
        print("✓ Added movie and screening to booking system")

        print("\n--- Verifying Movies and Screenings in System ---")
        # test that the movie and screening are in the booking system
        assert len(booking_system.movies) == 1
        assert len(booking_system.get_screening_for_movies(movie))== 1
        print("✓ Verified: 1 movie and 1 screening present in system")

        print("\n--- Checking Available Seats ---")
        # test that the available seats for the screening are correct
        assert len(booking_system.get_available_seats(screening)) == 100
        print("✓ Verified: 100 seats available for the screening")

        print("\n--- Booking a Ticket ---")
        # test that the booking system can book a ticket
        seat = room.layout.get_seats_by_position(0, 0)
        if seat:
            booking_system.book_ticket(screening, seat)
            assert booking_system.get_ticket_count(screening) == 1
            print("✓ Booked seat (0,0) for 'Test Movie' screening")
            print("✓ Verified: 1 ticket booked for the screening")

        print("\n--- Checking Ticket Price ---")
        # test the price of the ticket
        assert booking_system.get_tickets_for_screening(screening)[0].price == 10.00
        print("✓ Verified: Ticket price is $10.00")
        print("=== Movie Booking System Test Completed Successfully ===\n")
