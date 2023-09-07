from models import Restaurant, Customer, Review, session

res1 = Restaurant(name="Chipomwitu", price=5000)
res2 = Restaurant(name="Kibandaski", price=100)

customer1 = Customer(first_name="Joe", last_name="Karanja")
customer2 = Customer(first_name="Joseph", last_name="Kinyuru")

review1 = Review(customer=customer1, restaurant=res1, star_rating=3)
review2 = Review(customer=customer1, restaurant=res2, star_rating=5)
review3 = Review(customer=customer2, restaurant=res1, star_rating=4)

session.add_all([res1, res2, customer1, customer2, review1, review2, review3])

session.commit()


