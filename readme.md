# It Is What It Is

This project is a simple Flask web application that allows users to add and view entries. The entries are stored in a JSON file and can be accessed via an API.

## Features

- Add new entries via a POST request to `/api/entry`
- View all entries on the homepage
- Serve entries as JSON via `/entries.json`

## Setup

1. Clone the repository.
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Create a `.env` file with the following content:
    ```env
    AUTH_PW=your_password_here
    ```
4. Run the application:
    ```sh
    python app.py
    ```

## Endpoints

- `GET /` - View all entries.
- `POST /api/entry` - Add a new entry (requires `X-Password` header).
- `GET /entries.json` - Get all entries in JSON format.
