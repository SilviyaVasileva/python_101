import unittest
from datetime import datetime, timedelta
from cancellationPolicy import validate_conditions, ensure_conditions, group_conditions, get_cancellation_policy, get_current_condition, get_hours

class TestValidateConditions(unittest.TestCase):
    def test_validation_passes_with_valid_conditions(self):
        conditions = [
            {'hours': 10, 'percent': 10},
            {'percent': 100}
        ]

        validate_conditions(conditions)

    def test_raises_exception_if_all_conditions_have_hours(self):
        conditions = [
            {'hours': 10, 'percent': 10}
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid conditions.')

    def test_raises_exception_if_more_than_one_condition_with_no_hours(self):
        conditions = [
            {'hours': 10, 'percent': 10000},
            {'percent': 10},
            {'percent': 100}
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid conditions.')

    def test_raises_exception_if_hours_bigger_than_24(self):
        # ARRANGE
        conditions = [
            {'hours': 72, 'percent': 10000},
            {'percent': 10},
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Hours cannot be > 24.')


class TestEnsureConditions(unittest.TestCase):

	def test_ensure_conditions_true(self):
		conditions = [{'hours': 10, 'percent': 10}, {'percent': 20}]

		exc = ensure_conditions(conditions)

		self.assertEqual(exc, [{'hours': 10, 'percent': 10}, {'hours': 0,'percent': 20}])


class TestGroup(unittest.TestCase):
    def test_group_conditions(self):
        conditions = [{'hours': 12, 'percent': 15}, {'hours': 1, 'percent': 25}, {'hours': 20, 'percent': 10}]

        res = group_conditions(conditions)
        exp = [{'hours': 20, 'percent': 10}, {'hours': 12, 'percent': 15}, {'hours': 1, 'percent': 25}]

        self.assertEqual(exp, res)


class TestGetCancellationPolicy(unittest.TestCase):
    def test_get_cancellation_policy_now_bigger_then_start(self):
        conditions = [{'percent': 10}]
        price = 1000
        now = datetime.now()
        start = now - timedelta(hours=10)
        res = get_cancellation_policy(conditions, price, start, now)

        self.assertEqual(res, price) #nedoobmisleno!!!!
    
    def test_get_cancellation_policy_for_one_element(self):
        conditions = [{'percent': 10}]
        price = 1000
        now = datetime.now()
        start = now + timedelta(hours=10)
        res = get_cancellation_policy(conditions, price, start, now)

        self.assertEqual(res, 100)
    
    def test_get_cancellation_policy(self):
        conditions =  [{'hours': 10, 'percent': 10},{'hours': 5, 'percent': 50},
            {'hours':0, 'percent': 100}]
        price = 1000
        now = datetime.now()
        start = now + timedelta(hours=6)
        res = get_cancellation_policy(conditions, price, start, now)

        self.assertEqual(res, 100)
    

class TestGetCurrentConditions(unittest.TestCase):
    def test_get_current_condition_bigger_hour(self):
        conditions = [{'hours': 10, 'percent': 10},
            {'percent': 100}]
        now = datetime.now()
        start = now + timedelta(hours=21)

        res = get_current_condition(conditions, start, now)
            	
        self.assertTrue(21 <= res['hours'])

    
    def test_get_current_condition_hour_is_start(self):
        conditions = [{'hours': 10, 'percent': 10},
            {'hours': 0, 'percent': 100}]
        now = datetime.now()
        start = now

        res = get_current_condition(conditions, start, now)
                
        self.assertTrue(0 <= res['hours'])
    
    def test_get_current_condition_hour(self):
        conditions = [{'hours': 10, 'percent': 10},
            {'hours':0, 'percent': 100}]
        now = datetime.now()
        start = now + timedelta(hours=5)
    
        res = get_current_condition(conditions, start, now)
                
        self.assertTrue(5<= res['hours'])

    def test_get_current_condition_hour_2(self):
        conditions = [{'hours': 10, 'percent': 10},{'hours': 5, 'percent': 50},
            {'hours':0, 'percent': 100}]
        now = datetime.now()
        start = now + timedelta(hours=5)
    
        res = get_current_condition(conditions, start, now)
        self.assertTrue(5 <= res['hours'])


class TestGetHours(unittest.TestCase):
    def test_get_hours(self):
        now = datetime.now()
        start = now + timedelta(hours=55)

        h = get_hours(start, now)

        self.assertEqual(h, 55)
        


if __name__ == '__main__':
    unittest.main()