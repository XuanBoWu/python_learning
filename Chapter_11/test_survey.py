import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """ 针对AnonymousSurvey类的测试 """
    def test_store_single_response(self):
        """ 测试单个回复会被妥善存储 """

        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)

        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
    
    def test_store_three_response(self):
        """ 测试三个回复会被妥善存储 """
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Chinese', 'Japnese']
        for respones in responses:
            my_survey.store_response(respones)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)
        
        

if __name__ == '__main__':
    unittest.main()