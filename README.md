Projet_Facturation
Overview
Projet_Facturation is a Django-based application that allows users to manage clients, checks, and invoices. It provides functionality to create, update, view, delete, and generate PDF invoices for clients. The application is designed to be simple, user-friendly, and efficient for small businesses or freelancers who need to manage their financial documents.

Features
Clients Management: Create, read, update, and delete client information.
Checks Management: Manage checks issued to clients, including status and amount.
Invoices Management: Manage invoices for clients, including generating PDF versions.
Generate Invoices as PDFs: Generate invoices for each client or all clients in a PDF format using FPDF.
Bootstrap Styling: User interface styled with Bootstrap 4.5.2 for a clean and responsive design.
Technologies Used
Django: Backend framework for building the web application.
FPDF: Python library for generating PDF documents.
Bootstrap 4.5.2: CSS framework for responsive and modern UI design.
SQLite: Default database used by Django for development.
Project Structure
The project has a typical Django structure:

Installation and Setup
Clone the Repository:

bash
Copy code
git clone https://github.com/AnasM21/Projet_Facturation.git
cd Projet_Facturation
Create a Virtual Environment:

bash
Copy code
python -m venv env
Activate the Virtual Environment:

On Windows:
bash
Copy code
.\env\Scripts\activate
On macOS and Linux:
bash
Copy code
source env/bin/activate
Install the Required Packages:

bash
Copy code
pip install -r requirements.txt
Apply Migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the Development Server:

bash
Copy code
python manage.py runserver
The application will be accessible at http://127.0.0.1:8000/.

Usage
Home Page: Displays an overview with links to manage clients, checks, and invoices.
Clients Section: Allows you to add, edit, and delete clients.
Checks Section: Manage checks, view their statuses, and link them to clients.
Invoices Section: Add, update, delete invoices, and generate PDF invoices for each client.
Generate PDF Invoice
To generate a PDF invoice for a client:

Go to the Invoices section.
Click on the "Generate PDF Invoice" button next to the respective client.
The generated PDF will be downloaded directly.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contribution
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
Acknowledgements
Django - The web framework used.
FPDF - Library used to generate PDFs.
Bootstrap - Front-end component library.
Contact
For any questions or suggestions, please contact Anas M21.

