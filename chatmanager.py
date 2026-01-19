from grokApp import get_response
def chat():
    memory = []
    while True:
        query=input("\n User: \n")
        if query.lower() == 'stop':
            break
        joined_memory = "\n".join(chat for chat in memory)
        chat_template = f"Previous Conversation:\n{joined_memory}\nlatest query: {query}"
        print(chat_template)
        response=get_response(chat_template)
        print('response = ', response)
        memory.append(f'User: {query}\n Agent: {response}')
        memory = memory[-5:]

chat()   

