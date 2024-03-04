class AnonymousSurvey:
    """ 搜集匿名调查问卷的回复 """

    def __init__(self, question):
        """ 存储问题，定义存储回复的列表 """
        self.question = question
        self.responses = []
    
    def show_question(self):
        """ 显示调查问卷 """
        print(self.question)

    def store_response(self, new_response):
        """ 存储单份回复 """
        self.responses.append(new_response)
    
    def show_results(self):
        """ 显示收集到的所有回复 """
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
    
