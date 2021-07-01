from django.test import TestCase
from .models import Users
from .forms import Registration
from .views import *


class MainRouteTest(TestCase):
    def setUp(self):
        pass

    def test_method_get(self):
        response = self.client.get('/main')
        self.assertEqual(response.status_code, 200)

    def test_method_put(self):
        response = self.client.put('/main')
        self.assertEqual(response.status_code, 403)

    def test_method_post_with_missing_fields(self):
        response = self.client.post(
            '/main', {'FirstName': 'Kaneki'}, 'application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)
        latest_result = Response.objects.all().last()
        self.assertEqual(latest_result.Response, 'Bad Request')
        self.assertEqual(latest_result.Reason, 'Invalid Fields')

    def test_method_post_with_all_fields(self):
        data = {
            'FirstName': "Eren",
            'LastName': "Yeagar",
            'DOB': "1992-01-20",
            'Gender': "Male",
            'National': "Indian",
            'City': "Salem",
            'Pin': "123456",
            'State': "Bihar",
            'Qualification': "BSE",
            'Salary': "40000",
            'PanNum': "PAN9872",
        }
        form = Registration(data)
        response = self.client.post(
            '/main', form.data)
        self.assertEqual(response.status_code, 200)
        user = Users.objects.all().last()
        self.assertEqual(user.FirstName, 'Eren')
        self.assertEqual(user.LastName, 'Yeagar')
        self.assertEqual(user.Gender, 'Male')
        self.assertEqual(user.DOB, '1992-01-20')
        self.assertEqual(user.National, 'Indian')
        self.assertEqual(user.City, 'Salem')
        self.assertEqual(user.Pin, '123456')
        self.assertEqual(user.State, 'Bihar')
        self.assertEqual(user.Qualification, 'BSE')
        self.assertEqual(user.Salary, '40000')
        self.assertEqual(user.PanNum, 'PAN9872')

    def test_validate_form_fields(self):
        data = {
            'FirstName': "Eren",
            'LastName': "Yeagar",
            'DOB': "20-01-2000",
            'Gender': "Male",
            'National': "Indian",
            'City': "Salem",
            'Pin': "123456",
            'State': "Bihar",
            'Qualification': "BSE",
            'Salary': "40000",
            'PanNum': "PAN9872",
        }

        val = index2(data['DOB'])
        self.assertEqual(val, 'Format should be %Y-%m-%d')

    def test_validate_gender(self):
        data = {
            'FirstName': "Eren",
            'LastName': "Yeagar",
            'DOB': "1992-03-20",
            'Gender': "Mal",
            'National': "Indian",
            'City': "Salem",
            'Pin': "123456",
            'State': "Bihar",
            'Qualification': "BSE",
            'Salary': "40000",
            'PanNum': "PAN9872",
        }

        val = gender_data(data['Gender'])
        self.assertEqual(val, 'Not a Valid')

    def test_validate_city(self):
        data = {
            'FirstName': "Eren",
            'LastName': "Yeagar",
            'DOB': "1992-03-20",
            'Gender': "Male",
            'National': "Indian",
            'City': "Salem",
            'Pin': "123456",
            'State': "Bihar",
            'Qualification': "BSE",
            'Salary': "40000",
            'PanNum': "PAN9872",
        }
        val = get_city(data['City'])
        self.assertEqual(val, 'Salem')

    def test_validate_nation(self):
        data = {
            'FirstName': "Eren",
            'LastName': "Yeagar",
            'DOB': "1992-03-20",
            'Gender': "Male",
            'National': "India",
            'City': "Salem",
            'Pin': "123456",
            'State': "Bihar",
            'Qualification': "BSE",
            'Salary': "40000",
            'PanNum': "PAN9872",
        }
        val = get_nationality(data['National'])
        self.assertEqual(val, 'Enter valid nationality')

    def test_validate_pin(self):
        data = {
            'FirstName': "Eren",
            'LastName': "Yeagar",
            'DOB': "1992-03-20",
            'Gender': "Male",
            'National': "Indian",
            'City': "Salem",
            'Pin': "123456",
            'State': "Bihar",
            'Qualification': "BSE",
            'Salary': "40000",
            'PanNum': "PAN9872",
        }
        val = get_pin(data['Pin'])
        self.assertEqual(val, '123456')

    def test_validate_state(self):
        data = {
            'FirstName': "Eren",
            'LastName': "Yeagar",
            'DOB': "1992-03-20",
            'Gender': "Male",
            'National': "Indian",
            'City': "Salem",
            'Pin': "123456",
            'State': "Kerala",
            'Qualification': "BSE",
            'Salary': "40000",
            'PanNum': "PAN9872",
        }
        val = get_state(data['State'])
        self.assertEqual(val, 'State not present')

    def test_validate_qualification(self):
        data = {
            'FirstName': "Eren",
            'LastName': "Yeagar",
            'DOB': "1992-03-20",
            'Gender': "Male",
            'National': "Indian",
            'City': "Salem",
            'Pin': "123456",
            'State': "Bihar",
            'Qualification': "BSE",
            'Salary': "40000",
            'PanNum': "PAN9872",
        }
        val = get_qualification(data['Qualification'])
        self.assertEqual(val, 'BSE')

    def test_validate_salary(self):
        data = {
            'FirstName': "Eren",
            'LastName': "Yeagar",
            'DOB': "1992-03-20",
            'Gender': "Male",
            'National': "India",
            'City': "Salem",
            'Pin': "123456",
            'State': "Bihar",
            'Qualification': "BSE",
            'Salary': "1",
            'PanNum': "PAN9872",
        }
        val = get_salary(data['Salary'])
        self.assertEqual(val, 'Salary from 11,000 to 89,000')

    def test_validate_pan(self):
        data = {
            'FirstName': "Eren",
            'LastName': "Yeagar",
            'DOB': "1992-03-20",
            'Gender': "Male",
            'National': "India",
            'City': "Salem",
            'Pin': "123456",
            'State': "Bihar",
            'Qualification': "BSE",
            'Salary': "45000",
            'PanNum': "PAN9872",
        }
        val = pan_number(data['PanNum'])
        self.assertEqual(val, 'PAN9872')

    def test_validate_date(self):
        data = {
            'FirstName': "Eren",
            'LastName': "Yeagar",
            'DOB': "20-02-1990",
            'Gender': "Male",
            'National': "India",
            'City': "Salem",
            'Pin': "123456",
            'State': "Bihar",
            'Qualification': "BSE",
            'Salary': "45000",
            'PanNum': "PAN9872",
        }
        val = validate_date(22, data['Gender'])
        val2 = validate_date(20, data['Gender'])
        val3 = validate_date(index2(data['DOB']), data['Gender'])
        self.assertEqual(val, 'Success')
        self.assertEqual(val2, 'Invalid Input for DOB')
        self.assertEqual(val3, "Format should be %Y-%m-%d")

    def test_entry_data(self):
        data = {
            'FirstName': "Eren",
            'LastName': "Yeagar",
            'DOB': "20-02-1990",
            'Gender': "Male",
            'National': "Indian",
            'City': "Salem",
            'Pin': "123456",
            'State': "Bihar",
            'Qualification': "BSE",
            'Salary': "45000",
            'PanNum': "PAN9872",
        }
        val1, val2 = validate_all_data(
            "Format should be %Y-%m-%d", "Success", "Validate Success", data['State'], "45000", data['National'])
        val3, val4 = validate_all_data(
            22, "Invalid Input for DOB", "Validate Success", data['State'], "45000", data['National'])
        val5, val6 = validate_all_data(
            22, "Success", "Activity in last five days", data['State'], "45000", data['National'])

        val7, val8 = validate_all_data(
            22, "Success", "Validate Success", "State not present", "45000", data['National'])

        val9, val10 = validate_all_data(
            22, "Success", "Validate Success", data['State'], "Salary from 11,000 to 89,000", data['National'])

        val11, val12 = validate_all_data(
            22, "Success", "Validate Success", data['State'], data['Salary'], "Enter valid nationality")

        self.assertEqual(val1, "Validation Failure")
        self.assertEqual(val2, "Invalid Input for DOB")
        self.assertEqual(val3, "Failed")
        self.assertEqual(val4, "Age is less than excepted")
        self.assertEqual(val5, "Failed")
        self.assertEqual(val6, "Recently request received in last 5 days")
        self.assertEqual(val7, "Failed")
        self.assertEqual(val8, "State not present")
        self.assertEqual(val9, "Failed")
        self.assertEqual(val10, "Salary from 11,000 to 89,000")
        self.assertEqual(val11, "Failed")
        self.assertEqual(val12, "Enter valid nationality")

    def test_pan_data(self):
        data = {
            'FirstName': "Eren",
            'LastName': "Yeagar",
            'DOB': "1990-02-12",
            'Gender': "Male",
            'National': "Indian",
            'City': "Salem",
            'Pin': "123456",
            'State': "Bihar",
            'Qualification': "BSE",
            'Salary': "45000",
            'PanNum': "97678",
        }
        val1 = validate_pan(data['PanNum'])
        self.assertEqual(val1, "New User")
