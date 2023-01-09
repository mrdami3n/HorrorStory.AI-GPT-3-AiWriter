# HorrorShort.AI with Chat GPT-3
Create an AI tool that creates short horror stories 

# Get Started with this repo

1. Copy this repo and move to the root of the directory.

2. Create your OpenAI API key and add it to the config.py file  https://beta.openai.com/

3. Save the Open AI API key inside the file.

4. Install the required libraries inside the requirements txt file
   pip install -r requirements.txt
   
5. Run the program with default horror story system in place
   python app.py

6. To make changes go to blog.py

   engine="text-davinci-003" 
   
   Change the engine the API will use. Davinci is currently the best model but uses the most tokens.

   prompt="Generate an in depth horror story that's over 500 words about: {}".format(prompt1)

   This can be edited to suite your own needs. But please remember the user input is added at the end of the prompt.

   temperature=0.7

   What sampling temperature to use. Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer. We generally recommend altering this or top_p but not both.

   max_tokens=1000 

   The maximum number of tokens to generate in the completion.
   
   The token count of your prompt plus max_tokens cannot exceed the model's context length. Most models have a context length of 2048 tokens (except for the newest models, which support 4096).

   top_p=1

   An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

   We generally recommend altering this or temperature but not both.

   frequency_penalty=0,

   Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

   presence_penalty=0

   Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.


   You can follow me on Tiktok, Youtube and Twitter

   https://twitter.com/Ghost_idle
   https://www.tiktok.com/@ghost.idle
   https://www.youtube.com/@Ghost_idle

   and of course my GitHub

   https://github.com/ghostidle



