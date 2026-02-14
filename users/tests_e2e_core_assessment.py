import json
import uuid
from django.test import TestCase, Client
from django.urls import reverse
from users.models import UserRegistration
from resumeanalysis.models import TestAttempt
from django.utils import timezone

class CoreAssessmentE2ETest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a test user
        self.user_id = "testuser123"
        self.password = "password123"
        self.user = UserRegistration.objects.create(
            userid=self.user_id,
            password=self.password,
            email="testuser@example.com",
            mobile="1234567890",
            user_type='student'
        )
        # Login the user
        session = self.client.session
        session['userid'] = self.user.userid # Use 'userid' instead of 'user_id'
        session['username'] = self.user.userid # Also set 'username'
        session.save()

    def test_complete_core_assessment_flow(self):
        """Full E2E flow: Selection -> Variations -> Start -> Submit -> Unlock"""
        # 1. Access core assessment selection
        response = self.client.get(reverse('users:core_assessment_selection'))
        self.assertEqual(response.status_code, 200)
        # The actual template is 'mock_test/Core Assessment Areas/index.html'
        self.assertTemplateUsed(response, 'mock_test/Core Assessment Areas/index.html')
        self.assertContains(response, "Aptitude Modules")

        # 2. View variations for Aptitude
        # Note: test_variations is in the root URLconf (no namespace)
        response = self.client.get(reverse('test_variations', kwargs={
            'test_type': 'core',
            'category': 'aptitude',
            'test_index': 0
        }))
        self.assertEqual(response.status_code, 200)
        
        # Check if Module 1 is available and Module 2 is locked
        variations = response.context['variations']
        self.assertEqual(len(variations), 2)
        self.assertTrue(variations[0]['available'], "Module 1 should be available by default")
        self.assertFalse(variations[1]['available'], "Module 2 should be locked initially")

        # 3. Start Module 1
        response = self.client.get(reverse('start_exam', kwargs={
            'test_type': 'core',
            'category': 'aptitude',
            'test_index': 0
        }))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertIn('questions', data)
        self.assertTrue(len(data['questions']) > 0)
        
        # Store current test info in session (mimic frontend/backend session behavior)
        session = self.client.session
        session['current_test'] = {
            'type': 'core',
            'category': 'aptitude',
            'test_index': 0,
            'questions': data['questions']
        }
        session.save()

        # 4. Submit Module 1
        # Prepare answers (all correct for simplicity)
        user_answers = {}
        for i, q in enumerate(data['questions']):
            # Debug: print question info if it fails
            correct = q.get('correct') or q.get('correct_answer') or q.get('answer')
            user_answers[str(i)] = correct

        submit_data = {
            'test_type': 'core',
            'category': 'aptitude',
            'test_index': 0,
            'user_answers': json.dumps(user_answers),
            'time_taken': 600
        }
        
        # Also include questions in the payload just in case session is cleared
        submit_data['questions'] = json.dumps(data['questions'])
        
        response = self.client.post(reverse('submit_exam'), submit_data)
        self.assertEqual(response.status_code, 200)
        submit_result = response.json()
        self.assertEqual(submit_result['status'], 'success')
        
        # If percentage is not 100, let's see why
        if submit_result['results']['percentage'] != 100:
            print("\nDEBUG: Test failed to get 100%. Detailed results:")
            for res in submit_result['results']['detailed_results']:
                if not res['is_correct']:
                    print(f"Q: {res['question']}")
                    print(f"  User: {res['user_answer']} (type: {type(res['user_answer'])})")
                    print(f"  Correct: {res['correct_answer']} (type: {type(res['correct_answer'])})")
        
        self.assertEqual(submit_result['results']['percentage'], 100)

        # 5. Verify database storage
        attempt = TestAttempt.objects.filter(
            user=self.user,
            test_type='core',
            category='aptitude',
            module_index=0
        ).first()
        self.assertIsNotNone(attempt)
        self.assertEqual(attempt.status, 'completed')
        self.assertEqual(attempt.total_score, 100)

        # 6. Verify Module 2 is now unlocked
        response = self.client.get(reverse('test_variations', kwargs={
            'test_type': 'core',
            'category': 'aptitude',
            'test_index': 0
        }))
        variations = response.context['variations']
        self.assertTrue(variations[1]['available'], "Module 2 should now be available")

    def test_navigation_and_ui(self):
        """Verify navigation to core assessment selection"""
        response = self.client.get(reverse('users:core_assessment_selection'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mock_test/core/index.html')

    def test_invalid_category(self):
        """Verify handling of invalid categories"""
        response = self.client.get(reverse('test_variations', kwargs={
            'test_type': 'core',
            'category': 'invalid_cat',
            'test_index': 0
        }))
        # It should probably redirect or show error, based on current implementation
        # Looking at views_mock_test.py, it returns render for valid cats, or might fail
        self.assertEqual(response.status_code, 200) # Should still load but might show empty or default
