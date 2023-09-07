from models import Restaurant, Customer, Review, session
from sqlalchemy.orm.exc import NoResultFound

if __name__ == "__main__":

    chipomwitu = Restaurant(name="Shadle", price=3050)
    kibandaski = Restaurant(name="Kibandaski", price=120)

    customer1 = Customer(first_name="Joe", last_name="Karanja")
    customer2 = Customer(first_name="Joseph", last_name="Kinyuru")
    customer3 = Customer(first_name="Steve", last_name="Ndaba")

    session.add_all([chipomwitu, kibandaski, customer1, customer2, customer3])
    session.commit()

    fanciest_restaurant = Restaurant.fanciest()

    print(f"Fanciest restaurant: {fanciest_restaurant.name}")

    chipomwitu = session.query(Restaurant).filter_by(name="Shadle").first()

    if chipomwitu:
        lavender_lutta_reviewed = session.query(Review).filter(
            Review.customer_id == customer3.id,
            Review.restaurant_id == chipomwitu.id
        ).first()

        if not lavender_lutta_reviewed:
            review1 = Review(customer=customer3, restaurant=chipomwitu, star_rating=5)
            session.add(review1)
            session.commit()
            print("Added review for Chipomwitu by Lavender Lutta")
        else:
            print("Lavender Lutta has already reviewed Chipomwitu.")
    else:
        print("Shadle does not exist.")

    customer2 = session.query(Customer).filter_by(first_name="Joseph").first()

    if customer2:
        favorite_restaurant = customer2.favorite_restaurant()

        if favorite_restaurant:
            print(f"Favorite restaurant for Joseph Kinyuru: {favorite_restaurant.name}")
        else:
            print("Joseph Kinyuru has not reviewed any restaurants yet.")
    else:
        print("Customer Joseph Kinyuru not found.")

    chipomwitu = session.query(Restaurant).filter_by(name="Chipomwitu").first()

    if chipomwitu:
        review_count = session.query(Review).filter_by(restaurant_id=chipomwitu.id).count()

        print(f"Number of reviews for Chipomwitu: {review_count}")
    else:
        print("Chipomwitu does not exist.")
