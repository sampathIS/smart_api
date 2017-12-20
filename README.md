# Smart API

**Awesome API Checker.**

# Requirements

* Python (3.4, 3.5, 3.6)

# Example

Let's take a look at a quick example of using Smart API to build a simple for accessing API's.

Initiate a class 

    from smart_api import CSPApi
    
    my_instance = CSPApi(username="abcdefgijkl",
                         password="lkjigfedcba"
                         )

    my_appication_token = my_instance.application_token(url='https://endpoint.example.com/token/application')

    my_customer_token = my_instance.customer_token(url='https://endpoint.example.com/token/customer')
