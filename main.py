import vkconnect
import logic


def main():
    VBot = vkconnect.vkbot()
    message = VBot.get_message()
    userId = message['user']
    print(userId)
    DecisionMkng = logic.DecisionMaking(message['text'])
    DecisionMkng.clean_text()



if __name__ == "__main__":
    main()
