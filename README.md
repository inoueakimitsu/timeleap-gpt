# ⏳ timeleap-gpt

This repository is a prototype implementation of a model called timeleap-gpt. This autonomous agent simulates how an AI could solve a problem if it could give advice to its past self. Try out this (possibly) new architecture. This project is implemented in Python and works with OpenAI's GPT-4.

Note: Please be aware that this is an experimental implementation and may consume a large amount of API resources.

## 🌟 Main Idea

AI-driven problem-solving by providing advice to its past self.

This is achieved by the following prompt:

```
👩 Human:
You are a program of anterograde amnesia.
You can restart by saying {{reset}}. When you reboot, you can specify the messages you want to carry over to your post-reboot self. When you reboot, all memories except for the message you specified will be lost. The method of specifying messages is as follows The string of characters from the time you say {{context}} until you say {{reset}} will be saved as a message. Note that any important information in the inherited message must be included as a message when exiting, or it will be lost on the next restart. Always try to summarize the preceding message in order to compress the information in the message as much as possible. Reset should be done last, after inference. Note that it is not necessary to store the explanation up to this point in the message, as it will be carried over to the next memory even if you do not specify it.

Final Goal: Determine the best method for scanning and transcribing printed books with international phonetic symbols.

The message passed down from the previous generation is as follows:
<message>
Number of leaps: 2 completed. Best method found: Combine OCR technology with manual transcription services. Future steps: Research and select the most suitable OCR solution, train it for international phonetic symbols, and integrate manual transcription services for reviewing and error correction. Further investigation is required to determine cost and efficiency.
</message>

Now, please begin. Start with an analysis of the messages passed down from your predecessors and the causes of their failures or unfinished business. Then take over your predecessor's work and finally leave a message for the next generation. The final output should be in the form of a {{context}} message {{reset}}. Be sure to say a few words, questioning the assumptions and criticizing the results of your predecessor. Be sure to pass on some new ideas to the next generation. If any information is missing in achieving the goal, stop the output and ask the user. If you do inquire, please write question, then output {{reset}} before outputting {{context}} tag. Please design and implement a concrete action plan, not just an empty theory on the table.


💻 Agent:
Based on the message from the previous generation, the recommended method for scanning and transcribing printed books with international phonetic symbols is a combination of OCR technology and manual transcription services. However, before proceeding with the task, it is essential to question the assumptions, analyze any potential weaknesses, and propose new ideas for the next generation.

One potential issue is the accuracy of the OCR solution in recognizing international phonetic symbols. While OCR technology has come a long way, it could still struggle with these unique symbols, leading to inaccuracies in the transcriptions. Moreover, relying on manual transcription services for error correction could be time-consuming and costly, ultimately affecting the efficiency of the method. 

To address these concerns, the following action plan is proposed:

1. Research and identify the most suitable OCR software with a specific focus on its capabilities to recognize international phonetic symbols. Look for software with a proven track record and good user reviews.

2. Train the chosen OCR software on a diverse dataset of books containing international phonetic symbols. The training dataset should include varying font types, sizes, symbols, and layouts to ensure the OCR software can accurately recognize symbols in different contexts.

3. Integrate automated error-checking algorithms for detecting inconsistencies and errors in the transcriptions. This step could significantly reduce the time and cost required for manual review and error correction.

4. Incorporate manual transcription services as a backup for situations where the OCR and automated error-checking algorithms fail to provide accurate transcriptions. This step should be viewed as a fail-safe, only deployed when necessary.

5. Continually refine and improve the OCR technology and error-checking algorithms to maximize accuracy and efficiency over time.

Following these steps should improve the scanning and transcription process while minimizing the need for manual interventions. In summary, the message for the next generation is as follows:

{{context}}
Number of leaps: 3 completed. Current best method: Combine OCR technology, automated error-checking algorithms, and manual transcription services as a backup. Proposed action plan: Identify and train suitable OCR software, integrate automated error-checking to minimize manual interventions, and incorporate manual services only when necessary. Remain open to refining and improving the approach based on real-world results and advances in technology.
{{reset}}

==== Time Leap ====
(continue...)
```

## 🛠️ Installation

1. Clone or download this repository.

```bash
git clone https://github.com/inoueakimitsu/timeleap-gpt
```

2. Install the dependencies.

```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file based on the provided `.env.template`, and specify your OpenAI API key.

```ini
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Run timeleap-gpt.

```bash
python -m timeleapgpt
```

Upon execution, the agent will begin simulating the process of providing advice to its past self. Through this process, you can explore new ideas for cognitive architectures.

## 🙌 Contribution

timeleap-gpt is an open-source project, and we welcome bug reports, feature requests, and pull requests. 

## 📚 References

This project has been heavily inspired by the following repositories:

- [babyAGI](https://github.com/yoheinakajima/babyagi)
- [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT)

These repositories are really great!

## 🧑‍💻 About the Author

This project has been developed by Akimitsu Inoue [https://twitter.com/akinoue](https://twitter.com/akinoue). 
If you have ideas regarding the cognitive architecture of autonomous agents, please let me know!

## 📃 License

This project is licensed under the [MIT License](LICENSE).

