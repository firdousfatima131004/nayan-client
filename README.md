# E-commerce Website (Flask)

This is an E-commerce website built with Flask, where users can browse products, add items to the cart, and proceed with the checkout. Admin users can manage products, view user activity, and perform updates or removals. The website is designed to be user-friendly with an attractive and responsive layout using Bootstrap.

## Features

- **User Authentication:** Users can sign up, log in, and manage their accounts.
- **Admin Dashboard:** Admin can add, update, and remove products from the inventory.
- **Product Management:** Admin can see product details, modify them, and remove unwanted products.
- **Cart & Checkout:** Users can add products to their cart and proceed with payment.
- **Responsive Design:** Built with Bootstrap to ensure the website is mobile-friendly.

## Technologies Used

- **Flask:** The web framework for building the app.
- **SQLAlchemy:** ORM for managing database queries and interactions.
- **Bootstrap:** For responsive front-end design.
- **HTML5:** For structuring the web pages.
- **Python:** For back-end logic.
- **SQLite:** Database for storing user and product data.

Project Directory Structure
────────────────────────────────────────────────────────────────────
```plaintext
├── static/                   # Static files (user images, product images, CSS)
│   ├── userImg/              # User uploaded images
│   ├── img/                  # Product images
│   └── css/                  # CSS files for styling
│
├── templates/                # HTML templates for the pages
│   ├── aboutus.html          # About Us page
│   ├── add_product.html      # Admin page to add new products
│   ├── admin.html            # Admin dashboard
│   ├── cart.html             # User's shopping cart
│   ├── index.html            # Home page with product listings
│   ├── login.html            # User login page
│   ├── payment.html          # Payment page
│   ├── product_detail.html   # Product detail page
│   ├── signup.html           # User registration page
│   ├── update.html           # Page for updating product information
│   ├── user.html             # User profile page
│   └── view_product.html     # Page for viewing a specific product
│
├── README.md                 # Project documentation
├── app.py                    # Main Flask application
├── database.db               # SQLite database file
├── database.py               # Database configuration and functions
├── models.py                 # Database models
└── requirements.txt          # List of required packages
```
────────────────────────────────────────────────────────────────────

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ecommerce-flask.git
   cd ecommerce-flask
   ```
 
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3.Activate the Virtual Environment:
1. **Windows**:
   - The command to activate a virtual environment on **Windows** is:
     ```bash
     venv\Scripts\activate
     ```

2. **macOS/Linux**:
   - The command for **macOS/Linux** to activate the virtual environment is:
     ```bash
     source venv/bin/activate
     ```
4.Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```
5.Run the application:
  ```bash
  python app.py
  ```
6.Open your browser and navigate to http://127.0.0.1:5000 to view the website.

### Database Setup
The application uses SQLite for the database. On the first run, the database will be automatically created, and tables will be set up via SQLAlchemy.

### Endpoints
- `/admin`: Admin dashboard for managing products.
- `/add_product`: Admin page to add new products.
- `/product/<product_id>`: View details of a specific product.
- `/cart`: View and manage your cart.
- `/payment`: Proceed to the payment page.
- `/login`: User login page.
- `/signup`: User registration page.

### Requirements
- Python 3
- Flask
- SQLAlchemy
- Bootstrap (via CDN)
- HTML5

### You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```
## Contributing

If you want to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request with a description of what you have done.

### Authors
Sheikh Firdous Fatima - Initial work




