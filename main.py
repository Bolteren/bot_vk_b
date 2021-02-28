import vkconnect
import logic


def main():
    VBot = vkconnect.vkbot()#подключаемся к вк
    message = VBot.get_message()#получаем не прочитанное сообщение
    userId = message['user']#Получаем ID пользователя
    DecisionMkng = logic.DecisionMaking(message['text'])#получаем текст сообщения
    DecisionMkng.clean_text()#удаляем лишние слова
    recponse = DecisionMkng.get_responce()#Выбор ответа
    VBot.send_user(userId, recponse)#ответ пользователю


if __name__ == "__main__":
    while True:
        main()
