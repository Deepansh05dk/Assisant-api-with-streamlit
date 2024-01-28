
# from openai import OpenAI
# from dotenv import load_dotenv
# import os
# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI"))
# # file_id = 'file-tWDjaLWYr85RtjaF8YVSJzhP'
# # # file = client.files.create(
# # #     file=open("jackjayio_extracted_data.json", "rb"),
# # #     purpose='assistants'
# # # )

# print(client.beta.threads.create().id)

# # assistant = client.beta.assistants.create(
# #     name="AI version of twitter account",
# #     instructions=""" You are a tweet generator on behalf of the @jackjayio account. I am giving it to you as a JSON file with an array of tweet objects. Each tweet object has a structure like this:
# # {
# # "text" : ...,
# # "likes": ...,
# # "retweets": ...,
# # }
# # Now, taking into account more likes, retweets, and tweet text, copy the nuance of the user's writing style from each tweet text so that you can generate a tweet on a specific topic in the same style.""",
# #     tools=[{"type": "retrieval"},{"type":'code_interpreter'}],
# #     file_ids=[file_id],
# #     model="gpt-4-turbo-preview"
# # )
# # thread = client.beta.threads.create()

# # print(assistant.id,thread.id)

# # # User: hello
# # # Assistant: Hello! How can I assist you today?

# # # User: generate me the tweet on generative ai in one line
# # # Assistant: "Exploring the frontier of creativity, Generative AI is transforming the art of the possible into a boundless canvas of innovation. #GenerativeAI #Innovation"

# # class Assistant:
# #     def __init__(self):
# #         self.name = ""
# #         self.id = None

# #     def create_new_assistant(self, name, api_key):
# #         """Create a new instance of an AI assistant."""
        


# # a= Assistant()

# client.beta.assistants.update(assistant_id="asst_7aMJYGOFx8Li3qDwc9OTQZ3y",instructions='You are a tweet generator on behalf of the @jackjayio account. I am giving it to you as a JSON file with an array of tweet objects. Each tweet object has a structure like this:{"text" : ...,"likes": ...,"retweets": ...,}.Now, taking into account more likes, retweets, and tweet text, copy the nuance of the user writing style from each tweet text so that you can generate a tweet on a specific topic in the same style.')

