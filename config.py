TOKEN = ''

help_message = '<b>Привет</b>\nЯ помогу тебе в дтп! тебе нужно отвечать на вопросы и читать. В путь к огромной страховке!'
start_message = 'Привет я создан чтобы помогать в дтп. Начнём?'


tree = {'dtp': {'yes': {'text': 'Вы попали в дтп?', 
                        'yes': {'text': 'Вы единственный участник дтп?', 
                                'yes': {'text': 'test_yse', 
                                        'yes': 'test', 
                                        'no':'no test'},
                                'no': {'text': 'test_no', 
                                        'yes': 'tesst', 
                                        'no': 'no_test'}}, 
                        'no': {'text': 'Прости, мне нечем тебе помочь, обращайся при дтп!'}}}}
state = tree['dtp']
