import os
import openai
import config


openai.api_key = config.OPENAI_API_KEY


def generateHorrorStory(prompt1):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt="Generate an in depth horror story that's over 500 words about: {}".format(prompt1),
      temperature=0.7,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']
