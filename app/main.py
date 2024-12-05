from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str):

    new_customer_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    cleaner_name = Cleaner(cleaner)

    for customer in new_customer_list:
        CinemaBar.sell_product(customer, customer.food)

    CinemaHall(hall_number).movie_session(
        movie,
        new_customer_list,
        cleaner_name
    )
