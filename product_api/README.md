# Unified Product, Carts, and Users API with UI

This is a unified Flask application that serves as a backend API for products, carts, and users, and also includes a frontend UI to interact with this data.

## Features

### API Endpoints

*   **Products**
    *   `GET /api/products`: Retrieve all products.
    *   `GET /api/products/<int:id>`: Retrieve a specific product by ID.
    *   `GET /api/products/search?q=<query>`: Search products by title, description, or category.
*   **Carts**
    *   `GET /api/carts`: Retrieve all carts.
    *   `GET /api/carts/<int:id>`: Retrieve a specific cart by ID.
*   **Users**
    *   `GET /api/users`: Retrieve all users.
    *   `GET /api/users/<int:id>`: Retrieve a specific user by ID.

### Frontend UI

*   **Home**: Redirects to the product list.
*   **Products**: Browse and search products. View product details.
*   **Carts**: View all carts and their details.
*   **Users**: View all users and their profiles.

## Setup and Installation

1.  **Prerequisites**: Ensure you have Python 3.x installed.
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Application**:
    ```bash
    python app.py
    ```
4.  **Access the Application**:
    *   Open your browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

*   `app.py`: Main Flask application logic.
*   `products.json`: Product data.
*   `carts.json`: Cart data.
*   `users.json`: User data.
*   `static/`: CSS and other static assets.
*   `templates/`: HTML templates.
