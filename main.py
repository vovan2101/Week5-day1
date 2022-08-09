# --exersise 1
# -- answer 2
# SELECT *
# FROM actor
# WHERE last_name LIKE 'W%';
#
# --exersise 2
# --answer 5607
# SELECT *
# FROM payment
# WHERE amount >= 3.99 AND amount <= 5.99;
#
# --exersise 3
# --answer 32,33,34,35,36
# SELECT inventory_id, film_id, store_id
# FROM inventory;
#
# --exersise 4
# --answer 2
# SELECT *
# FROM customer
# WHERE first_name LIKE 'Wil%'
#
# --exersise 5
# --answer 2
# SELECT rental_id, rental_date, inventory_id, staff_id
# FROM rental;
#
# --exersise 6
# --answer 2
# SELECT first_name
# FROM staff;
#
# --exersise 7
# --answer Wrong Behavior(id 993)
# SELECT film_id, actor_id
# FROM film_actor;
#
#
# --exersise 8
# --answer 21
# SELECT store_id, last_name
# FROM customer
# WHERE last_name LIKE '%es';
#
# --exersise 9
# --answer
# SELECT *
# FROM rental
# GROUP BY customer_id
# HAVING;

# --exersise 10
# --answer 2 rating categories, Grosse Wonderful and more have the most rating
# SELECT rating, rental_rate, title, rental_rate,rental_duration
# FROM film;





