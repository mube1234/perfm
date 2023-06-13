<h1>PerFM - Personal Finance Manager</h1>

<p>PerFM is a powerful and intuitive personal finance manager designed to empower individuals in taking control of their financial journey. This project was developed as part of the Portfolio Project for Holberton School, with the aim of addressing the common struggles many people face when managing their finances.</p>

<h2>Features</h2>

<ul>
  <li><strong>Expense Tracking:</strong> Easily track your expenses and categorize them for better financial visibility.</li>
  <li><strong>Budget Management:</strong> Set budgets and monitor your spending to stay on track and achieve your financial goals.</li>
  <li><strong>Income Management:</strong> Record your income sources and keep a comprehensive overview of your financial inflows.</li>
  <li><strong>Category Management:</strong> Create and manage custom expense categories for personalized financial tracking.</li>
  <li><strong>User-Friendly Interface:</strong> PerFM provides a sleek and intuitive interface, making it easy to navigate and use the platform effectively.</li>
</ul>

<h2>Installation</h2>

<p>To run PerFM on your local machine, follow these steps:</p>

<ol>
  <li>Clone the repository: <code>git clone https://github.com/your-username/PerFM.git</code></li>
  <li>Navigate to the project directory: <code>cd PerFM</code></li>
  <li>Create a virtual environment: <code>python -m venv venv</code></li>
  <li>Activate the virtual environment:
    <ul>
      <li>For Windows: <code>venv\Scripts\activate</code></li>
      <li>For macOS/Linux: <code>source venv/bin/activate</code></li>
    </ul>
  </li>
  <li>Install the project dependencies: <code>pip install -r requirements.txt</code></li>
  <li>Apply database migrations: <code>python manage.py migrate</code></li>
  <li>Start the development server: <code>python manage.py runserver</code></li>
</ol>

<p>Visit <a href="http://localhost:8000">http://localhost:8000</a> in your web browser to access PerFM.</p>
