""" Class to handle the interactivity to the model and setting model system parameters """
from aigent.tools.display import print_message
from aigent.agent.agent import Agent


class Repl:
    def __init__(self, agent: Agent, command_handler: callable):
        self.agent = agent
        self.command_handler = command_handler
        self.show_token_count = False

    def run(self, first_prompt=''):
        while True:
            if first_prompt:  # If we have a first prompt, use it instead of asking the user first
                prompt = first_prompt
                first_prompt = None
            else:
                prompt = self.get_prompt()
            if prompt[0] == ':' or prompt[0] == '/':
                if not self.command_handler(prompt[1:]):
                    break
            else:
                message = self.agent.chat(prompt)
                if type(message) == str:
                    print_message(message, 'assistant')
                self.agent.after_response()
                if self.show_token_count:
                    print(f"[{self.agent.last_token_count()}]")

    @staticmethod
    def get_prompt():
        """ Default implementation, can be overridden """
        prompt = ''
        while not prompt:
            prompt = input("You: ")
        return prompt
