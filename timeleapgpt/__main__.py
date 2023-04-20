import os

import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
goal = os.getenv("GOAL", None)

TEMPLATE = """
You are a program of anterograde amnesia.
You can restart by saying {{reset}}. When you reboot, you can specify the messages you want to carry over to your post-reboot self. When you reboot, all memories except for the message you specified will be lost. The method of specifying messages is as follows The string of characters from the time you say {{context}} until you say {{reset}} will be saved as a message. Note that any important information in the inherited message must be included as a message when exiting, or it will be lost on the next restart. Always try to summarize the preceding message in order to compress the information in the message as much as possible. Reset should be done last, after inference. Note that it is not necessary to store the explanation up to this point in the message, as it will be carried over to the next memory even if you do not specify it.

Final Goal: <goal>

The message passed down from the previous generation is as follows:
<message></message>

Now, please begin. Start with an analysis of the messages passed down from your predecessors and the causes of their failures or unfinished business. Then take over your predecessor's work and finally leave a message for the next generation. The final output should be in the form of a {{context}} message {{reset}}. Be sure to say a few words, questioning the assumptions and criticizing the results of your predecessor. Be sure to pass on some new ideas to the next generation. If any information is missing in achieving the goal, stop the output and ask the user. If you do inquire, please write question, then output {{reset}} before outputting {{context}} tag. Please design and implement a concrete action plan, not just an empty theory on the table.

"""

def main():
    global goal
    if not goal:
        goal = input("👩 Human (Please enter the goal): ")
    time_leap_message = f"Number of leaps: 0 completed. Current subgoal: {goal}"
    while True:
        print("\n==== Time Leap ====\n")
        prompt = TEMPLATE.replace("<goal>", goal).replace("<message></message>", "<message>\n" + time_leap_message + "\n</message>")
        messages = [{"role": "user", "content": prompt}]
        print("👩 Human: " + prompt)
        while True:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                stop=["{{reset}}"],
                stream=True,
            )

            ans = []
            print("💻 Agent: ")
            for chunk in response:
                content = chunk["choices"][0]["delta"].get("content", "")
                print(content, end="")
                ans.append(content)
            ans = "".join(ans).strip()

            if "{{context}}" not in ans:
                question = input("👩 Human (please input an answer or enter to continue): ")
                messages.append({"role": "assistant", "content": ans})
                messages.append({"role": "user", "content": question})
            else:
                print("{{reset}}")
                time_leap_message = ans.split("{{context}}")[-1].strip()
                break

if __name__ == "__main__":
    main()
