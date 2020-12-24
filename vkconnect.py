import vk_api
import random
import botConfiguration as bc
import json

class vkbot:
    def __init__(self):
        tokens = bc.read_vk_config()
        self.vk = vk_api.VkApi(token=tokens['vk_tokens'])
        self.vk._auth_token()

    def get_message(self): #получить сообщение
        self.messages = self.vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if self.messages["count"] > 0:
            user_id = self.messages['items'][0]['last_message']['from_id']
            txt = self.messages['items'][0]['last_message']['text']
            return {'user': user_id, 'text': txt}

    def get_user_info(self, user_id):#получить пользователя по ID
        return self.vk.method('users.get', {'user_ids': user_id})

    def send_user(self, user_id, text):#ответить пользователю
        self.messages = self.vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        self.vk.method("messages.send",
                       {"user_id": user_id,
                        "message": text,
                        "random_id": random.randint(1, 100)})

    def load_and_send_immages(self, user_id, text, meddia):#загрузить картинку
        uploader = vk_api.VkUpload(self.vk)
        img = uploader.photo_messages(meddia)
        media_id = img[0]['id']
        owner_id = img[0]['owner_id']
        potos = "photo" + str(owner_id) + "_" + str(media_id)
        file = "dump.json"
        with open(file, 'a', encoding="utf-8") as f:
            json.dump(img, f, ensure_ascii=False)
        self.vk.method("messages.send",
                       {"user_id": user_id,
                        "message": text,
                        "attachment": potos,
                        "random_id": random.randint(1, 100)})

    def load_and_send_docs(self, user_id, text, docs):
        pass


def main():
    v = vkbot()
    print(v.get_message())


if __name__ == "__main__":
    main()
