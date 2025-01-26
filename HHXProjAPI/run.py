import os
from openai import OpenAI

from scripts.utils import print_with_color

def get_app(text_input):
    client = OpenAI(
        organization="",
        api_key=""
    )

    completion = client.chat.completions.create(
        model="gpt-4-turbo-2024-04-09",
        messages=[
            {"role": "system",
             "content": "Based on the input query, which app does the user want to open?"
                        "Just respond with the app name. Nothing else in the answer."
                        },
            {"role": "user", "content": text_input}
        ],
        temperature=0.5
    )

    op = completion.choices[0].message.content

    return op

def main(text_input):

    # arg_desc = "AppAgent - deployment phase"
    # parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=arg_desc)
    # parser.add_argument("--app")
    # parser.add_argument("--root_dir", default="./")
    # args = vars(parser.parse_args())
    #
    # app = args["app"]
    # root_dir = args["root_dir"]

    app = None
    root_dir = './'

    print_with_color("Welcome to the deployment phase of AppAgent!\nBefore giving me the task, you should first tell me "
                     "the name of the app you want me to operate and what documentation base you want me to use. I will "
                     "try my best to complete the task without your intervention. First, please enter the main interface "
                     "of the app on your phone and provide the following information.", "yellow")

    if not app:
        print_with_color("What is the name of the target app?", "blue")
        # app = input()
        app = get_app(text_input)
        print(app)
        app = app.replace(" ", "")


    os.system(f"python scripts/task_executor.py --app {app} --root_dir {root_dir} --input_text {text_input}")

    return f"{text_input} carried out"

main("open chrome and go to amazon.com")
