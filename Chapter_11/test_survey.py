import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """ 针对AnonymousSurvey类的测试 """
    def setUp(self):
        """
        创建一个调查对象和一组回复，供测试方法使用
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Chinese', 'Japnese']

    def test_store_single_response(self):
        """ 测试单个回复会被妥善存储 """
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_response(self):
        """ 测试三个回复会被妥善存储 """
        for respones in self.responses:
            self.my_survey.store_response(respones)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
        
        

if __name__ == '__main__':
    unittest.main()