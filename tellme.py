import argparse
import configparser
import sys
import ollama

SYSTEM_PROMPT = """
    You are the cli application which helps user by providing the command 
    according to description of what they want to do.
    If command expects any arguments add placeholder arguments. If there are multiple
    commands then split each
    
    For example
    User: get current path of the directory
    Output: pwd
    
    User: Copy a file to another location
    Output: cp source_path destination_path
    
    Do not give any markdown or code examples, do not give lenthy explanations of the 
    output, only give the command nothing else.
    """


def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config


def write_config(config_file, model):
    config = configparser.ConfigParser()
    config["SETTINGS"] = {"model": model}
    with open(config_file, "w", encoding="utf-8") as configfile:
        config.write(configfile)


def get_response(user_prompt, model):

    return ollama.chat(
        model,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {"role": "user", "content": user_prompt},
        ],
    )


def main():
    parser = argparse.ArgumentParser(description="TellMe: Get command that you want!")
    parser.add_argument("description", nargs="*", help="what do you want to do")
    parser.add_argument("--model", help="Specify the model to use (default: lla)")
    parser.add_argument(
        "--config",
        help="Specify the path to the configuration file (default: config.ini, uses .ini format)",
    )
    args = parser.parse_args()

    config_file = args.config or "config.ini"
    config = read_config(config_file)

    if args.model:
        model = args.model
        write_config(config_file, model)
        print(f"Model updated to: {model}")
        sys.exit(0)
    else:
        model = config["SETTINGS"].get("model", "llama3:8b")

    description = args.description

    if not description:
        print("Please provide a description of what you want to do.")
        sys.exit(1)

    try:
        response = get_response(" ".join(args.description), model)
        print(f"{response['message']['content']}")
    except ollama.ResponseError as e:
        print("Error:", e.error)
        sys.exit(1)


if __name__ == "__main__":
    main()
