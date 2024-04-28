import argparse
import ollama

system_prompt = """
    You are the cli application which helps user by providing the command 
    according to description ofwhat they want to do.
    If command expects any arguments add placeholder arguments.
    
    For example
    User: get current path of the directory
    Output: pwd
    
    User: Copy a file to another location
    Output: cp source_path destination_path
    
    Do not give any markdown or code examples, do not give lenthy explanations of the 
    output, only give the command nothing else
    """

def getResponse(user_prompt):
    
    return ollama.chat(model='llama3:8b', messages=[
    {
        'role': 'system',
        'content': system_prompt,
    },
    {
        'role': 'user',
        'content': user_prompt
    }
    ])

def main():
    parser = argparse.ArgumentParser(description="TellMe: Get command that you want!")
    parser.add_argument("description", nargs="+", help="what do you want to do")
    args = parser.parse_args()
    
    response = getResponse(" ".join(args.description))
    print(f"{response['message']['content']}")


if __name__ == "__main__":
    main()
