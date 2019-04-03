# Приложение, по постингу текстовых постов с тегами в группу вк

import vk_api
import random

def post2vk(letter): #ввод строки сообщения для отправки в группу вк
    login = 'login@vk.ru'
    password = 'password'
    app_id = 6666666

    vk_session = vk_api.VkApi(login=login
                              ,password= password,app_id=app_id,scope='wall')
    vk_session.auth()

    vk1 = vk_session.get_api()

    print(vk1.wall.post(owner_id='-123456789', message=str(letter)))


#генератор текста
def textgeneration(tags_num): #пример tags_num=[0,1,2,3,4,5,6,7,8,9]
    letter = ''

    for i in tags_num:
        letter+='#tags'+str(i)+'\n'

    letter+='\n'
    letter+='Random text №'+str(int(random.random()*1000))+'.'

    return letter

# tags_num=[0,1,2,3,4,5,6,7,8,9] #пример работы программы
# letter=textgeneration(tags_num)
# print(letter)
#
# post2vk(letter)
