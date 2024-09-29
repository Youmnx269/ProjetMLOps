import unittest
from appYH import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

def test_predict(self):
    # Simuler les données du formulaire
    test_data = {'credit_lines_outstanding': 10, 'loan_amt_outstanding': 20000,
                 'total_debt_outstanding': 5000, 'income': 40000, 'years_employed': 5, 'fico_score': 700}
    response = self.app.post('/predict', data=test_data)
    self.assertEqual(response.status_code, 200)
    print(str(response.data))  # Ajoutez cette ligne ici
    self.assertIn("Le client est à surveiller, il présente un risque d'être en défaut de paiement.", str(response.data))

if __name__ == '__main__':
    unittest.main()
